import scrapy


class ItclinicalSpider(scrapy.Spider):
    name = "itclinical"
    allowed_domains = ["itclinical.com"]
    start_urls = ["https://itclinical.com/ctms.php",
                  "https://itclinical.com/edc.php",
                  "https://itclinical.com/impo.php",
                  "https://itclinical.com/iwrs.php",
                  "https://itclinical.com/pharmacovigilance.php",
                  "https://itclinical.com/bibliovigilance.php"]

    def parse(self, response):
        #according to the webpage, the bulletpoints are <ul> elements with the class "check-list"
        bullet_points = response.css("ul.check-list li::text").getall()
        for point in bullet_points:
            print(point.strip())