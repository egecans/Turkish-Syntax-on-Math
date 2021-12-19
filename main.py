import re
keywords = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta'}
float_numbers=[]
for i in range (0,10):
    for t in range (0,10):
        float_numbers.append(str(float(str(i)+"."+str(t))))
integer_numbers=[]
for i in range (0,10):
    integer_numbers.append(str(int(i)))
meh=0
operators=["ve","veya","&","+","-","*","arti","eksi","carpi"]
tdigit=["sifir","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
tlogic=["dogru","yanlis"]
arithmetic_operators=["+","-","*","arti","eksi","carpi"]
paranthesis=["ac-parantez","kapa-parantez","(",")"]
ac_parantez=["ac-parantez","("]
kapa_parantez=["kapa-parantez",")"]
logic_operators=["ve","veya"]
digit_sonrasi_olabilecekler=arithmetic_operators+kapa_parantez
logic_sonrasi_olabilecekler=logic_operators+kapa_parantez
ar_op_sonra=ac_parantez+tdigit+integer_numbers+float_numbers
ar_op_once=kapa_parantez+tdigit+integer_numbers+float_numbers
lo_op_sonra=ac_parantez+tlogic
lo_op_once=kapa_parantez+tlogic
varandexp=[]
varandexpdigit=[]
varandexplogic=[]
exp=[]
Ana=False
Yeni=False
Sonuc=False
Sonuc_c=0
counter=0
line_counter=0
filename="calc.in"
f=open(filename)
liste=[]
for line in f:
    liste.append(1)
real_line_number=len(liste)
f.close()
f=open(filename)
try:
    for line in f:
        old_line_counter=line_counter
        yazilidigit = 0
        digitsayaci = 0
        ac_parantez_c = 0
        kapa_parantez_c = 0
        digit_c = 0
        a_operator_c = 0
        len_counter = 0
        logic_c = 0
        l_operator_c = 0
        dig_opsuz=0
        log_opsuz=0
        line_s=line.split()
        if line_s==[]:
            line_counter +=1
            continue
        if line_s==["AnaDegiskenler"] and counter==0:
            Ana=True
            counter+=1
            line_counter+=1
            continue
        if Ana==True and counter==1:
            Ana_Son = False
            l = line_s
            try:
                if not l[0] in keywords and l[0] not in varandexp:
                    t = re.search("[A-Za-z0-9]{1,10}", line)
                    if l[0] == t.group():
                        if l[1] == "degeri":
                            if len(l) == 4:
                                try:
                                    t = re.search("\d{1}.\d{1}", str(l[2]))
                                    if l[2] == t.group():
                                        Ana_Son = True
                                        varandexpdigit.append(l[0])
                                        varandexp.append(l[0])
                                        ar_op_once.append(l[0])
                                        ar_op_sonra.append(l[0])
                                except:
                                    pass
                                try:
                                    t = re.search("\d{1}", str(l[2]))
                                    if l[2] == t.group():
                                        Ana_Son = True
                                        varandexpdigit.append(l[0])
                                        varandexp.append(l[0])
                                        ar_op_once.append(l[0])
                                        ar_op_sonra.append(l[0])
                                except:
                                    pass
                                if Ana_Son == False and l[2] in tdigit:
                                    Ana_Son = True
                                    varandexpdigit.append(l[0])
                                    varandexp.append(l[0])
                                    ar_op_once.append(l[0])
                                    ar_op_sonra.append(l[0])
                                if Ana_Son == False and l[2] in tlogic:
                                    Ana_Son = True
                                    varandexplogic.append(l[0])
                                    varandexp.append(l[0])
                                    lo_op_once.append(l[0])
                                    lo_op_sonra.append(l[0])
                            elif len(l) == 6:
                                if l[2] in tdigit:
                                    if l[3] == "nokta":
                                        if l[4] in tdigit:
                                            Ana_Son = True
                                            varandexpdigit.append(l[0])
                                            varandexp.append(l[0])
                                            ar_op_once.append(l[0])
                                            ar_op_sonra.append(l[0])
                            if Ana_Son == True and l[-1] == "olsun":
                                line_counter += 1
                                continue
            except:
                pass
        if line_s == ["AnaDegiskenler"] and Ana==True:
            break
        if line_s==["YeniDegiskenler"] and Ana==True and counter==1:
            counter+=1
            Yeni=True
            line_counter += 1
            continue
        if line_s == ["YeniDegiskenler"] and Yeni == True:
            break
        if Yeni==True and counter==2:
            yenistr_lst=line_s
            for i in range(len(yenistr_lst)):
                if not yenistr_lst[0] in keywords and yenistr_lst[0] not in varandexp and yenistr_lst[-1] == "olsun":
                    t = re.search("[A-Za-z0-9]{1,10}", line)
                    if yenistr_lst[0] == t.group():
                        if yenistr_lst[1] == "degeri":
                            if i == 0 or i == 1:
                                len_counter += 1
                                continue
                    if len(yenistr_lst) >= 5:
                        if yazilidigit == digitsayaci:
                            yazilidigit = 0
                            digitsayaci = 0
                        if yazilidigit == 2:
                            digitsayaci += 1
                            continue
                        if yazilidigit == 0:
                            if yenistr_lst[i] in tdigit:
                                if yenistr_lst[i + 1] == "nokta":
                                    try:
                                        if yenistr_lst[i + 2] in tdigit and (
                                                yenistr_lst[i + 3] in digit_sonrasi_olabilecekler or i + 3 == len(
                                            yenistr_lst) - 1):
                                            digit_c += 1
                                            yazilidigit = 2
                                            digitsayaci = 0
                                            dig_opsuz=1
                                            len_counter += 3
                                    except:
                                        pass
                if yenistr_lst[i] in tdigit and yenistr_lst[i + 1] != "nokta" and (
                        yenistr_lst[i + 1] in digit_sonrasi_olabilecekler or i == len(yenistr_lst) - 2):
                    digit_c += 1
                    len_counter += 1
                    dig_opsuz = 1
                if yenistr_lst[i] in float_numbers and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                    dig_opsuz = 1
                if yenistr_lst[i] in integer_numbers and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                    dig_opsuz = 1
                if yenistr_lst[i] in varandexpdigit and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                    dig_opsuz = 1
                if yenistr_lst[i] in arithmetic_operators and yenistr_lst[i + 1] in ar_op_sonra and yenistr_lst[
                    i - 1] in ar_op_once:
                    a_operator_c += 1
                    len_counter += 1
                if yenistr_lst[i] in tlogic and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in logic_sonrasi_olabilecekler):
                    logic_c += 1
                    len_counter += 1
                    log_opsuz=1
                if yenistr_lst[i] in varandexplogic and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in logic_sonrasi_olabilecekler):
                    logic_c += 1
                    len_counter += 1
                    log_opsuz=1
                if yenistr_lst[i] in logic_operators and yenistr_lst[i + 1] in lo_op_sonra and yenistr_lst[
                    i - 1] in lo_op_once:
                    l_operator_c += 1
                    len_counter += 1
                if yenistr_lst[i] in ac_parantez and yenistr_lst[i + 1] not in kapa_parantez:
                    ac_parantez_c += 1
                    len_counter += 1
                if yenistr_lst[i] in kapa_parantez and ac_parantez_c > kapa_parantez_c:
                    kapa_parantez_c += 1
                    len_counter += 1
                if yenistr_lst[i] == "olsun" and i == len(yenistr_lst) - 1:
                    len_counter += 1
                if len_counter == len(yenistr_lst) and ac_parantez_c == kapa_parantez_c and (
                        a_operator_c + 1 == digit_c or l_operator_c + 1 == logic_c):
                    if dig_opsuz==1 and l_operator_c==0:
                        varandexpdigit.append(yenistr_lst[0])
                        ar_op_once.append(yenistr_lst[0])
                        ar_op_sonra.append(yenistr_lst[0])
                    if log_opsuz == 1 and a_operator_c==0:
                        varandexplogic.append(yenistr_lst[0])
                        lo_op_once.append(yenistr_lst[0])
                        lo_op_sonra.append(yenistr_lst[0])
                    varandexp.append(yenistr_lst[0])
                    line_counter += 1
                    continue
        if line_s==["Sonuc"] and Yeni==True and counter==2:
            counter+=1
            Sonuc=True
            line_counter += 1
            continue
        if Sonuc == True and counter == 3:
            yenistr_lst = line_s
            if Sonuc_c == 1 and yenistr_lst != []:
                break
            yenistr_lst.append(".")
            yenistr_lst.insert(0, ".")
            yenistr_lst.insert(0, ".")
            for i in range(len(yenistr_lst)):
                if len(yenistr_lst) >= 5:
                    if yazilidigit == digitsayaci:
                        yazilidigit = 0
                        digitsayaci = 0
                    if yazilidigit == 2:
                        digitsayaci += 1
                        continue
                    if yazilidigit == 0:
                        if yenistr_lst[i] in tdigit:
                            if yenistr_lst[i + 1] == "nokta":
                                try:
                                    if yenistr_lst[i + 2] in tdigit and (
                                            yenistr_lst[i + 3] in digit_sonrasi_olabilecekler or i + 3 == len(
                                        yenistr_lst) - 1):
                                        digit_c += 1
                                        yazilidigit = 2
                                        digitsayaci = 0
                                        len_counter += 3
                                except:
                                    pass
                if yenistr_lst[i] in tdigit and yenistr_lst[i + 1] != "nokta" and (
                        yenistr_lst[i + 1] in digit_sonrasi_olabilecekler or i == len(yenistr_lst) - 2):
                    digit_c += 1
                    len_counter += 1
                if yenistr_lst[i] in float_numbers and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                if yenistr_lst[i] in integer_numbers and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                if yenistr_lst[i] in varandexpdigit and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in digit_sonrasi_olabilecekler):
                    digit_c += 1
                    len_counter += 1
                if yenistr_lst[i] in arithmetic_operators and yenistr_lst[i + 1] in ar_op_sonra and yenistr_lst[
                    i - 1] in ar_op_once:
                    a_operator_c += 1
                    len_counter += 1
                if yenistr_lst[i] in tlogic and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in logic_sonrasi_olabilecekler):
                    logic_c += 1
                    len_counter += 1
                if yenistr_lst[i] in varandexplogic and (
                        i == (len(yenistr_lst) - 2) or yenistr_lst[i + 1] in logic_sonrasi_olabilecekler):
                    logic_c += 1
                    len_counter += 1
                if yenistr_lst[i] in logic_operators and yenistr_lst[i + 1] in lo_op_sonra and yenistr_lst[
                    i - 1] in lo_op_once:
                    l_operator_c += 1
                    len_counter += 1
                if yenistr_lst[i] in ac_parantez and yenistr_lst[i + 1] not in kapa_parantez:
                    ac_parantez_c += 1
                    len_counter += 1
                if yenistr_lst[i] in kapa_parantez and ac_parantez_c > kapa_parantez_c:
                    kapa_parantez_c += 1
                    len_counter += 1
                if len_counter == len(yenistr_lst) - 3 and ac_parantez_c == kapa_parantez_c and i == len(yenistr_lst)-1 and (
                        a_operator_c + 1 == digit_c or l_operator_c + 1 == logic_c):
                    Sonuc_c = 1
                    line_counter += 1
                    continue
        if old_line_counter==line_counter:
            break

    f.close()
except:
    line_counter==0
    pass


if real_line_number == line_counter:
    f1 = open("calc.out","w")
    f1.write("Here Comes the Sun")
    f1.close()

if real_line_number != line_counter:
    f2 = open("calc.out","w")
    f2.write("Dont Let Me Down")
    f2.close()
