import tkinter

main_window = tkinter.Tk()

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")

button1 = tkinter.Button(main_window, text= "tombol1")
button2 = tkinter.Button(main_window, text= "tombol2")

#methods positioning
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# menthods show gui
main_window.mainloop()
 
##tkinter adalah contoh GUI memakai OOP 