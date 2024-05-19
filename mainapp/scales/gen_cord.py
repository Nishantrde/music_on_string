from db import *
from gen_scales import *

class Gen_cords:
    def __init__(self, cord_note, scale_note, scale_list):

        self.scale = Scale_gen(scale_note, scale_list)
        self.lst = self.scale.gen_scale()
        self.lst.pop()
        self.note = cord_note
        self.cord = []
        self.cords = []
        self.lst = self.lst[self.lst.index(self.note):]+self.lst[:self.lst.index(self.note)]
        
        self.check_lst = []
        self.or_lst = []

        self.span = 0
        self.span_i = 0

        self.string_scale = []

        for note in TRIAD:
            self.cord.append(self.lst[note])
            self.check_lst.append(self.lst[note])
            self.or_lst.append(self.lst[note])
        
        for note in self.cord:
            for guitar_note in GUITAR:
                self.string_scale = [] 
                self.span_i += 1
                string = [guitar_note]
                for str_note in string:
                    if note is str_note:
                        self.span = self.span_i
                    else:
                        string.append()
                    


if __name__ == "__main__":
    gen_cord = Gen_cords("C", "C", MAJOR_LST)        
    print(gen_cord.cord)



