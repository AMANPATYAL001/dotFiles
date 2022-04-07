
# downloading beautiful pics from twitter account of @samdoesarts, displaying through sxiv and setting as wallpaper.
# python script is needed to fetch the image links

python3 im.py $1

sxiv_otps=" -tfpo -z 200" # o is needed for selection

walldir="$HOME/wall"

links=$(cat imgLink | tr '\n' ' ')


cachedir="$HOME/.cache/samdoesarts"

mkdir -p "$cachedir"    

echo $links | xargs -r wget -qP "$cachedir"

#sxiv "$cachedir"

image_ids="$(sxiv $sxiv_otps "$cachedir")"

#echo $image_ids |
mv $image_ids $walldir

latest_pic=$( ls $HOME/wall/ -t | head -n1 )
gsettings set org.gnome.desktop.background picture-uri file:///home/amanp/wall/"$latest_pic"

rm -rf "$cachedir"
