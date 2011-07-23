from BeautifulSoup import BeautifulSoup          # For processing HTML
import re, urllib, urllib2

def mapURL(index):
    options = { 0 : 1980,
                1 : 1985,
                2 : 1990, 
                3 : 1995, 
                4 : 2000, 
                5 : 2005 }
    return options[index]

#request links to magazines from 1980 - 2005
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

magazineYearURL=[];
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=1980#all_issues_anchor') #1980
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=1985#all_issues_anchor') #1985
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=1990#all_issues_anchor') #1990
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=1995#all_issues_anchor') #1995
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=2000#all_issues_anchor') #2000
magazineYearURL.append('http://books.google.com/books?id=b-8DAAAAMBAJ&source=gbs_all_issues_r&cad=1&atm_aiy=2005#all_issues_anchor') #2005

magazineURLs=[];
magazineDates=[];

#pull out href links to each magazine in the currently processed year
for url in range(len(magazineYearURL)):
    response = opener.open(magazineYearURL[url])
    soup = BeautifulSoup(response.read())
    for ele in soup.findAll("div", {"class" : "allissues_gallerycell"}):
        magazineURLs.append(str(ele.a['href']))
        magazineDates.append(mapURL(url))
    
#this operation can take some time so lets save it to a file
f = open('googleBooksUrlScrape.dat', 'w')
for url in magazineURLs:
    f.write("%s\n" % url)
f.close()

f = open('googleBooksDateScrape.dat', 'w')
for url in magazineDates:
    f.write("%s\n" % url)
f.close()