_l='column'
_k='mcversion'
_j='version'
_i='#94361c'
_h='#b34122'
_g='#474747'
_f='#462626'
_e='settings_frame'
_d='welcome_frame'
_c='HelveticaNeueCyr'
_b='Regular'
_a='Roman'
_Z=False
_Y='mods_list.delete'
_X='True'
_W='welcome_frame'
_V='green'
_U='#75321e'
_T='utf-8'
_S='edit_info'
_R='mods'
_Q='font'
_P='yellow'
_O='mods.main_info'
_N='#dedede'
_M='text'
_L='font_style'
_K='end'
_J='#652513'
_I='red'
_H='main'
_G='#2b2b2b'
_F='w'
_E='disabled'
_D='transparent'
_C='normal'
_B=None
_A='nsew'
import ctypes,os,sys,json,Localization,ModsHandling,MainHandling
from tkinter import messagebox
import customtkinter as ctk
from Localization import Locale
from OutputHandling import log
from MainHandling import*
from PIL import Image
ctk.set_appearance_mode('Dark')
ctk.set_widget_scaling(1.)
version='0.5.1 alpha'
icons_theme='light'
main_font='Minecraft Ten'
green='#208B38'
user32=ctypes.windll.user32
gdi32=ctypes.windll.gdi32
root_folder=os.getcwd()
log(f"Корневая папка: {root_folder}")
assets_folder=root_folder+'/assets/'
mods_folder=root_folder+'/mods/'
config_path=root_folder+'/config.ini'
if not os.path.exists(mods_folder):os.makedirs(mods_folder)
if not os.path.exists(config_path):
	config=configparser.ConfigParser();config[_H]={'language':'en_US','last_frame':_W,_Q:_c,_L:'Medium'};config[_R]={_S:_X}
	with open(config_path,_F,encoding=_T)as configfile:config.write(configfile)
