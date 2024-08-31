import os
import sys

import tkinter as tk
import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
import time
import threading

#For Download bing Images
from bing_image_downloader import downloader

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



#Images Downloader Function
def download_images(Query,Limit=10,dir="images"):
    try:
        #Hide Output frame
        output_label.pack_forget()
        #Show progress Frame
        input_frame3.pack(pady=4)
        #start Progress
        pb.start()
        downloader.download(Query, limit=Limit,output_dir=dir, adult_filter_off=False, force_replace=False)
        pass
    finally:
        # print("****Completed****"*5)
        
        #Display Output frame
        output_label.pack()
        #stop progress
        pb.stop()
        #Hide progress frame
        input_frame3.pack_forget()
        #Display Output string
        output_string.set("****Completed****")
        # time.sleep(1)
        # output_string.set("")
        
        
    
    

File_path = ''

# Main search function
def search_function():
    global File_path

    query = entry_string.get()
    limit = int(limit_spinbox.get())
    dir = File_path
    
    # print(f"Search : {entry_string.get()}, Limit: {limit_spinbox.get() }, Path: {File_path}  ")
    
    #create thread to execute main downloading function
    threading.Thread(target=download_images,args=(query,limit,dir)).start()

#floder Selection
def folder_selection():
    global File_path 
    File_path = r'{}'.format(askdirectory(title="Select Floder"))



# window 
window = ttk.Window(themename='cosmo')
window.title('Bing Image Downloader')
window.iconphoto(False, ttk.PhotoImage(file=resource_path("picture.png")))
window.geometry('600x600')

#title
title_label = ttk.Label(master=window, text="📷 Image Downloader" , font = 'Calibri 21 bold')
title_label.pack()

#input
##Frames
input_frame1 = ttk.Frame(master=window)
input_frame2 = ttk.Frame(master=window)
input_frame3 = ttk.Frame(master=window)

##Frame 1
entry_label = ttk.Label(master=input_frame1, text = "Search Query🔍", font = 'Calibri 15')
entry_string = tk.StringVar()
entry = ttk.Entry(master=input_frame1,
                  textvariable = entry_string,
                  width="30"
                  )
dir_button = ttk.Button(master=window,
                    text = 'Select Folder📁',
                    command = folder_selection,
                    bootstyle="secondary-outline",
                    padding=(40,16) 
                    )
##Frame 2
limit_label = ttk.Label(master=input_frame2, text = "Limit (1-10000)", font = 'Calibri 12')
limit_int = tk.IntVar()
limit_spinbox = ttk.Spinbox(master=input_frame2,
                            from_=1, to=10000,
                            textvariable = limit_int,
                            bootstyle="secondary"
                            
                            )

button = ttk.Button(master=window,
                    text = 'Search',
                    command = search_function,
                    bootstyle="success-outline",
                    padding=(40,16) 
                    )

##Frame 3
#Progress Bar
progress_label = ttk.Label(master=input_frame3, text = "Downloading....", font = 'Calibri 12')
pb = ttk.Progressbar(master = input_frame3,
                     orient='horizontal',
                     mode='determinate',
                     length=280,
                     bootstyle="success-striped"
                    )

#Packing all frames and components to master
entry_label.pack()
entry.pack()
input_frame1.pack(pady=20)
limit_label.pack()
limit_spinbox.pack()
input_frame2.pack(pady=5)
dir_button.pack(pady=8)
button.pack(pady=10)
progress_label.pack(pady=2)
pb.pack()



# output label
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font = 'Calibri 15', 
    textvariable = output_string,
    bootstyle="success"
    )
output_label.pack(pady=8)


#run
window.mainloop()