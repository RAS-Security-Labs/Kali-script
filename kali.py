#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires sudo privledges"
	sys.exit()
def main():
	try:
		print ('''

                       
                       \033[1;36m
                                                     ######     #     #####
                                                     #     #   # #   #     #
                                                     #     #  #   #  #
                                                     ######  #     #  #####
                                                     #   #   #######       #
                                                     #    #  #     # #     # 
                                                     #     # #     #  #####\033[1;m

                                                  



\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Forensics Tools
2) Vulnerability Analysis			9) Password Attacks
3) Web Applications				10) Reverse Engineering
4) Sniffing & Spoofing				11) Extra
5) Maintaining Access				
6) Reporting Tools 				
7) Exploitation Tools				
									
0) All

			 ''')
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install cisco-torch dmitry dnsenum dnsrecon enum4linux exploitdb maltego-teeth masscan metagoofil nmap p0f recon-ng set smtp-user-enum sslstrip theharvester wireshark hping3 cisco-auditing-tool cisco-global-exploiter cisco-ocs greenbone-security-assistant openvas-cli openvas-manager openvas-scanner sqlmap unix-privesc-check yersinia aircrack-ng fern-wifi-cracker kismet wifite apache-users burpsuite dirb dirbuster jboss-autopwn maltego-teeth padbuster recon-ng webscarab wfuzz wpscan zaproxy nishang powersploit dradis metagoofil armitage beef-xss binwalk p0f volatility cewl findmyhash hash-identifier john patator rainbowcrack wordlists apktool dex2jar jad jd && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Information Gathering\033[1;m

 1) bing-ip2hosts				
 2) DMitry					
 3) dnsenum					
 4) DNSRecon					
 5) enum4linux				
 6) exploitdb				
 7) Maltego Teeth			
 8) masscan				
 9) Metagoofil				
10) Nmap				
11) Recon-ng				
12) smtp-user-enum			
13) snmpcheck				
14) sslstrip				
15) theHarvester			
16) Wireshark				
17) hping3	
18) smbmap
19) smbclient			
20) nslookup

0) Install all Information Gathering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "2":
								cmd = os.system("apt-get install dmitry")
							elif opcion2 == "3":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dnsrecon")
							elif opcion2 == "5":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "6":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "7":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "8":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "9":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "10":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "11":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "12":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "13":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "14":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "15":
								cmd = os.system("apt-get install theharvester")
							elif opcion2 == "16":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "17":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "18":
								cmd = os.system("apt-get install smbmap")
							elif opcion2 == "19":
								cmd = os.system("apt-get install smbclient")
							elif opcion2 == "20":
								cmd = os.system("apt-get install dnsutils")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y dmitry dnsenum dnsrecon enum4linux exploitdb maltego-teeth masscan metagoofil nmap recon-ng smtp-user-enum snmpcheck sslstrip theharvester wireshark hping3 smbmap smbclient dnsutils && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) commix				
 2) Greenbone Security Assistant 					
 3) Nmap		
 4) openvas-administrator		
 5) openvas-cli			
 6) openvas-manager		
 7) openvas-scanner		
 8) sqlmap			
 9) unix-privesc-check		
10) Yersinia	
11) TestSSL		


