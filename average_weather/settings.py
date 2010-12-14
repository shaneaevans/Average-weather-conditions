# Scrapy settings for average_weather project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'average_weather'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['average_weather.spiders']
NEWSPIDER_MODULE = 'average_weather.spiders'
DEFAULT_ITEM_CLASS = 'average_weather.items.AverageWeatherItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

