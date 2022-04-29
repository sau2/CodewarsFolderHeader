from tkinter import Tk
from re import split
r = Tk()
r.withdraw()
s: str = r.clipboard_get()
# r.clipboard_clear()
r.clipboard_append(''.join(w.capitalize() if i else w.lower() for i, w in enumerate(split(r"\W+", s))))
r.update()
r.destroy()
