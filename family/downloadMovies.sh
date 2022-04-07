# while getopts q:e:s: option
# do
# case "${option}"
# in
# q) QUALITY=${OPTARG};;
# s) SEASON=${OPTARG};;
# e) EPISODE=${OPTARG};;
# esac
# done

# echo "$QUALITY"
# echo "$EPISODE"
# echo "$SEASON"
# read -p "Name: " name 

# python3 name.py "$name"


# titles=$(sed -n '1p' titleLinks.txt)
# links=$(sed -n '2p' titleLinks.txt)
# echo "$titles" | fzf
# t=$(cat -n Titles.txt | fzf --with-nth 2.. | awk '{print $1}')
# ls | cat -n | fzf --with-nth 2.. | awk '{print $1}'

# declare -a titles
# echo "${titles[2]}"
# for i in "${titles[@]}"; do
    # echo "$i"
#   t+=$(echo -e "$titles[$i]""\n")
# done

# echo "$t" Aman

# special=$(sed -n "$t p" Links.txt)

# rm Links.txt Titles.txt

# python3 sel.py "$special" 

Red=$'\e[1;31m'
Green=$'\e[1;32m'
Blue=$'\e[1;34m'

echo -e "$Red \t\t\t\v\t\t\v\t\t STILL $Blue IN $Green TESTING MODE \e[0m "

python3 sel.py $1

COUNTER=0

while IFS= read -r line
do
  
  (( COUNTER++ ))
  echo -e "$Green \t\t\t\v\t\t\v\t\t New EPISODE $COUNTER \e[0m "

  python3 third.py "$line"

  echo AMANmyvar
  # var=$( xclip  -o -selection clipboard )
  # echo "$var" >> res/temp
  var=$( cat res/oneL.txt )

  grep -oP "xyz/.*" res/oneL.txt | sed 's/xyz//g'

  timeout 5m axel -n6 -a -c "$var" -o res/

  echo $? no

  find res/ -size 0 -print -delete

done < 'res/episodeL.txt'

echo -e "\t\t\t\v\v All downloaded episodes"

ls res/ | grep -Po ".*\d{3}p" | tr -s ".720p"

# while IFS= read -r line
# do
#   axel -n10 -a -c "$line" -o res/
# done < 'res/temp'


# p=$(awk -F '\t' '{print $1,$2}' qualityLinks.txt | cat -n | fzf --with-nth 2.. | awk '{print $1}')

# special2=$(awk -F '\t' -v "li=$p" 'NR == li {print $3}' qualityLinks.txt)


# exit

# rm qualityLinks.txt
# # exit 1
# python3 third.py "$special2" 

# echo "$links"
# ret="$(python3 -c 'from name import func;func("$name")' "${arr[@]}")"

# lastL=$(cat lastLink.txt)
# myvar=$(curl -s  "$lastL" | grep 'Download Links' | sed 's/href=/\n/g' | grep '^"https' | grep  '.*"><') 
# echo "$i"
# echo "$myvar" | grep -o 'Epi.*</sp' | sed 's/<\/sp//g'  
# selectedM=$(echo "$myvar" | grep -o '.*"><' | sed 's/><//g' | sed -e 's/"//g' | fzf)

# echo "$selectedM"
# echo aman


# myvar=`axel -n 10 -a "$selectedM"`
# echo "$myvar"  

# SUB='unsupported'
# if [[ "$myvar" == *"$SUB"* ]]; then
#   echo "It's there.ERRRRRROR"
#   python3 fourth.py "$selectedM" 

#   gpload=$(cat gploadL.txt)
#   axel -n 10 -a "$gpload"
#   rm *php* gploadL.txt
  
# fi

# test_var='Aanchal Patyal'
# export test_var

# echo aman $ret
