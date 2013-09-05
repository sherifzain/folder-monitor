from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        print "Comment  :", data

parser = MyHTMLParser()