import string
from data_structures.hashtable import Hashtable


def first_repeated_word(book: str) -> str:
    formatted_book = book.translate(str.maketrans("", "", string.punctuation)).split()
    print(formatted_book)
    words = {}
    for word in formatted_book:
        if word.lower() in words.keys():
            return word.lower()
        else:
            words[word.lower()] = 1
    return "No words were repeated"


if __name__ == "__main__":
    first_test = "Once upon a time, there was a brave princess who..."
    second_test = ("It was the best of times, it was the worst of times, it was the age of wisdom, "
                   "it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, "
                   "it was the season of Light, it was the season of Darkness, it was the spring of hope, it was "
                   "the winter of despair, we had everything before us, we had nothing before us, we were all going "
                   "direct to Heaven, we were all going direct the other way – in short, the period was so far like "
                   "the present period, that some of its noisiest authorities insisted on its being received, for "
                   "good or for evil, in the superlative degree of comparison only...")
    third_test = ("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and "
                  "I didn’t know what I was doing in New York...")
    fourth_test = "Over the rainbow, and through the fields"
    fifth_test= "He counted 100 fishes and 100 fishes ..."
    print(first_repeated_word(first_test))
    print(first_repeated_word(second_test))
    print(first_repeated_word(third_test))
    print(first_repeated_word(fourth_test))
    print(first_repeated_word(fifth_test))


