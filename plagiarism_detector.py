class PlagiarismDetector():
    DEFAULT_TUPLE_SIZE = 3

    def __init__(self, files, synonyms, tuple_size):
        if tuple_size <= 0:
            raise Exception("Tuple size must be positive")
        if len(files) is not 2:
            raise Exception("Two Files must be provided")

        self.file1 = files[0]
        self.file2 = files[1]
        self.synonyms = synonyms
        self.tuple_size = tuple_size

    def get_percent_plagiarised(self):
        return "test"
