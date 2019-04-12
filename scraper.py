import bs4
import requests
import pandas as pd
import re
agent = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
session = requests.session()
'''url = 'https://www.yellowpages.com.au/search/listings?clue=African+Violets+%28Nurseries-Retail%29&locationClue=south+australia&lat=&lon=&selectedViewMode=list'
data = requests.get(url,headers=agent)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
'''
#this part is for scraping name of bussines
names = []
phone = []
links = []
with open('log.txt','a') as p:
    p.write("\n---------------------------------------------------------------------")
last = int(input("Enter last page number of that : "))
for c in range(1,last+1):
            url = 'https://www.yellowpages.com.au/search/listings?clue=Footwear+Wholesalers+%26+Manufacturers&locationClue=australia&pageNumber={0}&referredBy=www.yellowpages.com.au&&eventType=pagination'.format(c)

            with open('log.txt','a') as f:
                f.write("\n{0}".format(url))
            data = requests.get(url,headers=agent)
            soup = bs4.BeautifulSoup(data.text, 'html.parser')
            #NAMES
            for div in soup.find_all('div',{'class':'listing listing-search listing-data'}):
                if div.find_all('a',{'class':'listing-name'}):
                    names.append(div.find('a',{'class':'listing-name'}).text)
                else:
                    names.append('None')
             #PHONE       
            for div in soup.find_all('div',{'class':'listing listing-search listing-data'}):
                if div.find_all('a',{'class':'click-to-call contact contact-preferred contact-phone '}):
                    phone.append(div.find('a',{'class':'click-to-call contact contact-preferred contact-phone '}).get("href"))
                elif div.find_all('a',{'class':'click-to-call contact contact-preferred contact-mobile '}):
                    phone.append(div.find('a',{'class':'click-to-call contact contact-preferred contact-mobile '}).get("href"))
                else:
                    phone.append('None')
             #EMAIL
            for div in soup.find_all('div',{'class':'listing listing-search listing-data'}):
                if div.find_all('a',{'class':'contact contact-main contact-email '}):
                    links.append(div.find('a',{'class':'contact contact-main contact-email '}).get("data-email"))
                else:
                    links.append('None')
            
            '''for nxtpage in soup.find_all(class_=re.compile("pagination navigation")):
                nextPageLink = nxtpage.get('href')
                nextPageLink = 'https://www.yellowpages.com.au'+nextPageLink
                print(nextPageLink)
                agent = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
                session = requests.session()
                data = requests.get(nextPageLink,headers=agent)
                soup = bs4.BeautifulSoup(data.text, 'html.parser')
                #name = [name.text for name in soup.find_all('a',class_="listing-name")]
                for nam in soup.find_all('a',class_='listing-name'):
                    name.append(nam.text)
                #phone = [anc.text for anc in soup.find_all('span',{'class':'contact-text'})]i
                phone = []
                for phon in soup.find_all('span',{'class':'contact-text'}):
                    phone.append(phon.text)
                for p1 in phone:
                    number = ['0','1','2','3','4','5','6','7','8','9']
                    if p1[0] == "(" or p1[0] in number:
                        newP.append(p1)
                    else:
                        pasis
                for div in soup.find_all('a'):
                    if div.get("data-email"):
                        email.append(div.get("data-email"))
                    else :
                        pass'''
            '''print(name)
            print(newP)
            print(email)
            c=0
            for _ in email:
              c+=1
              print("{0}.{1}".format(c,_))'''
            print(url)


else:
    #print(name)
    #print(newP)
    #print(email)
    a=0 
    for _ in links:
        a+=1
        #print("{0}.{1}".format(a,_))
    print(a)
    b=0
    for _ in names:
        b+=1
        #print("{0}.{1}".format(b,_))
    print(b)
    c=0
    for _ in phone:
        c+=1
        #print("{0}.{1}".format(c,_))
    print(c)
    bname = input("Enter file name: ")
    raw_data = {
            'Name':names,
            'Phone':phone,
            'Emails':links,
            }
    df = pd.DataFrame(raw_data,columns = ['Name','Phone','Emails'])
    df.to_csv('{0}.csv'.format(bname))
    
    with open('log.txt','a') as q:
        q.write("\n------------------------------------------------------------------")
    print("Done...")
    




