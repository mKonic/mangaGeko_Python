from customtkinter import *

def get_search(entry):
    print(entry)

app = CTk()
app.geometry("500x400")
app.title("Flux - Search")


frame = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)

label = CTkLabel(master=frame, text="This is a frame")
entry = CTkEntry(master=frame, placeholder_text="Type something...")
btn = CTkButton(master=frame, text="Submit", command=get_search)


label.pack(anchor="s", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, pady=10, padx=30)
btn.pack(anchor="n", expand=True, padx=30, pady=20)



app.mainloop()