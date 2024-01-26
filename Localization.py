_E='/assets/lang/'
_D='main'
_C='red'
_B='utf-8'
_A='language'
import os,json
from OutputHandling import log
import configparser
root_folder=os.getcwd()
config_path=root_folder+'/config.ini'
def Locale(key):
	A=key;F=configparser.ConfigParser();F.read(config_path);D='';D=F.get(_D,_A);C=root_folder+_E
	if not os.path.exists(C):os.makedirs(C)
	else:
		G=os.path.join(C,f"{D}.json")
		if os.path.exists(G):
			with open(G,'r',encoding=_B)as E:
				B=json.load(E).get(A)
				if B is not None:return B
				else:
					log(f'Значение "{A}" не найдено в языке {D}.',_C)
					with open(os.path.join(C,'en_US.json'),'r',encoding=_B)as E:
						B=json.load(E).get(A)
						if B is not None:return B
						else:log(f'Значение "{A}" не найдено.',_C);return A
		else:log(f'Значение "{A}" не найдено.',_C);return A
def get_languages():
	B={};C=root_folder+_E;E=os.listdir(C)
	for D in E:
		A=os.path.join(C,D);F=D.replace('.json','')
		with open(A,'r',encoding=_B)as A:G=json.load(A).get(_A);B[G]=F
	return B
def change_language(language):
	C=get_languages();A=C[language];B=configparser.ConfigParser();B.read(config_path)
	try:
		with open(config_path,'w')as D:B.set(_D,_A,A);B.write(D)
		log(f"Язык изменен на: {A}",'green');return True
	except Exception as E:log(f"Не удалось изменить язык: {A}",_C);log(E);return False
def get_current_language():
	A=configparser.ConfigParser();A.read(config_path);B=A.get(_D,_A);C=root_folder+_E;D=os.path.join(C,f"{B}.json")
	with open(D,'r',encoding=_B)as E:F=json.load(E).get(_A)
	return F