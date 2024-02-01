_k='info_path'
_j='warning'
_i='Warning'
_h='#3b3b3b'
_g='#424242'
_f='info_type'
_e='Not Found'
_d='#474747'
_c='#462626'
_b='#94361c'
_a='#b34122'
_Z='#1d7330'
_Y='fabric.mod.json'
_X='mods_list.delete'
_W='mods.main_info'
_V='mods.info.empty.not.selected'
_U='mods'
_T='mods.toml'
_S='description'
_R='name'
_Q='modid'
_P='mcmod.info'
_O='mcversion'
_N='version'
_M='text'
_L=False
_K=True
_J='yellow'
_I='green'
_H='end'
_G='#333333'
_F='transparent'
_E='disabled'
_D='normal'
_C='red'
_B=None
_A='nsew'
import json,re,shutil,zipfile,customtkinter,toml,MainHandling,time,threading
from tkinter import messagebox
from Settings import*
from GUI.Widgets import*
from Localization import Locale
from OutputHandling import log
def create_mods_list_frame(self):B='<Configure>';A='mods.list';mods_list_frame=Frame(self);mods_list_frame.grid(row=0,column=1,padx=(5,10),pady=10,sticky=_A);mods_list_frame.grid_rowconfigure(1,weight=1);self.grid_columnconfigure(1,weight=1);mods_list_title=Label(mods_list_frame,text=Locale(A),corner_radius=0,font=MainHandling.set_font(main_font,_B,30));mods_list_title.grid(row=0,pady=20,sticky=_A,columnspan=2);self.all_locales[mods_list_title]=A;mods_list(self,mods_list_frame);mods_list_buttons(self,mods_list_frame);mods_list_info_frame=mods_list_info(self,mods_list_frame);self.mods_list_info_languages_frame.bind(B,lambda event:languages_size(self));self.mods_list_files_frame.bind(B,lambda event:mods_list_size(self));return mods_list_frame
def mods_list(self,mods_list_frame):A='mods.list.title';mods_list_files_frame=Frame(mods_list_frame);mods_list_files_frame.grid(row=1,column=0,padx=(10,5),pady=(0,5),sticky=_A);mods_list_files_title=Label(mods_list_files_frame,text=Locale(A),font=MainHandling.set_font(self.secondary_font,_B,18));self.all_locales[mods_list_files_title]=A;self.mods_list_files_title=mods_list_files_title;mods_list_files_title.grid(row=0,column=0,pady=(10,0),sticky=_A);mods_list_files_frame.grid_columnconfigure(0,weight=1);self.mods_list_files_frame=mods_list_files_frame;mods_list_files=ScrollableFrame(mods_list_files_frame,fg_color=_F,scrollbar_fg_color=_G,scrollbar_button_color=_G,scrollbar_button_hover_color=_G);mods_list_files.grid(row=1,column=0,padx=(10,0),pady=10,sticky=_A);mods_list_files_frame.grid_rowconfigure(1,weight=1);mods_list_files.grid_columnconfigure(0,weight=1);self.mods_list_files=mods_list_files;return mods_list_files_frame
def mods_list_info(self,mods_list_frame):M='mods.info.languages';L='mods.info.edit.cancel';K='mods.info.edit.save';J='mods.info.edit';I='mods.info.file';H='mods.info.mcversion';G='mods.info.version';F='mods.info.name';E='mods.info.modid';D='mods.info.empty.title';C='readonly';B='e';A=': ';mods_list_info_frame=Frame(mods_list_frame);mods_list_info_frame.grid(row=1,column=1,rowspan=3,padx=(5,10),pady=(0,10),sticky=_A);mods_list_frame.grid_columnconfigure((0,1),weight=1,minsize=390);mods_list_info_empty=Frame(mods_list_info_frame,fg_color=_F);mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);mods_list_info_empty.grid_columnconfigure(0,weight=1);self.mods_list_info_empty=mods_list_info_empty;mods_list_info_empty_title=Label(mods_list_info_empty,text=Locale(D),font=MainHandling.set_font(self.secondary_font,_B,18));mods_list_info_empty_title.grid(row=0,column=0,pady=(10,15),sticky=_A);self.all_locales[mods_list_info_empty_title]=D;mods_list_info_empty_reason=Label(mods_list_info_empty,text=Locale(_V),font=MainHandling.set_font(self.secondary_font,_B,14),text_color=_C);mods_list_info_empty_reason.grid(row=1,column=0,sticky=_A);self.all_locales[mods_list_info_empty_reason]=_V;self.mods_list_info_empty_reason=mods_list_info_empty_reason;mods_list_info_main=Frame(mods_list_info_frame,fg_color=_F);mods_list_info_frame.grid_columnconfigure(0,weight=1);mods_list_info_main_title=Label(mods_list_info_main,text=Locale(_W),font=MainHandling.set_font(self.secondary_font,_B,18));mods_list_info_main_title.grid(row=0,column=0,pady=(10,15),sticky=_A,columnspan=2);self.all_locales[mods_list_info_main_title]=_W;self.mods_list_info_main_title=mods_list_info_main_title;mods_list_info_main.grid_columnconfigure(1,weight=1);mods_list_info_main.grid_columnconfigure(0,minsize=100);self.mods_list_info_main=mods_list_info_main;mods_list_info_modid_title=Label(mods_list_info_main,text=Locale(E)+A,font=MainHandling.set_font(self.secondary_font,_B,14),anchor=B);mods_list_info_modid_title.grid(row=1,column=0,sticky=_A,padx=(0,10));self.all_locales[mods_list_info_modid_title]=E;mods_list_info_modid=Entry(mods_list_info_main,font=MainHandling.set_font(self.secondary_font,_B,14),fg_color=_F,border_width=0);mods_list_info_modid.configure(state=_D);mods_list_info_modid.delete(0,_H);mods_list_info_modid.insert(0,'-');mods_list_info_modid.configure(state=C);mods_list_info_modid.grid(row=1,column=1,sticky=_A,pady=(0,1));mods_list_info_name_title=Label(mods_list_info_main,text=Locale(F)+A,font=MainHandling.set_font(self.secondary_font,_B,14),anchor=B);mods_list_info_name_title.grid(row=2,column=0,sticky=_A,padx=(0,10));self.all_locales[mods_list_info_name_title]=F;mods_list_info_name=Entry(mods_list_info_main,font=MainHandling.set_font(self.secondary_font,_B,14),fg_color=_F,border_width=0);mods_list_info_name.configure(state=_D);mods_list_info_name.delete(0,_H);mods_list_info_name.insert(0,'-');mods_list_info_name.configure(state=C);mods_list_info_name.grid(row=2,column=1,sticky=_A,pady=(0,1));mods_list_info_version_title=Label(mods_list_info_main,text=Locale(G)+A,font=MainHandling.set_font(self.secondary_font,_B,14),anchor=B);mods_list_info_version_title.grid(row=3,column=0,sticky=_A,padx=(0,10));self.all_locales[mods_list_info_version_title]=G;mods_list_info_version=Entry(mods_list_info_main,font=MainHandling.set_font(self.secondary_font,_B,14),fg_color=_F,border_width=0);mods_list_info_version.configure(state=_D);mods_list_info_version.delete(0,_H);mods_list_info_version.insert(0,'-');mods_list_info_version.configure(state=C);mods_list_info_version.grid(row=3,column=1,sticky=_A,pady=(0,1));mods_list_info_mcversion_title=Label(mods_list_info_main,text=Locale(H)+A,font=MainHandling.set_font(self.secondary_font,_B,14),anchor=B);mods_list_info_mcversion_title.grid(row=4,column=0,sticky=_A,padx=(0,10));self.all_locales[mods_list_info_mcversion_title]=H;mods_list_info_mcversion=Entry(mods_list_info_main,font=MainHandling.set_font(self.secondary_font,_B,14),fg_color=_F,border_width=0);mods_list_info_mcversion.configure(state=_D);mods_list_info_mcversion.delete(0,_H);mods_list_info_mcversion.insert(0,'-');mods_list_info_mcversion.configure(state=C);mods_list_info_mcversion.grid(row=4,column=1,sticky=_A,pady=(0,1));mods_list_info_file_title=Label(mods_list_info_main,text=Locale(I)+A,font=MainHandling.set_font(self.secondary_font,_B,14),anchor=B);mods_list_info_file_title.grid(row=5,column=0,sticky=_A,padx=(0,10));self.all_locales[mods_list_info_file_title]=I;mods_list_info_file=Entry(mods_list_info_main,font=MainHandling.set_font(self.secondary_font,_B,14),fg_color=_F,border_width=0);mods_list_info_file.configure(state=_D);mods_list_info_file.delete(0,_H);mods_list_info_file.insert(0,'-');mods_list_info_file.configure(state=C);mods_list_info_file.grid(row=5,column=1,sticky=_A,pady=(0,1));self.mods_list_info_modid=mods_list_info_modid;self.mods_list_info_name=mods_list_info_name;self.mods_list_info_version=mods_list_info_version;self.mods_list_info_mcversion=mods_list_info_mcversion;self.mods_list_info_file=mods_list_info_file;mods_list_info_edit=Frame(mods_list_info_main);self.mods_list_info_edit=mods_list_info_edit;mods_list_info_edit.columnconfigure((0,1),weight=1);mods_list_info_edit_button=Button(mods_list_info_edit,text=Locale(J),font=MainHandling.set_font(self.secondary_font,_B,14),command=lambda:edit_mod_info(self));mods_list_info_edit_button.grid(row=0,column=0,sticky=_A,columnspan=2);self.all_locales[mods_list_info_edit_button]=J;self.mods_list_info_edit_button=mods_list_info_edit_button;mods_list_info_edit_save=Button(mods_list_info_edit,text=Locale(K),font=MainHandling.set_font(self.secondary_font,_B,14),command=lambda:edit_mod_info_save(self),fg_color=green,hover_color=_Z);self.all_locales[mods_list_info_edit_save]=K;mods_list_info_edit_save.grid_forget();self.mods_list_info_edit_save=mods_list_info_edit_save;mods_list_info_edit_cancel=Button(mods_list_info_edit,text=Locale(L),font=MainHandling.set_font(self.secondary_font,_B,14),command=lambda:edit_mod_info_cancel(self),fg_color=_a,hover_color=_b);self.all_locales[mods_list_info_edit_cancel]=L;self.mods_list_info_edit_cancel=mods_list_info_edit_cancel;mods_list_info_edit_status=Label(mods_list_info_main,text='',font=MainHandling.set_font(self.secondary_font,_B,14));self.mods_list_info_edit_status=mods_list_info_edit_status;mods_list_info_edit_status.grid_forget();mods_list_info_languages_frame=Frame(mods_list_info_frame,fg_color=_F);mods_list_info_frame.grid_rowconfigure(1,weight=1);mods_list_languages_title=Label(mods_list_info_languages_frame,text=Locale(M),font=MainHandling.set_font(self.secondary_font,_B,18));mods_list_languages_title.grid(row=0,column=0,pady=10,sticky=_A);self.all_locales[mods_list_languages_title]=M;mods_list_info_languages_frame.grid_columnconfigure(0,weight=1);self.mods_list_info_languages_frame=mods_list_info_languages_frame;mods_list_info_languages=ScrollableFrame(mods_list_info_languages_frame,fg_color=_F,scrollbar_button_color=_G,scrollbar_button_hover_color=_G,scrollbar_fg_color=_G);mods_list_info_languages.grid(row=1,column=0,sticky=_A);mods_list_info_languages_frame.grid_rowconfigure(1,weight=1);self.mods_list_info_languages=mods_list_info_languages;return mods_list_info_frame
def mods_list_buttons(self,mods_list_frame):C='mods_list.open_mods_folder';B='mods_list.refresh';A='mods_list.add';mods_list_buttons_frame=Frame(mods_list_frame,height=40,fg_color=_F);mods_list_buttons_frame.grid(row=2,column=0,padx=(10,5),pady=(5,10),sticky=_A);add_button=Button(mods_list_buttons_frame,text=Locale(A),height=40,width=0,font=MainHandling.set_font(self.secondary_font,_B,18),fg_color=green,hover_color=_Z,command=lambda:add_mod(self));add_button.grid(row=0,column=0,padx=(0,5),pady=(0,5),sticky=_A);self.all_locales[add_button]=A;del_button=Button(mods_list_buttons_frame,text=Locale(_X),state=_E,height=40,width=0,font=MainHandling.set_font(self.secondary_font,_B,18),fg_color=_c,text_color_disabled=_d,command=lambda:del_mod(self));del_button.grid(row=0,column=1,padx=(5,0),pady=(0,5),sticky=_A);self.all_locales[del_button]=_X;self.del_button=del_button;ref_button=Button(mods_list_buttons_frame,text=Locale(B),height=40,width=0,font=MainHandling.set_font(self.secondary_font,_B,18),command=lambda:refresh_mods_list(self));self.all_locales[ref_button]=B;open_mods_button=Button(mods_list_buttons_frame,text=Locale(C),height=40,width=0,font=MainHandling.set_font(self.secondary_font,_B,18),command=lambda:os.startfile(mods_folder));open_mods_button.grid(row=2,column=0,columnspan=2,pady=(5,0),sticky=_A);self.all_locales[open_mods_button]=C;mods_list_buttons_frame.grid_columnconfigure((0,1),weight=1);return mods_list_buttons_frame
def fill_mods_list(self,frame):
	log('Загрузка модов...','status')
	try:
		mods_info=get_mods()
		if len(mods_info)==0:log('Модов не найдено',_C)
		else:
			log(f"Найдено модов: {len(mods_info)}")
			try:
				for mod in mods_info:add_mod_to_mods_list(self,mod)
				log('Моды успешно загружены',_I)
			except Exception as e:log(f"Ошибка при загрузке модов: {e}",_C)
		return _K
	except Exception as e:log(f"Ошибка загрузки модов: {e}",_C);return _L
