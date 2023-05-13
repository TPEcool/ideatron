global genres
global subgenres
global soundtrack
global characters
global gametypes
global engines

genres = ["Sandbox","Real-time strategy","First-person shooter","Third person shooter","Simulator","Puzzle game","Action","Action-Adventure","Adventure","Survival","Platformer","Horror","Psychological horror","Sports","Party game","Role-playing game (RPG)","Point and Click"]
subgenres = ["Sandbox","Real-time strategy","First-person shooter","Third person shooter","Simulator","Puzzle game","Action","Action-Adventure","Adventure","Survival","Platformer","Horror","Psychological horror","Sports","Party game","Role-playing game (RPG)","Point and Click","Rage game","Story game","Hard game"]
soundtrack = ["Simple/8bit (square wave + sine)","Ambient/Dark ambient","Calm BG","Space-y","Fast-paced","Dynamic-paced"]
characters = ["A person","A camera in the skies","An alien","An animal","A robot","A moving piece of geometry (e.g. square)"]
gametypes = ["Open-world","Restricted","Randomized Open-world","Randomized Restricted"]
engines = ["Unreal Engine","Scratch","Unity","Godot","RPG Maker","GameMaker Studio","Construct","RPG in a Box","PyGame","No engine (SDL)"]

import datetime as dt
import tkinter as tk
import tkinter.messagebox as msg
import random as rd
import tkinter.filedialog as fs
import os
import sys
import webbrowser as web
from PIL import ImageTk as it, Image as img

version = "2.2"
editorver = "1.5"
year = "2023"
editoryear = '2023'

os.makedirs(os.getcwd()+'/saves',exist_ok=True)
os.makedirs(os.getcwd()+'/saves/lists',exist_ok=True)

app = tk.Tk()

def clamp(i,d,u):
    if i<d:
        return d
    elif i>u:
        return u
    else:
        return i

app.resizable(False,False)
app.geometry("450x120")
app.title("Ideatron v."+version)
app.iconphoto(False,tk.PhotoImage(file='media/ideatron.png'))

git_img = it.PhotoImage(img.open('media/icons/github.png'))
wiki_img = it.PhotoImage(img.open('media/icons/wikipedia.png'))
scratch_img = it.PhotoImage(img.open('media/icons/scratch.webp'))
editor_img = it.PhotoImage(img.open('media/icons/editor.png'))

class game:
    def __init__(self,genre,subgenre,music,char,gtype,eng):
        self.genre = genre
        self.subgenre = subgenre
        self.soundtrack = music
        self.character = char
        self.game_type = gtype
        self.engine = eng

idea = game("","","","","","")

def ask_save(idea):
    response = msg.askquestion(title="Save results?",message="Would you like to save the results?")
    if response == 'yes':
        file=fs.asksaveasfile(title="Save Ideatron game idea",mode='w',initialdir=os.getcwd()+"/saves",parent=app,initialfile=dt.datetime.now().strftime('%Y %B %d %I-%M %p.txt'),defaultextension=".txt")
        if file != None:
            file.write("Genre: "+idea.genre+"\r\nSubgenre: "+idea.subgenre+"\r\nSoundtrack type: "+idea.soundtrack+"\r\nCharacter type: "+idea.character+"\r\nGame type: "+idea.game_type+"\r\nEngine: "+idea.engine+"\r\r - Generated by Ideatron v."+version+"\rIteration count: "+str(clamp(int(iterations.get()),1,2500))+"\rSeed:"+seed.get())
            print("Save operation done!")
        
def gen():
    idea = game("","","","","",'')
    print("Generating game idea...")
    for i in range(0,clamp(int(iterations.get()),1,2500)):
        print("Beginning iteration "+str(i+1)+"...")
        idea = game(rd.choice(genres),rd.choice(subgenres),rd.choice(soundtrack),rd.choice(characters),rd.choice(gametypes),rd.choice(engines))
        print("Iteration "+str(i+1)+" complete!")
    print("Random iterations complete!")
    inf = msg.showinfo(title="Generation results",message="Genre: "+idea.genre+"\r\nSubgenre: "+idea.subgenre+"\r\nSoundtrack type: "+idea.soundtrack+"\r\nCharacter type: "+idea.character+"\r\nGame type: "+idea.game_type+"\r\nEngine: "+idea.engine)
    if inf=='ok':
        ask_save(idea)

