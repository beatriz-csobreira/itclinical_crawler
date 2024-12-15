import scrapy


class ItclinicalSpider(scrapy.Spider):
    name = "itclinical"
    allowed_domains = ["itclinical.com"]
    start_urls = [
        "https://itclinical.com/ctms.php",
        "https://itclinical.com/edc.php",
        "https://itclinical.com/impo.php",
        "https://itclinical.com/iwrs.php",
        "https://itclinical.com/pharmacovigilance.php",
        "https://itclinical.com/bibliovigilance.php"
    ]
    
    url_to_name = {
        "https://itclinical.com/ctms.php": "CTMS",
        "https://itclinical.com/edc.php": "EDC",
        "https://itclinical.com/impo.php": "IMPO",
        "https://itclinical.com/iwrs.php": "IRT:IWRS",
        "https://itclinical.com/pharmacovigilance.php": "Pharmacovigilance",
        "https://itclinical.com/bibliovigilance.php": "Bibliovigilance"
    }

    url_to_data = {}
    response_count = 0

    def parse(self, response):
        # according to the webpage, the bulletpoints are <ul> elements with the class "check-list"
        bullet_points = response.css("ul.check-list li::text").getall()
        self.url_to_data[response.url] = [s.strip() for s in bullet_points]

        self.response_count += 1

        # only print on the last response, the bullet points in order of 'start_urls'
        if self.response_count == len(self.start_urls):
            for url in self.start_urls:
                print(f"\n{self.url_to_name[url]}\n")
                for point in self.url_to_data[url]:
                    print(f"\t{point}")
            print()