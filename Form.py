

#label1 = tk.Label(root, text='Project Creator')
#label1.config(font=('helvetica', 14))
#canvas1.create_window(200, 25, window=label1)

import tkinter as tk
from tkinter import ttk, filedialog
from P_Creator import createProject
from Issue_Creator import *
import pandas as pd
import json

# Creating tkinter window
window = tk.Tk()
window.geometry('350x240')
window.title('Project Creator')
tkvar1 = tk.StringVar(window)

#title = ttk.Label(window, text='Project Creator',font=('helvetica', 14), anchor = "center" ).grid(
#                                             row=9, padx=0, pady=5)
#title.configure(anchor = "center")

def window_line(label, type, values, window, row_n):
    ttk.Label(window, label). grid(column=0, row = row_n, padx=10, pady=5)
    n = tk.StringVar()
    if type == "Combo":
        combo_box = ttk.Combobox(window, width=27,
                                 textvariable=n)


def open_file():
    temp_file = filedialog.askopenfilename(title="Open file", filetypes=[("Excel files", "*.csv")])
    temp_file = open(temp_file, "r")
    tkvar1.set(temp_file.read())
    df = pd.read_csv(temp_file)
    df = df.rename(columns={list(df)[0]: 'Name', list(df)[1]:'Type', list(df)[2]:'Due_Date', list(df)[3]:'Epic', list(df)[4]: 'Epic_number'}, inplace=True)
    Project_DataFrame = df
    return Project_DataFrame
    #print (Proj_df['Epic'].to_string(index=False))

DF1 = Project_DataFrame

print (DF1)

# Label
ttk.Label(window, text="Select the Client :",
          font=("helvetica", 10)).grid(column=0,
                                             row=10, padx=10, pady=5)

n = tk.StringVar()
clientchoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
clientchoosen['values'] = ('AT&T',
                          'Claro',
                          'Entel',
                          'Telecom',
                          'Telmex',
                          'Telefonica',
                          'TEST')

clientchoosen.grid(column=1, row=10 )

# Shows first as a default value


# Label2
ttk.Label(window, text="Select the Country :",
          font=("helvetica", 10)).grid(column=0,
                                             row=11, padx=10, pady=5)

n = tk.StringVar()
countrychoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

countrychoosen['values'] = ('Argentina',
                          'Brazil',
                          'Chile',
                          'Colombia',
                          'Paraguay',
                          'Peru',
                          'TEST')
# Adding combobox drop down list

countrychoosen.grid(column=1, row=11)

# Label3
ttk.Label(window, text="Select the Product :",
          font=("helvetica", 10)).grid(column=0,
                                             row=12, padx=10, pady=5)

n = tk.StringVar()
productchoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

productchoosen['values'] = ('CGNAT',
                          'NUX',
                          'MAT',
                          'MEM',
                          'SDP',
                          'TEST')
# Adding combobox drop down list

productchoosen.grid(column=1, row=12)

# Label4
ttk.Label(window, text="Project Description :",
          font=("helvetica", 10)).grid(column=0,
                                             row=13, padx=10, pady=5)

n = tk.StringVar()
description = ttk.Entry(window, width=27,
                            textvariable=n)
# Set description on window grid

description.grid(column=1, row=13)

# Label5
ttk.Label(window, text="Project Key :",
          font=("helvetica", 10)).grid(column=0,
                                             row=14, padx=10, pady=5)

n = tk.StringVar()
p_key = ttk.Entry(window, width=27,
                            textvariable=n)
# Set p_key on window grid

p_key.grid(column=1, row=14)

# Label6
ttk.Label(window, text="Upload project tasks",
          font=("helvetica", 10)).grid(column=0,
                                             row=15, padx=10, pady=5)

n = tk.StringVar()
open_button = ttk.Button(text='Select File...', command=open_file)
open_button.grid(column=1, row=15)

# Adding combobox drop down list

# Shows first as a default value
productchoosen.current(0)
countrychoosen.current(0)
clientchoosen.current(0)

info = []

def getInfo():
    #get values from fields in the form
    x1 = clientchoosen.get()
    x2 = countrychoosen.get()
    x3 = productchoosen.get()
    x4 = description.get()
    x5 = p_key.get()
    x6 = DF1
    #create project name based on uploaded parameters
    project_Name = x3 + " - " + x1 + " - " + x2 + " - " + x4
    #categorize based on product
    if x3 == "MAT":
        project_Category = 10003
    else:
        project_Category = 10002
    project_Description = x4
    #generate project key based on product and and admin ID
    project_Key = x3[0:3] + x5
    #create project
    #project = createProject(project_Key, project_Name, project_Description, project_Category)
    #project_id = project['id']
    #print(project_id)
    #upload template
    #create_from_template(Project_DataFrame, project_id)
    print (x6['Epic'].to_string(index=False))
    info = [x1, x2, x3]
    print (project_Name, project_Category, project_Key, project_Description)
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


button1 = ttk.Button(text='Create Project', command=getInfo)

button1.grid(column=0, row=16)

window.mainloop()

