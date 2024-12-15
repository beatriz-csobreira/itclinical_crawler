# README

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
- Go through the URLs of the "Our Software" section
- Extract the "Features" bulletpoints of each subsection of "Our Software"
- Optionally: write extracted information to a .csv