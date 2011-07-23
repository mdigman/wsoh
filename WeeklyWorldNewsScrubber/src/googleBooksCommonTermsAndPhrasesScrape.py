from BeautifulSoup import BeautifulSoup          # For processing HTML
import re, urllib, urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#load full set of urls to scrape
f = open("googleBooksUrlScrape.dat", "r")
magazineURLs = f.readlines()
f.close

f = open("googleBooksDateScrape.dat", "r")
magazineDates = f.readlines()
f.close

#now we have the url of every magazine from 1980 - 2005
#common terms and phrases are listed alphebetically with a quantized size to distinguish reoccurance of words
#terms do not common English constructs like "the" but they do include many proper nouns, may need to filter later

#dump EVERYTHING
f = open('googleBooksData.dat', 'w')

for url in range(len(magazineURLs)):
    print "%d of %d : %d%% complete" % (url, len(magazineURLs), 100*url/len(magazineURLs))
    response = opener.open(magazineURLs[url])
    soup = BeautifulSoup(response.read())
    for ele in soup.findAll("a", {"class" : "cloud0"}):
        #print "%s, %s, %s" % (str(ele.string), "0",  magazineDates[url])
        f.write("%s, %s, %s" % (str(ele.string), "0",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud1"}):
        f.write("%s, %s, %s" % (str(ele.string), "1",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud2"}):
        f.write("%s, %s, %s" % (str(ele.string), "2",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud3"}):
        f.write("%s, %s, %s" % (str(ele.string), "3",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud4"}):
        f.write("%s, %s, %s" % (str(ele.string), "4",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud5"}):
        f.write("%s, %s, %s" % (str(ele.string), "5",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud6"}):
        f.write("%s, %s, %s" % (str(ele.string), "6",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud7"}):
        f.write("%s, %s, %s" % (str(ele.string), "7",  magazineDates[url]))
    for ele in soup.findAll("a", {"class" : "cloud8"}):
        f.write("%s, %s, %s" % (str(ele.string), "8",  magazineDates[url]))
    f.close()
    f = open('googleBooksData.dat', 'a')

