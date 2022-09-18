#! /bin/bash
set -e

rm -rf build

#make html
make latexpdf

# Upload Answer HTMLs
#cd build/html
#dir="."
#find "$dir" -type f | while read f; do
#	rel="$(echo "$f" | sed -e "s#$dir##" -e "s# /#/#")";
#	curl -X POST https://content.dropboxapi.com/2/files/upload \
#        --header "Authorization: Bearer $AUTHORIZATION" \
#        --header "Dropbox-API-Arg: {\"path\": \"/tuteurs/website$rel\", \"mode\":\"overwrite\"}" \
#        --header "Content-Type: application/octet-stream" \
#        --data-binary @$f
#done
#cd ../..


f="linfo1121.pdf"

# Upload Answer PDFs
cd build/latex

curl -X POST https://content.dropboxapi.com/2/files/upload \
    --header "Authorization: Bearer $AUTHORIZATION" \
    --header "Dropbox-API-Arg: {\"path\": \"/tuteurs/answer-$f\", \"mode\":\"overwrite\"}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @$f

cd ../..

make html