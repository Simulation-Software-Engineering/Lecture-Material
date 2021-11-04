#! /usr/bin/env sh

TARGET_BASE="slides"

echo "In directory ${PWD}"
mkdir -p ${TARGET_BASE}
for f in $(find . -type f -iname "*_slides.md");
do
    echo $f
    output_dir=$(echo $f | cut -d "/" -f 2)
    target_dir=${TARGET_BASE}/${output_dir}
    mkdir -p ${target_dir}
    echo "Output directory: ${target_dir}"
    output_filename=$(echo $f | rev| cut -d "/" -f 1 | rev | sed "s/md/pdf/")
    echo "Output file name: ${output_filename}"
    pandoc -t beamer -V aspectratio=169 -V linkcolor:blue -V fontsize=12pt --listings -s --output=${target_dir}/${output_filename} ${f}
done
