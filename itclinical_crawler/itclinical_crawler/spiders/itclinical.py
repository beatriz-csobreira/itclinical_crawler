import scrapy


class ItclinicalSpider(scrapy.Spider):
    name = "itclinical"
    allowed_domains = ["itclinical.com"]
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        print(response)