def add_mod_to_mods_list(self,mod):row=self.buttons_mods_row+1;mod_button=Button(self.mods_list_files,anchor='w',fg_color=_F,hover_color='#242424',border_width=0,border_color='#dedede',text=mod,font=MainHandling.set_font(self.secondary_font,_B,14),command=lambda:threading.Thread(target=select_mod(self,mod_button,mod)).start());mod_button.grid(row=row,column=0,sticky=_A);self.buttons_mods_list.append(mod_button);self.buttons_mods_row+=1
def select_mod(self,btn,mod):
	if self.selected_mod is not _B:
		if mod==self.selected_mod.cget(_M):log('Мод уже выбран.',_J)
		else:log(f"Выбран мод: {mod}",_J);self.selected_mod.configure(border_width=0);threading.Thread(target=fill_mod_info(self,btn,mod)).start();langs=get_mod_languages(mod);threading.Thread(target=fill_mod_languages(self,langs)).start()
	else:threading.Thread(target=fill_mod_info(self,btn,mod)).start();langs=get_mod_languages(mod);threading.Thread(target=fill_mod_languages(self,langs)).start()
def fill_mod_info(self,btn,mod):
	self.mods_list_info_edit_status.grid_forget();btn.configure(border_width=1);self.selected_mod=btn;info_file=get_mod_info(mod)
	if info_file==_e:self.mods_list_info_main.grid_forget();self.mods_list_info_empty_reason.configure(text=Locale('error.info_file_not_found'));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);log('Info file not found.',_C)
	elif info_file=='Error':self.mods_list_info_main.grid_forget();self.mods_list_info_empty_reason.configure(text=Locale('error.error_reading_file'));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);log('Error reading file.',_C)
	else:
		self.mods_list_info_empty.grid_forget();self.mods_list_info_main.grid(row=0,column=0,sticky=_A,columnspan=3,padx=18);modid=info_file[_Q];name=info_file[_R];version=info_file[_N];mcversion=info_file[_O];description=info_file[_S];info_type=info_file[_f]
		if info_type==_P:self.mods_list_info_edit_button.configure(state=_D,fg_color='#1f6aa5');self.mods_list_info_edit_button.grid(row=0,column=0,sticky=_A,columnspan=2);self.mods_list_info_edit_save.grid_forget();self.mods_list_info_edit_cancel.grid_forget()
		else:self.mods_list_info_edit_button.configure(state=_E,fg_color='#144870')
		self.mods_list_info_modid.configure(state=_D,border_width=0);self.mods_list_info_modid.delete(0,_H);self.mods_list_info_modid.insert(0,modid);self.mods_list_info_modid.configure(state=_E);self.mods_list_info_name.configure(state=_D,border_width=0);self.mods_list_info_name.delete(0,_H);self.mods_list_info_name.insert(0,name);self.mods_list_info_name.configure(state=_E);self.mods_list_info_version.configure(state=_D,border_width=0);self.mods_list_info_version.delete(0,_H);self.mods_list_info_version.insert(0,version);self.mods_list_info_version.configure(state=_E);self.mods_list_info_mcversion.configure(state=_D,border_width=0);self.mods_list_info_mcversion.delete(0,_H);self.mods_list_info_mcversion.insert(0,mcversion);self.mods_list_info_mcversion.configure(state=_E);self.mods_list_info_file.configure(state=_D,border_width=0);self.mods_list_info_file.delete(0,_H);self.mods_list_info_file.insert(0,info_type);self.mods_list_info_file.configure(state=_E)
	self.mods_list_info_languages.yview_moveto(0);self.update_idletasks();state_del=self.del_button.cget('state')
	if state_del==_E:self.del_button.configure(state=_D,font=MainHandling.set_font(self.secondary_font,_B,18),fg_color=_a,hover_color=_b);self.del_button.grid(row=0,column=1,padx=(5,0),sticky=_A)