0) Install all Vulnerability Analysis tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "2":
                                                                cmd = os.system("apt-get install greenbone-security-assistant")
							elif opcion2 == "3":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install openvas-administrator")
							elif opcion2 == "5":
								cmd = os.system("apt-get install openvas-cli")
							elif opcion2 == "6":
								cmd = os.system("apt-get install openvas-manager")
							elif opcion2 == "7":
								cmd = os.system("apt-get install openvas-scanner")
							elif opcion2 == "8":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "9":
								cmd = os.system("apt-get install unix-privesc-check")
							elif opcion2 == "10":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "11":
								cmd = os.system("git clone https://github.com/drwetter/testssl.sh.git")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y greenbone-security-assistant nmap openvas-cli openvas-manager openvas-scanner sqlmap unix-privesc-check yersinia")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						
						while opcion1 == "3":
							print ('''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users			
 2) Burp Suite				
 3) commix				
 4) DIRB			
 5) DirBuster			
 6) jboss-autopwn		
 7) Maltego Teeth		
 8) PadBuster			
 9) Recon-ng			
10) Skipfish			
11) sqlmap			
12) Wfuzz			
13) WPScan			
14) zaproxy	
15) Gobuster	
16) Git	

0) Install all Web Applications tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apache-users")
							elif opcion2 == "2":
								cmd = os.system("apt-get install burpsuite")
							elif opcion2 == "3":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dirb")
							elif opcion2 == "5":
								cmd = os.system("apt-get install dirbuster")
							elif opcion2 == "6":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "7":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "8":
								cmd = os.system("apt-get install padbuster")
							elif opcion2 == "9":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "10":
								cmd = os.system("apt-get install skipfish")
							elif opcion2 == "11":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "12":
								cmd = os.system("apt-get install wfuzz")
							elif opcion2 == "13":
								cmd = os.system("apt-get install wpscan")
							elif opcion2 == "14":
								cmd = os.system("apt-get install zaproxy")	
							elif opcion2 == "15":
								cmd = os.system("apt-get install gobuster")	
							elif opcion2 == "16":
								cmd = os.system("apt-get install git")	
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apache-users burpsuite dirb dirbuster jboss-autopwn maltego-teeth padbuster recon-ng skipfish sqlmap wfuzz wpscan zaproxy gobuster")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				
 2) mitmproxy				
 3) sslstrip				
 4) WebScarab			
 5) Wireshark				
 6) Yersinia				
 7) zaproxy				
 
0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install burpsuite")
							elif opcion2 == "2":
								cmd = os.system("apt-get install mitmproxy")
							elif opcion2 == "3":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "4":
								cmd = os.system("apt-get install webscarab")
							elif opcion2 == "5":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "6":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "7":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("apt-get install -y burpsuite mitmproxy sslstrip webscarab wireshark yersinia zaproxy")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "5":
							print ('''
\033[1;36m=+[ Maintaining Access\033[1;m

 1) Nishang
 2) PowerSploit
 3) Webshells
 4) Weevely

0) Install all Maintaining Access tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install nishang")
							elif opcion2 == "2":
								cmd = os.system("apt-get install powersploit")
							elif opcion2 == "3":
								cmd = os.system("apt-get install webshells")
							elif opcion2 == "4":
								cmd = os.system("apt-get install weevely")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y nishang powersploit webshells weevely")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "6":
							print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) Dradis
2) Metagoofil

0) Install all Reporting Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install dradis")
							elif opcion2 == "2":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y dradis metagoofil ")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "7":
							print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) BeEF
 3) commix
 4) jboss-autopwn
 5) Maltego Teeth
 6) sqlmap
 7) Yersinia

0) Install all Exploitation Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install armitage")
							elif opcion2 == "2":
								cmd = os.system("apt-get install beef-xss")
							elif opcion2 == "3":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "4":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "5":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "6":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "7":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y armitage beef-xss jboss-autopwn maltego-teeth sqlmap yersinia ")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				
 2) p0f					
 3) Volatility				
 
0) Install all Forensics Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install binwalk")
							elif opcion2 == "2":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "3":
								cmd = os.system("apt-get install volatility")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y binwalk p0f volatility")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						
						while opcion1 == "9":
							print ('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) CeWL				
 2) cisco-auditing-tool			
 3) gpp-decrypt				
 4) hash-identifier			
 5) THC-Hydra			        
 6) John the Ripper			
 7) patator				
 8) RainbowCrack			
 9) THC-pptp-bruter			
10) wordlists				

0) Install all Password Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install cewl")
							elif opcion2 == "2":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "3":
								cmd = os.system("apt-get install gpp-decrypt")
							elif opcion2 == "4":
								cmd = os.system("apt-get install hash-identifier")
							elif opcion2 == "5":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "6":
								cmd = os.system("apt-get install john")
							elif opcion2 == "7":
								cmd = os.system("apt-get install patator")
							elif opcion2 == "8":
								cmd = os.system("apt-get install rainbowcrack")
							elif opcion2 == "9":
								cmd = os.system("apt-get install thc-pptp-bruter")
							elif opcion2 == "10":
								cmd = os.system("apt-get install wordlists")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y cewl cisco-auditing-tool gpp-decrypt hash-identifier john patator rainbowcrack thc-pptp-bruter wordlists ")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10" :
							print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) jad	
 4) JD-GUI
 5) OllyDbg
 6) YARA

0) Install all Reverse Engineering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apktool")
							elif opcion2 == "2":
								cmd = os.system("apt-get install dex2jar")
							elif opcion2 == "3":
								cmd = os.system("apt-get install jad")
							elif opcion2 == "4":
								cmd = os.system("apt-get install JD")
							elif opcion2 == "5":
								cmd = os.system("apt-get install OllyDbg")
							elif opcion2 == "6":
								cmd = os.system("apt-get install YARA")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apktool dex2jar jad JD OllyDbg YARA")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				''')
							print ("\033[1;32mInsert the number of the tool to install .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()

