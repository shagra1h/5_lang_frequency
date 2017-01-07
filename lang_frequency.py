import re
import operator
import sys
import os.path
from collections import Counter


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            filedata = input_file.read()
            filedata = filedata.lower().strip()
            return filedata


def get_most_frequent_words(text):
    words_in_text = re.findall(r'[\w]+', text)
    words_frequency = Counter(words_in_text)
    return words_frequency.most_common(10)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:
        print("You should specify a file to analyze!")
        sys.exit(0)
    if load_data(path_to_file):
        data_from_file = load_data(path_to_file)
    else:
        print("Incorrect path to the file!")
        sys.exit(0)
    lang_frequency = get_most_frequent_words(data_from_file)
    for word in lang_frequency:
        print("Word '%s' repeated in the text %s times" % (word[0], word[1]))
