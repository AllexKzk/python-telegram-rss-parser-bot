from bs4 import BeautifulSoup
from replit import db                   #replit database. Just replace on yours for file/db
from requests_html import HTMLSession
import bs4 as bs
import requests
import time

postPattern = {
	"title": "",
	"description": None,
	"link": ""
}

def check(name, newHead): #is it new post
  if name in db.keys() and db[name] == newHead:
    return False
  return True

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def rssParser(url, name):
  response = requests.get(url, headers = headers) #send req

  doc = bs.BeautifulSoup(response.text, 'xml') #parse res
  item = doc.item #get <item> block
  if not item:    #if no item
    return None   #you can rewrite this block for your aim
  headtext = item.title.text
  if not check(name, item.title.text):
    return None
  db[name] = item.title.text #add to db as checked

  post = postPattern.copy()
  post["title"] = name
  post["link"] = item.link.text
  
  return post
