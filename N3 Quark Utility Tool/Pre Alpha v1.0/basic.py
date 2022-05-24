# TO DO
# - Delete func.




import PySimpleGUI as sg
import os
import shutil
import settings
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# ----------------------------------------------------------

availableDirs = os.listdir(settings.UsbPath)

ScriptPath = settings.ScriptsPath
UsbPath = "/Volumes"
QuarkPath = "/Volumes/N3QUARK"
QuarkName = QuarkPath.replace("/Volumes/", "", 1)
os.system("rm -r __pycache__")

fvar = False

# ----------------------------------------------------------

# ----------------------------------------------------------


# LIST STUFF




matchlist = []

alllist = os.listdir(ScriptPath)

outlist = alllist

if ScriptPath != "":
  alllist = os.listdir(ScriptPath)

  
outlist = alllist
if ".DS_Store" in ScriptPath:
  os.system("rm -r '" + ScriptPath +  "/.DS_Store'")
if ".DS_Store" in outlist:
  outlist = outlist.remove(".DS_Store")
outlist = sorted(alllist)
  

for element in alllist:
  if element not in alllist:
    element = str(element)
    alllist.append(element)


def update():
  if ScriptPath != "":
    alllist = os.listdir(ScriptPath)
    
  outlist = alllist
  if ".DS_Store" in ScriptPath:
    os.system("rm -r '" + ScriptPath +  "/.DS_Store'")
  if ".DS_Store" in outlist:
    outlist = outlist.remove(".DS_Store")
  outlist = alllist
  

  for element in alllist:
    if element not in alllist:
      element = str(element)
      alllist.append(element)
      
  


  
  
        

update()

# ----------------------------------------------------------

fnt = 'Arial 15'
fntlarge = 'Arial 30'

# ----------------------------------------------------------

  










sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


if QuarkName in availableDirs:
  constat = ("Connected ✔")
elif QuarkName not in availableDirs:
  constat = ("Not Connected ✘")

constattext = constat

filestat = ""

def update_status():
  if QuarkName in availableDirs:
    constat = ("Connected ✔")
  elif QuarkName not in availableDirs:
    constat = ("Not Connected ✘")

if QuarkName in availableDirs:
  if "payload.dd" not in quarklist:
    filestat = "Error: 'payload.dd' file not present!"
  if "payload.dd" in quarklist:
    with open(QuarkPath + "/payload.dd") as f:
      lines = f.read()
      filestat = lines


if QuarkName not in availableDirs:
  filestat = "N3 QUARK is not connected!"




    



spaces = '                                                           '


update()

r_keys = ['-mac-', '-win-']

top = sg.Column([
[sg.Text('N3 QUARK UTILITY TOOL' + spaces, font = fntlarge), sg.Button('Exit'), sg.Button('Test')],
[sg.Text(constattext, font = fnt)]
])

onel = sg.Column([
  [sg.Text('Currently uploaded script', font = fnt)],
  [sg.Multiline(filestat, font = fnt, size=(30,20), key = '-currently-uploaded-')]
  ])



twol = sg.Column([
[sg.Text('Script Library', font = fnt)],
[sg.InputText('', key='-search-term-', size=(20,3), enable_events = True)],
  
[sg.Listbox(values=(outlist), key='-scr-lib-list-', size=(21,10) ) ],
[sg.Button('Save'), sg.Button('Select file')],
[sg.Button('Delete'), sg.Button('Upload')],
[sg.Button('Create file')]
  
])
threel = sg.Column([
  
  [sg.Button('Open'), sg.Text('Selected script', font = fnt), sg.InputText('', key='-filename-', size=(20,3), enable_events = True)],
  [sg.Multiline('Please open a file', font = fnt, size=(50,21), key = '-selected-script-text-')]
  
  ])

layout = [ [top],
         [onel, sg.VerticalSeparator(pad=None), twol, sg.VerticalSeparator(pad=None), threel]
  ]






window = sg.Window('N3 QUARK Utility Tool', layout, size=(950, 383)) #950, 170








