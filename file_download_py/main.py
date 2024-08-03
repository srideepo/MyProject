# Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
urlroot1 = "https://www.k5learning.com/free-math-worksheets/fourth-grade-4/word-problems/fractions"
#urlroot1="https://www.k5learning.com/free-math-worksheets/fourth-grade-4"                           #filter only href like 'grade-4'
#urlroot1="https://www.k5learning.com/free-math-worksheets/fourth-grade-4/place-value-rounding"      #filter only href like 'place-value-rounding'
localfolder = "C:\\Users\\..\\Documents\\_MyDocuments\\Kids Learning\\grammar\\topics\\"
urlroot1="https://www.k5learning.com/free-grammar-worksheets/topics"
downloadurlroot = "https://www.k5learning.com"
# lists 
urls=[]
linkCount:int=0

# function created 
def scrape(site):
    try:
        _site = site
        _scope = _site.rsplit('/', 1)[-1]
        _linkCount = 0   
        # getting the request from url 
        r = requests.get(_site) 
        
        # converting the text 
        s = BeautifulSoup(r.text,"html.parser") 
        links = s.find_all("a")
        links_of_interest = [link.get('href') for link in links if _scope in str(link.get('href')) and link.get('href').startswith('/') and not(link.get('href').endswith(_scope))]
        #for i in s.find_all("a"): 
        for i in links_of_interest:
            #href = i.attrs['href'] 
            href = i
            #print('href>>', i)   
            if href.startswith("/") and len(href) > 1: 
                _site = downloadurlroot+href 
                
                if _site not in  urls:
                    urls.append(_site)
                    if(_site.endswith(".pdf")):
                        #print(_site)
                        downloadfile(_site) 
                    # calling it self 
                    scrape(_site)
    except Exception as ex:
        #print(type(ex))    # the exception type
        #print(ex.args)     # arguments stored in .args
        print(ex)          # __str__ allows args to be printed directly,
                            # but may be overridden in exception subclasses
        #x, y = ex.args     # unpack args
        #print('x =', x)
        #print('y =', y)
    
def downloadfile(url):
    _filename = url.rsplit('/', 1)[-1]
    response = requests.get(url)
    # Write content in pdf file
    pdf = open(localfolder + _filename, 'wb')
    pdf.write(response.content)
    pdf.close()
    print("File downloaded: ", _filename)

scrape(urlroot1)
print('>>>', len(urls))
