import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#import nltk
#nltk.download('stopwords')
#nltk.download('punkt')

class WikiScraper:
    word_count = None
    filter_stop_words = True

    def __init__(self, start_url):
        self.url = start_url

    def request_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print("Failed to fetch page:", response.status_code)
            return None

    def get_words_with_count_in_class(self, url, class_name):
        response = self.request_url(url)

        if response:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find elements with the specified class
            target_elements = soup.find_all(class_=class_name)
            
            # Extract text from those elements
            text = ' '.join(element.get_text() for element in target_elements)


            if self.filter_stop_words:
                stop_words = set(stopwords.words('english'))
                word_tokens = word_tokenize(text)
                filtered_sentence  = [w for w in word_tokens if not w.lower() in stop_words]
                text = ' '.join(filtered_sentence )
            
            # Extract words using regular expression
            words = re.findall(r'\b\w+\b', text)

            # Count the frequency of each word
            self.word_count = Counter(words)
            self.total_word_count = sum(self.word_count.values())
            
            return self.word_count

    def get_unique_word_count(self):
        return len(self.word_count)
    
    def get_total_word_count(self):
        return self.total_word_count

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    scraper = WikiScraper(url)
    words = scraper.get_words_with_count_in_class(url, "mw-body-content")

    if words:
        print("Total words:", scraper.get_total_word_count())
        print(words)