import tkinter as tk
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqlconnector://root:minSEU32Hoshi@localhost/komal1db")

def my_invoice(my_w,bill_no):
    import tkinter as tk
    #global path_image,img_top2
    my_w_child=tk.Toplevel(my_w,background='#FFFFFF')
    my_w_child.geometry("800x600")
    my_w_child.title('www.plus2net.com')
    font1=('Times',32,'bold')
    font2=('Times',20,'normal')
    font3=('Times',16,'normal')
    
    my_line='--'
    for i in range(13):
        my_line=my_line+'------'
    query='SELECT * FROM plus2_bill WHERE bill_no=%s'
    my_cursor=my_conn.execute(query,bill_no)
    my_result = my_cursor.fetchone()
    dt=my_result[1].strftime('%d-%B-%Y')
    #print(my_result)
    query='SELECT b.p_name,a.p_id,a.price,a.quantity  FROM plus2_sell a, plus2_products b WHERE a.p_id=b.p_id and a.bill_no=%s '
    my_cursor2=my_conn.execute(query,bill_no)
    my_result2 = my_cursor2.fetchall()
    
    #img_top2 = tk.PhotoImage(file = path_image+"restaurant-4.png")
    #img_top2 = ImageTk.PhotoImage(Image.open("G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\restaurant-4.jpg"))
    
    #img_l_c = tk.Label(my_w_child,  image=img_top2)
    #img_l_c.grid(row=0,column=0)
    #img_l_c.draw()
    l1=tk.Label(my_w_child,text='Invoice',font=font1,fg='blue',bg='#ffffff')
    l1.grid(row=0,column=1)
    l2=tk.Label(my_w_child,text='Bill No :#'+str(bill_no),font=font2,bg='#ffffff')
    l2.grid(row=0,column=2,padx=10)
    l3=tk.Label(my_w_child,text='Date:'+dt,font=font2,bg='#ffffff')
    l3.grid(row=0,column=3,padx=10)
    l3=tk.Label(my_w_child,text=my_line,font=font2,bg='#ffffff')
    l3.grid(row=1,column=0,padx=10,columnspan=4,sticky='w')
    r=2
    #print(my_result2)
    total=0
    for i in my_result2:
        l_item=tk.Label(my_w_child,text=i[0],bg='#ffffff',font=font3)
        l_item.grid(row=r,column=0)
        l_item1=tk.Label(my_w_child,text=i[2],font=font3)
        l_item1.grid(row=r,column=1)
        l_item1=tk.Label(my_w_child,text=i[3],bg='#ffffff',font=font3,fg='blue')
        l_item1.grid(row=r,column=2)
        price=round(i[2]*i[3],2)
        l_item1=tk.Label(my_w_child,text=str(price),bg='#ffffff',font=font2)
        l_item1.grid(row=r,column=3,sticky='ne')
        total=round(total+price,2)
        r=r+1
    l4=tk.Label(my_w_child,text=my_line,font=font2,bg='#ffffff')
    l4.grid(row=r,column=0,padx=10,columnspan=4,sticky='w')
    r=r+1
    lr1=tk.Label(my_w_child,text='Total',font=font2)
    lr1.grid(row=r,column=0,sticky='ne')
    lr2=tk.Label(my_w_child,text=str(total),font=font2)
    lr2.grid(row=r,column=1,sticky='ne',columnspan=3)
    r=r+1
    lr21=tk.Label(my_w_child,text='Tax 10%',font=font2)
    lr21.grid(row=r,column=0,sticky='ne')
    tax=round(0.1*total,2)
    lr22=tk.Label(my_w_child,text=str(tax),font=font2)
    lr22.grid(row=r,column=1,sticky='ne',columnspan=3)
    r=r+1
    lr31=tk.Label(my_w_child,text='Total',font=font1,bg='#ffffff')
    lr31.grid(row=r,column=0,sticky='ne')
    final=round(total+tax,2)
    lr32=tk.Label(my_w_child,text=str(final),font=font1,bg='#ffffff',fg='red')
    lr32.grid(row=r,column=1,sticky='ne',columnspan=3)
    order_placed_text = tk.Label(my_w_child, text="Your order has been placed", font=font2, bg='#ffffff', fg='green')
    order_placed_text.pack()