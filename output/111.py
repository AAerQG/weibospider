import scrapy
import random

class RandomUserSpider(scrapy.Spider):
    name = 'random_user_spider'
    start_urls = [
        'https://weibo.com/u/3931333394'  # 替换为你的用户列表页面地址
    ]

    def parse(self, response):
        user_links = response.css('a.user-link::attr(href)').getall()
        random_user_link = random.choice(user_links)
        yield response.follow(random_user_link, callback=self.parse_user)

    def parse_user(self, response):
        user_id = response.css('div.user-id::text').get()
        yield {
            'user_id': user_id
        }
