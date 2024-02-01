import customtkinter as ctk,MainHandling
from Settings import*
from GUI.Widgets import*
from Localization import Locale
from PIL import Image
def create_home_frame(self):A='nsew';home_frame=Frame(self,corner_radius=0);home_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=A);home_frame.grid_rowconfigure(1,weight=1);home_frame.grid_columnconfigure(0,weight=1);self.grid_columnconfigure(1,weight=1);self.home_frame=home_frame;home_frame_title=Label(home_frame,height=0,corner_radius=0,text=Locale('home.title'),font=MainHandling.set_font(main_font,None,30),anchor='n');home_frame_title.grid(row=0,column=0,padx=0,pady=20,sticky=A);home_frame_title_text=Label(home_frame,height=0,corner_radius=0,text=Locale('home.text'),font=MainHandling.set_font(self.secondary_font,None,16),anchor='n');home_frame_title_text.grid(row=1,column=0,padx=0,pady=(25,0),sticky=A);self.home_frame_title_text=home_frame_title_text;home_frame_image=ctk.CTkImage(light_image=Image.open(plant),dark_image=Image.open(plant),size=(150,150));home_frame_image_label=Label(home_frame,text='',image=home_frame_image);home_frame_image_label.grid(row=1,column=0,padx=10,pady=10,sticky='es');self.home_frame.bind('<Configure>',lambda event:home_size(self));return home_frame
def home_size(self):self.update_idletasks();scale=self.get_system_scale();wrap_width=self.home_frame.winfo_width()*(2-scale)-64;self.home_frame_title_text.configure(wraplength=wrap_width)