import urllib.request

def read_text():
    quotes = open("/Users/shinji/Mydata/personalmarketing/english/canada/school/CICCC/subject/python/movie_quotes.txt")
    content_of_file  = quotes.read()
    print(content_of_file)
    check_content(content_of_file)
    quotes.close()

def check_content(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print("Result is " + output)
    connection.close()

read_text()
