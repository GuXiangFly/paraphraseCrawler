from crawlerweb.crawler_bing import CrawlerWeb
from crawlerweb.crawler_web_with_proxy import CrawlerWebWithProxy

if __name__ == '__main__':
    crawler_web = CrawlerWeb()
    crawler_web.run("bing")
    # crawler_web = CrawlerWebWithProxy()
    # crawler_web.run("bing")
