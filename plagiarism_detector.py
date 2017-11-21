import string


class PlagiarismDetector:
    """
        PlagiarismDetector calculates the percentage of a file plagiarized off another.
    """
    DEFAULT_TUPLE_SIZE = 3

    def __init__(self, files, synonyms, tuple_size):
        """
        Initializes the PlagiarismDetector Class.

        :param files: two files to be compared against each other
        :param synonyms: a list of synonyms
        :param tuple_size: the size of the desired tuple
        """
        if tuple_size <= 0:
            raise Exception("Tuple size must be positive")

        self.tuple_size = tuple_size
        self.synonyms = self.__file_to_dict(synonyms)
        self.original = self.__convert_to_tuples(files[0])
        self.possible_plagiarism = self.__convert_to_tuples(files[1])

    def __file_to_list(self, file):
        """
        Converts a file to a list containing its words.

        :param file: the file to be converted
        :return: a list where every element is a word in the file
        """
        file_words = []
        with open(file, 'r') as file:
            for line in file:
                file_words.extend(line.split())

        if len(file_words) < self.tuple_size:
            raise Exception("Tuple size is too large")

        return file_words

    def __file_to_dict(self, synonym_file):
        """
        Converts a file to a dictionary where keys are a word and values are synonyms to
        that word.

        :param synonym_file: a file containing a list of synonyms
        :return: the dictionary as described above
        """
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().translate(str.maketrans('', '', string.punctuation))  # noqa
                    synonyms[word] = words[0]
        return synonyms

    def __convert_to_tuples(self, file):
        """
        Converts a file to a list of overlapping tuples.

        :param file: the file to be converted
        :param synonymize: Whether or not to replace every word in the file with
                           its synonym (if possible)
        :return: a list of tuples
        """
        words = self.__file_to_list(file)

        for i, word in enumerate(words):
            if words[i] in self.synonyms:
                words[i] = self.synonyms[word]
            words[i] = words[i].lower().translate(str.maketrans('', '', string.punctuation))

        return [tuple(words[i:i + self.tuple_size]) for i in range(len(words) - self.tuple_size + 1)]  # noqa

    def get_percentage_plagiarized(self):
        """
        Calculates the percentage a file is plagiarized

        :return: a percentage ranging from 0 to 100
        """

        plagiarized = 0
        for set_of_words in self.possible_plagiarism:
            if set_of_words in self.original:
                plagiarized += 1

        return plagiarized / len(self.possible_plagiarism) * 100 if plagiarized is not 0 else 0  # noqa
