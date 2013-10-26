# A script that parses the wikipedia page into JSON.
# run wget wget http://en.wikipedia.org/wiki/List_of_mobile_country_codes
# then this..
from BeautifulSoup import BeautifulSoup

html = open('List_of_mobile_country_codes', 'r')

soup = BeautifulSoup(html)

data = []

for table in soup.findAll('table', attrs={'class': 'wikitable'}):
    for row in table.findAll('tr'):
        mcc, mnc, brand, operator = row.findChildren()[:4]
        if mcc.text in ['MCC', '']:
            continue
        print u'        Operator("{0}", "{1}", "{2}", u"{3}"),'.format(
            mcc.text, mnc.text, brand.text, operator.text)

