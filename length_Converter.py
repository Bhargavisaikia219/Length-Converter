from tkinter import *

window=Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="light blue")
window.geometry("320x220")
window.resizable(width=False, height=False)

feet_label=Label(window, text="Feet", bg="purple", fg="white", width=15)
feet_label.grid(column=0, row=0, padx=15, pady=15)

feet_value=DoubleVar()
feet_entry=Entry(window, textvariable="feet_value", width=15)
feet_entry.grid(column=1, row=0)
feet_entry.delete(0, "end")
window.mainloop()