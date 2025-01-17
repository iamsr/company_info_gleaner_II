# -*- coding: utf-8 -*-

# Scrapy settings for spider_51job_search project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

CODELTAFETCH_ENABLED = True
CODELTAFETCH_DIR = '/mnt/qinzhihao/search'


ITEM_PIPELINES = {
   'spider_51job_search.pipelines.CoDeltaFetch': 300,
   'spider_51job_search.pipelines.Spider51JobSearchPipeline': 200,
}

BOT_NAME = 'search_51job'

SPIDER_MODULES = ['spider_51job_search.spiders']
NEWSPIDER_MODULE = 'spider_51job_search.spiders'

# Exporting Settings
# FEED_URI = '/Users/Han/Desktop/Code/company_info_gleaner_II/spider_51job_search/%(name)s_20170610.txt'
# FEED_URI = '/root/users/JH/company_info_gleaner_II/spider_51job_search/%(name)s_20170610_名称海外.txt'
FEED_URI = '/mnt/qinzhihao/url_crawl/%(name)s_%(searchword)s_%(time)s.csv'
# FEED_URI = '%(name)s_%(time)s.csv'
FEED_FORMAT = 'csv'
FEED_STORAGES = {'file': 'scrapy.extensions.feedexport.FileFeedStorage',}
FEED_EXPORTERS = {'csv': 'spider_51job_search.items.TxtItemExporter',}
FEED_STORE_EMPTY = False
FEED_EXPORT_FIELDS = ["positionName",
                      "companyFullName",
                      "qc_job_loc",
                      "salary",
                      "qc_job_date",
                      "financeStage",
                      "companySize",
                      "industryField",
                      "description",
                      "qc_co_address"]
CSV_DELIMITER = "|"

# Logging Settings
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'search_51job.log'
LOG_LEVEL = 'INFO'
LOG_STDOUT = True

# Failure Retries
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [400,403,404,408,429,500,502,503]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'spider_51job_search.middlewares.RandomUserAgentMiddleware': 200,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 2
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

CONCURRENT_REQUESTS = 64
DOWNLOAD_DELAY = 0.25