import string


class PlagiarismDetector:
    DEFAULT_TUPLE_SIZE = 3

    def __init__(self, files, synonyms, tuple_size):
        if tuple_size <= 0:
            raise Exception("Tuple size must be positive")

        self.tuple_size = tuple_size
        self.synonyms = self.__file_to_dict(synonyms)
        self.original = self.__convert_to_tuples(files[0], False)
        self.possible_plagiarism = self.__convert_to_tuples(files[1], True)

    def __file_to_list(self, file):
        file_words = []
        with open(file, 'r') as file:
            for line in file:
                file_words.extend(line.split())

        if len(file_words) < self.tuple_size:
            raise Exception("Tuple size must be less than the number of words in the file")

        return file_words

    def __file_to_dict(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().translate(str.maketrans('', '', string.punctuation))
                    synonyms[word] = words[0]
        return synonyms

    def __convert_to_tuples(self, file, synonymize):
        words = self.__file_to_list(file)

        for i, word in enumerate(words):
            if synonymize:
                if words[i] in self.synonyms:
                    words[i] = self.synonyms[word]
            words[i] = word.lower().translate(str.maketrans('', '', string.punctuation))

        return [tuple(words[i:i + self.tuple_size]) for i in range(len(words) - self.tuple_size + 1)]

    def get_percentage_plagiarized(self):

        plagiarized = 0
        for word_set in self.possible_plagiarism:
            if word_set in self.original:
                plagiarized += 1

        return plagiarized / len(self.possible_plagiarism) * 100 if plagiarized is not 0 else 0
