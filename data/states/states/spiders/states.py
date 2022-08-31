import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapy import Spider, Request

class ApiItem(scrapy.Item):
    fips = scrapy.Field()
    cnty_nm = scrapy.Field()
    cnty_cd = scrapy.Field()
    st_cd = scrapy.Field() 
    state = scrapy.Field()       

class StatesSpider(XMLFeedSpider):
    name = 'states'
    allowed_domains = ['www.nrcs.usda.gov']
    start_urls = ['https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697']
 
    def parse(self, response):
        fips = response.xpath('//*[@id="detail"]/table//tr')
        for fip in fips[1:]:
            item = ApiItem()
            item['fips'] = fip.xpath('td[1]//text()').extract()[0].strip()
            parts = item['fips']
            st = parts[:2]
            cnty = (parts[-3:])
            item['st_cd'] = st
            item['cnty_cd'] = cnty
            item['cnty_nm'] = fip.xpath('td[2]//text()').extract()[0].strip()
            item['state'] = fip.xpath('td[3]//text()').extract()[0].strip()
            yield {
                'state' : item['state'],              
                'st_cd' : st,
                'cnty_cd' : cnty,
                'fips' : parts,
                'cnty_nm' : item['cnty_nm'],
            }    

    # def parse(self, response):
    #     jsonresponse = json.loads(response.body_as_unicode())

        # item = ApiItem()
        # item["state"] = jsonresponse[0]            

        # return item

        # for state in jsonresponse:
        #     item = ApiItem()
        #     # item['state'] = {}
        #     item['state'] = state
        #     item['st_cd'] = state:[{"st_cd"}]
        #     state_holder = {state: {"st_cd": 'test'}}
        #     yield state_holder

# class ExampleSpider(scrapy.Spider):
#     name = 'API'
#     allowed_domains = ["site.com"]
#     start_urls = [l.strip() for l in open('pages.txt').readlines()]

#     def parse(self, response):
#         filename = response.url.split("/")[-2]
#         open(filename, 'wb').write(response.body)
#         jsonresponse = json.loads(response.body_as_unicode())
#         item = ApiItem()
#         item["url"] = jsonresponse["uri"]
#         item["Name"] = jsonresponse["name"]
#         return item