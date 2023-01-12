from tkinter import *
from PIL import Image,ImageTk
from itertools import count, cycle

def load_image(path:str,width:int=50,height:int=50) -> PhotoImage:
    '''
    Charge une image avec son path, la redimensionne et retourne un objet image pour tkinter
    :param path:    chemin de l'image
    :param width:   largeur de l'image
    :param height:  hateur de l'image
    '''
    img = Image.open(path)
    img = img.resize((width,height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)
 
class ImageLabel(Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy().resize((1200,600) )))
                im.seek(i)
        except EOFError:
            pass

        self.number_frames = len(frames)
        self.frames = cycle(frames)
 
        self.counter = 0
        self.delay = 30
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            if self.number_frames == self.counter:
                pass
            else:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)
                self.counter += 1