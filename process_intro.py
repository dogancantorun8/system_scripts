#python içerisinden program çalıştırmak istersem prosses yaratırım
#bunun için "subprocess modülü" kullanılır
#subprocess içinde wrapper fonk yardımıyla çalıştırabilirim 



#######notepad.exe dosyasını python kodum içinden çalıştırabiliyorum
import subprocess
result = subprocess.run(['notepad.exe', 'sample.py'])
print('ok')

###bir process bittikten sonra çıktısını alıp kullanmak istersem capture output=True yazmalıyım
import subprocess  
#shell=True dersem shell komutlarımı yazabileceğimi belirtiyorum
result = subprocess.run("dir", shell=True, capture_output=True,encoding='utf-8') #cmd  açıkmış gibi işlem yap dir fonk çıktısını bize ver
print('ok') 
print(result.stdout)

#bir test python programımı başka bir python dosyasından çalışmak istersem 
import subprocess
result = subprocess.run(['python', 'test.py'], capture_output=True, encoding='utf-8')
print(result.stdout)

#######popen kullanımı#####  

#Not defterimi çalıştırdım
import subprocess
result = subprocess.Popen('notepad.exe')
print('ok')

#komut satırından çalıştırdığım fonk çıktısını bir değişkene atmak istersem 
import subprocess
result = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, encoding='UTF-8') #çıktıyı alıp atama yapmak istersem kullanıyorum
text = result.stdout.read() #dir fonksiyonumun çıktısını text değişkenime atadım 
print(text)

##Not:Subprocess.run ile subproces.popen arasındaki fark::ilkinde ilk programın bitmesi beklenirken popen da bu durum söz konusu değil 

##bir exeyi çalıştırıp communicate ile işlem yapmak communicate ile input verdim
import subprocess
result = subprocess.Popen('test.exe', encoding='utf-8', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, stderr = result.communicate('10 20 30 0')
print(stdout)