def fill_mod_languages(self,langs):
	row=2
	if len(self.all_lang_labels)>0:
		for btn in self.all_lang_labels:btn.destroy()
	for(key,values)in langs.items():
		mod_languages_menu_lang_folder=Label(self.mods_list_info_languages,text='◉ '+Locale('mods.info.languages.folder')+f": {key}",font=MainHandling.set_font(self.secondary_font,_B,14),anchor='w');mod_languages_menu_lang_folder.grid(row=row,columnspan=2,rowspan=1,column=0,padx=(18,0),pady=0,sticky=_A)
		for(lang_code,language)in values.items():row+=1;mod_languages_menu_lang=Label(self.mods_list_info_languages,text=f"• {lang_code.strip()} - {language}",font=MainHandling.set_font(self.secondary_font,_B,14),anchor='w');mod_languages_menu_lang.grid(row=row,columnspan=2,rowspan=1,column=0,padx=(32,0),pady=0,sticky=_A);self.all_lang_labels.append(mod_languages_menu_lang)
		row+=1;self.all_lang_labels.append(mod_languages_menu_lang_folder);self.mods_list_info_languages_frame.grid(row=1,column=0,sticky=_A)
	threading.Thread(target=languages_size(self)).start()
def languages_size(self):
	self.update_idletasks();mods_list_info_languages_height=self.mods_list_info_languages.winfo_height();mods_list_info_languages_frame_height=self.mods_list_info_languages_frame.winfo_height()-48
	if mods_list_info_languages_frame_height<mods_list_info_languages_height:log('Языки переполнены',_C);self.mods_list_info_languages.configure(scrollbar_button_color=_g,scrollbar_button_hover_color=_h)
	else:log('Языки не переполнены',_I);self.mods_list_info_languages.configure(scrollbar_button_color=_G,scrollbar_button_hover_color=_G)
