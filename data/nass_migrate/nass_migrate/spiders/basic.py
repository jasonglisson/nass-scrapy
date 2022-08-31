import scrapy
from scrapy import Spider, Request
from six.moves.urllib.parse import urljoin

class BasicSpider(scrapy.Spider):
    name = "basic"
    start_urls = ['https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/']

    def parse(self, response):
        surveys = response.xpath('//*[@id="field_body"]/ul/li/a/@href').extract()
        for s in surveys:
            url = urljoin(response.url, s)

            yield scrapy.Request(url, callback=self.parse_link)

    def parse_link(self, response):
        for info in response.css('div#field_body'):
            # alt_title = response.xpath('text()')
            yield {
                'survey_name': info.css('h4.survey-title::text').extract_first(),
                'referring_url' : response.request.url,
                'banner_image_urls' : info.xpath('//*[@id="field_body"]/img/@src').extract_first(),
                'body' : info.xpath('//*[@id="field_body"]/p/text()').getall(),
                'about' : info.xpath('//*[@id="about"]/*').getall(),
            }