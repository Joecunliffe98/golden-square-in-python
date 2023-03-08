class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        

    def format(self):
        return self.title + ": " + self.contents

    def count_words(self):
        count = 0
        if self.contents.strip() != "":
            for i in self.contents:
                if i == " ":
                    count += 1
            output = count + 1
        else:
            output = "The contents is empty"
        return output


    def reading_time(self, wpm):
        if self.contents == "":
            time = "The contents is empty"
        else:
            time = int(self.count_words() / wpm)
        return time
        

    def reading_chunk(self, wpm, minutes):
        contents = str(self.contents)
        read_string = []
        unread_string = contents.split()
        words_can_read = wpm * minutes
        if self.read_so_far > len(unread_string):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_can_read
        self.read_so_far = words_can_read
        read_string = unread_string[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(read_string)
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass