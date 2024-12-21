#! /bin/bash
set -e

rm -rf build

#echo "show_answers = True" >> source/conf.py

#make latexpdf

#f="linfo1121.pdf"

# Upload Answer PDFs
#cd build/latex



#curl -X POST https://content.dropboxapi.com/2/files/upload \
#    --header "Authorization: Bearer $AUTHORIZATION" \
#    --header "Dropbox-API-Arg: {\"path\": \"/tuteurs/answer-$f\", \"mode\":\"overwrite\"}" \
#    --header "Content-Type: application/octet-stream" \
#    --data-binary @$f

#cd ../..

echo "show_answers = False" >> source/conf.py

make html