class MainWindow(ctk.CTk):
	def __init__(self):
		B='white';A='';super().__init__();self.title(f"Minecraft Lang Helper - {version}");self.iconbitmap(os.path.join(assets_folder,'logo.ico'));screen_width=self.winfo_screenwidth();screen_height=self.winfo_screenheight();window_width=1100;window_height=580;self.minsize(1100,580);self.protocol('WM_DELETE_WINDOW',self.on_close);self.secondary_font=get_config_font();log(f"Текущий шрифт: {self.secondary_font}");x_position=(screen_width-window_width)//2;y_position=(screen_height-window_height)//2;self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}");self.grid_rowconfigure(0,weight=1);self.buttons_sidebar=[];self.buttons_mods_list=[];self.overflow_buttons=[];self.all_lang_labels=[];self.buttons_mods_row=1;self.font_size=14;self.timer=_B;self.selected_mod=_B;self.timer=self.after(10,self.resize_font);self.after_cancel(self.timer);self.bind('<Configure>',self.on_window_resize);self.sidebar_button_home=A;self.sidebar_button_mods_list=A;self.sidebar_button_settings=A
		def create_sidebar_frame():C='logo.png';sidebar_frame=XFrame(self,corner_radius=0,width=280);sidebar_frame.grid(row=0,column=0,padx=(10,5),pady=10,sticky=_A);sidebar_logo=ctk.CTkLabel(sidebar_frame,text=A,width=280,corner_radius=0,image=ctk.CTkImage(light_image=Image.open(os.path.join(assets_folder,C)),dark_image=Image.open(os.path.join(assets_folder,C)),size=(160,160)));sidebar_logo.grid(row=0,column=0,padx=0,pady=(10,0),sticky=_A);sidebar_logo_title=ctk.CTkLabel(sidebar_frame,height=0,width=280,corner_radius=0,text='Minecraft\nLang Helper',font=set_font(main_font,_B,30),text_color=B);sidebar_logo_title.grid(row=1,column=0,padx=0,pady=0,sticky=_A);sidebar_version_label=ctk.CTkLabel(sidebar_frame,height=0,corner_radius=0,text=f"{version}",font=set_font(main_font,_B,12),width=280,text_color=B);sidebar_version_label.grid(row=2,column=0,padx=0,pady=(0,10),sticky=_A);sidebar_button_home=ctk.CTkButton(sidebar_frame,corner_radius=0,height=46,width=190,text=Locale('menu.home'),command=lambda:self.show_frame(_d),font=set_font(self.secondary_font,_B,18),fg_color=_J,hover_color=_J,border_color=_N,border_width=2);sidebar_button_home.grid(row=3,column=0,padx=0,pady=5);self.sidebar_button_home=sidebar_button_home;self.buttons_sidebar.append(sidebar_button_home);sidebar_button_mods_list=ctk.CTkButton(sidebar_frame,corner_radius=0,height=46,width=190,text=Locale('menu.mods_list'),command=lambda:self.show_frame(_W),font=set_font(self.secondary_font,_B,18),fg_color=_U,hover_color=_J);sidebar_button_mods_list.grid(row=4,column=0,padx=0,pady=5);self.sidebar_button_mods_list=sidebar_button_mods_list;self.buttons_sidebar.append(sidebar_button_mods_list);sidebar_button_debug=ctk.CTkButton(sidebar_frame,corner_radius=0,height=46,width=190,text=Locale('menu.debug'),command=lambda:self.debug_func(),font=set_font(self.secondary_font,_B,18),fg_color=_U,hover_color=_J);self.buttons_sidebar.append(sidebar_button_debug);sidebar_button_settings=ctk.CTkButton(sidebar_frame,corner_radius=0,height=46,width=190,text=Locale('menu.settings'),command=lambda:self.show_frame(_e),font=set_font(self.secondary_font,_B,18),fg_color=_U,hover_color=_J);sidebar_button_settings.grid(row=6,column=0,padx=0,pady=5);self.sidebar_button_settings=sidebar_button_settings;self.buttons_sidebar.append(sidebar_button_settings);return sidebar_frame
		self.welcome_frame_title_text=A
		def create_welcome_frame():C='plant.png';welcome_frame=XFrame(self,corner_radius=0);welcome_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);welcome_frame.grid_rowconfigure(1,weight=1);welcome_frame.grid_columnconfigure(0,weight=1);self.grid_columnconfigure(1,weight=1);welcome_frame_title=ctk.CTkLabel(welcome_frame,height=0,corner_radius=0,text=Locale('welcome.title'),font=set_font(main_font,_B,30),text_color=B,anchor='n');welcome_frame_title.grid(row=0,column=0,padx=0,pady=20,sticky=_A);welcome_frame_title_text=ctk.CTkLabel(welcome_frame,height=0,corner_radius=0,text=Locale('welcome.text'),font=set_font(self.secondary_font,_B,16),text_color=B,anchor='n');welcome_frame_title_text.grid(row=1,column=0,padx=0,pady=(25,0),sticky=_A);self.welcome_frame_title_text=welcome_frame_title_text;welcome_frame_image=ctk.CTkImage(light_image=Image.open(assets_folder+C),dark_image=Image.open(assets_folder+C),size=(150,150));welcome_frame_image_label=ctk.CTkLabel(welcome_frame,text=A,image=welcome_frame_image);welcome_frame_image_label.grid(row=1,column=0,padx=10,pady=10,sticky='es');return welcome_frame
		self.mods_list_info_modid=A;self.mods_list_info_name=A;self.mods_list_info_version=A;self.mods_list_info_mcversion=A;self.mods_list_info_empty=A;self.mods_list_info_empty_reason=A;self.mods_list_info_main=A;self.mods_list_info_main_title=A;self.del_button=A;self.mods_list_info_languages_frame=A;self.mods_list_info_languages=A;self.mods_list_info_edit=A;self.mods_list_info_edit_save=A;self.mods_list_info_edit_cancel=A;self.mods_list_info_edit_status=A
		def create_mods_list_frame():F='#1d7330';E='readonly';D='-';C='e';B=': ';mods_list_frame=XFrame(self,corner_radius=0,fg_color=_D);mods_list_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);mods_list_frame.grid_rowconfigure(0,weight=1);self.grid_columnconfigure(1,weight=1);mods_list_buttons_frame=XFrame(mods_list_frame,height=40,corner_radius=0,fg_color=_D);mods_list_buttons_frame.grid(row=2,column=0,padx=(0,5),pady=(5,0),sticky=_A);add_button=ctk.CTkButton(mods_list_buttons_frame,text=Locale('mods_list.add'),height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),fg_color=green,hover_color=F,command=lambda:self.add_mod());add_button.grid(row=0,column=0,padx=(0,5),sticky=_A);del_button=ctk.CTkButton(mods_list_buttons_frame,text=Locale(_Y),state=_E,height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),fg_color=_f,text_color_disabled=_g,command=lambda:self.del_mod());del_button.grid(row=0,column=1,padx=(5,0),sticky=_A);self.del_button=del_button;ref_button=ctk.CTkButton(mods_list_buttons_frame,text=Locale('mods_list.refresh'),height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),command=lambda:self.refresh_mods_list());ref_button.grid(row=1,column=0,pady=10,columnspan=2,sticky=_A);ref_button=ctk.CTkButton(mods_list_buttons_frame,text=Locale('mods_list.open_mods_folder'),height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),command=lambda:os.startfile(mods_folder));ref_button.grid(row=2,column=0,columnspan=2,sticky=_A);mods_list_buttons_frame.grid_columnconfigure((0,1),weight=1);mods_list_info_frame=XFrame(mods_list_frame,corner_radius=0);mods_list_info_frame.grid(row=0,column=1,rowspan=3,padx=(5,0),pady=0,sticky=_A);mods_list_frame.grid_columnconfigure((0,1),weight=1,minsize=390);mods_list_info_empty=XFrame(mods_list_info_frame,corner_radius=0,fg_color=_D);mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);mods_list_info_empty.grid_columnconfigure(0,weight=1);self.mods_list_info_empty=mods_list_info_empty;mods_list_info_empty_title=ctk.CTkLabel(mods_list_info_empty,text=Locale('mods.info.empty.title'),corner_radius=0,font=set_font(self.secondary_font,_B,18));mods_list_info_empty_title.grid(row=0,column=0,pady=(10,15),sticky=_A);mods_list_info_empty_reason=ctk.CTkLabel(mods_list_info_empty,text=Locale('mods.info.empty.not.selected'),corner_radius=0,font=set_font(self.secondary_font,_B,14),text_color=_I);mods_list_info_empty_reason.grid(row=1,column=0,sticky=_A);self.mods_list_info_empty_reason=mods_list_info_empty_reason;mods_list_info_main=XFrame(mods_list_info_frame,corner_radius=0,fg_color=_D);mods_list_info_frame.grid_columnconfigure(0,weight=1);mods_list_info_main_title=ctk.CTkLabel(mods_list_info_main,text=Locale(_O),corner_radius=0,font=set_font(self.secondary_font,_B,18));mods_list_info_main_title.grid(row=0,column=0,pady=(10,15),sticky=_A,columnspan=2);self.mods_list_info_main_title=mods_list_info_main_title;mods_list_info_main.grid_columnconfigure(1,weight=1);mods_list_info_main.grid_columnconfigure(0,minsize=100);self.mods_list_info_main=mods_list_info_main;mods_list_info_modid_title=ctk.CTkLabel(mods_list_info_main,text=Locale('mods.info.modid')+B,corner_radius=0,font=set_font(self.secondary_font,_B,14),anchor=C);mods_list_info_modid_title.grid(row=1,column=0,sticky=_A,padx=(0,10));mods_list_info_modid=ctk.CTkEntry(mods_list_info_main,font=set_font(self.secondary_font,_B,14),corner_radius=0,fg_color=_D,border_width=0);mods_list_info_modid.configure(state=_C);mods_list_info_modid.delete(0,_K);mods_list_info_modid.insert(0,D);mods_list_info_modid.configure(state=E);mods_list_info_modid.grid(row=1,column=1,sticky=_A,pady=(0,1));mods_list_info_name_title=ctk.CTkLabel(mods_list_info_main,text=Locale('mods.info.name')+B,corner_radius=0,font=set_font(self.secondary_font,_B,14),anchor=C);mods_list_info_name_title.grid(row=2,column=0,sticky=_A,padx=(0,10));mods_list_info_name=ctk.CTkEntry(mods_list_info_main,font=set_font(self.secondary_font,_B,14),corner_radius=0,fg_color=_D,border_width=0);mods_list_info_name.configure(state=_C);mods_list_info_name.delete(0,_K);mods_list_info_name.insert(0,D);mods_list_info_name.configure(state=E);mods_list_info_name.grid(row=2,column=1,sticky=_A,pady=(0,1));mods_list_info_version_title=ctk.CTkLabel(mods_list_info_main,text=Locale('mods.info.version')+B,corner_radius=0,font=set_font(self.secondary_font,_B,14),anchor=C);mods_list_info_version_title.grid(row=3,column=0,sticky=_A,padx=(0,10));mods_list_info_version=ctk.CTkEntry(mods_list_info_main,font=set_font(self.secondary_font,_B,14),corner_radius=0,fg_color=_D,border_width=0);mods_list_info_version.configure(state=_C);mods_list_info_version.delete(0,_K);mods_list_info_version.insert(0,D);mods_list_info_version.configure(state=E);mods_list_info_version.grid(row=3,column=1,sticky=_A,pady=(0,1));mods_list_info_mcversion_title=ctk.CTkLabel(mods_list_info_main,text=Locale('mods.info.mcversion')+B,corner_radius=0,font=set_font(self.secondary_font,_B,14),anchor=C);mods_list_info_mcversion_title.grid(row=5,column=0,sticky=_A,padx=(0,10));mods_list_info_mcversion=ctk.CTkEntry(mods_list_info_main,font=set_font(self.secondary_font,_B,14),corner_radius=0,fg_color=_D,border_width=0);mods_list_info_mcversion.configure(state=_C);mods_list_info_mcversion.delete(0,_K);mods_list_info_mcversion.insert(0,D);mods_list_info_mcversion.configure(state=E);mods_list_info_mcversion.grid(row=5,column=1,sticky=_A,pady=(0,1));mods_list_info_edit=ctk.CTkButton(mods_list_info_main,text=Locale('mods.info.edit'),corner_radius=0,font=set_font(self.secondary_font,_B,14),command=lambda:self.edit_mod_info());self.mods_list_info_edit=mods_list_info_edit;mods_list_info_edit_save=ctk.CTkButton(mods_list_info_main,text=Locale('mods.info.edit.save'),corner_radius=0,font=set_font(self.secondary_font,_B,14),command=lambda:self.edit_mod_info_save(),fg_color=green,hover_color=F);mods_list_info_edit_save.grid_forget();self.mods_list_info_edit_save=mods_list_info_edit_save;mods_list_info_edit_cancel=ctk.CTkButton(mods_list_info_main,text=Locale('mods.info.edit.cancel'),corner_radius=0,font=set_font(self.secondary_font,_B,14),command=lambda:self.edit_mod_info_cancel(),fg_color=_h,hover_color=_i);self.mods_list_info_edit_cancel=mods_list_info_edit_cancel;mods_list_info_edit_status=ctk.CTkLabel(mods_list_info_main,text=A,corner_radius=0,font=set_font(self.secondary_font,_B,14));self.mods_list_info_edit_status=mods_list_info_edit_status;mods_list_info_edit_status.grid_forget();self.mods_list_info_modid=mods_list_info_modid;self.mods_list_info_name=mods_list_info_name;self.mods_list_info_version=mods_list_info_version;self.mods_list_info_mcversion=mods_list_info_mcversion;mods_list_info_languages_frame=XFrame(mods_list_info_frame,corner_radius=0,fg_color=_D);mods_list_info_frame.grid_rowconfigure(1,weight=1);mods_list_languages_title=ctk.CTkLabel(mods_list_info_languages_frame,text=Locale('mods.info.languages'),corner_radius=0,font=set_font(self.secondary_font,_B,18));mods_list_languages_title.grid(row=0,column=0,pady=10,sticky=_A);mods_list_info_languages_frame.grid_columnconfigure(0,weight=1);self.mods_list_info_languages_frame=mods_list_info_languages_frame;mods_list_info_languages=XScrollableFrame(mods_list_info_languages_frame,corner_radius=0,fg_color=_D,scrollbar_button_color=_G,scrollbar_button_hover_color=_G,scrollbar_fg_color=_G);mods_list_info_languages.grid(row=1,column=0,sticky=_A);mods_list_info_languages_frame.grid_rowconfigure(1,weight=1);self.mods_list_info_languages=mods_list_info_languages;return mods_list_frame
		def create_mods_list_files_frame():mods_list_files_frame=XFrame(self.mods_list_frame,corner_radius=0);mods_list_files_frame.grid(row=0,column=0,padx=(0,5),pady=(0,5),sticky=_A);mods_list_files_title=ctk.CTkLabel(mods_list_files_frame,text=Locale('mods.list'),corner_radius=0,font=set_font(self.secondary_font,_B,18));mods_list_files_title.grid(row=0,column=0,pady=(10,0),sticky=_A);mods_list_files_frame.grid_columnconfigure(0,weight=1);return mods_list_files_frame
		def create_mods_list_files():mods_list_files=XScrollableFrame(self.mods_list_files_frame,fg_color=_D,scrollbar_fg_color=_G,scrollbar_button_color=_G,scrollbar_button_hover_color=_G);mods_list_files.grid(row=1,column=0,padx=(10,0),pady=10,sticky=_A);self.mods_list_files_frame.grid_rowconfigure(1,weight=1);mods_list_files.grid_columnconfigure(0,weight=1);return mods_list_files
		self.settings_frame=A;self.settings_language=A;self.settings_edit_info=A;self.settings_font=A;self.settings_font_style=A;self.settings_font_style_title=A
		def create_settings_frame():settings_frame=XFrame(self,corner_radius=0,fg_color=_D);settings_frame.grid(row=0,column=1,pady=10,sticky=_A);settings_frame.grid_rowconfigure(1,weight=1);settings_frame.grid_columnconfigure(0,weight=1);self.settings_frame=settings_frame;settings_main_frame=XFrame(settings_frame,corner_radius=0);settings_main_frame.grid(row=1,column=0,padx=(0,5),sticky=_A);settings_main_title=ctk.CTkLabel(settings_main_frame,text=Locale('menu.settings.main'),corner_radius=0,font=set_font(self.secondary_font,_B,16),text_color=B);settings_main_title.grid(row=0,column=0,pady=10,sticky=_A);settings_main_frame.grid_columnconfigure(0,weight=1);settings_main_buttons_frame=XFrame(settings_main_frame,corner_radius=0,fg_color=_D);settings_main_buttons_frame.grid(row=1,column=0,pady=0,padx=0,sticky=_A);settings_main_buttons_frame.grid_columnconfigure(1,minsize=200);settings_language_title=ctk.CTkLabel(settings_main_buttons_frame,text=Locale('menu.settings.language'),corner_radius=0,font=set_font(self.secondary_font,_B,16),anchor=_F,text_color=B);settings_language_title.grid(row=1,column=0,pady=0,padx=(18,10),sticky=_A);settings_language=ctk.CTkOptionMenu(settings_main_buttons_frame,font=set_font(self.secondary_font,_B,14),dropdown_font=set_font(self.secondary_font,_B,12),corner_radius=0,values=self.get_lang_names(),command=self.change_language,dynamic_resizing=_Z);settings_language.set(self.load_lang());settings_language.grid(row=1,column=1,pady=10,sticky=_A);self.settings_language=settings_language;settings_font_title=ctk.CTkLabel(settings_main_buttons_frame,text=Locale('menu.settings.font'),corner_radius=0,font=set_font(self.secondary_font,_B,16),anchor=_F,text_color=B);settings_font_title.grid(row=2,column=0,pady=(10,2),padx=(18,10),sticky=_A);settings_font=ctk.CTkOptionMenu(settings_main_buttons_frame,font=set_font(self.secondary_font,_B,14),dropdown_font=set_font(self.secondary_font,_B,12),corner_radius=0,command=self.change_font);settings_font.grid(row=2,column=1,pady=(10,2),sticky=_A);self.settings_font=settings_font;settings_font_style_title=ctk.CTkLabel(settings_main_buttons_frame,text=Locale('menu.settings.font_style'),corner_radius=0,font=set_font(self.secondary_font,_B,16),anchor=_F,text_color=B);settings_font_style_title.grid(row=3,column=0,pady=0,padx=(18,10),sticky=_A);self.settings_font_style_title=settings_font_style_title;settings_font_style=ctk.CTkOptionMenu(settings_main_buttons_frame,font=set_font(self.secondary_font,_B,14),dropdown_font=set_font(self.secondary_font,_B,12),corner_radius=0,command=self.change_font_style);settings_font_style.grid(row=3,column=1,sticky=_A);self.settings_font_style=settings_font_style;settings_mods_frame=XFrame(settings_frame,corner_radius=0);settings_mods_frame.grid(row=1,column=1,padx=(5,0),sticky=_A);settings_frame.grid_columnconfigure((0,1),weight=1,minsize=390);settings_mods_title=ctk.CTkLabel(settings_mods_frame,text=Locale('menu.settings.mods'),corner_radius=0,font=set_font(self.secondary_font,_B,16),text_color=B);settings_mods_title.grid(row=0,column=0,pady=10,columnspan=2,sticky=_A);settings_mods_frame.grid_columnconfigure(0,weight=1);settings_edit_info_title=ctk.CTkLabel(settings_mods_frame,text=Locale('menu.settings.edit_info'),corner_radius=0,font=set_font(self.secondary_font,_B,16),anchor=_F,text_color=B);settings_edit_info_title.grid(row=1,column=0,pady=0,padx=(10,5),sticky=_A);settings_edit_info=ctk.CTkSwitch(settings_mods_frame,text=A,font=set_font(self.secondary_font,_B,18),command=lambda:self.enable_edit_info());settings_edit_info.grid(row=1,column=1,pady=10,padx=(5,10),sticky=_A);self.settings_edit_info=settings_edit_info;return settings_frame
		self.sidebar_menu=create_sidebar_frame();self.welcome_frame=create_welcome_frame();self.settings_frame=create_settings_frame();self.settings_frame.grid_forget();self.mods_list_frame=create_mods_list_frame();self.mods_list_frame.grid_forget();self.mods_list_files_frame=create_mods_list_files_frame();self.mods_list_files=create_mods_list_files();self.fill_mods_list(self.mods_list_files);self.resize_font();self.set_last_frame();self.load_settings()
	def change_font(self,choice):
		font_styles=get_font_styles(choice);font_style=_B
		if len(font_styles)>1:
			if _a in font_styles:font_style=_a
			elif _b in font_styles:font_style=_b
			self.settings_font_style_title.grid(row=3,column=0,pady=0,padx=10,sticky=_A);self.settings_font_style.grid(row=3,column=1,sticky=_A)
		else:font_style=font_styles[0];self.settings_font_style_title.grid_forget();self.settings_font_style.grid_forget()
		self.secondary_font=choice;self.save_settings(_H,_Q,choice);self.save_settings(_H,_L,font_style);self.settings_font_style.configure(values=font_styles);self.settings_font_style.set(font_style);restart_program()
	def change_font_style(self,choice):self.save_settings(_H,_L,choice);restart_program()
	def get_loaded_fonts(self):loaded_fonts=get_loaded_fonts();return loaded_fonts
	def get_config_font_style(self):config=configparser.ConfigParser();config.read(config_path);font_style=config.get(_H,_L);return font_style
	def on_close(self):
		if messagebox.askokcancel('Quit','Вы уверены, что хотите закрыть программу?'):self.destroy()
	def del_mod(self):
		name=self.selected_mod.cget(_M);delete=ModsHandling.del_mod(name)
		if delete:self.selected_mod=_B;self.refresh_mods_list()
	def add_mod(self):ModsHandling.add_mod();self.refresh_mods_list()
	def get_lang_names(self):langs=Localization.get_languages();lang_names=list(langs.keys());return lang_names
	def change_language(self,choice):
		changed=Localization.change_language(choice)
		if changed:restart_program()
	def load_settings(self):
		config=configparser.ConfigParser();config.read(config_path);edit_info=config.get(_R,_S)
		if edit_info==_X:self.settings_edit_info.select();self.enable_edit_info()
		else:self.settings_edit_info.deselect()
		font=config.get(_H,_Q);font_style=config.get(_H,_L);self.settings_font.set(font);self.settings_font.configure(values=self.get_loaded_fonts());self.settings_font_style.set(font_style);self.settings_font_style.configure(values=get_font_styles(font))
		if len(get_font_styles(font))==1:self.settings_font_style_title.grid_forget();self.settings_font_style.grid_forget()
	def save_settings(self,section,key,value):
		config=configparser.ConfigParser();config.read(config_path);config.set(section,key,value)
		with open(config_path,_F,encoding=_T)as configfile:config.write(configfile)
	def load_lang(self):lang=Localization.get_current_language();return lang
	def enable_edit_info(self):
		switch_state=self.settings_edit_info.get()
		if switch_state==self.settings_edit_info.cget('onvalue'):self.mods_list_info_edit.grid(row=6,column=1,padx=(0,10),sticky=_A);self.save_settings(_R,_S,_X)
		elif switch_state==self.settings_edit_info.cget('offvalue'):self.mods_list_info_edit.grid_forget();self.mods_list_info_edit_status.grid_forget();self.save_settings(_R,_S,'False')
	def edit_mod_info(self):self.mods_list_info_edit_status.grid_forget();self.mods_list_info_modid.configure(state=_C,border_width=1);self.mods_list_info_name.configure(state=_C,border_width=1);self.mods_list_info_version.configure(state=_C,border_width=1);self.mods_list_info_mcversion.configure(state=_C,border_width=1);self.mods_list_info_edit.grid_forget();self.mods_list_info_edit_save.grid(row=6,column=1,sticky=_A)
	def edit_mod_info_save(self):
		name=self.selected_mod.cget(_M);info_file=ModsHandling.get_mod_info(name)['info_path'];modid=self.mods_list_info_modid.get();name=self.mods_list_info_name.get();version=self.mods_list_info_version.get();mcversion=self.mods_list_info_mcversion.get();file_save=_Z
		try:
			with open(info_file,'r',encoding=_T)as file:
				data=json.load(file,strict=_Z)
				for mod in data:mod['modid']=modid;mod['name']=name;mod[_j]=version;mod[_k]=mcversion
			with open(info_file,_F,encoding=_T)as file:json.dump(data,file,indent=4)
			file_save=True
		except Exception as e:log(f"Ошибка сохранения файла: {e}",_I)
		self.mods_list_info_edit_save.grid_forget();self.mods_list_info_edit.grid(row=6,column=1,sticky=_A);self.mods_list_info_modid.configure(state=_E,border_width=0);self.mods_list_info_name.configure(state=_E,border_width=0);self.mods_list_info_version.configure(state=_E,border_width=0);self.mods_list_info_mcversion.configure(state=_E,border_width=0);self.mods_list_info_edit_status.grid(row=6,column=0,padx=(0,10),sticky=_A)
		if file_save:self.mods_list_info_edit_status.configure(text=Locale('mods.info.edit.save.success'),text_color=green)
		else:self.mods_list_info_edit_status.configure(text=Locale('mods.info.edit.save.error'),text_color=_I)
	def reset_info(self):
		if self.selected_mod is not _B:self.selected_mod.configure(border_width=0);self.selected_mod=_B
		self.mods_list_info_main.grid_forget();self.mods_list_info_main_title.configure(text=Locale(_O));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);state_del=self.del_button.cget('state')
		if state_del==_C:self.del_button.configure(text=Locale(_Y),state=_E,height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),fg_color=_f,text_color_disabled=_g,command=lambda:self.del_mod())
		if len(self.all_lang_labels)>0:
			for btn in self.all_lang_labels:btn.destroy()
		self.mods_list_info_languages_frame.grid_forget();self.mods_list_info_languages.yview_moveto(.0);self.mods_list_info_modid.configure(border_width=0);self.mods_list_info_name.configure(border_width=0);self.mods_list_info_version.configure(border_width=0);self.mods_list_info_mcversion.configure(border_width=0)
	def show_frame(self,frame):
		self.welcome_frame.grid_forget();self.mods_list_frame.grid_forget();self.settings_frame.grid_forget()
		for btn in self.buttons_sidebar:btn.configure(fg_color=_U,border_width=0)
		if frame==_d:self.welcome_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);self.sidebar_button_home.configure(fg_color=_J,border_color=_N,border_width=2)
		elif frame==_W:self.mods_list_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);self.sidebar_button_mods_list.configure(fg_color=_J,border_color=_N,border_width=2)
		elif frame==_e:self.settings_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);self.sidebar_button_settings.configure(fg_color=_J,border_color=_N,border_width=2)
		MainHandling.save_last_frame(frame)
	def set_last_frame(self):last_frame=MainHandling.load_last_frame();self.show_frame(last_frame)
	def select_mod(self,btn,name):
		if self.selected_mod is not _B:
			if name==self.selected_mod.cget(_M):log('Мод уже выбран.',_P)
			else:log(f"Выбран мод: {name}",_P);self.selected_mod.configure(border_width=0);self.fill_mod_info(btn,name)
		else:self.fill_mod_info(btn,name)
	def fill_mod_info(self,btn,name):
		self.mods_list_info_edit_status.grid_forget();state_del=self.del_button.cget('state')
		if state_del==_E:self.del_button.configure(text=Locale(_Y),state=_C,height=40,width=0,corner_radius=0,font=set_font(self.secondary_font,_B,18),fg_color=_h,hover_color=_i,command=lambda:self.del_mod())
		btn.configure(border_width=1);self.selected_mod=btn;langs=ModsHandling.get_mod_languages(name);info_file=ModsHandling.get_mod_info(name)
		if info_file=='Not Found':self.mods_list_info_main.grid_forget();self.mods_list_info_empty_reason.configure(text=Locale('error.info_file_not_found'));self.mods_list_info_main_title.configure(text=Locale(_O));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);log('Info file not found.',_I)
		elif info_file=='Error':self.mods_list_info_main.grid_forget();self.mods_list_info_empty_reason.configure(text=Locale('error.error_reading_file'));self.mods_list_info_main_title.configure(text=Locale(_O));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);log('Error reading file.',_I)
		else:
			self.mods_list_info_empty.grid_forget();self.mods_list_info_main.grid(row=0,column=0,sticky=_A,columnspan=3,padx=18);modid=info_file['modid'];name=info_file['name'];version=info_file[_j];mcversion=info_file[_k];description=info_file['description'];info_type=info_file['info_type']
			if info_type=='mcmod.info':self.mods_list_info_edit.configure(state=_C,fg_color='#1f6aa5');self.mods_list_info_edit_save.grid_forget()
			else:self.mods_list_info_edit.configure(state=_E,fg_color='#144870')
			self.mods_list_info_main_title.configure(text=Locale(_O)+f" ({info_type})");self.mods_list_info_modid.configure(state=_C,border_width=0);self.mods_list_info_modid.delete(0,_K);self.mods_list_info_modid.insert(0,modid);self.mods_list_info_modid.configure(state=_E);self.mods_list_info_name.configure(state=_C,border_width=0);self.mods_list_info_name.delete(0,_K);self.mods_list_info_name.insert(0,name);self.mods_list_info_name.configure(state=_E);self.mods_list_info_version.configure(state=_C,border_width=0);self.mods_list_info_version.delete(0,_K);self.mods_list_info_version.insert(0,version);self.mods_list_info_version.configure(state=_E);self.mods_list_info_mcversion.configure(state=_C,border_width=0);self.mods_list_info_mcversion.delete(0,_K);self.mods_list_info_mcversion.insert(0,mcversion);self.mods_list_info_mcversion.configure(state=_E)
		self.fill_mod_languages(langs);self.mods_list_info_languages.yview_moveto(0)
	def fill_mod_languages(self,langs):
		row=2
		if len(self.all_lang_labels)>0:
			for btn in self.all_lang_labels:btn.destroy()
		for(key,values)in langs.items():
			mod_languages_menu_lang_folder=ctk.CTkLabel(self.mods_list_info_languages,text='◉ '+Locale('mods.info.languages.folder')+f": {key}",font=set_font(self.secondary_font,_B,14),anchor=_F);mod_languages_menu_lang_folder.grid(row=row,columnspan=2,rowspan=1,column=0,padx=(18,0),pady=0,sticky=_A)
			for(lang_code,language)in values.items():row+=1;mod_languages_menu_lang=ctk.CTkLabel(self.mods_list_info_languages,text=f"• {lang_code.strip()} - {language}",font=set_font(self.secondary_font,_B,14),anchor=_F);mod_languages_menu_lang.grid(row=row,columnspan=2,rowspan=1,column=0,padx=(32,0),pady=0,sticky=_A);self.all_lang_labels.append(mod_languages_menu_lang)
			row+=1;self.all_lang_labels.append(mod_languages_menu_lang_folder);self.mods_list_info_languages_frame.grid(row=1,column=0,sticky=_A)
	def add_mod_to_mods_list(self,name):row=self.buttons_mods_row+1;mod_button=ctk.CTkButton(self.mods_list_files,anchor=_F,fg_color=_D,corner_radius=0,hover_color='#242424',border_width=0,border_color=_N,text=name,font=set_font(self.secondary_font,_B,14),command=lambda:self.select_mod(mod_button,name));mod_button.grid(row=row,column=0,sticky=_A);self.buttons_mods_list.append(mod_button);self.buttons_mods_row+=1
	def fill_mods_list(self,frame):
		log('Загрузка модов...',_P);mods_info=ModsHandling.get_mods()
		if len(mods_info)==0:log('Модов не найдено.',_I)
		else:
			log(f"Найдено модов: {len(mods_info)}")
			try:
				for mod in mods_info:self.add_mod_to_mods_list(mod)
				log('Моды успешно загружены.',_V)
			except Exception as e:log(f"Ошибка при загрузке модов: {e}",_I)
	def clean_mods_list(self):
		if len(self.buttons_mods_list)==0:log('Список модов пуст.',_V)
		else:
			log('Очистка списка модов...',_P)
			for btn in self.buttons_mods_list:btn.destroy()
			self.buttons_mods_list=[]
			if len(self.buttons_mods_list)==0:log('Список модов очищен.',_V)
			else:log('Ошибка при очистке списка модов.',_I)
	def refresh_mods_list(self):
		log('Обновление списка модов...',_P);mods_info=ModsHandling.get_mods();log(f"Текущее количество модов: {len(self.mods_list_files.winfo_children())}")
		if len(mods_info)==0:self.clean_mods_list()
		else:
			log(f"Получение списка модов...");current_mod_button_texts=[btn.cget(_M)for btn in self.buttons_mods_list]
			for btn_text in current_mod_button_texts:
				if btn_text not in mods_info:
					mod_button=next((mod for mod in self.buttons_mods_list if mod.cget(_M)==btn_text),_B)
					if mod_button:mod_button.destroy();self.buttons_mods_list.remove(mod_button);log(f"Мод {btn_text} удален.",_I);log(f"Текущее количество модов: {len(self.mods_list_files.winfo_children())}")
			for mod in mods_info:
				if mod not in current_mod_button_texts:self.add_mod_to_mods_list(mod)
			log('Список модов обновлен.',_V)
		self.reset_info()
	def get_system_dpi(self):desktop=user32.GetDC(0);dpi_x=gdi32.GetDeviceCaps(desktop,88);dpi_y=gdi32.GetDeviceCaps(desktop,90);user32.ReleaseDC(0,desktop);return dpi_x,dpi_y
	def get_system_scale(self):dpi_x,_=self.get_system_dpi();return dpi_x/96.
	def debug_func(self):self.update_idletasks()
	def on_window_resize(self,event):
		if self.timer:self.after_cancel(self.timer)
		self.timer=self.after(10,self.resize_font)
	def print_window_size(self):new_width=self.winfo_width();new_height=self.winfo_height();print(f"Новый размер окна: {new_width}x{new_height}")
	def resize_font(self):
		B='#3b3b3b';A='#424242';self.update_idletasks()
		for btn in self.buttons_mods_list:
			self.font_size=14;btn_text=btn.cget(_M);btn_width=btn.winfo_width();font=set_font(self.secondary_font,_B,self.font_size);btn_text_width=font.measure(btn_text)
			while btn_text_width>btn_width and self.font_size>1:self.font_size-=1;font=set_font(self.secondary_font,_B,self.font_size);btn.configure(font=font);btn_text_width=font.measure(btn_text)
		mods_list_files_height=self.mods_list_files.winfo_height();mods_list_files_frame_height=self.mods_list_files_frame.winfo_height();available_height_for_buttons=mods_list_files_frame_height-54-16
		if available_height_for_buttons<mods_list_files_height:self.mods_list_files.configure(scrollbar_button_color=A,scrollbar_button_hover_color=B)
		else:self.mods_list_files.configure(scrollbar_button_color=_G,scrollbar_button_hover_color=_G)
		mods_list_info_languages_height=self.mods_list_info_languages.winfo_height();mods_list_info_languages_frame_height=self.mods_list_info_languages_frame.winfo_height()-48
		if mods_list_info_languages_frame_height<mods_list_info_languages_height:self.mods_list_info_languages.configure(scrollbar_button_color=A,scrollbar_button_hover_color=B)
		else:self.mods_list_info_languages.configure(scrollbar_button_color=_G,scrollbar_button_hover_color=_G)
		scale=self.get_system_scale();wrap_width=self.welcome_frame.winfo_width()*(2-scale)-16;self.welcome_frame_title_text.configure(wraplength=wrap_width)
class XFrame(ctk.CTkFrame):
	def __repr__(self):grid_info=self.grid_info();return f"<Frame: row={grid_info['row']} | col={grid_info[_l]} | {int(self._current_width)}x{int(self._current_height)}>"
class XScrollableFrame(ctk.CTkScrollableFrame):
	def __repr__(self):grid_info=self.grid_info();return f"<Frame: row={grid_info['row']} | col={grid_info[_l]} | {int(self._current_width)}x{int(self._current_height)}>"
	def yview_moveto(self,fraction):self._parent_canvas.yview_moveto(fraction)
	def xview_moveto(self,fraction):self._parent_canvas.xview_moveto(fraction)
def get_config_font():
	config=configparser.ConfigParser();config.read('config.ini');font=config[_H][_Q];style=config[_H][_L]
	if style==_b or style==_a:font_gui=f"{font}"
	elif font==_c:font_gui=f"{font}-{style}"
	else:font_gui=f"{font} {style}"
	return font_gui
def start_program():global app;load_fonts();app=MainWindow();app.mainloop()
def restart_program():global app;app.destroy();start_program()
if __name__=='__main__':start_program()