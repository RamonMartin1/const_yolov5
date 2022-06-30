#!/bin/bash
for i in $(cat zipfiles.txt); do
  7z a -r "$i""/""$i"".zip" "$i""/*"
done