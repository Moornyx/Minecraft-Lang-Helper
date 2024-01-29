_H='column'
_G='font'
_F='Regular'
_E='Roman'
_D=None
_C='font_style'
_B='nsew'
_A='main'
import ctypes,customtkinter as ctk,os,Localization,MainHandling,Settings
from GUI import SidebarMenu,TabHome,TabModsList,TabSetting
from tkinter import messagebox
from Localization import Locale
from OutputHandling import log
from MainHandling import*
from Settings import*
ctk.set_appearance_mode(theme)
ctk.set_widget_scaling(1.)
user32=ctypes.windll.user32
gdi32=ctypes.windll.gdi32
if not os.path.exists(mods_folder):os.makedirs(mods_folder)
class MainWindow(ctk.CTk):
	def __init__(self):
		C='red';B='green';A='';super().__init__();self.title(f"Minecraft Lang Helper - {version}");self.iconbitmap(os.path.join(assets_folder,'logo.ico'));screen_width=self.winfo_screenwidth();screen_height=self.winfo_screenheight();window_width=1100;window_height=580;self.minsize(1100,580);self.protocol('WM_DELETE_WINDOW',self.on_close);self.secondary_font=get_config_font();log(f"Текущий шрифт: {self.secondary_font}");x_position=(screen_width-window_width)//2;y_position=(screen_height-window_height)//2;self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}");self.grid_rowconfigure(0,weight=1);self.buttons_sidebar=[];self.buttons_mods_list=[];self.overflow_buttons=[];self.all_lang_labels=[];self.buttons_mods_row=1;self.font_size=14;self.selected_mod=_D;self.home_frame_title_text=A;self.mods_list_info_modid=A;self.mods_list_info_name=A;self.mods_list_info_version=A;self.mods_list_info_mcversion=A;self.mods_list_info_empty=A;self.mods_list_info_empty_reason=A;self.mods_list_info_main=A;self.mods_list_info_main_title=A;self.del_button=A;self.mods_list_info_languages_frame=A;self.mods_list_info_languages=A;self.mods_list_info_edit=A;self.mods_list_info_edit_save=A;self.mods_list_info_edit_cancel=A;self.mods_list_info_edit_status=A;self.mods_list_info_edit_button=A;self.settings_frame=A;self.settings_language=A;self.settings_edit_info=A;self.settings_font=A;self.settings_font_style=A;self.settings_font_style_title=A;self.sidebar_menu=SidebarMenu.create_sidebar_menu(self)
		if self.sidebar_menu:log('Меню боковое создано',B)
		else:log('Меню боковое не создано',C)
		self.home_frame=TabHome.create_home_frame(self)
		if self.home_frame:log('Фрейм приветствия создан',B)
		else:log('Фрейм приветствия не создан',C)
		self.mods_list_frame=TabModsList.create_mods_list_frame(self)
		if self.mods_list_frame:log('Фрейм списка модов создан',B)
		else:log('Фрейм списка модов не создан',C)
		self.mods_list_files_frame=TabModsList.create_mods_list_files_frame(self)
		if self.mods_list_files_frame:log('Фрейм списка папок модов создан',B)
		else:log('Фрейм списка папок модов не создан',C)
		self.mods_list_files=TabModsList.create_mods_list_files(self)
		if self.mods_list_files:log('Список папок модов создан',B)
		else:log('Список папок модов не создан',C)
		self.fill_mods_list=TabModsList.fill_mods_list(self,self.mods_list_files)
		if self.fill_mods_list:log('Список папок модов заполнен',B)
		else:log('Список папок модов не заполнен',C)
		self.settings_frame=TabSetting.create_settings_frame(self)
		if self.settings_frame:log('Фрейм настроек создан',B)
		else:log('Фрейм настроек не создан',C)
		self.set_last_frame();self.load_settings();self.mods_list_files.bind('<Enter>',self.mod_list_piska)
	def change_font(self,choice):
		font_styles=get_font_styles(choice);font_style=_D
		if len(font_styles)>1:
			if _E in font_styles:font_style=_E
			elif _F in font_styles:font_style=_F
			self.settings_font_style_title.grid(row=3,column=0,pady=0,padx=10,sticky=_B);self.settings_font_style.grid(row=3,column=1,sticky=_B)
		else:font_style=font_styles[0];self.settings_font_style_title.grid_forget();self.settings_font_style.grid_forget()
		self.secondary_font=choice;self.save_settings(_A,_G,choice);self.save_settings(_A,_C,font_style);self.settings_font_style.configure(values=font_styles);self.settings_font_style.set(font_style);self.restart_program()
	def change_font_style(self,choice):self.save_settings(_A,_C,choice);self.restart_program()
	def get_loaded_fonts(self):loaded_fonts=get_loaded_fonts();return loaded_fonts
	def get_config_font_style(self):config=configparser.ConfigParser();config.read(config_path);font_style=config.get(_A,_C);return font_style
	def on_close(self):sys.exit()
	def get_lang_names(self):langs=Localization.get_languages();lang_names=list(langs.keys());return lang_names
	def change_language(self,choice):
		current_language=Localization.get_current_language();log(f"Изменение языка: {current_language} -> {choice}")
		if choice==current_language:return
		else:
			changed=Localization.change_language(choice)
			if changed:self.restart_program()
	def load_settings(self):
		config=configparser.ConfigParser();config.read(config_path);edit_info=config.get('mods','edit_info')
		if edit_info=='True':self.settings_edit_info.select();TabModsList.enable_edit_info(self)
		else:self.settings_edit_info.deselect()
		font=config.get(_A,_G);font_style=config.get(_A,_C);self.settings_font.set(font);self.settings_font.configure(values=self.get_loaded_fonts());self.settings_font_style.set(font_style);self.settings_font_style.configure(values=get_font_styles(font))
		if len(get_font_styles(font))==1:self.settings_font_style_title.grid_forget();self.settings_font_style.grid_forget()
	def save_settings(self,section,key,value):
		config=configparser.ConfigParser();config.read(config_path);config.set(section,key,value)
		with open(config_path,'w',encoding='utf-8')as configfile:config.write(configfile)
	def load_lang(self):lang=Localization.get_current_language();return lang
	def show_frame(self,frame):
		B='#dedede';A='#652513';self.home_frame.grid_forget();self.mods_list_frame.grid_forget();self.settings_frame.grid_forget()
		for btn in self.buttons_sidebar:btn.configure(fg_color='#75321e',border_width=0)
		if frame=='home_frame':self.home_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_B);self.sidebar_button_home.configure(fg_color=A,border_color=B,border_width=2)
		elif frame=='mods_list_frame':self.mods_list_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_B);self.sidebar_button_mods_list.configure(fg_color=A,border_color=B,border_width=2)
		elif frame=='settings_frame':self.settings_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_B);self.sidebar_button_settings.configure(fg_color=A,border_color=B,border_width=2)
		self.timer=self.after(5,self.resize_font);MainHandling.save_last_frame(frame)
	def set_last_frame(self):last_frame=MainHandling.load_last_frame();self.show_frame(last_frame)
	def get_system_dpi(self):desktop=user32.GetDC(0);dpi_x=gdi32.GetDeviceCaps(desktop,88);dpi_y=gdi32.GetDeviceCaps(desktop,90);user32.ReleaseDC(0,desktop);return dpi_x,dpi_y
	def get_system_scale(self):dpi_x,_=self.get_system_dpi();return dpi_x/96.
	def mod_list_piska(self,event):0
	def debug_func(self):0
	def on_window_resize(self,event):
		if self.timer:self.after_cancel(self.timer)
		self.timer=self.after(10,self.resize_font)
	def print_window_size(self):new_width=self.winfo_width();new_height=self.winfo_height();print(f"Новый размер окна: {new_width}x{new_height}")
	def resize_font(self):
		C='#3b3b3b';B='#424242';A='#2b2b2b';log('Изменение размера окна 2...','yellow');self.update_idletasks()
		for btn in self.buttons_mods_list:
			self.font_size=14;btn_text=btn.cget('text');btn_width=btn.winfo_width();font=set_font(self.secondary_font,_D,self.font_size);btn_text_width=font.measure(btn_text)
			while btn_text_width>btn_width and self.font_size>1:self.font_size-=1;font=set_font(self.secondary_font,_D,self.font_size);btn.configure(font=font);btn_text_width=font.measure(btn_text)
		mods_list_files_height=self.mods_list_files.winfo_height();mods_list_files_frame_height=self.mods_list_files_frame.winfo_height();available_height_for_buttons=mods_list_files_frame_height-54-16
		if available_height_for_buttons<mods_list_files_height:self.mods_list_files.configure(scrollbar_button_color=B,scrollbar_button_hover_color=C)
		else:self.mods_list_files.configure(scrollbar_button_color=A,scrollbar_button_hover_color=A)
		mods_list_info_languages_height=self.mods_list_info_languages.winfo_height();mods_list_info_languages_frame_height=self.mods_list_info_languages_frame.winfo_height()-48
		if mods_list_info_languages_frame_height<mods_list_info_languages_height:self.mods_list_info_languages.configure(scrollbar_button_color=B,scrollbar_button_hover_color=C)
		else:self.mods_list_info_languages.configure(scrollbar_button_color=A,scrollbar_button_hover_color=A)
		scale=self.get_system_scale();wrap_width=self.home_frame.winfo_width()*(2-scale)-16;self.home_frame_title_text.configure(wraplength=wrap_width)
	def restart_program(self):self.destroy();start_program()
class XFrame(ctk.CTkFrame):
	def __repr__(self):grid_info=self.grid_info();return f"<Frame: row={grid_info['row']} | col={grid_info[_H]} | {int(self._current_width)}x{int(self._current_height)}>"
class XScrollableFrame(ctk.CTkScrollableFrame):
	def __repr__(self):grid_info=self.grid_info();return f"<Frame: row={grid_info['row']} | col={grid_info[_H]} | {int(self._current_width)}x{int(self._current_height)}>"
	def yview_moveto(self,fraction):self._parent_canvas.yview_moveto(fraction)
	def xview_moveto(self,fraction):self._parent_canvas.xview_moveto(fraction)
def get_config_font():
	config=configparser.ConfigParser();config.read('config.ini');font=config[_A][_G];style=config[_A][_C]
	if style==_F or style==_E:font_gui=f"{font}"
	elif font=='HelveticaNeueCyr':font_gui=f"{font}-{style}"
	else:font_gui=f"{font} {style}"
	return font_gui
def start_program():global app;load_fonts();Settings.set_default_settings();app=MainWindow();app.mainloop()
if __name__=='__main__':start_program();myapp=start_program()