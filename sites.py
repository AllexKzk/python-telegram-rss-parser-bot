import siteParser

def parse(name): 
	return parseDict[name]["f"](parseDict[name]["url"], name) #call func from dict

parseDict = {
  "ESA Space Science": 		
					{"f": siteParser.rssParser, 
					 "url": "https://www.esa.int/rssfeed/Our_Activities/Space_Science"
					 },
  "NASA Breaking News": 
					{"f": siteParser.rssParser, 
					 "url": "https://www.nasa.gov/rss/dyn/breaking_news.rss"
					 },
  "NASA Image of the Day":
  				{"f": siteParser.rssParser, 
					 "url": "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
					 },
  "Astronomy & Astrophysics Press release":
  					{"f": siteParser.rssParser, 
					 "url": "http://feeds.feedburner.com/aa_pressreleases?format=xml"
					 },
  "Naked Science Astronomy":
  					{"f": siteParser.rssParser, 
					 "url": "https://naked-science.ru/article/category/astronomy/feed"
					 },
  "Naked Science Space projects":
  					{"f": siteParser.rssParser, 
					 "url": "https://naked-science.ru/article/category/cosmonautics/feed"
					 },
  "Naked Science Space posts":
  					{"f": siteParser.rssParser, 
					 "url": "https://naked-science.ru/article/category/nakedscience/feed"
					 }
}