from scrapy import cmdline

# cmdline.execute('scrapy crawl tongcheng_spider'.split())
cmdline.execute('scrapy crawl tongcheng_spider -o tongcheng.csv'.split())