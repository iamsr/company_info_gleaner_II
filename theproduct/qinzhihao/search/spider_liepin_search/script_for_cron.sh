#!/bin/sh
echo "hi, pretty~" > logpretty.txt
/usr/local/bin/scrapy crawl lpsearch -a searchword=海外 > log1 2>&1 &
/usr/local/bin/scrapy crawl lpsearch -a searchword=驻外 > log2 2>&1 &
/usr/local/bin/scrapy crawl lpsearch -a searchword=国外 > log3 2>&1 &
/usr/local/bin/scrapy crawl lpsearch -a searchword=美国 > log4 2>&1 &
/usr/local/bin/scrapy crawl lpsearch -a searchword=欧洲 > log5 2>&1 &

