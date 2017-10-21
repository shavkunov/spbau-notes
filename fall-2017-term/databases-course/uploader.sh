 #!/bin/bash 
message="$(gdrive upload --share main.pdf | awk 'END { print }')"
link="$(echo $message | awk '{print $NF}')"
view="${link/download/view}"

googleLink="=HYPERLINK(\"$view\", \"Мой конспект\")"
echo $googleLink | pbcopy
#value="{"values": [[$googleLink]]}"
#client="166532326030-dtgsfut4bkepinj0afsl0mo4us3gk1dc.apps.googleusercontent.com"
#curl --request PUT --header "Content-Type: application/json" "https://sheets.googleapis.com/v4/spreadsheets/1aKnrG37vTZw6xyiHV4NJ0ZMeUU1sy0f2hTOHNEQFDGo/values/H7?client_id=$apiKey" --globoff --data-binary $value