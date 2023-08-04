import random

char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1345678902`~!#$%^&*()_=+@<>,./\][{}"
pin = "1234567890"
u_case = "qwertyuiopasdfghjklzxcvbnm"
l_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
sp_ch = "`~!#$%^&*()_=+@<>,./\][{}"
len_chr = len(char)
password = ''
userpin=''
ask_user = int(input('Do you want a password or pin or custom password [1 for password]or[2 for pin]or[3 for custom password]:'))
if ask_user == 1:
    ask_char = int(input('Enter no of character in your password[Preferred 20]:'))
    ask_name = input('Do you want to add name to your password[yes or no]:')
    if ask_name.lower() == 'yes':
        ent_name = input('Enter your name:')
        r_c = random.randint(0, ask_char // 2)
        print('.....Generating Password.....')
        for i in range(0, r_c):
            rand = random.randint(0, len_chr)
            password += char[rand]
        password += ent_name
        for i in range(r_c, ask_char - len(ent_name)):
            rand = random.randint(0, len_chr)
            password += char[rand]
        print(password)
    else:
        print('.....Generating Password.....')
        for i in range(0, ask_char):
            rand = random.randint(0, len_chr)
            password += char[rand]
        print(password)
elif ask_user == 2:
    ask_char1 = int(input('Enter no of character in your password[Preferred 20]:'))
    print('.....Generating Password.....')
    for i in range(0, ask_char1):
        rand = random.randint(0, 10)
        password += pin[rand]
    print(password)
elif ask_user == 3:
    u = int(input('Enter no of upper case in your password:'))
    l = int(input('Enter no of lower case in your password:'))
    s = int(input('Enter no of special chr in your password:'))
    d = int(input('Enter no of digits in your password:'))
    add = u + l + s + d
    cuspass = ''
    ul = []
    ll = []
    sl = []
    dl = []
    for i in range(0, u):
        uc = random.randint(0, len(u_case))
        ul.append(u_case[uc])
    for i in range(0, l):
        lc = random.randint(0, len(l_case))
        ll.append(l_case[lc])
    for i in range(0, s):
        sc = random.randint(0, len(sp_ch))
        sl.append(sp_ch[sc])
    for i in range(0, d):
        dc=random.randint(0,len(pin))
        dl.append(pin[dc])
    while True:
        dom = random.randint(1, 4)
        if dom == 1 and ul != []:
            u_l = len(ul)
            u_r = random.randint(0, u_l - 1)
            cuspass += ul[u_r]
            del ul[u_r]
        elif dom == 2 and ll != []:
            l_l = len(ll)
            l_r = random.randint(0, l_l - 1)
            cuspass += ll[l_r]
            del ll[l_r]
        elif dom == 3 and sl != []:
            s_l = len(sl)
            s_r = random.randint(0, s_l - 1)
            cuspass += sl[s_r]
            del sl[s_r]
        elif dom == 4 and dl != []:
            d_l = len(dl)
            d_r = random.randint(0, d_l - 1)
            cuspass += dl[d_r]
            del dl[d_r]
        if len(cuspass) == add:
            break
        else:
            continue
    print(cuspass)
else:
    pass
