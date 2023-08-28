from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2, pady=5)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=51)
username_input.grid(column=1, row=2, columnspan=2, pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=32)
password_input.grid(column=1, row=3, pady=5)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
