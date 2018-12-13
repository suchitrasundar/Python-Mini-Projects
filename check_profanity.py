import urllib
def read_text():
    quotes = open("C:\Users\Suchitra Sundar\Desktop\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text) :
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q= "+text)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()
