import scrapy;import json
from academy.items import AcademyItem

class myspider(scrapy.Spider):
    name="myspider"
    start_urls = [
    "https://academyit.net/products/courses?page=6",            
    # "https://academyit.net/products/courses?page=5",        
    # "https://academyit.net/products/courses?page=4",        
    # "https://academyit.net/products/courses?page=3",        
    # "https://academyit.net/products/courses?page=2",            
    # "https://academyit.net/products/courses?page=1",               
    ]
    def parse(self,response):
        items = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div").extract()
        for num, item in enumerate(items):
            obj = AcademyItem()
            obj["title"] = response.xpath('/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div[{}]/article/div[1]/a/h2/text()'.format(num+1)).get()
            obj["teacher"] = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div/div/div[{}]/article/div[1]/div/span/a/text()".format(num+1)).get()         
            obj["price"] = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div[{}]/article/div[2]/div/span[2]/span[last()]/text()".format(num+1)).get()
            if obj["price"] == "تومان":
                obj["price"] = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div[{}]/article/div[2]/div/span[2]/span[2]/text()".format(num+1)).get()
            obj["image"] = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div[{}]/article/header/figure/a/img/@src".format(num+1)).get()
            obj["url"] = response.xpath("/html/body/div[1]/section[2]/div/div[2]/div[2]/div/div[{}]/article/header/figure/a/@href".format(num+1)).get()
            print(obj)