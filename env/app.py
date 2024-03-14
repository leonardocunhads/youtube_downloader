import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


def download_video():
    print("function download")


# create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of the window
root.title("Youtube Downloader")

# set min and max height and width
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the URL here:")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(padx="10p", pady= "5p")
entry_url.pack(padx="10p", pady="5p")

# create a doenload button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(padx="10p", pady="5p")

# create a resolutions combo box
resolutions = ["720px","360px","240px"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var )
resolution_combobox.pack(padx="10p", pady="5p")
resolution_combobox.set("720px")

# start the app
root.mainloop()