for file in *.py; do
    $files="${file%.*}"
    mkdir "$files" &&
    touch "$files"/README.md &&
    echo "This is the file for $file" >> "$files"/README.md &&
    mv "$file" ./"$files"
done