import tkinter.messagebox
from tkinter import *
from Mysql_Commands import *
from Mysql_connection import *


def center_screen():
    """ Makes a window 520x320 that starts at the center of the screen. """
    screen_x = gui.winfo_screenwidth()  # Returns the width of the monitor
    screen_y = gui.winfo_screenheight()  # Returns the height of the monitor
    center_x = int(screen_x / 2) - 250  # Width - 250 (width of the window) = Center X
    center_y = int(screen_y / 2) - 160  # Heights - 160 (height of the window) = Center Y
    return center_x, center_y


def query(*args):
    con = criar_conexao('localhost', 'root', '', 'python_login')
    print(args)
    if args[0] and args[1]:
        data = consultar_dados(nome=args[0], senha=args[1], con=con)
        if data:
            tkinter.messagebox.showinfo(message=f'Hello {data[0]}')
        else:
            tkinter.messagebox.showerror(message='Usuário e/ou senha inválidos')
    else:
        tkinter.messagebox.showerror(message='Usuário e/ou senha ausentes')


def insert(*args):
    con = criar_conexao('localhost', 'root', '', 'python_login')
    if args[0] and args[1]:
        if insere_usuario(nome=args[0],email=args[1], senha=args[2], con=con):
            tkinter.messagebox.showinfo(message='Conta adicionada')
        else:
            tkinter.messagebox.showerror(message='ERRO')
    else:
        tkinter.messagebox.showerror(message='Usuário e/ou Senha e/ou Email ausentes')


def new_window():
    window2 = Toplevel(gui)
    window2.title('Registrar')
    window2.config(bg='#222222')
    window2.geometry(f'500x430+{display_offset[0] - 50}+{display_offset[1] - 50}')

    text = Label(window2, text='Cadastro', font=('Arial', 30, 'bold'),bg='#222222',fg='#FFFFFF')
    text.place(x=160, y=20)

    new_user_name = Entry(window2, width=33, font=25)
    new_user_name.focus_set()
    new_user_name.place(x=100, y=130)

    new_user_email = Entry(window2, width=33, font=25)
    new_user_email.place(x=100, y=210)

    new_user_pass = Entry(window2, width=33, font=25)
    new_user_pass.place(x=100, y=290)

    new_username_label = Label(window2, text='Usuario', font=('Arial', 16), bg='#222222', fg='#FFFFFF')
    new_username_label.place(x=100, y=90)

    new_email_label = Label(window2, text='Email', font=('Arial', 16), bg='#222222', fg='#FFFFFF')
    new_email_label.place(x=100, y=170)

    new_password_label = Label(window2, text='Senha', font=('Arial', 16), bg='#222222', fg='#FFFFFF')
    new_password_label.place(x=100, y=250)

    button2 = Button(window2)
    button2.configure(width=14, height=1,border=0, text='Cadastrar',command=lambda :insert(new_user_name.get(),new_user_email.get(),new_user_pass.get()))
    button2.place(x=211, y=360)
    window2.mainloop()


def main(gui):
    text = Label(gui,text='Login', font=('Arial', 30, 'bold'),bg='#222222',fg='#FFFFFF')
    text.place(x=195, y=30)

    user_name = Entry(gui,width=33, font=25)
    user_name.focus_set()
    user_name.place(x=100, y=140)

    user_pass = Entry(gui,width=33, font=25)
    user_pass.place(x=100, y=215)

    username_label = Label(gui,text='Usuario', font=('Arial', 16),bg='#222222',fg='#FFFFFF')
    username_label.place(x=100, y=100)

    password_label = Label(gui,text='Senha', font=('Arial', 16),bg='#222222',fg='#FFFFFF')
    password_label.place(x=100, y=175)

    button = Button(gui)
    button.configure(width=10, height=1, text='Enviar dados',border=0, command=lambda: query(user_name.get(), user_pass.get()))
    button.place(x=130, y=260)

    button2 = Button(gui)
    button2.configure(width=10, height=1, text='Cadastrar',border=0, command=new_window)
    button2.place(x=297, y=260)

    gui.mainloop()


if __name__ == '__main__':
    gui = Tk()
    gui.configure(bg='#222222')
    gui.title('Entre em sua conta')
    display_offset = center_screen()
    gui.geometry(f'500x320+{display_offset[0]}+{display_offset[1]}')
    main(gui)
