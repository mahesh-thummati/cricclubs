## Below are the steps to use this code in your desktop
### 1. git clone this repo into your desktop dir your-local-path
### 2. install scrapy
### 3. cd your-local-path/cricclubs
### 4. to scrape bazookas scores for non-srcl tournaments run below command
#### scrapy crawl get_data_non_srcl -L ERROR 
### 5. to scrape bazookas scores for srcl tournaments run below command
#### scrapy crawl get_data_srcl -L ERROR
### 6. data will be stored as csv files in your-local-path/output/

