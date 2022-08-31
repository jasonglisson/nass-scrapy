Scrapy scripts

These scripts are built on the [Scrapy][scrapy] python framework.
[scrapy]:https://docs.scrapy.org/en/latest/index.html

You can pull this repository locally and run the scripts if you are running docker. 
-  Once you've pull the scripts and run `docker-compose up -d`
-  You'll need to shell into the docker container by running this command: `docker exec -it scrapy_scrapyd_1 /bin/sh`. 
-  Navigate to `/var/lib/scrapyd` and then into your specific folder for your crawler.
-  Follow the Scrapy documentation to create a new crawler. You can start a new project by typing `scrapy startproject myproject <project_directory_name>` with "project_directory_name" being the name of your new project.
 
To run your script, type `scrapy crawl <spider-name> -o <file tpy eot save>`

And example is: `scrapy crawl basic -o nass.json`