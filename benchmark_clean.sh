#!/bin/bash

TRAITS_PATH=dissect/traits
OUTPUT_PATH=$(realpath benchmark)

rm -rf $TRAITS_PATH/a*/a*__* $TRAITS_PATH/i*/i*__*
rm -rf $TRAITS_PATH/*/*.log
rm -rf $OUTPUT_PATH