from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from myproject.items import Day, FoodItem

class MenuItemSpider(CrawlSpider):
    name = 'menuitem'
    allowed_domains = ["nucuisine.com"]
    start_urls = ["http://www.nucuisine.com/menus/"]
    
    rules = (
             Rule(SgmlLinkExtractor(allow=r'[0-9]\.html', deny=[r'willies',r'tech']), callback='parse_item', follow=True),
             )


    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        menuitems = hxs.select('//tr//td//tr//td[@class="menuitem"]//div[@class="menuitem"]')
        for mi in menuitems:
            item = FoodItem()
            itemname =  mi.select('.//span[@class="ul"]/text()')[0].extract()
            item['name'] = itemname
            item['g'] = bool(mi.select('.//img[@alt="Vegan"]'))
            item['v'] = bool(mi.select('.//img[@alt="Vegetarian"]'))
            item['w'] = bool(mi.select('.//img[@alt="Well-Balanced"]'))

            if any(x for x in items if x['name'] == itemname):
                pass
            else:
                items.append(item)

        return items