import tkinter as tk

def bmı_calculate():
    try:
        height=int(height_entry.get())/100
        weight=int(weight_entry.get())
        bmı = (weight)/(height**2)

        if(bmı==18.5):
            write=("UNDERWEİGHT")
        elif(18.5<bmı<=24.9):
            write=("NORMAL")
        elif(25<bmı<=29.9):
            write=("OVERWEİGHT")
        elif(30<bmı<=34.9):
            write=("OBESE")
        elif(35<=bmı):
            write=("EXTREMLY OBESE!!!")
        
        write_label.config(text=f"{write}")
    except:
        error=("ERRRRORR!!")
        write_label.config(text=f"{error}")



win = tk.Tk()
win.geometry("300x300")
FONT=("Calibri",15,"bold")

tittle_label = tk.Label(text="BMI TEST",font=FONT)
tittle_label.pack()

#WEİGHT EDITOR
weight_label = tk.Label(text="Enter Your Weight(kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry()
weight_entry.pack()

#HEİGHT EDITOR
height_label = tk.Label(text="Enter Your Height(cm):")
height_label.pack(pady=5)

height_entry = tk.Entry()
height_entry.pack()

#CALCULATE EDITOR
calculate_button = tk.Button(text="CALCULATE",command=bmı_calculate)
calculate_button.pack(pady=15)

#WRİTE LABEL
write_label = tk.Label()
write_label.pack(pady=10)



win.mainloop()