changed_buttons=[]
def mods_list_size(self):
	self.update_idletasks();mods_list_files_height=self.mods_list_files.winfo_height();mods_list_files_frame_height=self.mods_list_files_frame.winfo_height();available_height_for_buttons=mods_list_files_frame_height-54-16
	if available_height_for_buttons<mods_list_files_height:log('Список модов переполнены',_C);self.mods_list_files.configure(scrollbar_button_color=_g,scrollbar_button_hover_color=_h)
	else:log('Список модов не переполнен',_I);self.mods_list_files.configure(scrollbar_button_color=_G,scrollbar_button_hover_color=_G)
	log(f"Изменённые кнопки: {changed_buttons}",_J)
	for btn in self.buttons_mods_list:
		self.font_size=14;btn_text=btn.cget(_M);btn_width=btn.winfo_width();font=MainHandling.set_font(self.secondary_font,_B,self.font_size);btn_text_width=font.measure(btn_text)
		if btn_text_width>btn_width:
			log('Название мода слишком длинное. Изменение шрифта.',_J);log(f"Ширина текста: {btn_text_width}");log(f"Ширина кнопки: {btn_width}");changed_buttons.append(btn)
			while btn_text_width>btn_width and self.font_size>1:log(f"Новая ширина текста: {btn_text_width}");self.font_size-=1;font=MainHandling.set_font(self.secondary_font,_B,self.font_size);btn.configure(font=font);btn_text_width=font.measure(btn_text);log('Шрифт изменен.',_J)
			log(f"Итоговая ширина текста: {btn_text_width}",_I)
		if btn in changed_buttons:
			log('Продолжение изменения шрифта кнопок.',_J)
			while self.font_size>1:
				bigger_font=MainHandling.set_font(self.secondary_font,_B,self.font_size+1);bigger_btn_text_width=bigger_font.measure(btn_text)
				if bigger_btn_text_width>btn_width:log('Шрифт кнопки не изменен.',_C);changed_buttons.remove(btn);break
				else:log('Шрифт кнопки изменен.',_I);self.font_size+=1;font=bigger_font
	log(f"Изменённые кнопки: {changed_buttons}",_J)