def setSeed():
    rd.seed(seed.get())

def about():
    msg.showinfo(title="About Ideatron v."+version,message="Ideatron v."+version+"\r\nCreated in "+year+" by electrovoyage#9148.\r\n"+str(len(genres)+len(subgenres)+len(soundtrack)+len(characters)+len(gametypes)+len(engines))+" options total.")

def listOpt():
    q = msg.askquestion(title="Export generatable options?",message="Would you like to save all generatable options into '/[app folder]/options_exported.txt'?")
    if q=='yes':
        with open("options_exported.txt",'w') as opt:
            print("Beggining exportable option save function...")
            opt.write("Genres:\r")
            for i in genres:
                print("Writing genre "+i+"... ["+str(genres.index(i)+1)+"/"+str(len(genres))+"]")
                opt.write(" - "+i+"\r")
            opt.write("\rSubgenres:\r")
            for i in subgenres:
                print("Writing subgenre "+i+"... ["+str(subgenres.index(i)+1)+"/"+str(len(subgenres))+"]")
                opt.write(" - "+i+"\r")
            opt.write("\rSoundtrack types:\r")
            for i in soundtrack:
                print("Writing soundtrack type "+i+"... ["+str(soundtrack.index(i)+1)+"/"+str(len(soundtrack))+"]")
                opt.write(" - "+i+"\r")
            opt.write("\rCharacters:\r")
            for i in characters:
                print("Writing character "+i+"... ["+str(characters.index(i)+1)+"/"+str(len(characters))+"]")
                opt.write(" - "+i+"\r")
            opt.write("\rGame types:\r")
            for i in gametypes:
                print("Writing game type "+i+"... ["+str(gametypes.index(i)+1)+"/"+str(len(gametypes))+"]")
                opt.write(" - "+i+"\r")
            opt.write("\rEngines:\r")
            for i in engines:
                print("Writing engine "+i+"... ["+str(engines.index(i)+1)+"/"+str(len(engines))+"]")
                opt.write(" - "+i+"\r")
            print("Generatable options exported!")
            opt.write("\rExported from Ideatron v."+version)
            opt.close()
            web.open(os.getcwd()+"/options_exported.txt")

spin_var = tk.StringVar(app)
spin_var.set(str(rd.randint(-10000,10000)))

def git():
    web.open("https://github.com/TPEcool/ideatron")
def issue():
    web.open("https://github.com/TPEcool/ideatron/issues")
def suggest():
    web.open("https://github.com/TPEcool/ideatron/issues/1")
def licens():
    web.open("https://en.wikipedia.org/wiki/MIT_License#License_terms")
def project():
    web.open("https://scratch.mit.edu/projects/756453841/")
def origRepo():
    web.open("https://github.com/TPEcool/Game-Idea-Generator/releases")
def openFl():
    web.open("file:///"+os.getcwd())
def edit_help():
    web.open('https://github.com/TPEcool/ideatron/wiki/IdeaMaker#how-to-use-ideamaker')
                
genBtn = tk.Button(app,text="Generate",command=gen)
genBtn.grid(row=2,column=1,pady=2,padx=20)

listBtn = tk.Button(app,text="List options",command=listOpt)
listBtn.grid(row=2,column=0,pady=2,padx=20)

tk.Label(text="Iterations").grid(row=0,column=0,pady=0,padx=20)

