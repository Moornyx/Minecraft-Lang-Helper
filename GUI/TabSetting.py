import customtkinter as ctk,MainHandling
from GUI import TabModsList
from Settings import*
from GUI.Widgets import*
from Localization import Locale
def create_settings_frame(self):E='transparent';D='w';C='white';B=None;A='nsew';settings_frame=Frame(self,corner_radius=0,fg_color=E);settings_frame.grid(row=0,column=1,pady=10,sticky=A);settings_frame.grid_rowconfigure(1,weight=1);settings_frame.grid_columnconfigure(0,weight=1);self.settings_frame=settings_frame;settings_main_frame=Frame(settings_frame,corner_radius=0);settings_main_frame.grid(row=1,column=0,padx=(0,5),sticky=A);settings_main_title=Label(settings_main_frame,text=Locale('menu.settings.main'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,16),text_color=C);settings_main_title.grid(row=0,column=0,pady=10,sticky=A);settings_main_frame.grid_columnconfigure(0,weight=1);settings_main_buttons_frame=Frame(settings_main_frame,corner_radius=0,fg_color=E);settings_main_buttons_frame.grid(row=1,column=0,pady=0,padx=0,sticky=A);settings_main_buttons_frame.grid_columnconfigure(1,minsize=200);settings_language_title=Label(settings_main_buttons_frame,text=Locale('menu.settings.language'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,14),anchor=D,text_color=C);settings_language_title.grid(row=1,column=0,pady=0,padx=(18,10),sticky=A);settings_language=ctk.CTkOptionMenu(settings_main_buttons_frame,font=MainHandling.set_font(self.secondary_font,B,14),dropdown_font=MainHandling.set_font(self.secondary_font,B,12),corner_radius=0,values=self.get_lang_names(),command=self.change_language,dynamic_resizing=False);settings_language.set(self.load_lang());settings_language.grid(row=1,column=1,pady=10,sticky=A);self.settings_language=settings_language;settings_font_title=Label(settings_main_buttons_frame,text=Locale('menu.settings.font'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,14),anchor=D,text_color=C);settings_font_title.grid(row=2,column=0,pady=(10,2),padx=(18,10),sticky=A);settings_font=ctk.CTkOptionMenu(settings_main_buttons_frame,font=MainHandling.set_font(self.secondary_font,B,14),dropdown_font=MainHandling.set_font(self.secondary_font,B,12),corner_radius=0,command=self.change_font);settings_font.grid(row=2,column=1,pady=(10,2),sticky=A);self.settings_font=settings_font;settings_font_style_title=Label(settings_main_buttons_frame,text=Locale('menu.settings.font_style'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,14),anchor=D,text_color=C);settings_font_style_title.grid(row=3,column=0,pady=0,padx=(18,10),sticky=A);self.settings_font_style_title=settings_font_style_title;settings_font_style=ctk.CTkOptionMenu(settings_main_buttons_frame,font=MainHandling.set_font(self.secondary_font,B,14),dropdown_font=MainHandling.set_font(self.secondary_font,B,12),corner_radius=0,command=self.change_font_style);settings_font_style.grid(row=3,column=1,sticky=A);self.settings_font_style=settings_font_style;settings_mods_frame=Frame(settings_frame,corner_radius=0);settings_mods_frame.grid(row=1,column=1,padx=(5,0),sticky=A);settings_frame.grid_columnconfigure((0,1),weight=1,minsize=390);settings_mods_title=Label(settings_mods_frame,text=Locale('menu.settings.mods'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,16),text_color=C);settings_mods_title.grid(row=0,column=0,pady=10,columnspan=2,sticky=A);settings_mods_frame.grid_columnconfigure(1,weight=1);settings_edit_info_title=Label(settings_mods_frame,text=Locale('menu.settings.edit_info'),corner_radius=0,font=MainHandling.set_font(self.secondary_font,B,14),anchor=D,text_color=C);settings_edit_info_title.grid(row=1,column=0,pady=0,padx=(18,5),sticky=A);settings_edit_info=ctk.CTkSwitch(settings_mods_frame,text='',font=MainHandling.set_font(self.secondary_font,B,18),command=lambda:TabModsList.enable_edit_info(self));settings_edit_info.grid(row=1,column=1,pady=10,sticky=A);self.settings_edit_info=settings_edit_info;return settings_frame