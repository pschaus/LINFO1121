#! /bin/bash
set -e

rm -rf build

make html
make latexpdf

# Upload Answer HTMLs
cd build/html
dir="."
find "$dir" -type f | while read f; do
	rel="$(echo "$f" | sed -e "s#$dir##" -e "s# /#/#")";
	curl -X POST https://content.dropboxapi.com/2/files/upload \
        --header "Authorization: Bearer $AUTHORIZATION" \
        --header "Dropbox-API-Arg: {\"path\": \"/tuteurs/website$rel\", \"mode\":\"overwrite\"}" \
        --header "Content-Type: application/octet-stream" \
        --data-binary @$f
done
cd ../..

# Upload Answer PDFs
cd build/latex
for f in s*.pdf
do
	curl -X POST https://content.dropboxapi.com/2/files/upload \
    	--header "Authorization: Bearer $AUTHORIZATION" \
    	--header "Dropbox-API-Arg: {\"path\": \"/tuteurs/answer-$f\", \"mode\":\"overwrite\"}" \
    	--header "Content-Type: application/octet-stream" \
    	--data-binary @$f
done
cd ../..

rm -rf build


echo "show_answers = False" >> source/conf.py
make latexpdf
cd build/latex
for f in s*.pdf
do
	curl -X POST https://content.dropboxapi.com/2/files/upload \
    	--header "Authorization: Bearer $AUTHORIZATION" \
    	--header "Dropbox-API-Arg: {\"path\": \"/tuteurs/$f\", \"mode\":\"overwrite\"}" \
    	--header "Content-Type: application/octet-stream" \
    	--data-binary @$f
done
cd ../..
rm -rf build

echo "respect_hide = True" >> source/conf.py
make html
make latexpdf
cd build/latex
for f in s*.pdf
do
	filesize=$(stat -c%s "$f" || gstat -c%s "$f")
	if (( filesize > 20000 )); then
		curl -X POST https://content.dropboxapi.com/2/files/upload \
    		--header "Authorization: Bearer $AUTHORIZATION" \
    		--header "Dropbox-API-Arg: {\"path\": \"/student/$f\", \"mode\":\"overwrite\"}" \
    		--header "Content-Type: application/octet-stream" \
    		--data-binary @$f
    fi
done
cd ../..
