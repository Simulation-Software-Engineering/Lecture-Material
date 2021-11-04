#! /usr/bin/env sh

TARGET_BASE="texts"

echo "In directory ${PWD}"
mkdir -p ${TARGET_BASE}
for f in $(find ./ -type f \( -iname \*_text.md -o -iname \*_quiz.md \));
do
    echo $f
    output_dir=$(echo $f | cut -d "/" -f 2)
    target_dir=${TARGET_BASE}/${output_dir}
    mkdir -p ${target_dir}
    echo "Output directory: ${target_dir}"
    output_filename=$(echo $f | rev| cut -d "/" -f 1 | rev | sed "s/md/pdf/")
    echo "Output file name: ${output_filename}"
    pandoc -V geometry:a4paper  -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=2.5cm -V geometry:top=2.5cm -V linkcolor:blue -V fontsize=10pt --listings --output=${target_dir}/${output_filename} ${f}
done
