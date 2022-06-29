from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    global password_entry
    password_entry.delete(0,END)

    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    letter_list=[random.choice(letters) for char in range(nr_letters)]

    sym_list=[random.choice(symbols) for char in range(nr_symbols)]

    num_list=[random.choice(numbers) for char in range(nr_numbers)]
    password_list = []
    password_list = letter_list+sym_list+num_list

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char


    password_entry.insert(0,string=password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_entry,password_entry,name_entry,website_lable
    if len(name_entry.get())==0 or len(website_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showinfo(title='Oops',message='There has been a empty field left '
                                            'please fill all field to save')

    else:
        is_ok=messagebox.askokcancel(title='conform',message=f'Please conform\n'
            f'Website: {website_entry.get()}\nEmail/Userid: {name_entry.get()}\nPassword: {password_entry.get()}\n'
                                                             f'Is this correct?')
        if is_ok:
            data = {
                website_entry.get():{
                'userid_or_email': name_entry.get(),
                'password': password_entry.get()
            }
            }
            try:
                with open('data.json','r') as file:
                    bfile=json.load(file)
                    bfile.update(data)
                with open('data.json','w') as file:
                    json.dump(bfile,file,indent=4)
            except FileNotFoundError:
                with open('data.json','w') as file:
                    json.dump(data,file,indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0, END)
            name_entry.delete(0, END)
            website_lable.focus()
            messagebox.showinfo(title='Saved',message='Data has been successfully saved')

        else:
            messagebox.showinfo(title='make correction',message='Make the correction!!')

def serch():
    global website_entry,password_entry,name_entry
    try:
        tofind=website_entry.get()
        notfound=True
        with open("data.json",'r') as file:
            data=json.load(file)
            for key in data:
                if key==tofind:
                    password_entry.delete(0, END)
                    name_entry.delete(0, END)
                    password_entry.insert(0,data[tofind]['password'])
                    name_entry.insert(0, data[tofind]['userid_or_email'])
                    notfound=False
            if notfound and len(website_entry.get())!=0:
                messagebox.showinfo(title='Not Found', message=f'{tofind} is not found')
            elif len(website_entry.get())==0:
                messagebox.showinfo(title='Enter Website Name', message=f'Enter the name of the Website you are looking')
    except FileNotFoundError:
        messagebox.showinfo(title='File Not Found',message='File you are looking is not found')


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.configure(padx=30,pady=30)
window.title('Password Manager')

canvas=Canvas(height=200,width=200)
background=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=background,)
canvas.grid(row=0,column=1)

website_lable= Label(text='Website:',font=("Helvetica", 12, "bold italic"))
website_lable.focus()
website_lable.grid(row=1,column=0)

name_lable= Label(text='Email/User Name:',font=("Helvetica", 12, "bold italic"))
name_lable.grid(row=2,column=0)

password_lable= Label(text='Password:',font=("Helvetica", 12, "bold italic"))
password_lable.grid(row=3,column=0)

website_entry= Entry(width=30,font=("Times",12 , "bold"))
website_entry.grid(row=1,column=1,columnspan=1,padx=10,pady=10)

name_entry= Entry(width=48,font=("Times",12 , "bold"))
name_entry.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

password_entry= Entry(width=30,font=("Times",12 , "bold"))
password_entry.grid(row=3,column=1,padx=10,pady=10,columnspan=1)

generate_pass_button=Button(text='Generate Password',background='#a8b75b',font=("Verdana", 10),command=generate)
generate_pass_button.grid(row=3,column=2,columnspan=2)

add_button=Button(text='Add',background='#a8b75b',font=("Verdana", 10),width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)

serch_butten=Button(text='Search',background='#a8b75b',font=("Verdana", 10),width=15,command=serch)
serch_butten.grid(row=1,column=2,columnspan=2)




window.mainloop()