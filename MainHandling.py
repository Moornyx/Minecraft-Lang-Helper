_E='utf-16-be'
_D='last_frame'
_C='FontManager error: '
_B='red'
_A=False
import configparser,os,random,shutil,string,sys,customtkinter as ctk
from typing import Union
from fontTools.ttLib import TTFont
from OutputHandling import log
root_folder=os.getcwd()
assets_folder=root_folder+'/assets/'
fonts_folder=root_folder+'/assets/fonts'
config_path=root_folder+'/config.ini'
loaded_fonts={}
def set_font(font,weight,size):
	A=weight
	if A==None:return ctk.CTkFont(family=f"{font}",size=size)
	else:return ctk.CTkFont(family=f"{font} {A}",size=size)
def generate_random_text(length):A=string.ascii_letters+string.digits+string.punctuation+' ';B=''.join(random.choice(A)for B in range(length));return B
def load_fonts():
	log('Загрузка шрифтов...')
	try:
		for A in os.listdir(fonts_folder):
			B=os.path.join(fonts_folder,A)
			if os.path.isdir(B):
				for C in os.listdir(B):
					try:XFontManager.load_font(os.path.join(fonts_folder,A,C))
					except:log(f"Не удалось загрузить шрифт: {C}",_B)
		log('Шрифты успешно загружены.','green');log(loaded_fonts)
	except:log('Ошибка загрузки шрифтов',_B)
def get_loaded_fonts():A=loaded_fonts.keys();return list(A)
def get_font_styles(font):A=loaded_fonts[font];return A
def save_last_frame(frame):
	A=frame;B=configparser.ConfigParser();B.read(config_path)
	try:
		with open(config_path,'w')as C:B.set('main',_D,A);B.write(C)
		log(f"Фрейм изменен на: {A}",'green')
	except Exception as D:log(f"Не удалось изменить фрейм: {A}",_B);log(D)
def load_last_frame():A=configparser.ConfigParser();A.read(config_path);B=A.get('main',_D);return B
class XFontManager(ctk.FontManager):
	@classmethod
	def windows_load_font(K,font_path,private=True,enumerable=_A):
		' Function taken from: https://stackoverflow.com/questions/11993290/truly-custom-font-in-tkinter/30631309#30631309 ';A=font_path;from ctypes import windll as B,byref,create_unicode_buffer as E,create_string_buffer as F;G=16;H=32
		if isinstance(A,bytes):C=F(A);D=B.gdi32.AddFontResourceExA
		elif isinstance(A,str):C=E(A);D=B.gdi32.AddFontResourceExW
		else:raise TypeError('font_path must be of type bytes or str')
		I=(G if private else 0)|(H if not enumerable else 0);J=D(byref(C),I,0);return bool(min(J,1))
	@classmethod
	def load_font(D,font_path):
		A=font_path
		if sys.platform.startswith('win'):
			E=D.windows_load_font(A,private=True,enumerable=_A)
			if E:
				B=XFontManager.get_font_family(A);C=XFontManager.get_font_style(A)
				if B not in loaded_fonts:loaded_fonts[B]=[C]
				elif C not in loaded_fonts[B]:loaded_fonts[B].append(C)
			return E
		elif sys.platform.startswith('linux'):
			try:shutil.copy(A,os.path.expanduser(D.linux_font_path));return True
			except Exception as F:sys.stderr.write(_C+str(F)+'\n');return _A
		else:return _A
	@classmethod
	def get_font_family(D,font_path):
		try:A=TTFont(font_path);B=A['name'].getName(1,3,1,1033).string.decode(_E);return B
		except Exception as C:sys.stderr.write(_C+str(C)+'\n');return''
	@classmethod
	def get_font_style(F,font_path):
		C='Regular'
		try:
			D=TTFont(font_path)
			for A in D['name'].names:
				if A.nameID==2 and A.platformID==3 and A.platEncID==1 and A.langID==1033:B=A.string.decode(_E);return B if B is not None else C
		except Exception as E:sys.stderr.write(_C+str(E)+'\n');return C