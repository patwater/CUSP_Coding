
import lxml
import urllib2


response = urllib2.urlopen('https://www.techmeme.com')
html = response.read()

dom = parse(html)
links = dom.cssselect('href')

print links



"""
Html_file= open("google.html","w")
Html_file.write(html)
Html_file.close()

"""