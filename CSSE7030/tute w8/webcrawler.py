__copyright__ = "Copyright 2018, University of Queensland"


from html.parser import HTMLParser
import urllib
import urllib.request


# Write the LinkParser class here
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()  # as rawdata in HTMLParser super class
        self.urls = []
    
    def handle_starttag(self, tag, attrs):  # attrs - attributes
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href':
                    self.urls.append(val)

    def get_urls(self):
        return self.urls
                

def find_links(url) :
    """Return a list of links from the given Web page.

    Return:
        (list[str]): List of all links found at the given URL.
    """
    # Open the webpage and read the HTML text
    fd = urllib.request.urlopen(url)
    text = fd.read()
    fd.close()

    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(str(text)) # Need to convert text to a str as read gives a
                           # bytes type which feed cannot process
                           # feed is a method of LinkParser class

    # Write a return statement here
    return parser.get_urls()


print(find_links('http://www.google.com/'))
