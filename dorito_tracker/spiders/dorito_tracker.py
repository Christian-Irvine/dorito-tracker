from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "dorito_tracker"

    def start_requests(self):
        urls = [
            "https://grocer",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"grocer-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")