def clean_mods_list(self):
	if len(self.buttons_mods_list)==0:log('Список модов пуст.',_I)
	else:
		log('Очистка списка модов...',_J)
		for btn in self.buttons_mods_list:btn.destroy()
		self.buttons_mods_list=[]
		if len(self.buttons_mods_list)==0:log('Список модов очищен.',_I)
		else:log('Ошибка при очистке списка модов.',_C)
def refresh_mods_list(self):
	log('Обновление списка модов...',_J);mods_info=get_mods();log(f"Текущее количество модов: {len(self.mods_list_files.winfo_children())}")
	if len(mods_info)==0:clean_mods_list(self)
	else:
		log(f"Получение списка модов...");current_mod_button_texts=[btn.cget(_M)for btn in self.buttons_mods_list]
		for btn_text in current_mod_button_texts:
			if btn_text not in mods_info:
				mod_button=next((mod for mod in self.buttons_mods_list if mod.cget(_M)==btn_text),_B)
				if mod_button:mod_button.destroy();self.buttons_mods_list.remove(mod_button);log(f"Мод {btn_text} удален.",_C);log(f"Текущее количество модов: {len(self.mods_list_files.winfo_children())}")
		for mod in mods_info:
			if mod not in current_mod_button_texts:add_mod_to_mods_list(self,mod)
		log('Список модов обновлен.',_I);self.mods_list_info_empty_reason.configure(text=Locale(_V))
	reset_info(self)
def del_mod(self,mod_folder_name):
	result=messagebox.askquestion(_i,f"Are you sure you want to remove {mod_folder_name}?\nThis action cannot be undone.",icon=_j)
	if result=='yes':log(f"Удаление мода: {mod_folder_name}");mod_folder_path=os.path.join(mods_folder,mod_folder_name);log(f"Путь к папке с модом: {mod_folder_path}");shutil.rmtree(mod_folder_path);log(f"Папка с модом успешно удалена.",_I);self.selected_mod=_B;refresh_mods_list(self)
	elif result=='no':log(f"Отмена удаления мода: {mod_folder_name}",_C)
def add_mod(self):
	file_path=customtkinter.filedialog.askopenfilename(title='Choose a mod',filetypes=[('Minecraft mod','*.jar')],initialdir=mods_folder,multiple=_K)
	for filename in file_path:
		if file_path:
			log(f"Добавление мода: {filename}");mod_folder_name=os.path.splitext(os.path.basename(filename))[0];mod_folder_path=os.path.join(mods_folder,mod_folder_name)
			if os.path.exists(mod_folder_path):
				result=messagebox.askquestion(_i,f"{filename} has already been added to the program.\nUpdate files?",icon=_j)
				if result=='yes':extract_mod_assets(filename)
			else:extract_mod_assets(filename)
	refresh_mods_list(self)
def extract_mod_assets(file_path):
	A='lang/';lang_folder_path='';lang_exists=_L;mod_folder_path=os.path.join(mods_folder,os.path.splitext(os.path.basename(file_path))[0])
	with zipfile.ZipFile(file_path,'r')as zip_ref:
		for file_info in zip_ref.infolist():
			log(f"Проверка файла: {file_info.filename}")
			if(file_info.filename.endswith(A)or A in file_info.filename)and'readme'not in file_info.filename.lower():
				lang_exists=_K;log(f"Найдена папка lang: {file_info.filename}");lang_folder_path=os.path.dirname(file_info.filename);log(f"Путь к папке с lang: {lang_folder_path}")
				try:zip_ref.extractall(mod_folder_path,members=[file_info]);log(f"Файл извлечен: {mod_folder_path}/{file_info.filename}",_I)
				except:log(f"Ошибка извлечения файла: {mod_folder_path}/{file_info.filename}",_C);break
		if not lang_exists:messagebox.showwarning('Ошибка',f"{file_path} не содержит файлов локализации.")
		else:
			for file_info in zip_ref.infolist():
				if _P in file_info.filename:zip_ref.extractall(mod_folder_path,members=[file_info]);break
				elif _T in file_info.filename:zip_ref.extractall(mod_folder_path,members=[file_info]);break
				elif _Y in file_info.filename:zip_ref.extractall(mod_folder_path,members=[file_info]);break
