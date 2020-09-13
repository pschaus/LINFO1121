FROM ubuntu:focal
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
 && apt-get install -y \
      curl \
      git \
      graphviz \
      make \
      python3 \
      python3-dev \
      python3-pip \
      python3-pil \
      unzip \
      vim \
      latexmk \
      lmodern \
      texlive-latex-recommended \
      texlive-fonts-recommended \
      texlive-latex-extra \
      imagemagick \
      librsvg2-bin \
 && apt-get autoremove \
 && apt-get clean

RUN pip3 install sphinx sphinxcontrib-svg2pdfconverter sphinx-press-theme
