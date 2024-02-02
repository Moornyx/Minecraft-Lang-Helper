import configparser,os
root_folder=os.getcwd()
assets_folder=root_folder+'/assets/'
sounds_folder=assets_folder+'sounds/'
mods_folder=root_folder+'/mods/'
config_path=root_folder+'/config.ini'
logo=root_folder+'/assets/logo.png'
plant=root_folder+'/assets/plant.png'
version='0.6.3 alpha'
icons_theme='light'
main_font='Minecraft Ten'
green='#208B38'
theme='Dark'
def set_default_settings():
	if not os.path.exists(config_path):
		A=configparser.ConfigParser();A['main']={'language':'en_US','last_frame':'home_frame','font':'HelveticaNeueCyr','font_style':'Medium'};A['mods']={'edit_info':'True'}
		with open(config_path,'w',encoding='utf-8')as B:A.write(B)