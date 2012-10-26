# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Day(Item):
    hall = Field()
    name = Field()
    absoluteWeek = Field()
    breakfast = Field()
    brunch = Field()
    lunch = Field()
    dinner = Field()
    lateNight = Field()


