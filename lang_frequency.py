import re
import operator
import sys
import os.path


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            filedata = input_file.read()
            filedata = filedata.strip()
            return filedata


def get_most_frequent_words(text):
    words_in_text = re.findall(r'[\w]+', text)
    words_frequency = {}
    for word in words_in_text:
        word = word.lower()
        if word in words_frequency.keys():
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    return sorted(words_frequency.items(), key=operator.itemgetter(1), reverse=True)


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
    for iterator, word in enumerate(lang_frequency):
        print("Word '%s' repeated in the text %s times" % (word[0], word[1]))
        if iterator >= 9:
            break
