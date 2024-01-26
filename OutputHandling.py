import datetime
debug_mode=True
def log(message=None,color=None):
	E='reset';B=color;A=message
	if A is None:A=''
	if debug_mode:
		F=datetime.datetime.now().strftime('[%d.%m.%Y %H:%M:%S]');C={'red':'\x1b[91m','green':'\x1b[92m','yellow':'\x1b[93m','blue':'\x1b[94m','purple':'\x1b[95m',E:'\x1b[0m'}
		if B and B in C:D=f"{C[B]}{A}{C[E]}"
		else:D=A
		print(f"{F} {D}")