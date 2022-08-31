import scrapy

class FarmersSpider(scrapy.Spider):
    name = "farmers2"
    
    def start_requests(self):
        
        # The USDA OIP data URL sans the ID at the end
        base_link = 'https://offices.usda.gov/locator/eForms?form=1&office='
        
        # This is the number of pages we want to crawl
        n_pages = 140000
        
        # We are starting at 1 and crawling URLs until we get to n_pages
        for i in range (66680,n_pages+1):
            # Loop through IDs at the end of the URL
            url = base_link+str(i)
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        for site in response.css('office'):
            yield {
                'id': site.xpath('@id').extract_first(),
                'site_id': site.xpath('//site/@id').extract_first(),
                'status': site.css('status::text').extract_first(),
                'mailingAddress': site.css('mailingAddress address::text').extract_first(),
                'mailingCity': site.css('mailingAddress city::text').extract_first(),
                'mailingState': site.css('mailingAddress state::text').extract_first(),
                'mailingZip': site.css('mailingAddress zipCode::text').extract_first(),                                              
                'latitude': site.css('latitude::text').extract_first(),
                'longitude': site.css('longitude::text').extract_first(),
                'phone': site.css('contact phone::text').extract_first(),                                                                                   
            }


