from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class super:
    def __init__(self,window):
        self.backgroundcolor="#253C43"
        self.fontcolor="#fff"
        self.color_button="#D6E4B1"
        self.window=window
        self.window.iconbitmap('D:\\icone.ico')
        window.geometry("1360x700")
        window.resizable(False,False)
        window.title("restaurant")
    def close():
       window.destroy()      
    def header(self):
        self.header_frame=Button(window,text="online restaurant",width=520,bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",15,"bold"),borderwidth=10,state=DISABLED).pack()
    def data_customer(self,name,phone):
        self.f1=Frame(window,width=350,height=200,bg=self.backgroundcolor).place(x=1016,y=60)
        self.text=Label(window,text="بيانات المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",15,"bold")).place(x=1240,y=70)
        #store value_input
        self.name_store=StringVar()
        self.phone_store=StringVar()
        self.nameuser=Label(window,text="اسم المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=1220,y=120)
        self.name_input=Entry(window,width=20,textvariable=self.name_store).place(x=1080,y=125)
        self.phoneuser=Label(window,text="رقم المشتري",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=1220,y=160)
        self.phone_input=Entry(window,width=20,textvariable=self.phone_store).place(x=1080,y=165)
    def choice(self):
        self.s = ttk.Style()
        self.s.theme_use('default')
        self.s.configure('TNotebook.Tab', background="#aaa")
        self.nb = ttk.Notebook(window)
        self.f11= ttk.Frame(self.nb, width= 1010, height=518)
        self.nb.add(self.f11, text='\t\t\t Sandwitches\t\t\t')
        self.f22 = ttk.Frame(self.nb)
        self.nb.add(self.f22, text= "\t\t\tMain dishes\t\t\t")
        self.f23 = ttk.Frame(self.nb)
        self.nb.add(self.f23, text= "\t\t\tHot drinks\t\t\t\t")
        self.nb.place(x=0,y=60)
   



    def drink(self):
        self.frame_drink=Frame(self.f11,height=500,width=1000).place(x=0,y=0)
        self.value_input1=IntVar()  
        self.value_input2=IntVar()
        self.value_input3=IntVar()
        self.value_input4=IntVar()
        self.value_input5=IntVar()
        self.value_input6=IntVar()
        self.value_input7=IntVar()
        self.value_input8=IntVar()
        self.value_input9=IntVar()
        self.value_input10=IntVar()
        self.value_input11=IntVar()
        self.value_input12=IntVar()
        self.value_input13=IntVar()
        self.value_input14=IntVar()
        self.value_input15=IntVar()
        self.value_input16=IntVar()
        self.value_input17=IntVar()
        self.value_input18=IntVar()
        self.value_input19=IntVar()
        self.value_input20=IntVar()
        self.value_input21=IntVar()
        self.value_input22=IntVar()
        self.value_input23=IntVar()
        self.value_input24=IntVar()
        self.value_input25=IntVar()
        self.value_input26=IntVar()
        self.value_input27=IntVar()
        self.value_input28=IntVar()
        self.dicti1={
       "Beefburger cheese       ":250,
       "chicken burger          ":250,
       "beefburger special      ":300,
       "chawarma pain           ":100,
       "chawarma raghif         ":100,
       "chawarma special        ":100,
       "chawarma garnie         ":200,
       "souffle poulet          ":100,
       "souffle viande          ":170,
       "souffle mixte           ":150,
       "souffle merguaz         ":170,
       "souffle garnie         ":130,
       "malfouf special        ":200,
       "malfouf poulet         ":120,
       }
        self.dicti2={
       "crepe kebda      ":100,
       "crepe viande      ":150,
       "crepe chicken     ":130,
       "corn mayo         ":60,
       "corn cheese       ":40,
       "corn lays mayo    ":70,
       "corn lays cheese   ":60,
       "corn mayo tomato   ":60,
       "veg mayo Grilled   ":70,
       "veg club cheese    ":50,
       "veg Grilled sndwitch":70,
       "veg sandwitch       ":40,
       "Bhujia sandwitch Grill":60,
       "Bhujia sandwitch cheese":60,
       }
        self.hot_drink_text=Label(self.f11,text="Sandwitches",font=("arail",15,"bold")).place(x=20,y=10)
        self.x=50
        self.y=50
        self.background="#fff"
      #row1
        for key,value in self.dicti1.items():
          text=Label(self.f11,text=key).place(x=self.x,y=self.y)
          text=Label(self.f11,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)
      #row2
        self.x2=480
        self.y2=50
        for key,value in self.dicti2.items():
          text=Label(self.f11,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f11,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
        def clear_entry(event, entry):
          entry.delete(0, END)
          entry.unbind('<Button-1>', click_event)
        self.textinput1 = Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input1,justify='center')
        self.textinput1.pack()
        self.textinput1.place(x=290,y=50)
        self.textinput1.bind("<Button-1>", lambda event: clear_entry(event, self.textinput1))
        self.textinput2=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input2,justify='center')
        self.textinput2.pack()
        self.textinput2.place(x=290,y=80)
        self.textinput2.bind("<Button-1>", lambda event: clear_entry(event, self.textinput2))
        self.textinput3=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input3,justify='center')
        self.textinput3.pack()
        self.textinput3.place(x=290,y=110)
        self.textinput3.bind("<Button-1>", lambda event: clear_entry(event, self.textinput3))
        self.textinput4=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input4,justify='center')
        self.textinput4.pack()
        self.textinput4.place(x=290,y=140)
        self.textinput4.bind("<Button-1>", lambda event: clear_entry(event, self.textinput4))
        self.textinput5=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input5,justify='center')
        self.textinput5.pack()
        self.textinput5.place(x=290,y=170)
        
        self.textinput5.bind("<Button-1>", lambda event: clear_entry(event, self.textinput5))
        self.textinput6=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input6,justify='center')
        self.textinput6.pack()
        self.textinput6.place(x=290,y=200)
        
        self.textinput6.bind("<Button-1>", lambda event: clear_entry(event, self.textinput6))
        self.textinput7=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input7,justify='center')
        self.textinput7.pack()
        self.textinput7.place(x=290,y=230)
        
        self.textinput7.bind("<Button-1>", lambda event: clear_entry(event, self.textinput7))
        self.textinput8=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input8,justify='center')
        self.textinput8.pack()
        self.textinput8.place(x=290,y=260)
        
        self.textinput8.bind("<Button-1>", lambda event: clear_entry(event, self.textinput8))
        self.textinput9=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input9,justify='center')
        self.textinput9.pack()
        self.textinput9.place(x=290,y=290)
        
        self.textinput9.bind("<Button-1>", lambda event: clear_entry(event, self.textinput9))
        self.textinput10=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input10,justify='center')
        self.textinput10.pack()
        self.textinput10.place(x=290,y=320)
        
        self.textinput10.bind("<Button-1>", lambda event: clear_entry(event, self.textinput10))
        self.textinput11=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input11,justify='center')
        self.textinput11.pack()
        self.textinput11.place(x=290,y=350)
        
        self.textinput11.bind("<Button-1>", lambda event: clear_entry(event, self.textinput11))
        self.textinput12=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input12,justify='center')
        self.textinput12.pack()
        self.textinput12.place(x=290,y=380)
        
        self.textinput12.bind("<Button-1>", lambda event: clear_entry(event, self.textinput12))
        self.textinput13=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input13,justify='center')
        self.textinput13.pack()
        self.textinput13.place(x=290,y=410)
       
        self.textinput13.bind("<Button-1>", lambda event: clear_entry(event, self.textinput13))
        self.textinput14=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input14,justify='center')
        self.textinput14.pack()
        self.textinput14.place(x=290,y=440)
        
        self.textinput14.bind("<Button-1>", lambda event: clear_entry(event, self.textinput14))
        self.textinput15=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input15,justify='center')
        self.textinput15.pack()
        self.textinput15.place(x=720,y=50)
        
        self.textinput15.bind("<Button-1>", lambda event: clear_entry(event, self.textinput15))
        self.textinput16=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input16,justify='center')
        self.textinput16.pack()
        self.textinput16.place(x=720,y=80)
       
        self.textinput16.bind("<Button-1>", lambda event: clear_entry(event, self.textinput16))
        self.textinput17=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input17,justify='center')
        self.textinput17.pack()
        self.textinput17.place(x=720,y=110)
        
        self.textinput17.bind("<Button-1>", lambda event: clear_entry(event, self.textinput17))
        self.textinput18=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input18,justify='center')
        self.textinput18.pack()
        self.textinput18.place(x=720,y=140)
        
        self.textinput18.bind("<Button-1>", lambda event: clear_entry(event, self.textinput18))
        self.textinput19=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input19,justify='center')
        self.textinput19.pack()
        self.textinput19.place(x=720,y=170)
        
        self.textinput19.bind("<Button-1>", lambda event: clear_entry(event, self.textinput19))
        self.textinput20=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input20,justify='center')
        self.textinput20.pack()
        self.textinput20.place(x=720,y=200)
       
        self.textinput20.bind("<Button-1>", lambda event: clear_entry(event, self.textinput20))
        self.textinput21=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input21,justify='center')
        self.textinput21.pack()
        self.textinput21.place(x=720,y=230)
       
        self.textinput21.bind("<Button-1>", lambda event: clear_entry(event, self.textinput21))
        self.textinput22=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input22,justify='center')
        self.textinput22.pack()
        self.textinput22.place(x=720,y=260)
        
        self.textinput22.bind("<Button-1>", lambda event: clear_entry(event, self.textinput22))
        self.textinput23=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input23,justify='center')
        self.textinput23.pack()
        self.textinput23.place(x=720,y=290)
        
        self.textinput23.bind("<Button-1>", lambda event: clear_entry(event, self.textinput23))
        self.textinput24=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input24,justify='center')
        self.textinput24.pack()
        self.textinput24.place(x=720,y=320)
        
        self.textinput24.bind("<Button-1>", lambda event: clear_entry(event, self.textinput24))
        self.textinput25=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input25,justify='center')
        self.textinput25.pack()
        self.textinput25.place(x=720,y=350)
        
        self.textinput25.bind("<Button-1>", lambda event: clear_entry(event, self.textinput25))
        self.textinput26=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input26,justify='center')
        self.textinput26.pack()
        self.textinput26.place(x=720,y=380)
        
        self.textinput26.bind("<Button-1>", lambda event: clear_entry(event, self.textinput26))
        self.textinput27=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input27,justify='center')
        self.textinput27.pack()
        self.textinput27.place(x=720,y=410)
        
        self.textinput27.bind("<Button-1>", lambda event: clear_entry(event, self.textinput27))
        self.textinput28=Entry(self.f11,width=20,bg=self.fontcolor,textvariable=self.value_input28,justify='center')
        self.textinput28.pack()
        self.textinput28.place(x=720,y=440)
       
        self.textinput28.bind("<Button-1>", lambda event: clear_entry(event, self.textinput28))  
        
 
    def calculate_drink(self):
        self.price1=self.value_input1.get()*250
        self.price2=self.value_input2.get()*250
        self.price3=self.value_input3.get()*300
        self.price4=self.value_input4.get()*100
        self.price5=self.value_input5.get()*100
        self.price6=self.value_input6.get()*100
        self.price7=self.value_input7.get()*200
        self.price8=self.value_input8.get()*100
        self.price9=self.value_input9.get()*170
        self.price10=self.value_input10.get()*150
        self.price11=self.value_input11.get()*170
        self.price12=self.value_input12.get()*130
        self.price13=self.value_input13.get()*200
        self.price14=self.value_input14.get()*120
        self.price15=self.value_input15.get()*100
        self.price16=self.value_input16.get()*150
        self.price17=self.value_input17.get()*130
        self.price18=self.value_input18.get()*60
        self.price19=self.value_input19.get()*40
        self.price20=self.value_input20.get()*40
        self.price21=self.value_input21.get()*60
        self.price22=self.value_input22.get()*60
        self.price23=self.value_input23.get()*70
        self.price24=self.value_input24.get()*50
        self.price25=self.value_input25.get()*70
        self.price26=self.value_input26.get()*40
        self.price27=self.value_input27.get()*60
        self.price28=self.value_input28.get()*60
        self.total=float(
                        self.price1+self.price2+self.price3+self.price4+self.price5+self.price6+self.price7+self.price8+self.price9+self.price10+self.price11+self.price12+self.price13+self.price14+self.price15+self.price16+self.price17+self.price18+self.price19+self.price20+self.price21+self.price22+self.price23+self.price24+self.price25+self.price26+self.price27+self.price28)
        self.sandwitch.set(str(self.total)+" $")
        #price main dishes
        self.price1a=self.value_input1a.get()*350
        self.price2a=self.value_input2a.get()*450
        self.price3a=self.value_input3a.get()*300
        self.price4a=self.value_input4a.get()*250
        self.price5a=self.value_input5a.get()*150
        self.price6a=self.value_input6a.get()*100
        self.price7a=self.value_input7a.get()*100
        self.price8a=self.value_input8a.get()*100
        self.price9a=self.value_input9a.get()*120
        self.price10a=self.value_input10a.get()*150
        self.price11a=self.value_input11a.get()*170
        self.price12a=self.value_input12a.get()*250
        self.price13a=self.value_input13a.get()*190
        self.price14a=self.value_input14a.get()*170
        self.price15a=self.value_input15a.get()*250
        self.price16a=self.value_input16a.get()*350
        self.price17a=self.value_input17a.get()*310
        self.price18a=self.value_input18a.get()*200
        self.price19a=self.value_input19a.get()*130
        self.price20a=self.value_input20a.get()*150
        self.price21a=self.value_input21a.get()*350
        self.price22a=self.value_input22a.get()*120
        self.price23a=self.value_input23a.get()*180
        self.price24a=self.value_input24a.get()*250
        self.price25a=self.value_input25a.get()*270
        self.price26a=self.value_input26a.get()*160
        self.price27a=self.value_input27a.get()*190
        self.price28a=self.value_input28a.get()*130
        self.total2=float(
                        self.price1a+self.price2a+self.price3a+self.price4a+self.price5a+self.price6a+self.price7a+self.price8a+self.price9a+self.price10a+self.price11a+self.price12a+self.price13a+self.price14a+self.price15a+self.price16a+self.price17a+self.price18a+self.price19a+self.price20a+self.price21a+self.price22a+self.price23a+self.price24a+self.price25a+self.price26a+self.price27a+self.price28a)
        self.dishes.set(str(self.total2)+" $")
        #hot drinks
        self.price1aa=self.value_input1aa.get()*15
        self.price2aa=self.value_input2aa.get()*25
        self.price3aa=self.value_input3aa.get()*30
        self.price4aa=self.value_input4aa.get()*25
        self.price5aa=self.value_input5aa.get()*10
        self.price6aa=self.value_input6aa.get()*10
        self.price7aa=self.value_input7aa.get()*10
        self.price8aa=self.value_input8aa.get()*15
        self.price9aa=self.value_input9aa.get()*17
        self.price10aa=self.value_input10aa.get()*30
        self.price11aa=self.value_input11aa.get()*10
        self.price12aa=self.value_input12aa.get()*12
        self.price13aa=self.value_input13aa.get()*20
        self.price14aa=self.value_input14aa.get()*40
        self.price15aa=self.value_input15aa.get()*20
        self.price16aa=self.value_input16aa.get()*25
        self.price17aa=self.value_input17aa.get()*32
        self.price18aa=self.value_input18aa.get()*35
        self.price19aa=self.value_input19aa.get()*27
        self.price20aa=self.value_input20aa.get()*37
        self.price21aa=self.value_input21aa.get()*40
        self.price22aa=self.value_input22aa.get()*30
        self.price23aa=self.value_input23aa.get()*28
        self.price24aa=self.value_input24aa.get()*34
        self.price25aa=self.value_input25aa.get()*17
        self.price26aa=self.value_input26aa.get()*14
        self.price27aa=self.value_input27aa.get()*20
        self.price28aa=self.value_input28aa.get()*36
        self.total3=float(
                        self.price1aa+self.price2aa+self.price3aa+self.price4aa+self.price5aa+self.price6aa+self.price7aa+self.price8aa+self.price9aa+self.price10aa+self.price11aa+self.price12aa+self.price13aa+self.price14aa+self.price15aa+self.price16aa+self.price17aa+self.price18aa+self.price19aa+self.price20aa+self.price21aa+self.price22aa+self.price23aa+self.price24aa+self.price25aa+self.price26aa+self.price27aa+self.price28aa)
        self.hotdrink.set(str(self.total3)+" $") 
        self.totall = self.total +self.total2 + self.total3
    def drink2(self):
      self.frame_drink2=Frame(self.f22,height=500,width=1000).place(x=0,y=0)
      
      self.value_input1a=IntVar()
      self.value_input2a=IntVar()
      self.value_input3a=IntVar()
      self.value_input4a=IntVar()
      self.value_input5a=IntVar()
      self.value_input6a=IntVar()
      self.value_input7a=IntVar()
      self.value_input8a=IntVar()
      self.value_input9a=IntVar()
      self.value_input10a=IntVar()
      self.value_input11a=IntVar()
      self.value_input12a=IntVar()
      self.value_input13a=IntVar()
      self.value_input14a=IntVar()
      self.value_input15a=IntVar()
      self.value_input16a=IntVar()
      self.value_input17a=IntVar()
      self.value_input18a=IntVar()
      self.value_input19a=IntVar()
      self.value_input20a=IntVar()
      self.value_input21a=IntVar()
      self.value_input22a=IntVar()
      self.value_input23a=IntVar()
      self.value_input24a=IntVar()
      self.value_input25a=IntVar()
      self.value_input26a=IntVar()
      self.value_input27a=IntVar()
      self.value_input28a=IntVar()      
      self.dicti={
       "chawarma              ":350,
       "corden bleu            ":450,
       "scalpoe creme          ":300,
       "balles grille          ":250,
       "poulet marine          ":150,
       "fried wings            ":100,
       "lemon paper wings      ":100,
       "jerk wings             ":100,
       "creole wings           ":120,
       "fish filet             ":150,
       "Griot                 ":170,
       "Grilled chicken       ":250,
       "creole shrimp         ":190,
       "fried shrimp          ":170,
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f22,text="Main dishes",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f22,text=key).place(x=self.x,y=self.y)
          text=Label(self.f22,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)
      def clear_entry(event, entry):
          entry.delete(0, END)
          entry.unbind('<Button-1>', click_event)
      self.textinput1a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input1a,justify='center')
      self.textinput1a.pack()
      self.textinput1a.place(x=290,y=50)
      
      self.textinput1a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput1a))
      self.textinput2a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input2a,justify='center')
      self.textinput2a.pack()
      self.textinput2a.place(x=290,y=80)
      
      self.textinput2a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput2a))
      self.textinput3a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input3a,justify='center')
      self.textinput3a.pack()
      self.textinput3a.place(x=290,y=110)
     
      self.textinput3a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput3a))
      self.textinput4a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input4a,justify='center')
      self.textinput4a.pack()
      self.textinput4a.place(x=290,y=140)
      
      self.textinput4a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput4a))
      self.textinput5a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input5a,justify='center')
      self.textinput5a.pack()
      self.textinput5a.place(x=290,y=170)
      
      self.textinput5a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput5a))
      self.textinput6a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input6a,justify='center')
      self.textinput6a.pack()
      self.textinput6a.place(x=290,y=200)
      
      self.textinput6a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput6a))
      self.textinput7a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input7a,justify='center')
      self.textinput7a.pack()
      self.textinput7a.place(x=290,y=230)
     
      self.textinput7a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput7a))
      self.textinput8a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input8a,justify='center')
      self.textinput8a.pack()
      self.textinput8a.place(x=290,y=260)
     
      self.textinput8a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput8a))
      self.textinput9a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input9a,justify='center')
      self.textinput9a.pack()
      self.textinput9a.place(x=290,y=290)
     
      self.textinput9a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput9a))
      self.textinput10a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input10a,justify='center')
      self.textinput10a.pack()
      self.textinput10a.place(x=290,y=320)
      
      self.textinput10a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput10a))
      self.textinput11a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input11a,justify='center')
      self.textinput11a.pack()
      self.textinput11a.place(x=290,y=350)
      
      self.textinput11a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput11a))
      self.textinput12a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input12a,justify='center')
      self.textinput12a.pack()
      self.textinput12a.place(x=290,y=380)
      
      self.textinput12a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput12a))
      self.textinput13a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input13a,justify='center')
      self.textinput13a.pack()
      self.textinput13a.place(x=290,y=410)
      
      self.textinput13a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput13a))
      self.textinput14a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input14a,justify='center')
      self.textinput14a.pack()
      self.textinput14a.place(x=290,y=440)
      
      self.textinput14a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput14a))
      
      #row2
      self.dicti2={
       "steamed shrip           ":250,
       "oxtail                  ":350,
       "fried conch             ":310,
       "Grill conch             ":200,
       "slew conch             " :130,
       "fried fish              ":150,
       "lobster tail            ":140,
       "crabe creole (seasonal) ":120,
       "stew chicken           ":180,
       "Grilled chicken         ":250,
       "stew fish               ":270,
       "lobster tail            ":350,
       "fried pork              ":160,
       "steamed conch           ":190,
       "colombo                 ":130
       }
      self.x2=480
      self.y2=50
      for key,value in self.dicti2.items():
          text=Label(self.f22,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f22,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
      self.textinput15a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input15a,justify='center')
      self.textinput15a.pack()
      self.textinput15a.place(x=720,y=50)
     
      self.textinput15a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput15a))
      self.textinput16a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input16a,justify='center')
      self.textinput16a.pack()
      self.textinput16a.place(x=720,y=80)
      
      self.textinput16a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput16a))
      self.textinput17a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input17a,justify='center') 
      self.textinput17a.pack()
      self.textinput17a.place(x=720,y=110)
     
      self.textinput17a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput17a))
      self.textinput18a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input18a,justify='center') 
      self.textinput18a.pack()
      self.textinput18a.place(x=720,y=140)
     
      self.textinput18a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput18a))
      self.textinput19a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input19a,justify='center') 
      self.textinput19a.pack()
      self.textinput19a.place(x=720,y=170)
     
      self.textinput19a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput19a))
      self.textinput20a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input20a,justify='center') 
      self.textinput20a.pack()
      self.textinput20a.place(x=720,y=200)
      
      self.textinput20a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput20a))
      self.textinput21a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input21a,justify='center')  
      self.textinput21a.pack()
      self.textinput21a.place(x=720,y=230)
      
      self.textinput21a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput21a))
      self.textinput22a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input22a,justify='center')
      self.textinput22a.pack()
      self.textinput22a.place(x=720,y=260)
      
      self.textinput22a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput22a))
      self.textinput23a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input23a,justify='center') 
      self.textinput23a.pack()
      self.textinput23a.place(x=720,y=290)
     
      self.textinput23a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput23a))
      self.textinput24a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input24a,justify='center') 
      self.textinput24a.pack()
      self.textinput24a.place(x=720,y=320)
     
      self.textinput24a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput24a))
      self.textinput25a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input25a,justify='center') 
      self.textinput25a.pack()
      self.textinput25a.place(x=720,y=350)
      
      self.textinput25a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput25a))
      self.textinput26a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input26a,justify='center') 
      self.textinput26a.pack()
      self.textinput26a.place(x=720,y=380)
      
      self.textinput26a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput26a))
      self.textinput27a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input27a,justify='center')
      self.textinput27a.pack()
      self.textinput27a.place(x=720,y=410)
      
      self.textinput27a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput27a))
      self.textinput28a=Entry(self.f22,width=20,bg=self.background,textvariable=self.value_input28a,justify='center') 
      self.textinput28a.pack()
      self.textinput28a.place(x=720,y=440)
      
      self.textinput28a.bind("<Button-1>", lambda event: clear_entry(event, self.textinput28a))
      
    

    def drink3(self):
      self.frame_drink3=Frame(self.f23,height=500,width=1000).place(x=0,y=0)
      self.value_input1aa=IntVar()
      self.value_input2aa=IntVar()
      self.value_input3aa=IntVar()
      self.value_input4aa=IntVar()
      self.value_input5aa=IntVar()
      self.value_input6aa=IntVar()
      self.value_input7aa=IntVar()
      self.value_input8aa=IntVar()
      self.value_input9aa=IntVar()
      self.value_input10aa=IntVar()
      self.value_input11aa=IntVar()
      self.value_input12aa=IntVar()
      self.value_input13aa=IntVar()
      self.value_input14aa=IntVar()
      self.value_input15aa=IntVar()
      self.value_input16aa=IntVar()
      self.value_input17aa=IntVar()
      self.value_input18aa=IntVar()
      self.value_input19aa=IntVar()
      self.value_input20aa=IntVar()
      self.value_input21aa=IntVar()
      self.value_input22aa=IntVar()
      self.value_input23aa=IntVar()
      self.value_input24aa=IntVar()
      self.value_input25aa=IntVar()
      self.value_input26aa=IntVar()
      self.value_input27aa=IntVar()
      self.value_input28aa=IntVar()      
      self.dicti={
       "Hot oats                 ":15,
       "Hot lotus                ":25,
       "Hot chocolate marshmallow":30,
       "Hot chocolate            ":25,
       "lipton tea               ":10,
       "green tea                ":10,
       "Taylors tea              ":10,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "Ahmed tea                ":15,
       "Sahlab                   ":17,
       "sahlab special Al Dawood ":30,
       "herbs                    ":10,
       "Lemon with boney         ":12,
       "warm milk                ":20,
       "Espresso                 ":40 
       }
      self.x=50
      self.y=50
      self.background="#fff"

      self.hot_drink_text=Label(self.f23,text="Hot Drinks",font=("arail",15,"bold")).place(x=20,y=10)
      for key,value in self.dicti.items():
          text=Label(self.f23,text=key).place(x=self.x,y=self.y)
          text=Label(self.f23,text=value).place(x=self.x+(170),y=self.y)
          self.y=self.y+(30)

      def clear_entry(event, entry):
          entry.delete(0, END)
          entry.unbind('<Button-1>', click_event)
      self.textinput1aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input1aa,justify='center') 
      self.textinput1aa.pack()
      self.textinput1aa.place(x=290,y=50)
      
      self.textinput1aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput1aa))
      self.textinput2aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input2aa,justify='center')
      self.textinput2aa.pack()
      self.textinput2aa.place(x=290,y=80)
     
      self.textinput2aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput2aa))
      self.textinput3aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input3aa,justify='center')
      self.textinput3aa.pack()
      self.textinput3aa.place(x=290,y=110)
      
      self.textinput3aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput3aa))
      self.textinput4aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input4aa,justify='center')
      self.textinput4aa.pack()
      self.textinput4aa.place(x=290,y=140)
      
      self.textinput4aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput4aa))
      self.textinput5aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input5aa,justify='center')
      self.textinput5aa.pack()
      self.textinput5aa.place(x=290,y=170)
      
      self.textinput5aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput5aa))
      self.textinput6aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input6aa,justify='center')
      self.textinput6aa.pack()
      self.textinput6aa.place(x=290,y=200)
     
      self.textinput6aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput6aa))
      self.textinput7aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input7aa,justify='center')
      self.textinput7aa.pack()
      self.textinput7aa.place(x=290,y=230)
     
      self.textinput7aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput7aa))
      self.textinput8aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input8aa,justify='center')
      self.textinput8aa.pack()
      self.textinput8aa.place(x=290,y=260)
     
      self.textinput8aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput8aa))
      self.textinput9aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input9aa,justify='center')
      self.textinput9aa.pack()
      self.textinput9aa.place(x=290,y=290)
     
      self.textinput9aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput9aa))
      self.textinput10aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input10aa,justify='center')
      self.textinput10aa.pack()
      self.textinput10aa.place(x=290,y=320)
      
      self.textinput10aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput10aa))
      self.textinput11aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input11aa,justify='center')
      self.textinput11aa.pack()
      self.textinput11aa.place(x=290,y=350)
      
      self.textinput11aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput11aa))
      self.textinput12aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input12aa,justify='center')
      self.textinput12aa.pack()
      self.textinput12aa.place(x=290,y=380)
      
      self.textinput12aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput12aa))
      self.textinput13aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input13aa,justify='center')
      self.textinput13aa.pack()
      self.textinput13aa.place(x=290,y=410)
      
      self.textinput13aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput13aa))
      self.textinput14aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input14aa,justify='center')
      self.textinput14aa.pack()
      self.textinput14aa.place(x=290,y=440)
     
      self.textinput14aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput14aa))
      #row2
      self.dicit2={
       "Hot penicillin           ":20,
       "moneygun toddy           ":25,
       "Hot turmeric             ":32,
       "tahini Hot chocolate     ":35,
       "mexican Hot chocolate    ":27,
       "coffe                    ":37,
       "vintage coffe            ":40,
       "matcha latte             ":30,
       "hot toddy                ":28,
       "caramel latte            ":34,
       "hot cocoa                ":17,
       "warm hazelnut            ":14,
       "magic cocoa              ":20,
       "piccole latte            ":36 
          }
      self.x2=480
      self.y2=50
      for key,value in self.dicit2.items():
          text=Label(self.f23,text=key).place(x=self.x2,y=self.y2)
          text=Label(self.f23,text=value).place(x=self.x2+(170),y=self.y2)
          self.y2=self.y2+(30)
          
      self.textinput15aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input15aa,justify='center')
      self.textinput15aa.pack()
      self.textinput15aa.place(x=720,y=50)
      
      self.textinput15aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput15aa))
      self.textinput16aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input16aa,justify='center')
      self.textinput16aa.pack()
      self.textinput16aa.place(x=720,y=80)
     
      self.textinput16aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput16aa))
      self.textinput17aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input17aa,justify='center')
      self.textinput17aa.pack()
      self.textinput17aa.place(x=720,y=110)
     
      self.textinput17aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput17aa))
      self.textinput18aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input18aa,justify='center')
      self.textinput18aa.pack()
      self.textinput18aa.place(x=720,y=140)
     
      self.textinput18aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput18aa))
      self.textinput19aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input19aa,justify='center')
      self.textinput19aa.pack()
      self.textinput19aa.place(x=720,y=170)
      
      self.textinput19aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput19aa))
      self.textinput20aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input20aa,justify='center')
      self.textinput20aa.pack()
      self.textinput20aa.place(x=720,y=200)
      
      self.textinput20aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput20aa))
      self.textinput21aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input21aa,justify='center')
      self.textinput21aa.pack()
      self.textinput21aa.place(x=720,y=230)
     
      self.textinput21aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput21aa))
      self.textinput22aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input22aa,justify='center')
      self.textinput22aa.pack()
      self.textinput22aa.place(x=720,y=260)
     
      self.textinput22aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput22aa))
      self.textinput23aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input23aa,justify='center')
      self.textinput23aa.pack()
      self.textinput23aa.place(x=720,y=290)
     
      self.textinput23aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput23aa))
      self.textinput24aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input24aa,justify='center')
      self.textinput24aa.pack()
      self.textinput24aa.place(x=720,y=320)
      
      self.textinput24aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput24aa))
      self.textinput25aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input25aa,justify='center')
      self.textinput25aa.pack()
      self.textinput25aa.place(x=720,y=350)
     
      self.textinput25aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput25aa))
      self.textinput26aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input26aa,justify='center')
      self.textinput26aa.pack()
      self.textinput26aa.place(x=720,y=380)
      
      self.textinput26aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput26aa))
      self.textinput27aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input27aa,justify='center')
      self.textinput27aa.pack()
      self.textinput27aa.place(x=720,y=410)
      
      self.textinput27aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput27aa))
      self.textinput28aa=Entry(self.f23,width=20,bg=self.background,textvariable=self.value_input28aa,justify='center')
      self.textinput28aa.pack()
      self.textinput28aa.place(x=720,y=440)
      
      self.textinput28aa.bind("<Button-1>", lambda event: clear_entry(event, self.textinput28aa))
    def alfatora(self):
       self.textfatora=Label(window,text="[الفواتير]",font=("arial",13,"bold"),fg="gold",bg=self.backgroundcolor).place(x=1157,y=200)
       self.F5 = Frame(self.window,bd=0,width=220,bg='white',height=200)
       self.F5.place(x=1016,y=220)
       scrol_y= Scrollbar(self.F5,orient=VERTICAL)
       self.txtarea=Text(self.F5,yscrollcommand=scrol_y.set)
       scrol_y.pack(side=LEFT,fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH,expand=1)
       self.txtarea.insert(END,"\tمطعم الهنا يرحب بكم")
       self.txtarea.insert(END,"\n  ====================================")
       self.txtarea.insert(END,f"\n\t Name   : {self.name_store.get()}")
       self.txtarea.insert(END,f"\n\t Phone  : {self.phone_store.get()}")
       self.txtarea.insert(END,"\n======================================")
       self.txtarea.insert(END,f"\nالسعر\t      العدد\t       المشتريات ")
       self.txtarea.insert(END,"\n======================================")
       
    def billing(self):
        if self.name_store.get()=="" or self.phone_store.get()=="":
            messagebox.showerror("حدث خطأ","لا يجوز ترك حقل الاسم ورقم الهاتف فارغا")
        elif self.hotdrink.get()=="0.0 $" and self.sandwitch.get()=="0.0 $" and self.dishes.get()=="0.0 $":
            messagebox.showerror("حدث خطأ"," ليس هناك منتجات محددة ولم يتم اختيار احداها يجب اختيار عدد المنتجات")
        else:
            self.alfatora()
            if self.value_input1.get()!=0:
                 self.txtarea.insert(END,f"\n {self.price1}\t\t{self.value_input1.get()}\tbeefburger cheese")
            if self.value_input2.get()!=0:
                self.txtarea.insert(END,f"\n {self.price2}\t\t{self.value_input2.get()}\tchicken burger")
            if self.value_input3.get()!=0:
                self.txtarea.insert(END,f"\n {self.price3}\t\t{self.value_input3.get()}\tbeefburger special")
            if self.value_input4.get()!=0:
                self.txtarea.insert(END,f"\n {self.price4}\t\t{self.value_input4.get()}\tchawarma pain ")
            if self.value_input5.get()!=0:
                self.txtarea.insert(END,f"\n {self.price5}\t\t{self.value_input5.get()}\tchawarma raghif")
            if self.value_input6.get()!=0:
                self.txtarea.insert(END,f"\n {self.price6}\t\t{self.value_input6.get()}\tchawarma special")
            if self.value_input7.get()!=0:
                self.txtarea.insert(END,f"\n {self.price7}\t\t{self.value_input7.get()}\tchawarma garnie ")
            if self.value_input8.get()!=0:
                self.txtarea.insert(END,f"\n {self.price8}\t\t{self.value_input8.get()}\tsouffle poulet")
            if self.value_input9.get()!=0:
                self.txtarea.insert(END,f"\n {self.price9}\t\t{self.value_input9.get()}\tsouffle viande")
            if self.value_input10.get()!=0:
                self.txtarea.insert(END,f"\n {self.price10}\t\t{self.value_input10.get()}\tsouffle mixte")
            if self.value_input11.get()!=0:
                self.txtarea.insert(END,f"\n {self.price11}\t\t{self.value_input11.get()}\tsouffle merguaz")
            if self.value_input12.get()!=0:
                self.txtarea.insert(END,f"\n {self.price12}\t\t{self.value_input12.get()}\tsouffle garnie")
            if self.value_input13.get()!=0:
                self.txtarea.insert(END,f"\n {self.price13}\t\t{self.value_input13.get()}\tmalfouf special")
            if self.value_input14.get()!=0:
                self.txtarea.insert(END,f"\n {self.price14}\t\t{self.value_input14.get()}\tmalfouf poulet")
            if self.value_input15.get()!=0:
                self.txtarea.insert(END,f"\n {self.price15}\t\t{self.value_input15.get()}\tcrepe kepda")
            if self.value_input16.get()!=0:
                self.txtarea.insert(END,f"\n {self.price16}\t\t{self.value_input16.get()}\tcerpe viande")
            if self.value_input17.get()!=0:
                self.txtarea.insert(END,f"\n {self.price17}\t\t{self.value_input17.get()}\tcrepe chicken")
            if self.value_input18.get()!=0:
                self.txtarea.insert(END,f"\n {self.price18}\t\t{self.value_input18.get()}\tcorn mayo")
            if self.value_input19.get()!=0:
                self.txtarea.insert(END,f"\n {self.price19}\t\t{self.value_input19.get()}\tcorn cheese")
            if self.value_input20.get()!=0:
                self.txtarea.insert(END,f"\n {self.price20}\t\t{self.value_input20.get()}\tcorn lays mayo")
            if self.value_input21.get()!=0:
                self.txtarea.insert(END,f"\n {self.price21}\t\t{self.value_input21.get()}\tcorn lays cheese")
            if self.value_input22.get()!=0:
                self.txtarea.insert(END,f"\n {self.price22}\t\t{self.value_input22.get()}\tcorn mayp tomato")
            if self.value_input23.get()!=0:
                self.txtarea.insert(END,f"\n {self.price23}\t\t{self.value_input23.get()}\tveg mayo crilled")
            if self.value_input24.get()!=0:
                self.txtarea.insert(END,f"\n {self.price24}\t\t{self.value_input24.get()}\tveg club cheese")
            if self.value_input25.get()!=0:
                self.txtarea.insert(END,f"\n {self.price25}\t\t{self.value_input25.get()}\tveg crilled sandwitch")
            if self.value_input26.get()!=0:
                self.txtarea.insert(END,f"\n {self.price26}\t\t{self.value_input26.get()}\tveg sandwitch")
            if self.value_input27.get()!=0:
                self.txtarea.insert(END,f"\n {self.price27}\t\t{self.value_input27.get()}\tbhujia sandwitch crill")
            if self.value_input28.get()!=0:
                self.txtarea.insert(END,f"\n {self.price28}\t\t{self.value_input28.get()}\tbhujia sandwitch cheese")
                
            if self.value_input1a.get()!=0:
                 self.txtarea.insert(END,f"\n {self.price1a}\t\t{self.value_input1a.get()}\tchawarema")
            if self.value_input2a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price2a}\t\t{self.value_input2a.get()}\tcorden bleu")
            if self.value_input3a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price3a}\t\t{self.value_input3a.get()}\tscalope creme")
            if self.value_input4a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price4a}\t\t{self.value_input4a.get()}\tballes grill ")
            if self.value_input5a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price5a}\t\t{self.value_input5a.get()}\tpoulet marine")
            if self.value_input6a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price6a}\t\t{self.value_input6a.get()}\tfried wings")
            if self.value_input7a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price7a}\t\t{self.value_input7a.get()}\tlemon paper wings")
            if self.value_input8a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price8a}\t\t{self.value_input8a.get()}\tjerk wings")
            if self.value_input9a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price9a}\t\t{self.value_input9a.get()}\tcreole wings")
            if self.value_input10a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price10a}\t\t{self.value_input10a.get()}\tfish filet")
            if self.value_input11a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price11a}\t\t{self.value_input11a.get()}\tGriot")
            if self.value_input12a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price12a}\t\t{self.value_input12a.get()}\tGrilled chicken")
            if self.value_input13a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price13a}\t\t{self.value_input13a.get()}\tcreole shrimp")
            if self.value_input14a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price14a}\t\t{self.value_input14a.get()}\tfried shrimp")
            if self.value_input15a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price15a}\t\t{self.value_input15a.get()}\tsteamed shrip")
            if self.value_input16a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price16a}\t\t{self.value_input16a.get()}\toxtail")
            if self.value_input17a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price17a}\t\t{self.value_input17a.get()}\tfried conch")
            if self.value_input18a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price18a}\t\t{self.value_input18a.get()}\tGrill conch")
            if self.value_input19a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price19a}\t\t{self.value_input19a.get()}\tslew conch")
            if self.value_input20a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price20a}\t\t{self.value_input20a.get()}\tfried fish")
            if self.value_input21a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price21a}\t\t{self.value_input21a.get()}\tlobster tail")
            if self.value_input22a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price22a}\t\t{self.value_input22a.get()}\tcrabe creole")
            if self.value_input23a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price23a}\t\t{self.value_input23a.get()}\tstew chicken")
            if self.value_input24a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price24a}\t\t{self.value_input24a.get()}\tGrilled chicken")
            if self.value_input25a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price25a}\t\t{self.value_input25a.get()}\tstew fish")
            if self.value_input26a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price26a}\t\t{self.value_input26a.get()}\tfried pork")
            if self.value_input27a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price27a}\t\t{self.value_input27a.get()}\tsteamed conch")
            if self.value_input28a.get()!=0:
                self.txtarea.insert(END,f"\n {self.price28a}\t\t{self.value_input28a.get()}\tcolombo")
                
                
            if self.value_input1aa.get()!=0:
                 self.txtarea.insert(END,f"\n {self.price1aa}\t\t{self.value_input1aa.get()}\thot oate")
            if self.value_input2aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price2aa}\t\t{self.value_input2aa.get()}\thot lotus")
            if self.value_input3aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price3aa}\t\t{self.value_input3aa.get()}\thot chocolate marshmllow")
            if self.value_input4aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price4aa}\t\t{self.value_input4aa.get()}\thot chocolate ")
            if self.value_input5aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price5aa}\t\t{self.value_input5aa.get()}\tlipton tea")
            if self.value_input6aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price6aa}\t\t{self.value_input6aa.get()}\tgreen tea")
            if self.value_input7aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price7aa}\t\t{self.value_input7aa.get()}\ttaylors tea")
            if self.value_input8aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price8aa}\t\t{self.value_input8aa.get()}\tahmed tea")
            if self.value_input9aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price9aa}\t\t{self.value_input9aa.get()}\tsahlab")
            if self.value_input10aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price10aa}\t\t{self.value_input10aa.get()}\tsahlab special aldawood")
            if self.value_input11aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price11aa}\t\t{self.value_input11aa.get()}\tlemon with honey")
            if self.value_input12aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price12aa}\t\t{self.value_input12aa.get()}\therbs")
            if self.value_input13aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price13aa}\t\t{self.value_input13aa.get()}\twarm milk")
            if self.value_input14aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price14aa}\t\t{self.value_input14aa.get()}\tespresso")
            if self.value_input15aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price15aa}\t\t{self.value_input15aa.get()}\thot penicillin")
            if self.value_input16aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price16aa}\t\t{self.value_input16aa.get()}\tmoneygun toddy")
            if self.value_input17aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price17aa}\t\t{self.value_input17aa.get()}\thot turmeric")
            if self.value_input18aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price18aa}\t\t{self.value_input18aa.get()}\ttahini hot chocolate")
            if self.value_input19aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price19aa}\t\t{self.value_input19aa.get()}\tmexican hot chocolate")
            if self.value_input20aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price20aa}\t\t{self.value_input20aa.get()}\tcoffe")
            if self.value_input21aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price21aa}\t\t{self.value_input21aa.get()}\tventage coffe")
            if self.value_input22aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price22aa}\t\t{self.value_input22aa.get()}\tmatcha latte")
            if self.value_input23aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price23aa}\t\t{self.value_input23aa.get()}\thot todde")
            if self.value_input24aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price24aa}\t\t{self.value_input24aa.get()}\tcaramel latte")
            if self.value_input25aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price25aa}\t\t{self.value_input25aa.get()}\thot coct")
            if self.value_input26aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price26aa}\t\t{self.value_input26aa.get()}\twarm hazelnu")
            if self.value_input27aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price27aa}\t\t{self.value_input27aa.get()}\t\tmagic coca")
            if self.value_input28aa.get()!=0:
                self.txtarea.insert(END,f"\n {self.price28aa}\t\t{self.value_input28aa.get()}\tpiccole latte")
                
            self.txtarea.insert(END,"\n......................................")
            self.txtarea.insert(END,f"\n\t{self.totall} $\t     المجموع الكلي")
            self.txtarea.insert(END,"\n......................................")
            
    
    
    def calculate_price(self):
        self.sandwitch=StringVar()
        self.sandwitch.set("00")
        self.dishes=StringVar()
        self.dishes.set("00")
        self.hotdrink=StringVar()
        self.hotdrink.set("00")
        f3=Frame(window,width=1360,height=100,bg=self.backgroundcolor).place(x=0,y=600)
        self.button_1=Button(window,text="الحساب",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.calculate_drink).place(x=1225,y=620)
        self.button_2=Button(window,text="افراغ الحقول",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.clear).place(x=1110,y=620)
        self.button_3=Button(window,text="تصدير الفاتوره",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.billing).place(x=1225,y=660)
        self.button_4=Button(window,text="اغلاق البرنامج",bg=self.color_button,width=10,borderwidth=2,cursor="hand2",font=("arial",13,"bold"),command=self.close).place(x=1110,y=660)
        self.text_price1=Label(window,text="حساب الكلي مشروبات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=880,y=630)
        self.input_price1=Entry(window,textvariable=self.hotdrink,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=750,y=630)
        self.text_price2=Label(window,text="حساب الكلي أطباق رئيسية",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=550,y=630)
        self.input_price2=Entry(window,textvariable=self.dishes,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=420,y=630)
        self.text_price3=Label(window,text="حساب الكلي الستدويتشات",bg=self.backgroundcolor,fg=self.fontcolor,font=("arial",13,"bold")).place(x=220,y=630)
        self.input_price3=Entry(window,textvariable=self.sandwitch,bg=self.fontcolor,font=("arial",13,"bold"),width=12).place(x=90,y=630)
    def clear(self):
        self.hotdrink.set("00")
        self.dishes.set("00")
        self.sandwitch.set("00")
        self.value_input1.set(0)
        self.value_input2.set(0)
        self.value_input3.set(0)
        self.value_input4.set(0)
        self.value_input5.set(0)
        self.value_input6.set(0)
        self.value_input7.set(0)
        self.value_input8.set(0)
        self.value_input9.set(0)
        self.value_input10.set(0)
        self.value_input11.set(0)
        self.value_input12.set(0)
        self.value_input13.set(0)
        self.value_input14.set(0)
        self.value_input15.set(0)
        self.value_input16.set(0)
        self.value_input17.set(0)
        self.value_input18.set(0)
        self.value_input19.set(0)
        self.value_input20.set(0)
        self.value_input21.set(0)
        self.value_input22.set(0)
        self.value_input23.set(0)
        self.value_input24.set(0)
        self.value_input25.set(0)
        self.value_input26.set(0)
        self.value_input27.set(0)
        self.value_input28.set(0)
        self.value_input1a.set(0)
        self.value_input2a.set(0)
        self.value_input3a.set(0)
        self.value_input4a.set(0)
        self.value_input5a.set(0)
        self.value_input6a.set(0)
        self.value_input7a.set(0)
        self.value_input8a.set(0)
        self.value_input9a.set(0)
        self.value_input10a.set(0)
        self.value_input11a.set(0)
        self.value_input12a.set(0)
        self.value_input13a.set(0)
        self.value_input14a.set(0)
        self.value_input15a.set(0)
        self.value_input16a.set(0)
        self.value_input17a.set(0)
        self.value_input18a.set(0)
        self.value_input19a.set(0)
        self.value_input20a.set(0)
        self.value_input21a.set(0)
        self.value_input22a.set(0)
        self.value_input23a.set(0)
        self.value_input24a.set(0)
        self.value_input25a.set(0)
        self.value_input26a.set(0)
        self.value_input27a.set(0)
        self.value_input28a.set(0)
        self.value_input1aa.set(0)
        self.value_input2aa.set(0)
        self.value_input3aa.set(0)
        self.value_input4aa.set(0)
        self.value_input5aa.set(0)
        self.value_input6aa.set(0)
        self.value_input7aa.set(0)
        self.value_input8aa.set(0)
        self.value_input9aa.set(0)
        self.value_input10aa.set(0)
        self.value_input11aa.set(0)
        self.value_input12aa.set(0)
        self.value_input13aa.set(0)
        self.value_input14aa.set(0)
        self.value_input15aa.set(0)
        self.value_input16aa.set(0)
        self.value_input17aa.set(0)
        self.value_input18aa.set(0)
        self.value_input19aa.set(0)
        self.value_input20aa.set(0)
        self.value_input21aa.set(0)
        self.value_input22aa.set(0)
        self.value_input23aa.set(0)
        self.value_input24aa.set(0)
        self.value_input25aa.set(0)
        self.value_input26aa.set(0)
        self.value_input27aa.set(0)
        self.value_input28aa.set(0)        
          
window=Tk()
my_class=super(window)
my_class.header()

my_class.calculate_price() 
my_class.choice()
my_class.drink()
my_class.drink2()
my_class.drink3()
#my_class.calculate_drink2()

#my_class.calculate_drink3()

my_class.data_customer("reham",18)

my_class.alfatora()

window.mainloop()