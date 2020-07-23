
from tkinter import filedialog
import pandas as pd
from tkinter import *

root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TAB files","*.TAB"),("csv files","*.csv"),("all files","*.*")))
fileLocation = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TAB files","*.TAB"),("csv files","*.csv"),("all files","*.*")))
# print (root.filename)
if fileLocation.endswith(".csv"):
    print("YES this is CSV file")
    myData = pd.read_csv(fileLocation)
elif fileLocation.endswith(".tab"):
    print("YES this is TAB file")
    # doc = codecs.open('document','rU','UTF-16')
    myData = pd.read_csv(fileLocation, sep='\t',lineterminator='\r',index_col=(0))
else:
    raise TypeError("You should select .csv or .tab extension files!")
print (fileLocation)
print(myData.sample())
print(myData.info())
print(type(fileLocation))