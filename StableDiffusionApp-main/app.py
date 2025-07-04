import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk
from authtoken import auth_token
from customtkinter import CTkImage
from PIL import Image

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud") 
ctk.set_appearance_mode("dark")

# root = ctk.CTk()
# root.geometry("800x600")  # ✅ Corrected geometry format
# root.title("Stable Bud")

# prompt = ctk.CTkEntry(master=root, height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white") 
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")

prompt.place(x=10, y=20)
prompt.pack(pady=20)


lmain = ctk.CTkLabel(master=app ,height=512, width=512,text="")
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
pipe.to(device) 

def generate(): 
    with autocast(device): 
        # image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
        image = pipe(prompt.get(), guidance_scale=8.5).images[0]

    
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img) 

trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate) 
trigger.configure(text="Generate") 
trigger.place(x=206, y=60) 

app.mainloop()