def modify():

    sel = tk.StringVar(app,'none')
    
    modWi = tk.Toplevel()
    modWi.geometry('400x500')
    modWi.resizable(False,False)
    modWi.title('IdeaMaker v.'+editorver)
    modWi.iconphoto(False,tk.PhotoImage(file='media/new_editor.png'))

    def selectGenres():
        selection = genres
        sel.set('genres')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    def selectSubs():
        selection = subgenres
        sel.set('subgenres')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    def selectMus():
        selection = soundtrack
        sel.set('soundtrack types')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    def selectChars():
        selection = characters
        sel.set('characters')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    def selectTypes():
        selection = gametypes
        sel.set('game types')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    def selectEngines():
        selection = engines
        sel.set('engines')
        listBox.delete(0,tk.END)
        selectionLabel.config(text='Selection: '+sel.get())
        for i in selection:
            listBox.insert(tk.END,i)

    listPick = tk.Menu(modWi)
    modWi.config(menu=listPick)

    fileMenu_editor = tk.Menu(listPick,tearoff=False)
    listPick.add_cascade(label='File',menu=fileMenu_editor)

    def showInfoe():
        msg.showinfo(title='IdeaMaker info',message='Welcome to the IdeaMaker! This tool allows you to edit the lists this program can generate! Please note, however, that this program does NOT save the list edits between app sessions.  All changes are applied immediately. Happy editing!')

    def aboute():
        msg.showinfo(title='About IdeaMaker v.'+editorver,message='IdeaMaker v.'+editorver+' by electrovoyage.#9148. Made in '+editoryear+' as a side application for Ideatron.')

    fileMenu_editor.add_command(label='Info',command=showInfoe)
    fileMenu_editor.add_command(label='About',command=aboute)
    fileMenu_editor.add_command(label='Help page', command = edit_help,image=git_img,compound=tk.LEFT)
    
    fileMenu_editor.add_separator()

    def saveEditor():
        file=fs.asksaveasfile(title="Save lists",mode='w',initialdir=os.getcwd()+"/saves/lists",parent=modWi,initialfile=dt.datetime.now().strftime('%Y %B %d %I-%M %p.idea'),defaultextension=".idea",filetypes=[('List save file','*.idea')])
        if file != None:
            c = 0
            for i in genres:
                if c==len(genres)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c==c+1
            file.write('@')
            c = 0
            for i in subgenres:
                if c==len(subgenres)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c=c+1
            file.write('@')
            c = 0
            for i in soundtrack:
                if c==len(soundtrack)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c=c+1
            file.write('@')
            c = 0
            for i in characters:
                if c==len(characters)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c=c+1
            file.write('@')
            c = 0
            for i in gametypes:
                if c==len(gametypes)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c=c+1
            file.write('@')
            c = 0
            for i in engines:
                if c==len(engines)-1:
                    file.write(i)
                else:
                    file.write(i+'|')
                c=c+1

    def loadEditor():
        file=fs.askopenfile(title="Load lists",mode='r',initialdir=os.getcwd()+"/saves/lists",parent=modWi,defaultextension=".idea",filetypes=[('List save file','*.idea')])
        if file != None:
            data = file.read()
            field_dat = data.split('@')
            genres.clear()
            subgenres.clear()
            soundtrack.clear()
            characters.clear()
            gametypes.clear()
            for i in field_dat[0].split('|'):
                genres.append(i)
            for i in field_dat[1].split('|'):
                subgenres.append(i)
            for i in field_dat[2].split('|'):
                soundtrack.append(i)
            for i in field_dat[3].split('|'):
                characters.append(i)
            for i in field_dat[4].split('|'):
                gametypes.append(i)
            for i in field_dat[5].split('|'):
                engines.append(i)

    fileMenu_editor.add_command(label='Save',command=saveEditor)
    fileMenu_editor.add_command(label='Load',command=loadEditor)

    fileMenu_editor.add_separator()
    
    fileMenu_editor.add_command(label='Quit',command=modWi.destroy)

    listPicker = tk.Menu(listPick,tearoff=False)
    listPick.add_cascade(label="Load",menu=listPicker)
    
    listPicker.add_command(label="Genres",command = selectGenres)
    listPicker.add_command(label='Subgenres',command = selectSubs)
    listPicker.add_command(label='Soundtrack types', command = selectMus)
    listPicker.add_command(label='Characters',command=selectChars)
    listPicker.add_command(label='Game types',command = selectTypes)
    listPicker.add_command(label='Engines',command = selectEngines)

    listFrame = tk.Frame(modWi)
    listFrame.grid(row=0,column=0,pady=10,padx=25)

    listScroll = tk.Scrollbar(listFrame)
    listScroll.pack(side=tk.RIGHT, fill = tk.Y)

    listBox = tk.Listbox(listFrame, yscrollcommand = listScroll.set)
    listBox.pack(side=tk.LEFT,ipadx=110,ipady=100)

    listScroll.config(command = listBox.yview)

    def addOpt():

        confirm = msg.askyesno(title='Are you sure you want to add this option?',message='Are you sure you want to add this option to the list? If there are any grammatical mistakes, you will have to load a save or restart the app!')

        if confirm==True:
            listBox.insert(tk.END,listField.get())
            if listField.get()!='' and not ('@' in listField.get() or '|' in listField.get()):
                if sel.get()=='genres':
                    genres.append(listField.get())
                elif sel.get()=='subgenres':
                    subgenres.append(listField.get())
                elif sel.get()=='soundtrack types':
                    soundtrack.append(listField.get())
                elif sel.get()=='characters':
                    characters.append(listField.get())
                elif sel.get()=='game types':
                    gametypes.append(listField.get())
                elif sel.get()=='engines':
                    engines.append(listField.get())
                else:
                    msg.showerror(title='No container selected!',message='Please load a container from the "Load" menu and try again.')
            elif  ('@' in listField.get()) or ('|' in listField.get()):
                msg.showerror(title='Foreign chars',message='The entered text contains "@" or "|" characters! They are not allowed because they are used for .list file saving.')
            else:
                msg.showerror(title='The field is empty!',message='Please enter something into the text field and try again.')
            print('Added to list!')

    def delOpt():
        match sel.get():
            case 'genres':
                genres.pop(listBox.curselection()[0])
                selectGenres()
            case 'subgenres':
                subgenres.pop(listBox.curselection()[0])
                selectSubs()
            case 'soundtrack types':
                soundtrack.pop(listBox.curselection()[0])
                selectMus()
            case 'characters':
                characters.pop(listBox.curselection()[0])
                selectChars()
            case 'game types':
                gametypes.pop(listBox.curselection()[0])
                selectTypes()
            case 'engines':
                engines.pop(listBox.curselection()[0])
                selectEngines()

    buttonFrame = tk.Frame(modWi)
    buttonFrame.grid(row=1,column=0)

    selectionLabel = tk.Label(buttonFrame,text='Selection: '+sel.get())
    selectionLabel.grid(row=1,column=0,padx=10,pady=10)

    addBtn = tk.Button(buttonFrame,text="Add",command = addOpt)
    addBtn.grid(row=0,column=1,padx=5,ipadx=10)

    delBtn = tk.Button(buttonFrame,text='Delete',command=delOpt)
    delBtn.grid(row=0,column=2,padx=5,ipadx=10)

    listField = tk.Entry(buttonFrame)
    listField.grid(row=0,column=0,padx=5,ipadx=10)

    showInfoe()

