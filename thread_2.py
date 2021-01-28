# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 01:02:04 2021

@author: Dogancan Torun
"""


#Bir cpuda kuyrukta ne kadar fazla eleamn varsa işlemden o kadar geç sonuç alırız.O andaki sistem yükü resp time için önemlidir



#Bir thread nasıl yaratılır:
#Bir thread threading sınıfının modülüyle yaratılır. 
#thread.start() verilerek threadin akışı başlatılır 
##iki threadli bir akış örneği:Main thread içerisinde 2. bir thread yaratıyorum  
#ekran çıktısındaki tuhaflık threadlerin asenkron biçimde çalışması kaynaklıdır 
import threading
import time

def thread_func():
    for i in range(10):
        print(f'new thread: {i}')
        time.sleep(1) #thread_func threadini bir saniye durdurur diğer threadim çalışmaya devam eder

def main():
    t = threading.Thread(target=thread_func) #thread yaratma şeklim
    t.start() # t nesnemi start diyip çalıştırıyorum
    
    for i in range(10):
        print(f'main thread: {i}')
        time.sleep(1) #main threadimi bir saniye durdurur diğer threadim çalışmaya devam eder

main() 
#------------------------------------------------------------- 

#Bir threade parametre geçirmek istersem;args içine tuple şeklinde yazımı verdim ve thread_fuc methoduna geçti
import threading
import time

def thread_func(msg):
    for i in range(10):
        print(f'{msg}: {i}')
        time.sleep(1)

def main():
    t = threading.Thread(target=thread_func, args=('new thread',)) #tuple aliyor arguman olarak
    t.start()
    
    for i in range(10):
        print(f'main thread: {i}')
        time.sleep(1)

main() 

##bir threade aşağıdaki gibi iki tane  parametre geçirmek istersem :
import threading
import time

def thread_func(msg, xxx):
    for i in range(10):
        print(f'{msg}: {i}')
        time.sleep(1)
    print('xxx', '=', xxx)

def main():
    t = threading.Thread(target=thread_func, args=('new thread',), kwargs={'xxx': 100})
    t.start()
    
    for i in range(10):
        print(f'main thread: {i}')
        time.sleep(1)

main()

#aynı fonksiyonu birden fazla thread işletebilir. 
#yerel değişkenler stackte yaratılır ve her threadin stacki farklıdır 
import threading
import time

def foo(msg):
    i = 0
    while i < 10:
        print(msg, '=>', i) #her thread yereldegiskenin farkli kopyasini olusturuyor
        i += 1
        time.sleep(1)
    

def thread_func():
    foo('N')#her thread foo fonksiyonunu çağırıyor

def main():
    t = threading.Thread(target=thread_func)
    t.start()
    foo('M')#her thread foo fonksiyonunu çağırıyor
    

main()

#threadlerde global değişken kullanma kuralı
##global degiskenler ortak 

import threading
import time

i = 0 #her thread diğerinin arttırdığı i değişkenini alıp arttıryor yerel bir kopya yapmıyor

def foo(msg):
    global i
    
    while i < 10:
        print(msg, '=>', i)
        i += 1
        time.sleep(1)
    
def thread_func():
    foo('N')

def main():
    t = threading.Thread(target=thread_func)
    t.start()
    foo('M')
    
main()

##Bir thread ne zaman biter? =>>pythonda tipik olarak bir thread bittiğinde sonlanır bir müdahale vs olmaz 
#aşağıdaki örnekte bir thread çalışırken diğeri bekliyor.
import threading
import time
    
def thread_func():
    for i in range(10):
        print(i, end=' ')
        time.sleep(1)

def main():
    t = threading.Thread(target=thread_func)
    t.start()
    s = input('Adı Soyadı:')
    print(s)  
main()

#bir thread icindeki herhangi bir exception tüm programı çökertmez yalnızca o threadi sonlandırır. 
import threading
import time
     
def thread_func():
    for i in range(10):
        print(f'new thread: {i}')
        time.sleep(1)
        if i == 5:
            raise ValueError('Exception occurred!') #yalnızca bu thread sonlandırılır

#eğer main threadde exception olsaydı tüm programım patlardı
def main():
    t = threading.Thread(target=thread_func)
    t.start()
    
    time.sleep(0.5)
    
    for i in range(10):
        print(f'Main thread: {i}')
        time.sleep(1)
        
main()

#Bazı programlama dillerinde ana thread biterse program sonlanır.(C gibi) 
#Bazı programlama dillerinde ana threadin bitmesiyle program sonlanmz ve son thread bitene kadar devam eder.(java,python) 
import threading
import time
     
def thread_func():
    for i in range(10):
        print(f'new thread: {i}')
        time.sleep(1)

def main():
    t = threading.Thread(target=thread_func)
    t.start()
    print('main thread ends...')   #ana thread bitti ama diğer threadimim çalışmaya devam etti
        
main()

#daemeon thread :ana thread daemeon thread değildir. Processin daemeon olmayan threadi sonlandığında iş biter 

#is_alive:O anda o thread yaşıyor mu onu kontrol etmek için kullanılır.True false şeklinde toggle yapar
import threading
import time
     
def thread_func():
    for i in range(10):
        print(i, end=' ')
        time.sleep(1)

def main():
    t = threading.Thread(target=thread_func)
    print(t.is_alive())
    t.start()
    print(t.is_alive())
    input('Press ENTER to continue...')
    print(t.is_alive())
        
main()

####
import threading
import time
     
def thread_func():
    for i in range(10):
        print(i, end=' ')
        time.sleep(1)

def main():
    t = threading.Thread(target=thread_func)
    t.start()    
    t.join() #zaman verilmezse diğer threadler bitene kadar main thread bekler. hepsi bitince ok der geçer t.join(x) x saniye bekliyor 
    #♦t.join(4) 4 saniyeye kadar diğeri bitmezse main thread kladığı yerden devam eder.
    print('Ok')
        
main()
