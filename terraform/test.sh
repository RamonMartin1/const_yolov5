#! /bin/sh.

# file = "zipfiles.txt"
# while read -r line
# do
#   echo "$(line)/*"
#   # 7z a "$line"
# done < "$file"

files = "/*"
for i in $(cat zipfiles.txt); do
# echo "$i""/*"
# echo "$i""/""$i"".zip"
7z a -r "$i""/""$i"".zip" "$i""/*"
done
# wait