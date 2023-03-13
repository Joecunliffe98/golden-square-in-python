class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked == True:
            raise Exception("Go Away!")
        elif self.locked == False:
            return self.diary.contents
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False