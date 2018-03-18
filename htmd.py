#! ../usr/bin/python2

import subprocess,time,random,sys

#colour

G = "\033[32m"; O = "\033[33m"; B = "\033[34m"; R = "\033[31m"; W = "\033[0m";

#random.colour

x = "\033["
color = (x+"32m",x+"34m",x+"35m",x+"36m")
Z = random.choice(color)

def logo():
	if sys.platform == 'linux' or sys.platform == 'linux2':
		subprocess.call("clear", shell=True)
		time.sleep(1)

	else:
		subprocess.call("cls", shell=True)
		time.sleep(1)


	print Z+"    _   _ _             ____"
	print Z+"   | | | | |_ _ __ ___ |  _ \ "
	print Z+"   | |_| | __| '_ ` _ \| | | |"
	print Z+"   |  _  | |_| | | | | | |_| |"
	print Z+"   |_| |_|\__|_| |_| |_|____/"

# Mengganti Author Tidak akan membuat anda menjadi PRO

	print R+"\n  0={==> "+W+"Html Downloader"+R+" <==}=0\n"
	print R+"[+]"+O+" author : "+G+"Ci Ku "+O+"a.k.a"+G+" XnVer404"
	print R+"[+]"+O+" thanks to "+G+"OneSec Onz "+O+"and"+G+" Null\n"
	use()



def use():
	website = raw_input(B+"[?]"+G+" website  : "+O)
	if "http" in website or "https" in website:
		output = raw_input(B+"[?]"+G+" file output (ex: hasil) : "+O)
		time.sleep(1)

		print R+"[+] Curl started . . .\n"+G
		time.sleep(1)
		subprocess.call("curl -o "+output+".htm "+website,shell=True)
		time.sleep(1)
		print B+"\n[*]"+G+" File save : "+O+output+".htm"
		exit()
	else:
		print R+"using http or https"
		use()

logo()
