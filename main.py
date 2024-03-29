from bs4 import BeautifulSoup
import requests

def main(url):
    output = ''
    xml_data = requests.get(url).content
    soup = BeautifulSoup(xml_data, "lxml")
    child = soup.find("item")
    for i in range(3):
        output = output + 'Article ' + str(i+1) + ': ' +child.findChild("title").text + '. \n'
        child = child.findNextSibling()
    return output

def businessNews():
    return(main("https://www.cnbc.com/id/10001147/device/rss/rss.html"))
    
def worldNews():
    return(main("https://www.cnbc.com/id/100727362/device/rss/rss.html"))

def topNews():
    return(main("https://www.cnbc.com/id/100003114/device/rss/rss.html"))

def earningsNews():
    return(main("https://www.cnbc.com/id/15839135/device/rss/rss.html"))

def realEstateNews():
    return(main("https://www.cnbc.com/id/10000115/device/rss/rss.html"))

def healthCareNews():
    return(main("https://www.cnbc.com/id/10000108/device/rss/rss.html"))

def mediaNews():
    return(main("https://www.cnbc.com/id/10000110/device/rss/rss.html"))

def techNews():
    return(main("https://www.cnbc.com/id/19854910/device/rss/rss.html"))

def financeNews():
    return(main("https://www.cnbc.com/id/10000664/device/rss/rss.html"))    

def derivativesNews():
    return(main("https://www.risk.net/feeds/rss/category/derivatives/equity-derivatives"))    

if __name__ == "__main__":
    print(businessNews())
    print(worldNews())
    print(topNews()) 
    print(earningsNews()) 
    print(realEstateNews()) 
    print(healthCareNews()) 
    print(mediaNews()) 
    print(techNews()) 
    print(financeNews()) 
    print(derivativesNews()) 
    
