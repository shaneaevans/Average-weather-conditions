import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from average_weather.items import AverageWeatherItem

class BbcSpider(CrawlSpider):
    name = 'bbc'
    allowed_domains = ['www.bbc.co.uk']
    start_urls = [
	"http://www.bbc.co.uk/weather/world/city_guides/index.shtml?show=%s_guides" % \
	chr(c) for c in range(97, 123)]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'results\.shtml'), 
		callback='parse_item', follow=True),
    )
   
    table_data = ('month', 'sunlight', 'avg_min_temp', 'avg_max_temp',
        'record_min_temp', 'record_max_temp', 'heat_discomfort', 'humidity_am',
        'humidity_pm', 'precipitation', 'wet_days')

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        location_data = hxs.select('//td/h2/text()').extract()
        location = location_data[0] if location_data else None
        for row in hxs.select('//tr[@bgcolor="#ffffff"]'):
            item = AverageWeatherItem(location=location)
            data = row.select('td/strong/text()|td/text()').extract()
            for i, name in enumerate(self.table_data):
                text = data[i]
                if text != '-':
                    item[name] = text
            yield item
