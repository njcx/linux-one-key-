#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
\033[1;91mmooooooooooo   nnnn  nnnnnnnn        eeeeeeeeeeee    
 oo:::::::::::oo n:::nn::::::::nn    ee::::::::::::ee  
o:::::::::::::::on::::::::::::::nn  e::::::eeeee:::::ee
o:::::ooooo:::::onn:::::::::::::::ne::::::e     e:::::e
o::::o     o::::o  n:::::nnnn:::::ne:::::::eeeee::::::e
o::::o     o::::o  n::::n    n::::ne:::::::::::::::::e 
o::::o     o::::o  n::::n    n::::ne::::::eeeeeeeeeee  
o::::o     o::::o  n::::n    n::::ne:::::::e           
o:::::ooooo:::::o  n::::n    n::::ne::::::::e          
o:::::::::::::::o  n::::n    n::::n e::::::::eeeeeeee  
 oo:::::::::::oo   n::::n    n::::n  ee:::::::::::::e  
   ooooooooooo     nnnnnn    nnnnnn    eeeeeeeeeeeeee\033[1;m      
\033[1;36mkkkkkkkk                                                   
k::::::k                                                   
k::::::k                                                   
k::::::k                                                   
 k:::::k    kkkkkkk eeeeeeeeeeee  yyyyyyy           yyyyyyy
 k:::::k   k:::::kee::::::::::::ee y:::::y         y:::::y 
 k:::::k  k:::::ke::::::eeeee:::::eey:::::y       y:::::y  
 k:::::k k:::::ke::::::e     e:::::e y:::::y     y:::::y   
 k::::::k:::::k e:::::::eeeee::::::e  y:::::y   y:::::y    
 k:::::::::::k  e:::::::::::::::::e    y:::::y y:::::y     
 k:::::::::::k  e::::::eeeeeeeeeee      y:::::y:::::y      
 k::::::k:::::k e:::::::e                y:::::::::y       
k::::::k k:::::ke::::::::e                y:::::::y        
k::::::k  k:::::ke::::::::eeeeeeee         y:::::y         
k::::::k   k:::::kee:::::::::::::e        y:::::y          
kkkkkkkk    kkkkkkk eeeeeeeeeeeeee       y:::::y           
                                        y:::::y            
                                       y:::::y             
                                      y:::::y              
                                     y:::::y               
                                    yyyyyyy\033[1;m               
+ -- -- +=[ Author: nJcx | Homepage: www.nJcxs.cc


''')


		def inicio1():
			while True:
				print ('''
1) Red hat/Centos  

2) Debian/Ubuntu


			''')

				opcion0 = raw_input("\033[1;36mnJcx > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Makecache
2)Some tools to install
3)Back


					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("yum makecache")
					elif repo == "2":
						cmd1 = os.system("yum install -y ")
					elif repo == "3":
						inicio1()
					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "2":
					print (''' 
1) Update
2)Some tools to install 
3)Back

''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-get update")
					elif repo == "3":
						inicio1()
					elif repo == "2":
						cmd1 = os.system("apt-get install -y --allow-unauthenticated gparted zim amule skype redshift x11vnc remmina ssvnc htop shutter gdebi bleachbit gedit fcitx-sunpinyin fcitx-googlepinyin fcitx-module-cloudpinyin fcitx fcitx-config-common kchmviewer synaptic software-center bluefish zip unzip qmmp hardinfo fcitx-config-gtk libmysqlclient-dev zlib1g-dev automake checkinstall vlc python-pip kodi python3-pip vim mysql-server mysql-client apache2 umbrello dia boa-constructor")
						cmd2 = os.system("apt-get install -y --allow-unauthenticated eclipse qemu-kvm libvirt-bin virt-manager virtualenv bridge-utils labyrinth smplayer amarok chromium-browser filezilla putty git spyder ninja-ide idle-python3.5 rar unrar geany idle-python2.7 emacs spe eric fish spyder3 php7.0 fbreader vym semantik filelight mysql-workbench arduino codeblocks libapache2-mod-php7.0 php7.0-mysql phpmyadmin")
						cmd3 = os.system("apt-get install -y --allow-unauthenticated pepperflashplugin-nonfree ")
						cmd4 = os.system("update-pepperflashplugin-nonfree --install&&cp libflashplayer.so /usr/lib/firefox/browser/plugins&&dpkg -i lantern-installer-beta-64-bit.deb&&apt-get -f install -y&&dpkg -i kwplayer_3.5.2-1_all.deb&&apt-get -f install -y&&dpkg -i sogoupinyin_2.0.0.0078_amd64.deb&&apt-get -f install -y&&dpkg -i xware-desktop_0.13.20160328_amd64.deb&&apt-get -f install -y&&dpkg -i aliwangwang_1.00-00_amd64.deb&&apt-get -f install -y&&dpkg -i wiznote_2.3.2.4_amd64.deb&&apt-get -f install -y")

                inicio1()
	except KeyboardInterrupt:
		print ("Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