while True:
  event, values = window.read()
    #if event == "":








  if event == '-search-term-':
    string = values['-search-term-'].lower()
    if string:
        files = [file for file in alllist if string in file.lower()]
    else:
        files = alllist[:]
        files = sorted(files)
    window['-scr-lib-list-'].update(files)

  def filter():
    string = values['-search-term-'].lower()
    if string:
        files = [file for file in alllist if string in file.lower()]
    else:
        files = alllist[:]
        files = sorted(files)
    window['-scr-lib-list-'].update(files)







  if event != 'Save':        
    if values['-scr-lib-list-'] != values['-filename-']:
      selected_file = values['-scr-lib-list-']     
      selected_file = str(selected_file)
      selected_file = selected_file.replace("['", "")
      selected_file = selected_file.replace("']", "")
      if event == 'Open':
        window.Element('-filename-').Update(selected_file)

      extfile = str(ScriptPath + "/" + selected_file)
      if extfile != (ScriptPath + "/[]"):
        with open(extfile) as f:
          lines = f.read()
          lines = lines.replace("REM ", "")  
        window.Element('-selected-script-text-').Update(lines)
      fvar = True
#      filter()
    
  if event == 'Create file':
    os.chdir(ScriptPath)
    count = 0
    for i in ScriptPath:
      if "newfile" in i:
        count += 1
    if count == 0:
      newf = "newfile.dd"
    if count > 0:
      newf = "newfile" + str(count) + ".dd"
          
    os.system("touch " + newf)
    os.system("cd ..")



    if ".DS_Store" in outlist:
      outlist = outlist.remove(".DS_Store")

    alllist = os.listdir(ScriptPath)
    outlist = alllist
    if ".DS_Store" in ScriptPath:
      os.system("rm -r '" + ScriptPath +  "/.DS_Store'")
    if ".DS_Store" in outlist:
      outlist = outlist.remove(".DS_Store")

    for element in alllist:
      if element not in alllist:
        element = str(element)
        alllist.append(element)
        
    outlist = sorted(alllist)
      
      

    window.Element('-scr-lib-list-').Update(values=outlist)
    filename = "newfile.dd"
    window.Element('-filename-').Update(filename)
    with open(filename) as f:
        lines = f.read()
        lines = lines.replace("REM ", "")  
    window.Element('-selected-script-text-').Update(lines)

  if event == 'Save':

    with open(extfile, 'r+') as f:
        
        # Save text to file
      f.truncate(0)
      print(f.read)
      f.write(values['-selected-script-text-'])
        

        
      fi = ScriptPath + "/" + values['-filename-']
        # Change title
      os.rename(extfile, fi)
        
        
      alllist = os.listdir(ScriptPath)
      if ".DS_Store" in alllist:
        os.system("rm -r '" + ScriptPath +  "/.DS_Store'")
      alllist = os.listdir(ScriptPath)
      outlist = alllist
      outlist = sorted(outlist)
      if ".DS_Store" in alllist:
        alllist = list.remove(".DS_Store")
        
      selected_file = values['-scr-lib-list-']     
      selected_file = str(selected_file)
      selected_file = selected_file.replace("['", "")
      selected_file = selected_file.replace("']", "")
      
      window.Element('-scr-lib-list-').Update(values=outlist)
      window.Element('-filename-').Update("")
      window.Element('-selected-script-text-').Update("")

  if event == 'Delete':
    selected_file = values['-scr-lib-list-']     
    selected_file = str(selected_file)
    selected_file = selected_file.replace("['", "")
    selected_file = selected_file.replace("']", "")
    selected_file = ScriptPath + "/" + selected_file

    os.system("rm -r '" + selected_file + "'")
      
    alllist = os.listdir(ScriptPath)
    outlist = alllist
    if ".DS_Store" in ScriptPath:
      os.system("rm -r '" + ScriptPath +  "/.DS_Store'")
    if ".DS_Store" in outlist:
      outlist = outlist.remove(".DS_Store")
    outlist = alllist
      
    window.Element('-scr-lib-list-').Update(values=outlist)
    selected_file = selected_file.replace((ScriptPath + "/"), "")

      


      
  if event == sg.WIN_CLOSED or event == 'Exit':
      
    break

  if event == 'Upload':
    one = str(ScriptPath + "/" + values['-filename-'])
    two = str(QuarkPath + "/payload.dd")
    print(one)
    print(two)
    if two in QuarkPath:
      os.system("rm -r " + two)
    shutil.copyfile(one, two)
