import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["coppel.com"]
    start_urls = (
        'https://coppel.com/mejores-ofertas/',
    )

    def parse(self, response):
        productos = response.xpath('//div[@class="product clearfix enlace-listado"]')
        for product in productos:
            product_name = product.xpath('.//p[@class="m0"]/text()').extract_first()
            price = product.xpath('.//div[@class="pcontado"]/input/@value').extract_first()

            yield{
                'Product': product_name,
                'Price': price
            }
        