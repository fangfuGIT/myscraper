# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import JobBoleArticleItem
from ArticleSpider.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1、获取文章列表页中的文章url并交给scrapy下载后进行解析
        2、获取下一页url信息并交给scrapy进行下载，下载完成后交给parse
        """
        # post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            image_url = post_node.css("::attr(src)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)

        #提取下一页并交给scrapy下载
        next_urls = response.css(".next.page-numbers ::attr(href)").extract_first()
        if next_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)


    def parse_detail(self, response):
        #提取文章的具体字段，通过xpath提取
        # title = response.xpath('//*[@class="grid-8"]/div[1]/div[1]/h1/text()').extract_first()
        # get_date = response.xpath("//*[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·", "").strip()
        # praise_nums = response.xpath("//*[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        #
        # fav_nums = response.xpath("//*[contains(@class, 'bookmark-btn')]/text()").extract()[0].strip()
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = match_re.group(1)
        #
        # comments_nums = response.xpath("//a[contains(@href, '#article-comment')]/span/text()").extract()[0].strip()
        # match_re = re.match(".*?(\d+).*", comments_nums)
        # if match_re:
        #     comments_nums = match_re.group(1)
        #
        # content = response.xpath("//div[@class='entry']").extract()[0]
        # tag_list = response.xpath("//*[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [num for num in tag_list if not num.strip().endswith("评论")]
        # tags = ",".join(tag_list)


        article_item = JobBoleArticleItem()


        #通过CSS选择器提取字段
        front_image_url = response.meta.get("front_image_url", "")
        title = response.css(".entry-header h1::text").extract()[0]
        create_data = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comments_nums = response.css(".hide-on-480::text").extract()[2].strip()
        match_re = re.match(".*?(\d+).*", comments_nums)
        if match_re:
            comments_nums = int(match_re.group(1))
        else:
            comments_nums = 0

        content = response.css("div.entry").extract()[0]
        tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
        tag_list = [num for num in tag_list if not num.strip().endswith("评论")]
        tags = ",".join(tag_list)

        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        article_item["create_date"] = create_data
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["fav_nums"] = fav_nums
        article_item["comments_nums"] = comments_nums
        article_item["tags"] = tags
        article_item["content"] = content

        yield article_item

        pass