def get_mods():
	mods_in_folder=[];mods_count=0
	for folder in os.listdir(mods_folder):
		if os.path.isdir(os.path.join(mods_folder,folder)):mods_in_folder.append(folder);mods_count+=1
	return mods_in_folder
def enable_edit_info(self):
	A='edit_info';switch_state=self.settings_edit_info.get()
	if switch_state==self.settings_edit_info.cget('onvalue'):self.mods_list_info_edit.grid(row=6,column=0,sticky=_A,pady=(5,0),columnspan=2);self.save_settings(_U,A,'True')
	elif switch_state==self.settings_edit_info.cget('offvalue'):edit_mod_info_cancel(self);self.mods_list_info_edit.grid_forget();self.mods_list_info_edit_status.grid_forget();self.save_settings(_U,A,'False')
def edit_mod_info(self):self.mods_list_info_edit_status.grid_forget();self.mods_list_info_modid.configure(state=_D,border_width=1);self.mods_list_info_name.configure(state=_D,border_width=1);self.mods_list_info_version.configure(state=_D,border_width=1);self.mods_list_info_mcversion.configure(state=_D,border_width=1);self.mods_list_info_edit_button.grid_forget();self.mods_list_info_edit_save.grid(row=0,column=0,padx=(0,5),sticky=_A);self.mods_list_info_edit_cancel.grid(row=0,column=1,padx=(5,0),sticky=_A)
def edit_mod_info_save(self):
	A='utf-8';name=self.selected_mod.cget(_M);info_file=get_mod_info(name)[_k];modid=self.mods_list_info_modid.get();name=self.mods_list_info_name.get();version=self.mods_list_info_version.get();mcversion=self.mods_list_info_mcversion.get();file_save=_L
	try:
		with open(info_file,'r',encoding=A)as file:
			data=json.load(file,strict=_L)
			for mod in data:mod[_Q]=modid;mod[_R]=name;mod[_N]=version;mod[_O]=mcversion
		with open(info_file,'w',encoding=A)as file:json.dump(data,file,indent=4)
		file_save=_K
	except Exception as e:log(f"Ошибка сохранения файла: {e}",_C)
	edit_mod_info_cancel(self);self.mods_list_info_edit_status.grid(row=7,column=0,padx=(0,10),sticky=_A,columnspan=2)
	if file_save:self.mods_list_info_edit_status.configure(text=Locale('mods.info.edit.save.success'),text_color='#00ff00')
	else:self.mods_list_info_edit_status.configure(text=Locale('mods.info.edit.save.error'),text_color=_C)
def edit_mod_info_cancel(self):self.mods_list_info_edit_save.grid_forget();self.mods_list_info_edit_cancel.grid_forget();self.mods_list_info_edit.grid(row=6,column=0,sticky=_A,pady=(5,0),columnspan=2);self.mods_list_info_modid.configure(state=_E,border_width=0);self.mods_list_info_name.configure(state=_E,border_width=0);self.mods_list_info_version.configure(state=_E,border_width=0);self.mods_list_info_mcversion.configure(state=_E,border_width=0);self.mods_list_info_edit_button.grid(row=0,column=0,sticky=_A,columnspan=2)
def reset_info(self):
	if self.selected_mod is not _B:self.selected_mod.configure(border_width=0);self.selected_mod=_B
	self.mods_list_info_main.grid_forget();self.mods_list_info_main_title.configure(text=Locale(_W));self.mods_list_info_empty.grid(row=0,column=0,sticky=_A,padx=18);state_del=self.del_button.cget('state')
	if state_del==_D:self.del_button.configure(text=Locale(_X),state=_E,height=40,width=0,font=MainHandling.set_font(self.secondary_font,_B,18),fg_color=_c,text_color_disabled=_d)
	if len(self.all_lang_labels)>0:
		for btn in self.all_lang_labels:btn.destroy()
	self.mods_list_info_languages_frame.grid_forget();self.mods_list_info_languages.yview_moveto(.0);self.mods_list_info_modid.configure(border_width=0);self.mods_list_info_name.configure(border_width=0);self.mods_list_info_version.configure(border_width=0);self.mods_list_info_mcversion.configure(border_width=0)
