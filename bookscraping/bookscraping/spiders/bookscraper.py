import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            title = book.css('h3 a::text').get()
            price = book.css('div.product_price .price_color::text').get()
            url = book.css('h3 a').attrib['href'],

            yield {
                'title': title,
                'price': price,
                'url': url,
            }