import requests as r
from bs4 import BeautifulSoup as bs

import json
import UserAgents as ua
import random

def createUserAgents():
    return f"User-Agent : ${ua.UserAgents[random.randint(0,len(ua.UserAgents)-1)]}"
    
def createRiskyUserAgents():
    return f"User-Agent : ${ua.RiskyUserAgents[random.randint(0,len(ua.RiskyUserAgents)-1)]}"

def get(url):
    headers = createRiskyUserAgents()
    page = r.get(url,headers)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

def save_to_csv(emails):
    try:
        with open('psp_emails.csv', 'w') as out:
            for email in emails:
                out.write(email + ",")
    except IOError:
        print("I/O error") 

def psp(url):
    psp_soup = soup(get(url))
    urls = []
    for span in psp_soup.find_all("span", class_="name"):
        span = span.find("a")
        href = span.get("href")
        url = f"https://www.psp.cz/sqw/{href}"
        urls.append(url)
    print(urls)
    emails = []
    for url in urls:
        psp_detail_soup = soup(get(url))
        emails.append(psp_detail_soup.find_all("li", class_="mail")[0].text)
    print(emails)
    save_to_csv(emails)
def Main():
    psp_url = "https://www.psp.cz/sqw/hp.sqw?k=192"
    psp(psp_url) 
    """
Parse your things here from the soup object - suggest using things like find_all("a", class_="sister") / you can also use list ("a", ["stylelistrowone", "stylelistrow"])
expected usage is soup(get("https://example.com")) and then anything you love.

Scrape the world! 
"""
Main()
