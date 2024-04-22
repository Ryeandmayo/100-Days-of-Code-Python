from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
EMAIL= "Email@email.com"
FONT_NAME = "arial"

#For random pass gen

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    import pyperclip
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    pw_join = "".join(password_list)
    pass_entry.insert(0,pw_join)
    pyperclip.copy(pw_join) #Copies generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website= web_entry.get()
    username= user_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS :(", message= "Please make sure you havent left any fields empty")
    else:
        is_okay = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:\n"
                                                                     f"website: {website}\n"
                                                                     f"username: {username}\n"
                                                                     f"password: {password}\n"
                                                                     f"Is it okay to save?")
        if is_okay:
            with open("password.txt", "a") as f:
                f.write(f"website: {website} | username: {username}| password: {password}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


#Labels:
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entries:
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2,  columnspan=2)
user_entry.insert(0, EMAIL)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

#Buttons
gen_button = Button(text="Generate Password", command=pass_gen)
gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()