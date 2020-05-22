#!/bin/bash

for file in *.py;do
    if [[ $file != *group.py* ]]
    then
        files="${file%.*}"
        mkdir "$files" 
        echo "This is the file for $file" > ./"$files"/README.md 
        mv "$file" ./"$files"
    fi
done