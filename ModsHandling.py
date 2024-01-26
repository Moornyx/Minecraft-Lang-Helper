_H='warning'
_G='Warning'
_F='fabric.mod.json'
_E=False
_D='mods.toml'
_C='mcmod.info'
_B='red'
_A=True
import configparser,re,shutil,customtkinter,os,zipfile
from tkinter import messagebox
from Localization import Locale,get_current_language
from OutputHandling import log
import toml
root_folder=os.getcwd()
mods_folder=root_folder+'/mods/'
def add_mod():
	B=customtkinter.filedialog.askopenfilename(title='Choose a mod',filetypes=[('Minecraft mod','*.jar')],initialdir=mods_folder,multiple=_A)
	for A in B:
		if B:
			log(f"Добавление мода: {A}");C=os.path.splitext(os.path.basename(A))[0];D=os.path.join(mods_folder,C)
			if os.path.exists(D):
				E=messagebox.askquestion(_G,f"{A} has already been added to the program.\nUpdate files?",icon=_H)
				if E=='yes':extract_mod_assets(A)
			else:extract_mod_assets(A)
def del_mod(mod_folder_name):
	A=mod_folder_name;B=messagebox.askquestion(_G,f"Are you sure you want to remove {A}?\nThis action cannot be undone.",icon=_H)
	if B=='yes':log(f"Удаление мода: {A}");C=os.path.join(mods_folder,A);log(f"Путь к папке с модом: {C}");shutil.rmtree(C);log(f"Папка с модом успешно удалена.",'green');return _A
	elif B=='no':log(f"Отмена удаления мода: {A}",_B);return _E
def extract_mod_assets(file_path):
	G='lang/';D=file_path;E='';F=_E;B=os.path.join(mods_folder,os.path.splitext(os.path.basename(D))[0])
	with zipfile.ZipFile(D,'r')as C:
		for A in C.infolist():
			log(f"Проверка файла: {A.filename}")
			if(A.filename.endswith(G)or G in A.filename)and'readme'not in A.filename.lower():
				F=_A;log(f"Найдена папка lang: {A.filename}");E=os.path.dirname(A.filename);log(f"Путь к папке с lang: {E}")
				try:C.extractall(B,members=[A]);log(f"Файл извлечен: {B}/{A.filename}",'green')
				except:log(f"Ошибка извлечения файла: {B}/{A.filename}",_B);break
		if not F:messagebox.showwarning('Ошибка',f"{D} не содержит файлов локализации.")
		else:
			for A in C.infolist():
				if _C in A.filename:C.extractall(B,members=[A]);break
				elif _D in A.filename:C.extractall(B,members=[A]);break
				elif _F in A.filename:C.extractall(B,members=[A]);break
def get_mod_info(button_text):
	E=button_text;D='None';A=D;C=D;G=os.path.join(mods_folder,E)
	for(F,I,H)in os.walk(G):
		for B in H:
			if B==_C:A=_C;C=os.path.join(F,B);break
			elif B==_D:A=_D;C=os.path.join(F,B);break
			elif B==_F:A=_F;break
	if A==D:log(f"Информация о моде {E} не найдена.",_B);return'Not Found'
	else:return extract_mod_info(C,A)
def extract_mod_info(info_file,info_type):
	S='mods';R='name';Q='modid';N='mcversion';M='version';L='description';D=info_type;C=info_file;E=F=G=H=I='-'
	try:
		if D==_C:
			with open(C,'r')as J:
				K=J.read();T='"(modid|name|description|version|mcversion)":\\s*"([^"]+)"';U=re.findall(T,K)
				for O in U:
					A=O[0];B=O[1]
					if A==Q:E=B
					elif A==R:F=B
					elif A==L:G=B
					elif A==M:H=B
					elif A==N:I=B
		elif D==_D:
			V={}
			try:
				with open(C,'r')as J:K=J.read()
				P=toml.loads(K)
				if S in P:
					W=P[S][0]
					for(A,B)in W.items():
						V[A]=B
						if A=='modId':E=B
						elif A=='displayName':F=B
						elif A==L:G=B
						elif A==M:H=B
						elif A==N:I=B
			except(FileNotFoundError,toml.TomlDecodeError):print('Ошибка при разборе файла')
		X={Q:E,R:F,L:G,M:H,N:I,'info_type':D,'info_path':C};return X
	except Exception as Y:log(f"Не удалось получить информацию о моде: {Y}",_B)
