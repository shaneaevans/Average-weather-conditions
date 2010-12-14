# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AverageWeatherItem(Item):
    location = Field()
    month = Field()
    sunlight = Field()
    avg_min_temp = Field()
    avg_max_temp = Field()
    record_min_temp = Field()
    record_max_temp = Field()
    heat_discomfort = Field()
    humidity_am = Field()
    humidity_pm = Field()
    precipitation = Field()
    wet_days = Field()
