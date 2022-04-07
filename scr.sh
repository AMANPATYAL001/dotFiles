
# links for bash commands from howtogeek platform

myvar=$(curl -s https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/ | grep "</a><strong>")

final=''
for val in $myvar
do
  if [[ $val == *https:* ]] 
  then
      newval=$(echo $val | sed 's/href=//g; s/<\/a>//g; s/<\/td>//g;s/<strong>//g; s/<\/strong>//g; s/>/---> /g')
      final="${final}\n${newval}"
  fi
  done

  echo -e $final | awk -F '---> ' '{OFS=" \t "} {print $2,$1}'

