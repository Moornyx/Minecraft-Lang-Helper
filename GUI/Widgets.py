import customtkinter as ctk
from typing import Union,Tuple,Optional
class Frame(ctk.CTkFrame):
	def __init__(B,master,corner_radius=0,**A):super().__init__(master=master,corner_radius=corner_radius,**A)
class ScrollableFrame(ctk.CTkScrollableFrame):
	def __init__(B,master,corner_radius=0,**A):super().__init__(master=master,corner_radius=corner_radius,**A)
	def yview_moveto(A,fraction):A._parent_canvas.yview_moveto(fraction)
	def xview_moveto(A,fraction):A._parent_canvas.xview_moveto(fraction)
class Button(ctk.CTkButton):
	def __init__(B,master,corner_radius=0,**A):super().__init__(master=master,corner_radius=corner_radius,**A)
class Label(ctk.CTkLabel):
	def __init__(B,master,corner_radius=0,**A):super().__init__(master=master,corner_radius=corner_radius,**A)
class Entry(ctk.CTkEntry):
	def __init__(B,master,corner_radius=0,**A):super().__init__(master=master,corner_radius=corner_radius,**A)