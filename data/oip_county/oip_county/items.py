# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OipCountyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ref_st = scrapy.Field() 
    ref_cnty = scrapy.Field() 
    county_url = scrapy.Field() 
    org_unit_id = scrapy.Field() 
    agcy_abr = scrapy.Field() 
    org_unit_name = scrapy.Field() 
    site_nm = scrapy.Field() 
    cnty_nm = scrapy.Field()
    st_cd = scrapy.Field() 
    cnty_cd = scrapy.Field() 
    str_city_nm = scrapy.Field() 
    str_st_abr = scrapy.Field() 
    str_zip_cd = scrapy.Field() 
    str_dlvy_adr = scrapy.Field() 
    cnty_nm = scrapy.Field() 
    site_phn_nbr = scrapy.Field() 
    site_phn_ext = scrapy.Field() 
    org_unit_phn_nbr = scrapy.Field() 
    org_unit_phn_extn = scrapy.Field() 
    org_unit_poc_phn_nbr = scrapy.Field() 
    org_unit_poc_phn_extn = scrapy.Field() 
    org_unit_fax_nbr = scrapy.Field() 
    org_unit_poc_fax_nbr = scrapy.Field()     
    site_fax_nbr = scrapy.Field() 
    org_unit_poc_nm = scrapy.Field() 
    org_unit_poc_email_adr = scrapy.Field() 
    site_id = scrapy.Field()         

    pass
