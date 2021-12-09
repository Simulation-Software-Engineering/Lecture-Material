#!/usr/bin/env bash

PANDOC_SLIDE_OPTIONS=("--pdf-engine=xelatex" "-t beamer" "-V aspectratio=169" "-V linkcolor:blue" "-V fontsize=12pt" "--listings" "-s")
PANDOC_TEXT_OPTIONS=("--pdf-engine=xelatex" "-V geometry:a4paper" "-V geometry:left=2.5cm" "-V geometry:right=2.5cm" "-V geometry:bottom=2.5cm" "-V geometry:top=2.5cm" "-V colorlinks:true" "-V linkcolor:blue" "-V fontsize=10pt" "--listings" "-s")

if [[ $# == 1 ]];
then
    TARGET_FILES="$1"
else
    echo "Error: Expect one parameter passed to script!"
    echo "  Valid arguments are: slides, quiz, text, notes, or exercise"
    exit 1
fi

if [[ "$TARGET_FILES" == "slides" ]] || [[ "$TARGET_FILES" == "quiz" ]] || [[ "$TARGET_FILES" == "demo" ]] || [[ "$TARGET_FILES" == "exercise" ]];
then
    file_list=$(find . -type f -iname "*_${TARGET_FILES}.md")
else
    echo "Error: Argument not supported."
    echo "  Supplied argument: ${TARGET_FILES}"
    echo "  Valid arguments are: slides, quiz, demo, or exercise"
    exit 1
fi

if [[ "$TARGET_FILES" == "slides" ]];
then
    output_options="${PANDOC_SLIDE_OPTIONS[@]}"
    target_base="slides"
else
    output_options="${PANDOC_TEXT_OPTIONS[@]}"
    target_base="texts"
fi

echo "In directory ${PWD}"
mkdir -p ${target_base}
for f in ${file_list};
do
    echo $f
    output_dir=$(echo $f | cut -d "/" -f 2)
    target_dir=${target_base}/${output_dir}
    mkdir -p ${target_dir}
    echo "Output directory: ${target_dir}"

    output_filename=$(echo $f | rev| cut -d "/" -f 1 | rev | sed "s/md/pdf/")
    echo "Output file name: ${output_filename}"

    pandoc ${output_options} --output=${target_dir}/${output_filename} ${f}

    if test -f "${target_dir}/${output_filename}"; then
        echo "${target_dir}/${output_filename} successfully created."
    else
        echo "Creation of ${target_dir}/${output_filename} failed."
        echo "  Aborting..."
        exit 1
    fi
done
