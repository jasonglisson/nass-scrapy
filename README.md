Service Center Locator Data Ingestion for JSON File and ElasticSearch
===

This repository contains the docker containers and scripts to harvest data for the Service Center Locator on Farmers.gov.

These scripts are built on the [Scrapy][scrapy] python framework.
[scrapy]:https://docs.scrapy.org/en/latest/index.html

You can pull this repository locally and run the scripts if you are running docker. 
Once you've pull the scripts and run `docker-compose up -d`, you'll need to shell into the docker container by running this command:
`docker exec -it scrapy_scrapyd_1 /bin/bash`. Once inside the container the following scripts can be run. 

(You may also be able to run these scripts on XXX server if you have access).

The data for the Service Center Locator may be loaded into the module two ways: By a JSON file or by ElasticSearch.

## JSON
---
This script is for compiling all of the service center locator data within one JSON file. The file is then uploaded into the Drupal module.
To run this script, proceed to `/var/lib/scrapyd/scl`. Once there you'll execute the following command:
`scrapy crawl scl -o scl.json`.

When the script finished (takes approx. 1.5 - 3 minutes depending on your internet connection), download the file and upload it into the environment of your choice.
at the path `/admin/config/farmers-service-center-locator/admin-settings`.

Make sure that you have selected the JSON radio button and then upload this file and click "Save Configuration" at the bottom of the page.

## ElasticSearch
---
This script is for ingesting data into the ElasticSearch container that the module and script point to. Right now, these scripts point to the QA environment.
To run this script, proceed to this path `/var/lib/scrapyd`.

Once there, you'll see a shell script titled `scrapy-entrypoint.sh`.

To execute this script, type `./scrapy-entrypoint.sh` in your command prompt.

This script does several things:

1. Fetches OIP County Data
2. Fetches Location Data in two different batches
3. Deletes USDA OIP Index in ElasticSearch
4. Deletes USDA Location Index in ElasticSearch
5. Ingests the newly harvested USDA OIP Data into ElasticSearch
6. Ingests the newly harvested USDA Location Data into ElasticSearch

You will see prompts in your terminal for each of these steps. This takes approximately 25 - 35 mins to complete. There is no further action required inside the docker container for this step.

Within the Service Center Locator module (located here: `/admin/config/farmers-service-center-locator/admin-settings`) you must make sure that you have the ElasticSearch endpoint set correctly and the ElasticSearch API key set correctly.
To set the ElasticSearch API key, you must have direct access to the ElasticSearch ReadOnlyRest Docker Container where this Key was created. Currently, this key is set to: `OWz9xg5XX9KrLYaYUMgCxcWvoSEII2ixgeLK27Xh` This is a master key that has read and write ability.
TODO: We need to create a read only key for the module to use for ElasticSearch connections.

If this API Key has been changed for any reason, it must be changed in the module settings page and in the shell script that executes this ElasticSearch ingestion (`
scrapy-entrypoint.sh`)

Lastly, ensure that you've selected the correct radio button for ElasticSearch data within the Service Center Locator module.