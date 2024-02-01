_G='\x1b[0m'
_F='\x1b[93m'
_E='\x1b[92m'
_D='[%d.%m.%Y %H:%M:%S]'
_C='\x1b[91m'
_B=None
_A='reset'
import datetime
debug_mode=True
def log(message=_B,color=_B):
	G='yellow';F='green';E='red';C=message;A=color
	if C is _B:C=''
	if debug_mode:
		H=datetime.datetime.now().strftime(_D);B={E:_C,F:_E,G:_F,'blue':'\x1b[94m','purple':'\x1b[95m',_A:_G}
		if A and A in B:
			if A==E:D=f"  [ERROR] {B[A]}{C}{B[_A]}"
			elif A==G:D=f" [STATUS] {B[A]}{C}{B[_A]}"
			elif A==F:D=f"[SUCCESS] {B[A]}{C}{B[_A]}"
			else:D=f"   [INFO] {B[A]}{C}{B[_A]}"
		else:D=f"   [INFO] {C}"
		print(f"{H} {D}")
def logs(message=_B,type=_B):
	G='success';F='warning';E='error';D='status';B=message
	if B is _B:B=''
	if debug_mode:
		H=datetime.datetime.now().strftime(_D);A={D:_F,E:_C,F:_C,G:_E,_A:_G}
		if type in A:
			if type==E:C=f"  [ERROR] {A[type]}{B}{A[_A]}"
			elif type==D:C=f" [STATUS] {A[type]}{B}{A[_A]}"
			elif type==G:C=f"[SUCCESS] {A[type]}{B}{A[_A]}"
			elif type==F:C=f"[WARNING] {A[type]}{B}{A[_A]}"
			else:C=f"   [INFO] {A[type]}{B}{A[_A]}"
		else:C=f"   [INFO] {B}"
		print(f"{H} {C}")