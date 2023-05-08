import pandas as pd
import tkinter as tk
import os
from openpyxl import load_workbook
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

user_inp = simpledialog.askstring(title="File location", prompt="Input excel file path and name: ")
user_out = simpledialog.askstring(title="Folder location", prompt="Input the output path: ")

df = pd.read_excel(user_inp)

for i in range(len(df)):
    job_num = df.iloc[i,0]
    description = df.iloc[i,1]
    file_name = job_num + "-" +description
    if user_out[-1] != "/":
        user_out = user_out + "/"
    new_dir = os.path.join(user_out, file_name)
    os.mkdir(new_dir)