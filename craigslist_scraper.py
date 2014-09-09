# H/T BMuller for the gist
# http://stackoverflow.com/questions/14634108/automate-python-script to automate and store in a daily csv

# To Do: Figure out how to pull just price AND figure out how to deal with the cragslist doesn't like me pinging them question 

from robostrippy.resource import attr, attrList, Resource

class Connection(Resource):
    subject = attr("h2.postingtitle")
    subject = attr("h2.{hasPrice}price")
    datetime = attr("time", attribute = "datetime")

class ConnectionListItem(Resource):
    url = attr("a", attribute = 'href')

    @property
    def details(self):
        return Connection(self.absoluteURL(self.url))

class ConnectionsList(Resource):
    connections = attrList("span.pl", ConnectionListItem)

clist = ConnectionsList('https://newyork.craigslist.org/bik/#list')

# List of cities for comps and NYC 5 boroughs for depth

for connection in clist.connections:
    print connection.details