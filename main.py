
import tkinter as tk
from tkinter import *
from tkinter import ttk
from sqlalchemy import create_engine
from  datetime import date
from my_invoice import my_invoice
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk

from config import *
my_conn = create_engine("mysql+mysqlconnector://root:minSEU32Hoshi@localhost/komal1db")
sb=[]
my_w=None


app_name_window = tk.Tk()
app_name_window.title("My App Name")
app_name_window.attributes('-fullscreen', True)
app_name_window.geometry("1580x800+0+0")

app_name_window.configure(bg="blue")
image_path = "C:/Users/Yameeni/bur.png" 
background_image = Image.open(image_path)  
window_width = app_name_window.winfo_screenwidth()
window_height = app_name_window.winfo_screenheight()
background_image = background_image.resize((window_width, window_height))# Replace "background.jpg" with your image file
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(app_name_window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




app_name_label = tk.Label(app_name_window, text="THE YUM XPRESS", font=("Algerian", 70))
app_name_label.pack(pady=200)
# Create a function to open the login window
def open_login_window():
    app_name_window.withdraw() 
   
    login_window.deiconify()
  


start_button = tk.Button(app_name_window, text="Start ->", command=open_login_window,font=("Algerian", 25),width=10, height=3)
start_button.pack()


login_window = tk.Toplevel()
login_window.title("Login")
login_window.attributes('-fullscreen', True)
login_window.geometry("1580x900+0+0")
login_window.withdraw() 

def perform_login():
    username = username_entry.get()
    password = password_entry.get()

 
    query = f"SELECT * FROM users1 WHERE username = '{username}' AND password = '{password}'"
    result = my_conn.execute(query).fetchone()

    if result:
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

label_font = ("Arial", 30) 
window_width = login_window.winfo_screenwidth()
window_height = login_window.winfo_screenheight()
image = Image.open("C:/Users/Yameeni/food.png")
image = image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(login_window, image=background_image)
background_label.place(relwidth=1, relheight=1)

username_label = tk.Label(login_window, text="Username", font=("Algerian",25), bg="white")
username_label.place(relx=0.5, rely=0.1, anchor="center")

username_entry = tk.Entry(login_window, font=label_font)
username_entry.place(relx=0.5, rely=0.18, anchor="center")

password_label = tk.Label(login_window, text="Password", font=("Algerian",25), bg="white")
password_label.place(relx=0.5, rely=0.3, anchor="center")

password_entry = tk.Entry(login_window, show="*", font=label_font)
password_entry.place(relx=0.5, rely=0.38, anchor="center")

login_button = tk.Button(login_window, text="Login in app", command=perform_login, font=("Algerian",25))
login_button.place(relx=0.5, rely=0.49, anchor="center")
def exit_application():
    my_w.destroy()  # Close the main application window
    login_window.destroy()



exit_button = tk.Button(login_window, text="Leave this page", command=exit_application, font=("Algerian", 15), width=30, height=1)
exit_button.pack(side='bottom', pady=(250, 0), anchor='center')


def open_main_window():
     login_window.withdraw()
     my_w.deiconify()
     my_w.attributes('-fullscreen', True)

my_w = tk.Tk()
my_w.geometry("1580x800+0+0") 
my_w.withdraw()

my_w.columnconfigure(0,weight=8)
my_w.columnconfigure(1,weight=2)
my_w.rowconfigure(0, weight=1) 
my_w.rowconfigure(1, weight=14) 
my_w.rowconfigure(2, weight=2)

frame_top=tk.Frame(my_w,bg='black')
frame_bottom=tk.Frame(my_w,bg='black')
text_label = tk.Label(frame_top, text="THE YUM XPRESS",font=("Algerian", 90))
text_label.pack(padx=0, pady=100)
#f8fab4
frame_m_right=tk.Frame(my_w,bg='yellow')
frame_m_left=tk.Frame(my_w,bg='blue')


#placing in grid
frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
frame_m_left.grid(row=1,column=0,sticky='WENS')
frame_m_right.grid(row=1,column=1,sticky='WENS')
frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
trv = ttk.Treeview(frame_m_right, selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

# column identifiers 
trv["columns"] = ("1", "2","3")
trv.column("#0", width = 80, anchor ='w')
trv.column("1", width = 60, anchor ='w')
trv.column("2", width =50 , anchor ='c')
trv.column("3", width = 50, anchor ='c')
  
# Headings  
# respective columns
trv.heading("#0", text ="Item",anchor='w')
trv.heading("1", text ="Price",anchor='w')
trv.heading("2", text ="qty",anchor='c')
trv.heading("3", text ="Total",anchor='c')
def my_reset():
    global total, tax
    for item in trv.get_children():
        trv.delete(item)
    l1=[]
    for i in range(8):
        l1.append(tk.IntVar(value=0))
    for i in range(len(sb)):
        sb[i].config(textvariable=l1[i])

    for w in frame_m_right.grid_slaves(1):
        w.grid_remove()
    for w in frame_m_right.grid_slaves(2):
        w.grid_remove()    
    for w in frame_m_right.grid_slaves(3):
        w.grid_remove()
    dt=date.today().strftime('%Y-%m-%d') # todays date
    query="INSERT INTO  plus2_bill (total,tax,`bill_date`) \
                  VALUES (%s,%s,%s)"
    data=[total,tax,dt]
    id=my_conn.execute(query,data)
    #print(total, tax)
    bill_no=id.lastrowid
    for i in dl:
        i.insert(3,bill_no)
        i.insert(4,dt)
    query="INSERT INTO plus2_sell(p_id,price,quantity,bill_no,bill_date)\
                  VALUES(%s,%s,%s,%s,%s)"
    id=my_conn.execute(query,dl)
      
    lr1=tk.Button(frame_m_right,text='Bill',font=font1,command=lambda:my_invoice(my_w,bill_no))
    lr1.grid(row=1,column=0,sticky='nw')                
dl=[]    
total,tax,final=0,0,0
def my_bill():
    global dl,total,tax,final 
    total,tax,final=0,0,0
    dl.clear()
    for item in trv.get_children():
        trv.delete(item)
    
    for i in range(len(sb)):
        if(int(sb[i].get())>0): 
            price=int(sb[i].get())*my_menu[i][2]
            total=round(total+price,2)
            my_str1=(str(my_menu[i][2]), str(sb[i].get()), str(price))
            trv.insert("",'end',iid=i,text=my_menu[i][1],values=my_str1)
            dl.append([my_menu[i][0],my_menu[i][2],int(sb[i].get())])
    lr1=tk.Label(frame_m_right,text='Total',font=font1)
    lr1.grid(row=1,column=0,sticky='nw')
    lr2=tk.Label(frame_m_right,text=str(total),font=font1)
    lr2.grid(row=1,column=1,sticky='nw')
    lr21=tk.Label(frame_m_right,text='Tax 10%',font=font1)
    lr21.grid(row=2,column=0,sticky='nw')
    tax=round(0.1*total,2)
    lr22=tk.Label(frame_m_right,text=str(tax),font=font1)
    lr22.grid(row=2,column=1,sticky='nw')
    lr31=tk.Label(frame_m_right,text='Total',font=font2)
    lr31.grid(row=3,column=0,sticky='nw')
    final=round(total+tax,2)
    lr32=tk.Label(frame_m_right,text=str(final),font=font2)
    lr32.grid(row=3,column=1,sticky='nw')
    
        
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
font1=('Times',19,'normal')
font2=('Times',30,'bold')
pdx,pdy=3,7

my_menu={} # Dictionary to store items with price
sb=[]
r,c,i=0,0,0
def show_items(cat):
    global r, c, i, my_menu, sb
    
    # Clear existing labels from frame_m_left
    for widget in frame_m_left.winfo_children():
        widget.destroy()

    my_menu.clear()
    sb.clear()
    r, c, i = 0, 0, 0
    r_set = my_conn.execute("SELECT * FROM plus2_products WHERE available=1 and p_cat=" + str(cat))

    for item in r_set:
        menu = tk.Label(frame_m_left, text=item[1] + '(' + str(item[3]) + ')', font=font1, bg='white')
        menu.grid(row=r, column=c, padx=10, pady=10)
        r1 = r + 1
        sbox = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font2, width=1, bg='white')
        sbox.grid(row=r1, column=c, padx=pdx, pady=0)
        sb.append(sbox)
        my_menu[i] = [item[0], item[1], item[3]]
        i += 1
        if c > 2:
            c = 0
            r += 2
        else:
            c += 1

show_items(1)
r=r+1
r1_v = tk.IntVar(value=1) # We used integer variable here 

r1 = tk.Radiobutton(frame_bottom, text='Breakfast', variable=r1_v, value=1,command=lambda:show_items(1))
r1.grid(row=r,column=0) 

r2 = tk.Radiobutton(frame_bottom, text='Lunch', variable=r1_v, value=0,command=lambda:show_items(2))
r2.grid(row=r,column=1) 

r3 = tk.Radiobutton(frame_bottom, text='Dinner', variable=r1_v, value=5,command=lambda:show_items(3))
r3.grid(row=r,column=2)

b1=tk.Button(frame_bottom,text='Get Bill',command=my_bill)
b1.grid(row=r,column=3,padx=10)
b2=tk.Button(frame_bottom,text='Confirm ( Reset)',command=my_reset)
b2.grid(row=r,column=4,padx=10)
# Create a frame to hold the "Exit" button

my_w.deiconify()
# Add this function to exit the application
def exit_application():
    my_w.destroy()
    login_window.destroy()  # Close the main application window
    app_name_window.destroy()  # Close the app name window

# Create an "Exit" button in your main application window
exit_button = tk.Button(my_w, text="Exit", command=exit_application, font=("Algerian", 10), width=20, height=1)
exit_button.grid(row=2, column=1, sticky='ne')
my_w.withdraw()  # Hide the main application window initially


# Start the tkinter main loop for the app name window
app_name_window.mainloop()


   


