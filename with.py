# import io
# from pprint import pprint
#
# name = 'sample2.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         for char in line:
#             # print(line, end='')
#             print(char, end='')
#     print(file.tell())
# # print(file.read())



class WordsFinder:


    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
                    words = cleaned_text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print()
        return all_words

    def find(self, word):
        positions = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                result = words.index(word.lower()) + 1
                positions[name] = result
        return positions

    def count(self, word):
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word.lower())
        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

