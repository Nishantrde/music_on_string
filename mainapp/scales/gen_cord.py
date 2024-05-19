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
        self.string_index = []
        self.covered_string = 0

        for note in TRIAD:
            self.cord.append(self.lst[note])
            self.check_lst.append(self.lst[note])
            self.or_lst.append(self.lst[note])

        for note in GUITAR:
            
            print(MUSIC_NOTES[MUSIC_NOTES.index(note):]+MUSIC_NOTES[:MUSIC_NOTES.index(note)])
            self.string_scale.append(MUSIC_NOTES[MUSIC_NOTES.index(note):]+MUSIC_NOTES[:MUSIC_NOTES.index(note)])
        for note in self.cord:
            print("note:"+note)
            for scale in self.string_scale:
                span_i = 0
                for nt in scale:
                    if span_i is not HAND_SPAN:
                        span_i+=1
                        # print(span_i)
                        if nt is note:
                            self.span = span_i
                            print(nt)
                            break


if __name__ == "__main__":
    gen_cord = Gen_cords("C", "C", MAJOR_LST)        
    print(gen_cord.cord)



