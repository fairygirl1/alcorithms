#!/bin/bash

directory="exam_issues/" # Замените на путь к целевой директории

count=1
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    new_filename="${count}_${filename}"
    mv "$file" "$directory/$new_filename"
    count=$((count + 1))
  fi
done
