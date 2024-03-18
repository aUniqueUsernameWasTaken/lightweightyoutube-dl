import tkinter
import customtkinter
import conf
from pytube import YouTube


# Download Function

def startDownload():
    status.configure(text='Downloading..')
    if audioorvideo.get() == "MP4":
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink, on_progress_callback=findprecentage)
            video = ytObject.streams.get_highest_resolution()
            video.download(conf.final_dir)
            status.configure(text='Download Complete!', text_color="lime")
            title.configure(text="Title: "+ytObject.title)
        except:
            status.configure(text='Link Invalid!', text_color="red")
    else:
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink, on_progress_callback=findprecentage)
            video = ytObject.streams.get_audio_only()
            video.download(conf.final_dir)
            status.configure(text='Download Complete!', text_color="lime")
            title.configure(text="Title: "+ytObject.title)
        except:
            status.configure(text='Link Invalid!', text_color="red")
######

# Precentage Calculator

def findprecentage(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    precetage_completed = bytes_downloaded / total_size * 100
    precetage_completed_rounded = str(int(precetage_completed))
    print(precetage_completed)
    pnumber.configure(text=str(precetage_completed_rounded)+"%")
    pnumber.update()
    pbar.set((bytes_downloaded / total_size))
    pbar.update()



# sys settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# fram

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Lightweight Youtube Downloader")

# ui element

title = customtkinter.CTkLabel(app, text="Please enter a youtube link")
title.pack(padx=10,pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack(padx=10,pady=10)

# combobox
audioorvideo = customtkinter.CTkComboBox(app, width=150, corner_radius=2, values=["MP4", "MP3"])
audioorvideo.pack()

# download status

status = customtkinter.CTkLabel(app, text="")
status.pack()

# button (for downloading

download = customtkinter.CTkButton(app, text="Press for Download", command=startDownload)
download.pack(padx=10,pady=10)

# progress

pnumber = customtkinter.CTkLabel(app, text="0%")
pnumber.pack(padx=10,pady=5)

pbar = customtkinter.CTkProgressBar(app, width=400)
pbar.set(0)
pbar.pack(padx=10,pady=10)

# Youtube Title

title = customtkinter.CTkLabel(app, text="")
title.pack(padx=10,pady=10)

# Not working as of now
# Creator
#
#creator = customtkinter.CTkLabel(app, text="")
#creator.pack(pady=10)

# run
app.mainloop()