def get_mod_languages(button_text):
	A4='tlh_AA';A3='sr_Latn_RS';A2='sr_Cyrl_RS';A1='sco_GB';A0='quz_PE';z='ka_GE';y='ja_JP';x='it_IT';w='is_IS';v='id_ID';u='hy_AM';t='hu_HU';s='hr_HR';r='hi_IN';q='he_IL';p='gu_IN';o='gl_ES';n='ga_IE';m='fr_FR';l='fr_CA';k='fil_PH';j='fi_FI';i='fa_IR';h='eu_ES';g='et_EE';f='es_MX';e='es_ES';d='es_CL';c='es_AR';b='es_VE';a='es_UY';Z='eo_UY';Y='enp_IU';X='en_US';W='en_UD';V='en_PT';U='en_NZ';T='en_GB';S='en_CA';R='en_AU';Q='el_GR';P='de_DE';O='da_DK';N='cs_CZ';M='ca_ES';L='bs_BA';K='bn_IN';J='bg_BG';I='be_BY';H='az_AZ';G='ast_ES';F='ar_SA';E='an_ES';D='am_ET';C='af_ZA';B='lang';A='ru_RU';mod_folder_path=os.path.join(mods_folder,button_text);lang_dict={};parent_folder='';lang_finded=_L;config_path=root_folder+'/config.ini';config=configparser.ConfigParser();config.read(config_path);language=config.get('main','language')
	if language==A:languages_dictionary={C:'Африкаанс',D:'Амхарский',E:'Арагонский',F:'Арабский',G:'Астурийский',H:'Азербайджанский',I:'Белорусский',J:'Болгарский',K:'Бенгальский',L:'Боснийский',M:'Каталанский',N:'Чешский',O:'Датский',P:'Немецкий',Q:'Греческий',R:'Английский (Австралия)',S:'Английский (Канада)',T:'Английский (Великобритания)',U:'Английский (Новая Зеландия)',V:'Английский (Пиратский язык)',W:'Английский (вверх ногами)',X:'Английский (Соединенные Штаты)',Y:'Английский (Шекспир)',Z:'Эсперанто',a:'Испанский (Уругвай)',b:'Испанский (Венесуэла)',c:'Испанский (Аргентина)',d:'Испанский (Чили)',e:'Испанский (Испания)',f:'Испанский (Мексика)',g:'Эстонский',h:'Баскский',i:'Персидский',j:'Финский',k:'Филиппинский',l:'Французский (Канада)',m:'Французский (Франция)',n:'Ирландский',o:'Галисийский',p:'Гуджарати',q:'Иврит',r:'Хинди',s:'Хорватский',t:'Венгерский',u:'Армянский',v:'Индонезийский',w:'Исландский',x:'Итальянский',y:'Японский',z:'Грузинский','kk_KZ':'Казахский','km_KH':'Кхмерский','kn_IN':'Каннада','ko_KR':'Корейский','ky_KG':'Киргизский','lb_LU':'Люксембургский','lo_LA':'Лаосский','lt_LT':'Литовский','lv_LV':'Латышский','mi_NZ':'Маори','mk_MK':'Македонский','ml_IN':'Малаялам','mn_MN':'Монгольский','mr_IN':'Маратхи','ms_MY':'Малайский','mt_MT':'Мальтийский','nb_NO':'Норвежский (Букмол)','ne_NP':'Непальский','nl_BE':'Голландский (Бельгия)','nl_NL':'Голландский (Нидерланды)','nn_NO':'Норвежский (Нюнорск)','no_NO':'Норвежский','oc_FR':'Окситанский','or_IN':'Ория','pa_IN':'Панджаби','pl_PL':'Польский','pt_BR':'Португальский (Бразилия)','pt_PT':'Португальский (Португалия)',A0:'Кечуа','ro_RO':'Румынский',A:'Русский',A1:'Шотландский','si_LK':'Сингальский','sk_SK':'Словацкий','sl_SI':'Словенский','sq_AL':'Албанский',A2:'Сербский (кириллица)',A3:'Сербский (латиница)','sv_SE':'Шведский','sw_TZ':'Суахили','ta_IN':'Тамильский','te_IN':'Телугу','th_TH':'Тайский',A4:'Клингонский','tr_TR':'Турецкий','ug_CN':'Уйгурский','uk_UA':'Украинский','ur_PK':'Урду','vi_VN':'Вьетнамский','wa_BE':'Валлонский','wo_SN':'Волоф','zh_CN':'Китайский (Китай)','zh_HK':'Китайский (Гонконг)','zh_TW':'Китайский (Тайвань)','zu_ZA':'Зулу','te_ST':'Тестовый язык'}
	else:languages_dictionary={C:'Afrikaans',D:'Amharic',E:'Aragonese',F:'Arabic',G:'Asturian',H:'Azerbaijani',I:'Belarusian',J:'Bulgarian',K:'Bengali',L:'Bosnian',M:'Catalan',N:'Czech',O:'Danish',P:'German',Q:'Greek',R:'English (Australia)',S:'English (Canada)',T:'English (United Kingdom)',U:'English (New Zealand)',V:'English (Pirate Speak)',W:'English (Upside Down)',X:'English (United States)',Y:'English (Shakespeare)',Z:'Esperanto',a:'Spanish (Uruguay)',b:'Spanish (Venezuela)',c:'Spanish (Argentina)',d:'Spanish (Chile)',e:'Spanish (Spain)',f:'Spanish (Mexico)',g:'Estonian',h:'Basque',i:'Persian',j:'Finnish',k:'Filipino',l:'French (Canada)',m:'French (France)',n:'Irish',o:'Galician',p:'Gujarati',q:'Hebrew',r:'Hindi',s:'Croatian',t:'Hungarian',u:'Armenian',v:'Indonesian',w:'Icelandic',x:'Italian',y:'Japanese',z:'Georgian','kk_KZ':'Kazakh','km_KH':'Khmer','kn_IN':'Kannada','ko_KR':'Korean','ky_KG':'Kyrgyz','lb_LU':'Luxembourgish','lo_LA':'Lao','lt_LT':'Lithuanian','lv_LV':'Latvian','mi_NZ':'Maori','mk_MK':'Macedonian','ml_IN':'Malayalam','mn_MN':'Mongolian','mr_IN':'Marathi','ms_MY':'Malay','mt_MT':'Maltese','nb_NO':'Norwegian (Bokmål)','ne_NP':'Nepali','nl_BE':'Dutch (Belgium)','nl_NL':'Dutch (Netherlands)','nn_NO':'Norwegian (Nynorsk)','no_NO':'Norwegian','oc_FR':'Occitan','or_IN':'Oriya','pa_IN':'Punjabi','pl_PL':'Polish','pt_BR':'Portuguese (Brazil)','pt_PT':'Portuguese (Portugal)',A0:'Quechua','ro_RO':'Romanian',A:'Russian',A1:'Scots','si_LK':'Sinhala','sk_SK':'Slovak','sl_SI':'Slovenian','sq_AL':'Albanian',A2:'Serbian (Cyrillic)',A3:'Serbian (Latin)','sv_SE':'Swedish','sw_TZ':'Swahili','ta_IN':'Tamil','te_IN':'Telugu','th_TH':'Thai',A4:'Klingon','tr_TR':'Turkish','ug_CN':'Uyghur','uk_UA':'Ukrainian','ur_PK':'Urdu','vi_VN':'Vietnamese','wa_BE':'Walloon','wo_SN':'Wolof','zh_CN':'Chinese (China)','zh_HK':'Chinese (Hong Kong)','zh_TW':'Chinese (Taiwan)','zu_ZA':'Zulu','te_ST':'Test Language'}
	for(root,dirs,files)in os.walk(mod_folder_path):
		if B in dirs:
			lang_folder=os.path.join(root,B)
			for(lang_root,lang_dirs,lang_files)in os.walk(lang_folder):
				if lang_files!=[]:
					lang_files_path=os.path.join(lang_root,lang_files[0]);parent_folder=os.path.split(os.path.dirname(lang_files_path))[-1]
					if parent_folder==B:parent_folder=os.path.split(os.path.dirname(lang_folder))[-1]
					if parent_folder not in lang_dict:
						lang_dict[parent_folder]={}
						for file in lang_files:
							lang_code=file.split('.')[0]
							for(code,language)in languages_dictionary.items():
								if lang_code.strip().lower()==code.strip().lower():lang_dict[parent_folder][lang_code]=language;lang_finded=_K
							if not lang_finded:lang_dict[parent_folder][lang_code]=Locale('mods.info.languages.unknown')
	return lang_dict
