from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from myproject.items import Day

class NucuisineSpider(CrawlSpider):
    name = 'nucuisine'
    allowed_domains = ["nucuisine.com"]
    start_urls = ["http://www.nucuisine.com/menus/"]
    
    rules = (
             Rule(SgmlLinkExtractor(allow=r'1\.html', deny=[r'willies',r'tech']), callback='parse_item', follow=True),
             )
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        dayOfWeek = ['"monday"','"tuesday"','"wednesday"','"thursday"','"friday"','"saturday"','"sunday"']
        items = []
        for day in dayOfWeek:
            tempWeek = hxs.select('//tr/td[@class="titlecell"]//text()').extract()[2]
            #site = hxs.select('//tr//td[@id=' + day + ']')
            item = Day()
            item['hall'] = hxs.select('//tr/td[@class="titlecell"]/span[1]//text()').extract()
            item['absoluteWeek'] = tempWeek[15:]
            item['name'] = day.strip('"')
            item['breakfast'] = hxs.select('//tr//td[@id=' + day + ']//tr[@class="brk"]//td[@class="menuitem"]//div[@class="menuitem"]//span[@class="ul"]//text()').extract()
            item['lunch'] = hxs.select('//tr//td[@id=' + day + ']//tr[@class="lun"]//td[@class="menuitem"]//div[@class="menuitem"]//span[@class="ul"]//text()').extract()
            item['dinner'] = hxs.select('//tr//td[@id=' + day + ']//tr[@class="din"]//td[@class="menuitem"]//div[@class="menuitem"]//span[@class="ul"]//text()').extract()
            items.append(item)
        return items