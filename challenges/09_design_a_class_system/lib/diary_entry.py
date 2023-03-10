class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        self.total_word_count = 0
    
    def format(self):
        return self.title + ": " + self.contents

    def count_words(self):
        if self.contents == "":
            return "The contents is empty"
        else:
            return len(self.contents.split())


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