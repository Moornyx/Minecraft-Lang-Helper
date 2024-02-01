import customtkinter as ctk,MainHandling
from Settings import*
from GUI.Widgets import*
from Localization import Locale
from PIL import Image
def create_sidebar_menu(self):D='#75321e';C='nsew';B='#652513';A=None;sidebar_frame=Frame(self,width=280);sidebar_frame.grid(row=0,column=0,padx=(10,5),pady=10,sticky=C);sidebar_logo=Label(sidebar_frame,text='',width=280,image=ctk.CTkImage(light_image=Image.open(logo),dark_image=Image.open(logo),size=(160,160)));sidebar_logo.grid(row=0,column=0,padx=0,pady=(10,0),sticky=C);sidebar_logo_title=Label(sidebar_frame,height=0,width=280,text='Minecraft\nLang Helper',font=MainHandling.set_font(main_font,A,30));sidebar_logo_title.grid(row=1,column=0,padx=0,pady=0,sticky=C);sidebar_version_label=Label(sidebar_frame,height=0,text=f"{version}",font=MainHandling.set_font(main_font,A,12),width=280);sidebar_version_label.grid(row=2,column=0,padx=0,pady=(0,10),sticky=C);sidebar_button_home=Button(sidebar_frame,height=46,width=190,text=Locale('menu.home'),command=lambda:self.show_frame('home_frame'),font=MainHandling.set_font(self.secondary_font,A,18),fg_color=B,hover_color=B,border_color='#dedede',border_width=2);sidebar_button_home.grid(row=3,column=0,padx=0,pady=5);self.sidebar_button_home=sidebar_button_home;self.buttons_sidebar.append(sidebar_button_home);sidebar_button_mods_list=Button(sidebar_frame,height=46,width=190,text=Locale('menu.mods_list'),command=lambda:self.show_frame('mods_list_frame'),font=MainHandling.set_font(self.secondary_font,A,18),fg_color=D,hover_color=B);sidebar_button_mods_list.grid(row=4,column=0,padx=0,pady=5);self.sidebar_button_mods_list=sidebar_button_mods_list;self.buttons_sidebar.append(sidebar_button_mods_list);sidebar_button_debug=Button(sidebar_frame,height=46,width=190,text=Locale('menu.debug'),command=lambda:self.debug_func(),font=MainHandling.set_font(self.secondary_font,A,18),fg_color=D,hover_color=B);sidebar_button_debug.grid(row=5,column=0,padx=0,pady=5);self.buttons_sidebar.append(sidebar_button_debug);sidebar_button_settings=Button(sidebar_frame,height=46,width=190,text=Locale('menu.settings'),command=lambda:self.show_frame('settings_frame'),font=MainHandling.set_font(self.secondary_font,A,18),fg_color=D,hover_color=B);sidebar_button_settings.grid(row=6,column=0,padx=0,pady=5);self.sidebar_button_settings=sidebar_button_settings;self.buttons_sidebar.append(sidebar_button_settings);return sidebar_frame