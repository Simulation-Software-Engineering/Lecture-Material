#! /usr/bin/env sh

echo "In directory ${PWD}"
mkdir -p texts
for f in $(find ./ -type f \( -iname \*_text.md -o -iname \*_quiz.md \));
do
    echo $f
    output_filename=$(echo $f | rev| cut -d "/" -f 1 | rev | sed "s/md/pdf/")
    echo $output_filename
    pandoc -V geometry:a4paper  -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=2.5cm -V geometry:top=2.5cm -V linkcolor:blue -V fontsize=10pt --listings --output=texts/${output_filename} ${f}
done
