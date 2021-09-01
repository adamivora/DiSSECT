#!/bin/bash

set -e

VENV_PATH=venv
TRAITS_PATH=dissect/traits
OUTPUT_PATH=$(realpath benchmark)
PYTHON=$(realpath $VENV_PATH/bin/python)
TRAITS=$(for TRAIT in $TRAITS_PATH/*[0-9][0-9]; do echo ${TRAIT#$TRAITS_PATH/}; done)
SAMPLING_SECONDS=600

mkdir -p $OUTPUT_PATH

cd $TRAITS_PATH
for TRAIT in $TRAITS
do
    echo "Running trait $TRAIT..."
    py-spy record -s -o $OUTPUT_PATH/$TRAIT.json -d $SAMPLING_SECONDS -- $PYTHON run_traits_single.py -c all -a any -n $TRAIT
    ps -f | grep "run_traits_single.py" | awk '{print $2}' | xargs kill 2>/dev/null || true
done
