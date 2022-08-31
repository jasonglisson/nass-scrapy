#!/bin/bash

#enter oip_county project directory
cd /var/lib/scrapyd/oip_county

#get data from offices.usda.gov
printf "\n============== Fetching OIP County Data ==============\n"
sleep 5s
scrapy crawl oipcounty

#delete old USDA OIP data in ElasticSearch
printf "\n============== Deleting USDA OIP Index ==============\n"
sleep 5s
curl -XDELETE 'http://elasticsearch:9200/oip_county/'

#delete old state data in ElasticSearch
printf "\n============== Deleting State Index ==============\n"
sleep 5s
curl -XDELETE 'http://elasticsearch:9200/states/'

#ingest USDA OIP data into ElasticSearch
printf "\n============== Ingesting USDA OIP Data into ElasticSearch ==============\n"
sleep 2s
curl -H "Content-Type: application/json" -XPOST 'http://elasticsearch:9200/oip_county/_bulk?pretty' --data-binary @/var/lib/scrapyd/oip_county/oip_county.jl

#ingest State data
printf "\n============== Ingesting State Data & FIPS Codes into ElasticSearch ==============\n"
sleep 5s
curl -H "Content-Type: application/json" -XPOST 'http://elasticsearch:9200/states/_bulk?pretty' --data-binary @/var/lib/scrapyd/states/states.jl

printf "\n============== Service Center Locator Data Import Complete ==============\n"
sleep 2s

exit 0