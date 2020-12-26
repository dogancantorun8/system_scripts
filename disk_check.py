#this script check storage of directory
#!/usr/bin/python
import os
command="df -h"
stdout=os.popen(command)
#read = file.readlines()
read=stdout.readlines()
#print(read)
for line in read:
    line=line.split()
    for i in line:
        if(i=="/dev/mapper/app2vg-u02lv"):
            #print(line[4].strip('%'))
            esik_deger=int(line[4].strip('%'))
            if esik_deger>90 :
                os.system("echo 'Bu mail Doğancan Torun tarafindan  atilmaktadir XX.XX.XX.XXX sunucusunda, /dev/mapper/app2vg-u02lv dizininde doluluk orani %90 uzerindedir lutfen kontrol ediniz' | mail -s 'DIZIN_DOLULUK_ORANI' -r sendermail@gmail.com receievemail@gmail.com")

                print('ok')