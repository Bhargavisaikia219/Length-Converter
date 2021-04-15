from tkinter import *
from tkinter import ttk

#declaring convertunit funciton to convert unit and its value by pressing convert button
def convertunit():

    SI = {'millimeter': 0.001, 'centimeter': 0.01, 'meter': 1, 'kilometer': 1000,
          'inch': 0.0254, 'feet': 0.3048, 'yard': 0.9144, 'mile': 1609.35}

    unit_input = unit_label.get()
    unit_output = result_label.get()                            #getting values of each variables using get() method
    value_input = float(source_value_entry.get())

    if unit_input in SI.keys() and unit_output in SI.keys():    #check if input and output units are in SI
        input_ratio = float(SI.get(unit_input))                 #getting the value from SI
        output_ratio = float(SI.get(unit_output))
        result = value_input * input_ratio / output_ratio       #convert length from one unit to another
        result_value.set("%.4f" % result)

#declaring delete funciton to clear all fields by pressing clear button
def delete():
    unit_label.set("")          #sets an empty string
    result_label.set("")
    source_value.set("")
    result_value.set("")

window = Tk()                                   #create a new window and assign it to the variable 'window'
window.title("Length Conversion App")           #sets the title of the window
window.configure(background="light blue")       #set the background of tkinter window
window.geometry("320x220")                      #creating fixed geometry of the tkinter window with dimensions 320x220
window.resizable(width=False, height=False)     #freezes the window width and height, not resizable


#creating a drop-down list to select output unit, store the selected unit in length_unit
length_unit = StringVar()                                                                                   #Holds a string; default value ""
unit_label = ttk.Combobox(window, textvariable=length_unit, width=15 )                                      #label refers to the textbox to put any text or image
unit_label["value"] = ("millimeter", "centimeter", "meter", "kilometer", "inch", "feet", "yard", "mile")    #options to be appeared on the drop-down list
unit_label.grid(column=0, row=0, padx=35, pady=25)                                                          #organizes a textbox in a table-like structure

#to create a textbox to take input value
source_value = DoubleVar()                                                  #Holds a float; default value 0.0
source_value_entry = Entry(window, textvariable=source_value, width=15)     #to input value entry from the user
source_value_entry.grid(column=1, row=0, pady=25)


#creating a drop-down list to select output unit, store the selected unit in result_unit
result_unit = StringVar()
result_label = ttk.Combobox(window, textvariable=result_unit, width=15)
result_label["value"] = ("millimeter", "centimeter", "meter", "kilometer", "inch", "feet", "yard", "mile")
result_label.grid(column=0, row=1, padx=15, pady=30)

#to create a textbox to display output value
result_value = DoubleVar()
result_entry = Entry(window, textvariable=result_value, width=15)       #to display output entry
result_entry.grid(column=1, row=1, pady=30)
result_entry.delete(0, "end")                                           #deleting content from textbox

#To add covert and clear button
convert = Button(window, text="Convert", bg="blue", fg="white", width=10, command=convertunit)      #command calls convertunit function
convert.grid(column=0, row=3, padx=15, pady=3)

clear = Button(window, text="Clear", bg="grey", fg="white", width=10, command=delete)               #command calls delete function
clear.grid(column=1, row=3, padx=15, pady=3)

#tells Python to run the Tkinter event loop
window.mainloop()
