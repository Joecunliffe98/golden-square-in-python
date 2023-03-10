import math

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry):
        self._diary_entries.append(entry)

    def all(self):
        if self._diary_entries == []:
            raise Exception("Diary is empty")
        else:
            return self._diary_entries

    def count_words(self):
        total = 0
        for entries in self._diary_entries:
            total += entries.count_words()
        return total
        
        pass

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("You cannot read anything with 0 wpm")
        else:
            words_to_read = self.count_words() 
            return int(math.ceil((words_to_read / wpm)))

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_can_read = wpm * minutes
        longest_readable = None
        longest_so_far = 0
        for entries in self._diary_entries:
            if entries.count_words() <= words_can_read:
                if entries.count_words() > longest_so_far:
                    longest_readable = entries
        return longest_readable