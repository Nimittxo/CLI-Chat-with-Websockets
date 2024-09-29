''' This is Just for refrence !, 
this GUI is not used in the application !
Currently the Chat Application supports CLI only,
                                             ~ github.com/Nimittxo 2024'''

'''GUI To be Integrated soon :)'''

''' USE ``` pip install customtkinter ``` for using this GUI'''



import customtkinter

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("600x550")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()