iterations = tk.Spinbox(from_=1,to=2500)
iterations.grid(row=1,column=0,pady=2,padx=20)

ui_menu = tk.Menu(app,tearoff=False)
app.config(menu=ui_menu)
fileMenu = tk.Menu(ui_menu, tearoff=False)
ui_menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "About Ideatron v."+version+"...",command = about)
fileMenu.add_command(label="Open application folder",command = openFl)
fileMenu.add_separator()
fileMenu.add_command(label="Open IdeaMaker",command=modify, image=editor_img,compound=tk.LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Quit",command = sys.exit)

ln_menu = tk.Menu(ui_menu,tearoff = False)
ui_menu.add_cascade(label="Links",menu=ln_menu)
ln_menu.add_command(label="GitHub repository",command = git,image=git_img,compound=tk.LEFT)
ln_menu.add_command(label="Issues page",command=issue,image=git_img,compound=tk.LEFT)
ln_menu.add_command(label="Suggestions page",command = suggest,image=git_img,compound=tk.LEFT)
ln_menu.add_separator()
ln_menu.add_command(label="License",command = licens,image=wiki_img,compound=tk.LEFT)
ln_menu.add_separator()
ln_menu.add_command(label="Original project",command = project,image=scratch_img,compound=tk.LEFT)
ln_menu.add_command(label="Original repository", command = origRepo,image=git_img,compound=tk.LEFT)

full_tools = it.PhotoImage(img.open('media/small_ftools.png'))
tk.Label(image=full_tools).grid(row=0,column=1,rowspan=2)

tk.Label(text="Random seed").grid(row=0,column=2,pady=0,padx=20)
seed = tk.Spinbox(from_=-10000,to=10000,textvariable = spin_var)
seed.grid(row=1,column=2,padx=20,pady=2)
setSeedBtn = tk.Button(app,text="Set seed",command = setSeed)
setSeedBtn.grid(row=2,column=2,padx=20,pady=5)

tk.mainloop()
