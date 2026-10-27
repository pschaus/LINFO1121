import re
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst import directives
from docutils.transforms import Transform
from sphinx.addnodes import toctree
from sphinx.locale import _, admonitionlabels
from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import SphinxDirective


class answer_node(nodes.Admonition, nodes.Element):
    pass


def visit_answer_node_html(self, node):
    self.visit_admonition(node)


def depart_answer_node_html(self, node):
    self.depart_admonition(node)


def visit_answer_node_latex(self, node):
    title = str(node.children[0].children[0])
    self.body.append('\n\\begin{tcolorbox}[title='+title+']')
    node.children = node.children[1:]
    self.no_latex_floats += 1


def depart_answer_node_latex(self, node):
    self.body.append('\\end{tcolorbox}\n')
    self.no_latex_floats -= 1


class AnswerDirective(BaseAdmonition, SphinxDirective):
    node_class = answer_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        show_answers = self.config['show_answers']
        if not show_answers:
            return []
    
        if not self.options.get('class'):
            self.options['class'] = ['admonition-answer']

        (todo,) = super().run()
        if isinstance(todo, nodes.system_message):
            return [todo]
        elif isinstance(todo, answer_node):
            todo.insert(0, nodes.title(text=_('Answer')))
            todo['docname'] = self.env.docname
            self.add_name(todo)
            self.set_source_info(todo)
            self.state.document.note_explicit_target(todo)
            return [todo]
        else:
            raise RuntimeError  # never reached here


class FormatExercisesTransform(SphinxTransform):
    """
    Automatically classifies exercise sections on exercise pages into
    'exercise-theory' or 'exercise-inginious' (by detecting INGInious links or
    optional 'INGInious:' title prefixes) and prepends a compact icon to each
    exercise heading and TOC entry—without requiring hardcoded exercise numbers
    or redundant text labels.
    """
    default_priority = 300

    def apply(self, **kwargs):
        docname = getattr(self.env, 'docname', '')
        if not re.match(r'^part\d+/(ex\d+|s13)$', docname):
            return

        root_sections = [n for n in self.document.children if isinstance(n, nodes.section)]
        if not root_sections:
            return
        root_section = root_sections[0]

        first_exercise_section = None

        for section in [n for n in root_section.children if isinstance(n, nodes.section)]:
            if not section.children or not isinstance(section.children[0], nodes.title):
                continue
            title_node = section.children[0]
            raw_text = title_node.astext().strip()

            # Support optional legacy prefixes if ever used in the future, while keeping clean titles
            m = re.match(r'^Exercise\s+[\d\.]+\s*(?:\((.*)\))?$', raw_text, flags=re.IGNORECASE)
            if m and m.group(1):
                clean_title = m.group(1).strip()
            else:
                clean_title = raw_text

            has_inginious_prefix = bool(re.match(r'^inginious\s*[:\-]', clean_title, flags=re.IGNORECASE))
            if has_inginious_prefix:
                clean_title = re.sub(r'^inginious\s*[:\-]\s*', '', clean_title, flags=re.IGNORECASE).strip()

            has_inginious_link = any(
                'inginious' in ref.get('refuri', '').lower()
                for ref in section.findall(nodes.reference)
            )
            is_inginious = has_inginious_prefix or has_inginious_link

            if first_exercise_section is None:
                first_exercise_section = section

            if is_inginious:
                section['classes'].extend(['exercise-section', 'exercise-inginious'])
                icon_class = 'ex-icon-inginious'
            else:
                section['classes'].extend(['exercise-section', 'exercise-theory'])
                icon_class = 'ex-icon-theory'

            new_children = [
                nodes.inline('', '', classes=['ex-icon', icon_class]),
                nodes.Text(' '),
                nodes.inline('', clean_title, classes=['ex-title-text']),
            ]

            title_node.clear()
            for child in new_children:
                title_node += child

        if first_exercise_section is not None and first_exercise_section.parent is not None:
            legend_html = (
                '<div class="exercise-legend" role="note" aria-label="Exercise types legend">'
                '<span class="legend-item">'
                '<span class="ex-icon ex-icon-theory" title="Theoretical exercise"></span>'
                '<span class="legend-desc">Theoretical &amp; conceptual</span>'
                '</span>'
                '<span class="legend-item">'
                '<span class="ex-icon ex-icon-inginious" title="INGInious exercise"></span>'
                '<span class="legend-desc">INGInious coding &amp; grading</span>'
                '</span>'
                '</div>'
            )
            legend_node = nodes.raw('', legend_html, format='html')
            parent = first_exercise_section.parent
            idx = parent.index(first_exercise_section)
            parent.insert(idx, legend_node)


class HideNextWeeksFiles(SphinxTransform):
    default_priority = 400

    def apply(self, **kwargs):
        if not self.config['respect_hide']:
            return

        filename = self.document.attributes['source'].split('/')[-1]
        if not filename.startswith('s') or not filename.endswith('.rst'):
            return
        try:
            filename = int(filename[1:-4])
        except:
            return

        if filename <= self.config['current_week'] or filename % 2 == 1:
            return

        self.document.children = []


class HideNextWeeksTOC(SphinxTransform):
    default_priority = 400

    def apply(self, **kwargs):
        if not self.config['respect_hide']:
            return

        fname = self.document.attributes['source'].split('/')[-1]

        if fname == "index.rst":
            def check(x):
                try:
                    name = x.split('/')[1]
                    if not name.startswith('s'):
                        return True
                    name = int(name[1:])
                    return name <= self.config['current_week'] or name % 2 == 1
                except:
                    return True

            for node in self.document.traverse():
                if node.tagname == "toctree":
                    node.attributes['entries'] = [
                        x
                        for x in node.attributes['entries']
                        if check(x[1])
                    ]
                    node.attributes['includefiles'] = [
                        x
                        for x in node.attributes['includefiles']
                        if check(x)
                    ]
                    print(node)


def override_papertheme_data(app, pagename, templatename, context, doctree):
    for entry in context.get('toctree_data', []):
        entry['title'] = entry['title'].split(' | ')[0]
    context['toctree_data'] = [
        x
        for x in context.get('toctree_data', [])
        if not x['title'].startswith('Partie ') or len(x['entries']) != 0
    ]


def setup(app):
    app.add_node(answer_node,
                 html=(visit_answer_node_html, depart_answer_node_html),
                 latex=(visit_answer_node_latex, depart_answer_node_latex))

    app.add_directive('answer', AnswerDirective)
    app.add_transform(FormatExercisesTransform)
    app.add_transform(HideNextWeeksFiles)
    app.add_transform(HideNextWeeksTOC)
    app.connect('html-page-context', override_papertheme_data, priority=800)

    app.add_config_value('show_answers', False, 'env')
    app.add_config_value('respect_hide', False, 'env')
    app.add_config_value('current_week', 1, 'env')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
