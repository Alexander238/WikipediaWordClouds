from word_bubble import WordBubbles
import matplotlib.pyplot as plt
import wiki_scraper

def split_dictionary(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys, values

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    scraper = wiki_scraper.WikiScraper(url)
    words = scraper.get_words_with_count_in_class(url, "mw-body-content")

    identifiers, values = split_dictionary(words)

    W_Bubble = WordBubbles(identifiers, values)
    fig, ax = plt.subplots()
    W_Bubble.plot(ax, "")

    plt.show()