import pandas as pd
from tkinter import Tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import *

Tk().withdraw()
fileName = filedialog.askopenfile(initialdir="/home", filetypes=[("Text files", "*.txt")])
fileToConvert = pd.read_fwf(fileName)
fileInput = simpledialog.askstring(title="CSV file name", prompt="Enter CSV file name")
newFile = "%s.csv" %fileInput
fileToConvert.to_csv(newFile, index=False)
