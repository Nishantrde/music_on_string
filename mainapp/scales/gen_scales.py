from db import * 
class Scale_gen:
    def __init__(self, note, lst):
        
        self.music_notes = MUSIC_NOTES
        self.lst = lst
        self.i = self.music_notes.index(note)
        self.op_ar = []

    def gen_scale(self):
        for n in self.lst:
            self.op_ar.append(self.music_notes[self.i])
            if n == 't':
                self.i += 2
                if self.i >= len(self.music_notes):
                    self.i -= len(self.music_notes)
            else:
                self.i += 1
                if self.i >= len(self.music_notes):
                    self.i -= len(self.music_notes)
        return self.op_ar

if __name__ == '__main__':

    scale = Scale_gen("C", MAJOR_LST)
    lst = scale.gen_scale()
    
    for note in lst:
        print(note, end='  ')
    


