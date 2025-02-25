#!/usr/bin/sh

#
# 第1引数：フルパスのスクショファイル名
# 第2引数：画像をフルで出力（=true）、ショートで出力（=true以外、デフォルト）
#


if [ $# -eq 0 ]; then
  echo "引数を指定して"
  echo "第1引数：フルパスのスクショファイル名"
  echo "第2引数：画像をフルで出力（=true）、ショートで出力（=true以外、デフォルト）"
  echo "実行ディレクトリで中間ファイルや成果物を生成"
  exit 1
fi

file_argment=$1

file_name_within_ext="${file_argment##*/}"
file_name_without_ext="${file_name_within_ext%.*}"
file_name_ext="${file_argment##*.}"

file_name_output=""
if [[ "$2" == "true" ]]; then
  # full
  file_name_output="_${file_name_without_ext}_full.${file_name_ext}"
else
  # short
  file_name_output="_${file_name_without_ext}_short.${file_name_ext}"
fi
echo $file_name_output


#
# 切り取り
#

magick ${file_argment} -gravity SouthWest -crop 1920x500+0+0 zz110.png
magick ${file_argment} -gravity SouthWest -crop 900x100+0+0  zz121.png
magick ${file_argment} -gravity SouthEast -crop 900x100+0+0  zz122.png

#
# 透明埋め合わせ画像作成
#

magick -size 45x500 xc:none zz210.png
magick -size 20x100 xc:none zz221.png
magick -size 920x10 xc:none zz222.png

#
# 全体画像の両端に透明埋め合わせ画像を結合
#

magick zz210.png zz110.png zz210.png +append zz310.png

#
# 全体画像を縮小
#

magick zz310.png -resize 920x zz410.png

#
# 横に、切り取り画像と透明埋め合わせ画像を結合
#

magick zz121.png zz221.png +append zz511.png
magick zz221.png zz122.png +append zz512.png

#
# 仕上げ
#

if [[ "$2" == "true" ]]; then
  # full
  magick zz511.png zz222.png zz512.png zz222.png zz222.png zz410.png -append $file_name_output
else
  # short
  magick zz511.png zz222.png zz512.png -append $file_name_output
fi

#
# 不要ファイル削除
#

rm zz110.png zz121.png zz122.png zz210.png zz221.png zz222.png zz310.png zz410.png zz511.png zz512.png

