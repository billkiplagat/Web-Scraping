# Web Scraping for Jobs on www.timesjobs.com

This project utilizes Python 3 and the BeautifulSoup library to scrape job details from www.timesjobs.com. The script extracts information such as job publish date, company name, skills needed, and the link to apply for each job listing.

# Prerequisites
To run this project, you'll need the following:

* Python 3.x installed on your machine.
* The BeautifulSoup library installed. You can install it by running the following command:

```pip install beautifulsoup4```

# Usage
1. Open the timesjobs_scraper.py file in a text editor or an Integrated Development Environment (IDE) of your choice.
2. Modify the URL variable in the script to specify the URL of the job listings page on www.timesjobs.com that you want to scrape.
3. Run the script by executing the following command in your terminal or command prompt:

```python timesjobs_scraper.py```
4. The script will retrieve the job details from the specified URL and display them in the console. The job details will include the job publish date, company name, skills needed, and the link to apply for each job listing.

# Note:!!
Make sure you install the lxml parser library by running the following command:

```pip install lxml```