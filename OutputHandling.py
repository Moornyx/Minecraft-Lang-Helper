import datetime
debug_mode=True
def log(message=None,color=None):
	H='yellow';G='green';F='red';E='reset';C=message;A=color
	if C is None:C=''
	if debug_mode:
		I=datetime.datetime.now().strftime('[%d.%m.%Y %H:%M:%S]');B={F:'\x1b[91m',G:'\x1b[92m',H:'\x1b[93m','blue':'\x1b[94m','purple':'\x1b[95m',E:'\x1b[0m'}
		if A and A in B:
			if A==F:D=f"  [ERROR] {B[A]}{C}{B[E]}"
			elif A==H:D=f" [STATUS] {B[A]}{C}{B[E]}"
			elif A==G:D=f"[SUCCESS] {B[A]}{C}{B[E]}"
			else:D=f"   [INFO] {B[A]}{C}{B[E]}"
		else:D=f"   [INFO] {C}"
		print(f"{I} {D}")