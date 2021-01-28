# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:40:44 2021

@author: doğancan torun
"""

#Threadlerle çalışma:  
#bir programda farklı akışlar yaratmak istersem threadleri kullanıyorum
#bir programın farklı iki akışı  olsun veya yeni akışlarla kordineli işlemler yapsın istersem thread kullanıyorum 
#Her program bir threadle başlar diğer tüm threadleri biz yaratırız.
#------------------------
import time
import threading 

def foo():
    for i in range(10):
        print('other thread: {}'.format(i))
        time.sleep(1)

def main():
    for i in range(10):
        print('main thread: {}'.format(i))
        time.sleep(1)
        
        
thread = threading.Thread(target=foo) #yeni threadler thread sınıfıyla yaratılıyor
thread.start() #threadimi start methodumla başlatıyorum
main() #main thread program başladğında çalışan threadim  bu akışta 2 thread çalıştı

###3 farklı thread çalıştırmak istersem 

import time
import threading

def foo():
    for i in range(10):
        print('1.thread: {}'.format(i))
        time.sleep(1)

def bar():
    for i in range(10):
        print('2.thread: {}'.format(i))
        time.sleep(1)

def main():
    for i in range(10):
        print('main thread: {}'.format(i))
        time.sleep(1)
        
       
thread1 = threading.Thread(target=foo)
thread1.start()

thread2 = threading.Thread(target=bar)
thread2.start()
main()

######################  TEORİK ANLATIM  ##################

#Bir process akış bakımından threadlerden oluşuyor 
#Thread yapısı 90 larda başlamıştır.Threadden önce çalışma zaman paylaşımlı yapmaktadır 
#Zaman paylaşımlı işleme methodu :cpu da bir thread çalışıyor , yarıda bırakıp  diğeri başlıyor.   
#işletim sistemleri çalıştıracağı threadleri "runqueeue" da biriktirir.ve schedule olarak çalıştırır. 
 

            ##Threadlere neden gereksinim duyulur## 
#1)periyodik arka plan işlemleri yapmak için  
#2)bir programı hızlandırmak için;
    #Concurrency:Akışların beraber işleme alınmasına denir.Alt başlıkları aşağıdaki gibidir
    #Multithread programming:Concurrency alt başlığında bulunur.Programı threadlere ayırarak çalışmasını sağlar 
    #Disturbited programming:Bir işi birden fazla bilgisayara bir network aracılığıyla  dağıtarak yapma işlemi. 
    #Parallel programming:Aynı makina içerisinde threadler oluşturup corelara bilinçli şekilde atayıp çalıştırma işlemine denir 
    #Not:Pythonda global programlama yok iken python kütüphanelerinden keras vs de paralel programlama kullanılır. Kerasta kodun içinde C kodu koşturulur.
 
#3)Blokeli IO işlemleri için kullanılır;
    #Server-Client IO uygulamalarında multithreading yapı kullanılır.

#4)Bazı GUI programlarda kullanılıyor 

   

#--- #Tkinter thread kullanım örneği;  

#GUI programlarda herhangi bir işlemin messagequeda uzun süre kalmasını istemediğimizde threadleri kullanırız 


import threading 
import tkinter as tk
import tkinter.messagebox
import threading

import time

class GUI:
    def __init__(self, master):
        master.geometry('400x350')
        master.title('Sample Data Binding')
        self.master = master
        
        self.button_start = tk.Button(master, text='Çalıştır', command=self.button_start_handler)
        self.button_start.place(x=100, y=10, width=70, height=70)
        
        self.button_stop = tk.Button(master, text='Stop', command=self.button_stop_handler)
        self.button_stop.place(x=200, y=10, width=70, height=70)
  
    def do_something(self): #yapmak istediğim işlemi do_something icerisinde yazıyorum ve mesaj döngüsünde kalıyorum
        for i in range(100):
            if self.flag:
                 break
            print(i)
            time.sleep(1)
  
    def button_start_handler(self): 
        """  
        thread yaratıyoruz ve işlemi threade yaptırıp program akışımıza kaldığımız yerden devam ediyoruz
        akışımız bu şekilde ilerliyor
        """
        self.flag = False
        self.thread = threading.Thread(target=self.do_something) #butona bastığımda bir thread yaratıyorum
        self.thread.start() #threadi çalıştırıyorum
        
       
    def button_stop_handler(self):
        self.flag = True
       
    
root = tk.Tk()
gdb = GUI(root)
root.mainloop()

