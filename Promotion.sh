
#sh ./documents/github/PromoAssist/Promotion.sh
repo=(

)
company='CompanyHere'

echo Welcome to the Promotion Cycle setup assist thingy. Please input a valid token:
read usertoken

echo $(date)
for i in ${repo[@]}
  do
    echo $i
    #delete the info in the preexisting files so it doesnt just add to the bottom of the file
    if test -f "./documents/github/PromoAssist/JSON_data/$i.json"; then
      echo "./documents/github/PromoAssist/JSON_data/$i.json exist and is being replaced"
      rm ./documents/github/PromoAssist/JSON_data/$i.json
    fi
    #gather the json data and put them in a file
    curl -u token:$usertoken https://api.github.com/repos/$company/$i/compare/master...develop >> ./documents/github/PromoAssist/JSON_data/$i.json

  done


python3 ./documents/github/PromoAssist/Promotion.py
#py ./documents/github/PromoAssist/Promotion.py
#if you are on windows try to use the second option instead, you may need to change the python calling thingy to something different depending on how you installed python
