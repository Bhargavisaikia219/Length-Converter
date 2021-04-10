from tkinter import *
from tkinter import ttk

window=Tk()
window.title("Length Conversion App")
window.configure(background="light blue")
window.geometry("320x220")
window.resizable(width=False, height=False)

length_unit=StringVar()
unit_label=ttk.Combobox(window, textvariable=length_unit, width=15)
unit_label["value"]=("milimeter", "centimeter", "meter", "kilometer", "inch", "feet", "yard", "mile")
unit_label.grid(column=0, row=0, padx=15, pady=15)

source_value=DoubleVar()
source_value_entry=Entry(window, textvariable="source_value", width=15)
source_value_entry.grid(column=1, row=0)

result_unit=StringVar()
result_label=ttk.Combobox(window, textvariable=result_unit, width=15)
result_label["value"]=("milimeter", "centimeter", "meter", "kilometer", "inch", "feet", "yard", "mile")
result_label.grid(column=0, row=1, padx=15, pady=15)

result_value=DoubleVar()
result_entry=Entry(window, textvariable="result_value", width=15)
result_entry.grid(column=1, row=1)
result_entry.delete(0, "end")



window.mainloop()