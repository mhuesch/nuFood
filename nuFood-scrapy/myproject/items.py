# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Day(Item):
    name = Field()
    absoluteWeek = Field()
    breakfast = Field()
    lunch = Field()
    dinner = Field()
    lateNight = Field()


