# README

## How To Use

### Prerequisites

- Python 3 installed
- Scrapy installed (via conda or pip)

### Run

```sh
git clone git@github.com:beatriz-csobreira/itclinical_crawler.git
cd itclinical_crawler/itclinical_crawler/
scrapy crawl itclinical --nolog
```

## TODO

- Create a virtual environment ("itclinical_crawler")
```sh
    conda create -n itclinical_crawler
    conda activate itclinical_crawler
```
- Install scrapy and check installation
```sh
    conda install -c conda-forge scrapy
    scrapy --version
```
- Read scrapy tutorial (https://docs.scrapy.org/en/latest/intro/tutorial.html) and create first spider for ITClinical webpage (https://itclinical.com/it.php)
```sh
    scrapy startproject itclinical_crawler
    cd itclinical_crawler
    scrapy genspider itclinical https://itclinical.com/it.php
```
- Go through the URLs of the "Our Software" section
- Extract the "Features" bulletpoints of each subsection of "Our Software"
- Optionally: write extracted information to a .csv