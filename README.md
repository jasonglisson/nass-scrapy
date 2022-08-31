Scrapy scripts

These scripts are built on the [Scrapy][scrapy] python framework.
[scrapy]:https://docs.scrapy.org/en/latest/index.html

You can pull this repository locally and run the scripts if you are running docker. 
Once you've pull the scripts and run `docker-compose up -d`, you'll need to shell into the docker container by running this command:
`docker exec -it scrapy_scrapyd_1 /bin/bash`. Once inside the container the following scripts can be run. 

(You may also be able to run these scripts on XXX server if you have access).

To run your script, type `scrapy crawl <spider-name> -o <file tpy eot save>`

And example is: `scrapy crawl basic -o nass.json`