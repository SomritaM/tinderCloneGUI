from bs4 import BeautifulSoup as soup
import requests

my_url = "http://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=off"
r = requests.get(my_url)

flip_soup = soup(r.content, "html.parser")

containers = flip_soup.find_all("div",{"class":"_1-2Iqu row"})
#print(soup.prettify(containers[0]))
f = open("products.csv","a",encoding='utf8')
for container in containers:
    name = container.find_all("div",{"class":"_3wU53n"})
    print(name[0].text)

    cost = container.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    print(cost[0].text)
    rating = container.find_all("div",{"class":"niH0FQ"})
    print(rating[0].text,"\n")

    f.write(name[0].text+"  "+cost[0].text+"  "+rating[0].text+"\n")
f.close()