def get_mods():
	A=[];C=0
	for B in os.listdir(mods_folder):
		if os.path.isdir(os.path.join(mods_folder,B)):A.append(B);C+=1
	return A
def get_mod_languages(button_text):
	A4='tlh_AA';A3='sr_Latn_RS';A2='sr_Cyrl_RS';A1='sco_GB';A0='quz_PE';z='he_IL';y='gu_IN';x='gl_ES';w='ga_IE';v='fr_FR';u='fr_CA';t='fil_PH';s='fi_FI';r='fa_IR';q='eu_ES';p='et_EE';o='es_MX';n='es_ES';m='es_CL';l='es_AR';k='es_VE';j='es_UY';i='eo_UY';h='enp_IU';g='en_US';f='en_UD';e='en_PT';d='en_NZ';c='en_GB';b='en_CA';a='en_AU';Z='el_GR';Y='de_DE';X='da_DK';W='cs_CZ';V='ca_ES';U='bs_BA';T='bn_IN';S='bg_BG';R='be_BY';Q='az_AZ';P='ast_ES';O='ar_SA';N='an_ES';M='am_ET';L='af_ZA';G='lang';F='ru_RU';A5=os.path.join(mods_folder,button_text);B={};A='';H=_E;A6=root_folder+'/config.ini';I=configparser.ConfigParser();I.read(A6);C=I.get('main','language')
	if C==F:J={L:'Африкаанс',M:'Амхарский',N:'Арагонский',O:'Арабский',P:'Астурийский',Q:'Азербайджанский',R:'Белорусский',S:'Болгарский',T:'Бенгальский',U:'Боснийский',V:'Каталанский',W:'Чешский',X:'Датский',Y:'Немецкий',Z:'Греческий',a:'Английский (Австралия)',b:'Английский (Канада)',c:'Английский (Великобритания)',d:'Английский (Новая Зеландия)',e:'Английский (Пиратский язык)',f:'Английский (вверх ногами)',g:'Английский (Соединенные Штаты)',h:'Английский (Шекспир)',i:'Эсперанто',j:'Испанский (Уругвай)',k:'Испанский (Венесуэла)',l:'Испанский (Аргентина)',m:'Испанский (Чили)',n:'Испанский (Испания)',o:'Испанский (Мексика)',p:'Эстонский',q:'Баскский',r:'Персидский',s:'Финский',t:'Филиппинский',u:'Французский (Канада)',v:'Французский (Франция)',w:'Ирландский',x:'Галисийский',y:'Гуджарати',z:'Иврит','hi_IN':'Хинди','hr_HR':'Хорватский','hu_HU':'Венгерский','hy_AM':'Армянский','id_ID':'Индонезийский','is_IS':'Исландский','it_IT':'Итальянский','ja_JP':'Японский','ka_GE':'Грузинский','kk_KZ':'Казахский','km_KH':'Кхмерский','kn_IN':'Каннада','ko_KR':'Корейский','ky_KG':'Киргизский','lb_LU':'Люксембургский','lo_LA':'Лаосский','lt_LT':'Литовский','lv_LV':'Латышский','mi_NZ':'Маори','mk_MK':'Македонский','ml_IN':'Малаялам','mn_MN':'Монгольский','mr_IN':'Маратхи','ms_MY':'Малайский','mt_MT':'Мальтийский','nb_NO':'Норвежский (Букмол)','ne_NP':'Непальский','nl_BE':'Голландский (Бельгия)','nl_NL':'Голландский (Нидерланды)','nn_NO':'Норвежский (Нюнорск)','no_NO':'Норвежский','oc_FR':'Окситанский','or_IN':'Ория','pa_IN':'Панджаби','pl_PL':'Польский','pt_BR':'Португальский (Бразилия)','pt_PT':'Португальский (Португалия)',A0:'Кечуа','ro_RO':'Румынский',F:'Русский',A1:'Шотландский','si_LK':'Сингальский','sk_SK':'Словацкий','sl_SI':'Словенский','sq_AL':'Албанский',A2:'Сербский (кириллица)',A3:'Сербский (латиница)','sv_SE':'Шведский','sw_TZ':'Суахили','ta_IN':'Тамильский','te_IN':'Телугу','th_TH':'Тайский',A4:'Клингонский','tr_TR':'Турецкий','ug_CN':'Уйгурский','uk_UA':'Украинский','ur_PK':'Урду','vi_VN':'Вьетнамский','wa_BE':'Валлонский','wo_SN':'Волоф','zh_CN':'Китайский (Китай)','zh_HK':'Китайский (Гонконг)','zh_TW':'Китайский (Тайвань)','zu_ZA':'Зулу','te_ST':'Тестовый язык'}
	else:J={L:'Afrikaans',M:'Amharic',N:'Aragonese',O:'Arabic',P:'Asturian',Q:'Azerbaijani',R:'Belarusian',S:'Bulgarian',T:'Bengali',U:'Bosnian',V:'Catalan',W:'Czech',X:'Danish',Y:'German',Z:'Greek',a:'English (Australia)',b:'English (Canada)',c:'English (United Kingdom)',d:'English (New Zealand)',e:'English (Pirate Speak)',f:'English (Upside Down)',g:'English (United States)',h:'English (Shakespeare)',i:'Esperanto',j:'Spanish (Uruguay)',k:'Spanish (Venezuela)',l:'Spanish (Argentina)',m:'Spanish (Chile)',n:'Spanish (Spain)',o:'Spanish (Mexico)',p:'Estonian',q:'Basque',r:'Persian',s:'Finnish',t:'Filipino',u:'French (Canada)',v:'French (France)',w:'Irish',x:'Galician',y:'Gujarati',z:'Hebrew','hi_IN':'Hindi','hr_HR':'Croatian','hu_HU':'Hungarian','hy_AM':'Armenian','id_ID':'Indonesian','is_IS':'Icelandic','it_IT':'Italian','ja_JP':'Japanese','ka_GE':'Georgian','kk_KZ':'Kazakh','km_KH':'Khmer','kn_IN':'Kannada','ko_KR':'Korean','ky_KG':'Kyrgyz','lb_LU':'Luxembourgish','lo_LA':'Lao','lt_LT':'Lithuanian','lv_LV':'Latvian','mi_NZ':'Maori','mk_MK':'Macedonian','ml_IN':'Malayalam','mn_MN':'Mongolian','mr_IN':'Marathi','ms_MY':'Malay','mt_MT':'Maltese','nb_NO':'Norwegian (Bokmål)','ne_NP':'Nepali','nl_BE':'Dutch (Belgium)','nl_NL':'Dutch (Netherlands)','nn_NO':'Norwegian (Nynorsk)','no_NO':'Norwegian','oc_FR':'Occitan','or_IN':'Oriya','pa_IN':'Punjabi','pl_PL':'Polish','pt_BR':'Portuguese (Brazil)','pt_PT':'Portuguese (Portugal)',A0:'Quechua','ro_RO':'Romanian',F:'Russian',A1:'Scots','si_LK':'Sinhala','sk_SK':'Slovak','sl_SI':'Slovenian','sq_AL':'Albanian',A2:'Serbian (Cyrillic)',A3:'Serbian (Latin)','sv_SE':'Swedish','sw_TZ':'Swahili','ta_IN':'Tamil','te_IN':'Telugu','th_TH':'Thai',A4:'Klingon','tr_TR':'Turkish','ug_CN':'Uyghur','uk_UA':'Ukrainian','ur_PK':'Urdu','vi_VN':'Vietnamese','wa_BE':'Walloon','wo_SN':'Wolof','zh_CN':'Chinese (China)','zh_HK':'Chinese (Hong Kong)','zh_TW':'Chinese (Taiwan)','zu_ZA':'Zulu','te_ST':'Test Language'}
	for(A7,A8,AD)in os.walk(A5):
		if G in A8:
			K=os.path.join(A7,G)
			for(A9,AE,D)in os.walk(K):
				if D!=[]:
					AA=os.path.join(A9,D[0]);A=os.path.split(os.path.dirname(AA))[-1]
					if A==G:A=os.path.split(os.path.dirname(K))[-1]
					if A not in B:
						B[A]={}
						for AB in D:
							E=AB.split('.')[0]
							for(AC,C)in J.items():
								if E.strip().lower()==AC.strip().lower():B[A][E]=C;H=_A
							if not H:B[A][E]=Locale('mods.info.languages.unknown')
	return B