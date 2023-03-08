class GrammarStats:
    def __init__(self):
        self.num_checked = 0
        self.num_passed = 0

    def check(self, text):
        punctuation = "?!."
        if text[0].isupper() == True and text[-1] in punctuation:
            self.num_passed += 1
            self.num_checked += 1
            return True
            
        else:
            self.num_checked += 1
            return False
            

    def percentage_good(self):
        if self.num_checked == 0:
            return 0
        else:
            return int(self.num_passed / self.num_checked * 100)