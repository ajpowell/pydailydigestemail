'''
    createQuotesFile.py

    Pull down quotes from an API and store in a local csv file

    Use an api discussed here: https://forum.freecodecamp.org/t/free-api-inspirational-quotes-json-with-code-examples/311373

    Endpoint is: https://type.fit/api/quotes
    Returns: quotes in json array { "text": "quote", "author": "author" }

'''

from urllib.request import Request, urlopen
import json
from random import randint

api_endpoint = 'https://type.fit/api/quotes'
quotes_filename = 'quotes.csv'

def getQuotes(endpoint):
    # Note: need to specify a useragent else get a 403 Forbidden error
    req = Request(endpoint, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req,timeout=10)
    quotes = json.load(resp)

    #for quote in quotes:
    #    print(quote)
    #    print('==========================\n{}\n[ {} ]'.format(quote['text'], quote['author']))

    print('\nNumber of quotes: {}'.format(len(quotes)))

    return quotes

def writeQuotesToFile(quotes, filename):
    #print(quotes)
    # open the target file
    with open(filename, 'w') as quotesfile:
        header = 'text|author\n'
        quotesfile.write(header)
        for quote in quotes:
            print(quote)
            #print('==========================\n{}\n[ {} ]'.format(quote['text'], quote['author']))
            text = quote['text']
            author = quote['author']
            print(author)
            if author is None:
                author = 'Anon'
            line = text + '|' + author + '\n'
            quotesfile.write(line)

'''
    Get linecount for a file efficently - using enumerate means the file is not
    fully loaded into memory  - gets a line at a time
'''
def file_linecount(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getRandomQuoteFromFile(filename):
    linecount = file_linecount(filename)-1 # ignore the header!

    rand = randint(1,linecount)

    print('Getting quote No. {} or {}\n'.format(rand,linecount))

    # loop through the file to get to the row of interest
    with open(filename) as quotesfile:
        for i, line in enumerate(quotesfile):
            if i == rand:
                break

    # Parse out the values from the line
    quote = line.split('|')[0]
    author = line.split('|')[1][:-1] # Strip of last character as it is a newline!

    # Display the data
    print('{}\n{}'.format(quote, author))
    


if __name__ == '__main__':
    print('\ncreateQuotesFile.py\n')

    #quotes = getQuotes(api_endpoint)
    #writeQuotesToFile(quotes, quotes_filename)

    getRandomQuoteFromFile(quotes_filename)

    print('\nDone.\n')