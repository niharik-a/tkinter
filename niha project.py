# import tkinter
# from tkinter import*
# root = Tk()

# # root.title('MY BOX GUI')
# # # root.iconbitmap("star.ico")
# # root.geometry("500x500")

# my_label = Label(root,text ='how old r u ').pack()
# my_label2 = Label(root,text ="your r like a kid ").pack()

# # # my_label.grid(row=0,column=1)
# # # my_label2.grid(row=0,column=2)


# b1 = Button(root,text = "choose a color", font =("Arial Black",20))

# def my_com():
#     pass

# def call_me():
#     l1 = Label(root,text =" developed by XYZ",font=('arial',20)).pack()


# my_menu= Menu(root)
# root.config(menu = my_menu)



# my_label =Label(root,text ='Hi').pack()
# my_label2 =Label(root,text ="where are u from").pack()

# my_label = Label (root,text = 'how r u !!')

# my_label.pack()

# root.mainloop()

# m =tkinter.Tk()
# m.mainloop()


# # # from tkinter import*
# # # from tkinter import messagebox
# # # root=Tk()
# # # # root.iconbitmap('apple.ico')
# # # root.title('MENU FRAME')
# # # root.geometry('600x600')
# # # root.configure(background = '#68615f')



from tkinter import*
root=Tk()
def send():
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>hi")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"bot=>hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"bot=>fine and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"bot=>okay")
    elif(e.get()=="what are you doing"):
        txt.insert(END,"\n"+"bot=>i am studing")
    elif(e.get()=="how is your studies"):
        txt.insert(END,"\n"+"bot=>good and you")
    else:
        txt.insert(END,"\n"+"bot=>nice to hear")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOX")
root.mainloop()


# from tkinter import*
# root=Tk()
# def send():
#     send="you=>"+e.get()
#     txt.insert(END,"\n"+send)
#     if(e.get()=="hello"):
#         txt.insert(END,"\n"+"Bot=>hi")
#     elif (e.get()=="hi"):
#         txt.insert(END,"\n"+"bot=>hello")
#     elif(e.get()=="how are you"):
#         txt.insert(END,"\n"+"bot=>fine and you")
#     elif(e.get()=="fine"):
#         txt.insert(END,"\n"+"bot=>okay")
#     elif(e.get()=="what are you doing"):
#         txt.insert(END,"\n"+"bot=>i am studing")
#     elif(e.get()=="how is your studies"):
#         txt.insert(END,"\n"+"bot=>good and you")
#     else:
#         txt.insert(END,"\n"+"bot=>nice to hear")
#     e.delete(0,END)
# txt=Text(root)
# txt.grid(row=0,column=0,columnspan=2)
# e=Entry(root,width=100)
# send=Button(root,text="send",command=send).grid(row=1,column=1)
# e.grid(row=1,column=0)
# root.title("CHATBOX")
# root.mainloop()



































