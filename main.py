from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


def save():
    with open("data.txt", mode="a") as data_file:
        data_file.write(f"\n {website_entry.get()} | {username_entry.get()} | {password_entry.get()}")
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")
    website_entry.focus()

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()
username_entry = Entry(width=51)
username_entry.grid(column=1, row=2, columnspan=2, pady=5)
username_entry.insert(0, "aniaplecka@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, pady=5)

# Buttons
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save, )
add_button.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