def get_mod_info(button_text):
	A='None';info_file_type=A;info_file_path=A;mod_folder_path=os.path.join(mods_folder,button_text)
	for(root,dirs,files)in os.walk(mod_folder_path):
		for file in files:
			if file==_P:info_file_type=_P;info_file_path=os.path.join(root,file);break
			elif file==_T:info_file_type=_T;info_file_path=os.path.join(root,file);break
			elif file==_Y:info_file_type=_Y;break
	if info_file_type==A:log(f"Информация о моде {button_text} не найдена.",_C);return _e
	else:return extract_mod_info(info_file_path,info_file_type)
def extract_mod_info(info_file,info_type):
	modid=name=description=version=mcversion='-'
	try:
		if info_type==_P:
			with open(info_file,'r')as file:
				content=file.read();regex_pattern='"(modid|name|description|version|mcversion)":\\s*"([^"]+)"';matches=re.findall(regex_pattern,content)
				for match in matches:
					key=match[0];value=match[1]
					if key==_Q:modid=value
					elif key==_R:name=value
					elif key==_S:description=value
					elif key==_N:version=value
					elif key==_O:mcversion=value
		elif info_type==_T:
			mod_values={}
			try:
				with open(info_file,'r')as file:content=file.read()
				data=toml.loads(content)
				if _U in data:
					mod_section=data[_U][0]
					for(key,value)in mod_section.items():
						mod_values[key]=value
						if key=='modId':modid=value
						elif key=='displayName':name=value
						elif key==_S:description=value
						elif key==_N:version=value
						elif key==_O:mcversion=value
			except(FileNotFoundError,toml.TomlDecodeError):print('Ошибка при разборе файла')
		mod_info_data={_Q:modid,_R:name,_S:description,_N:version,_O:mcversion,_f:info_type,_k:info_file};return mod_info_data
	except Exception as e:log(f"Не удалось получить информацию о моде: {e}",_C)