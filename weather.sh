
# weather info fetching from metaweather API and parsing using jq
read -p 'Enter city :) ' city

myvar=$(curl -s https://www.metaweather.com/api/location/search/?query="$city") 
data=$( echo ${myvar[0]} | jq '.[].woeid') 


city_data=$( curl -s https://www.metaweather.com/api/location/$data/)

cityD=$(echo "$city_data" | jq '. | "location--> \(.title) \ntimezone--> \(.timezone)\n"')
tempD=$(echo "$city_data" | jq '.consolidated_weather[]' | jq  '"--> Data: \(.applicable_date) , Weather: \(.weather_state_name), Min.Temp: \(.min_temp), Max.Temp: \(.max_temp), Humidity: \(.humidity)\n"')

echo -e "$cityD"| sed -e 's/^"//' -e 's/"$//'
echo -e "$tempD"| sed -e 's/^"//' -e 's/"$//'

