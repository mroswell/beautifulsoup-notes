from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep # be nice

drone_caucus_url = "http://unmannedsystemscaucus.mckeon.house.gov/about/membership.shtml"
# system("wget drone_caucus_url")

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

#def get_category_links(section_url):
#    soup = make_soup(section_url)
#    print soup
#    boccat = soup.find("dl", "boccat")
#    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
#    return category_links

#def get_members(category_url):
#    soup = make_soup(category_url)
#    category = soup.find("h1", "headline").string
#    caucus_name = "Unmanned Systems Caucus"
#    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
#    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
#    return {"caucus_name": caucus_name,
#            "category_url": category_url,
#            "winner": winner,
#            "runners_up": runners_up}

def get_members(membership_url):
    soup = make_soup(membership_url)
#    category = soup.find("h1", "headline").string
    caucus_name = "Unmanned Systems Caucus"
    cell = soup.findAll("td")
    for item in cell:
        if item != '<td valign="top" id="middlecopy">&nbsp;</td>' or item != '<td id="middlecopy" valign="top">&nbsp;</td>':
            print item
            print"\n"
    return {"caucus_name": caucus_name,
            "cell": cell}


if __name__ == '__main__':
    data = []
    themembers = get_members(drone_caucus_url)
    data.append(themembers)
    #print data
    sleep(1)


