from tkinter import *
from tkinter import filedialog as tkFileDialog

import main

filename = ''

black_lst = []
proxy_lst = []


def browsefunc():
    global filename
    filename = tkFileDialog.askopenfilename(filetypes=(("txt files","*.txt"),("All files","*.*")))
    ent1.insert(END, filename) # add this


root = Tk()
root.geometry("500x500")

lab_3 = Label(width=100, fg='black', text='Прокси не найдено')


def str_to_sort_list(event):
    print(filename)
    file = open(filename, 'r')
    s = file.read()
    proxy_lst = s.replace(' ', '').split('\n')
    proxy_lst.remove('')
    if proxy_lst != []:
        lab_3.config(text='\n'.join(proxy_lst))
#    main.main(proxy)
    file.close()


ent1=Entry(root,font=40)


ent2=Entry(root,font=40)
ent2.insert(0, "0")


ent3=Entry(root,font=40)


but = Button(text="Запуск программы")
lab = Label(width=100, fg='black', text='Нажмите на кнопку')
lab_1 = Label(width=100, fg='black', text='Введите количество октетов')
lab_2 = Label(width=100, fg='black', text='Нажмите на кнопку')


but.bind('<Button-1>', str_to_sort_list)



b1=Button(root,text="DEM",font=40,command=browsefunc)

ent1.pack()
b1.pack()

lab_3.pack()

ent2.pack()

ent3.pack()
if black_lst!=[]:
    lab_proxy_bl = Label(width=100, fg='black', text=f'\n'.join(black_lst))
    lab_proxy_bl.pack()


lab.pack()
but.pack()


root.mainloop()
#str_to_sort_list()
