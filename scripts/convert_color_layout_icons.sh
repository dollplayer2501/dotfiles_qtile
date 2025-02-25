#!/usr/bin/bash

DIR_EXT="/usr/lib/python3.13/site-packages/libqtile/resources/layout-icons/*.png"
PATH_OUTPUT="${HOME}/.config/qtile/icons/"

if [ ! -d ${PATH_OUTPUT} ]; then
  mkdir ${PATH_OUTPUT}
else
  rm -rf ${PATH_OUTPUT}
  mkdir  ${PATH_OUTPUT}
fi

for file_path in $(eval echo $DIR_EXT); do 
  # echo $file_path
  file_name=$(basename "$file_path")
  # echo $file_name
  magick $file_path -fuzz 10% -fill "#FF7F7F" -opaque "#ffffff" ${PATH_OUTPUT}$file_name
done

# 'LightBlue':        '#7FBAFF',
# 'Purple':           '#7F3FBF',
# 'Oreange':          '#FF7F7F',
# 'Red':              '#CC3980',

