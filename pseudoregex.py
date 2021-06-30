prueba_arr = []
a_0 = None
a_1 = None
a_2 = None
a_3 = None
a_4 = None
a_5 = None
a_6 = None
a_7 = None
a_8 = None
a_9 = None
a_10 = None
a_11 = None
a_12 = None
a_13 = None
a_14 = None
a_15 = None
a_16 = None
a_17 = None
a_18 = None
a_19 = None
a_20 = None
a_21 = None
a_22 = None
a_23 = None
a_24 = None
a_25 = None
a_26 = None
a_27 = None
a_28 = None
a_29 = None
a_30 = None
a_31 = None
a_32 = None
a_33 = None
a_34 = None
a_35 = None
a_36 = None
a_37 = None
a_38 = None
a_39 = None
regex_0 = []
regex_final = None
n = 0
largo_before = None

with open('prueba.txt', 'r') as f:
    first_line = f.readline()
    prueba_arr.append(first_line)
    for i in f:
        prueba_arr.append(i)

def concatenar_lista(lista, caracter):
    if isinstance(lista, list):
        return caracter.join(map(str, lista))

head0, sep0, tail0 = prueba_arr[0].partition('@')
head1, sep1, tail1 = prueba_arr[1].partition('@')
head2, sep2, tail2 = prueba_arr[2].partition('@')
head3, sep3, tail3 = prueba_arr[3].partition('@')
head4, sep4, tail4 = prueba_arr[4].partition('@')
head5, sep5, tail5 = prueba_arr[5].partition('@')
head6, sep6, tail6 = prueba_arr[6].partition('@')
head7, sep7, tail7 = prueba_arr[7].partition('@')
head8, sep8, tail8 = prueba_arr[8].partition('@')
head9, sep9, tail9 = prueba_arr[9].partition('@')
head10, sep10, tail10 = prueba_arr[10].partition('@')
head11, sep11, tail11 = prueba_arr[11].partition('@')
head12, sep12, tail12 = prueba_arr[12].partition('@')
head13, sep13, tail13 = prueba_arr[13].partition('@')
head14, sep14, tail14 = prueba_arr[14].partition('@')
head15, sep15, tail15 = prueba_arr[15].partition('@')
head16, sep16, tail16 = prueba_arr[16].partition('@')
head17, sep17, tail17 = prueba_arr[17].partition('@')
head18, sep18, tail18 = prueba_arr[18].partition('@')
head19, sep19, tail19 = prueba_arr[19].partition('@')
head20, sep20, tail20 = prueba_arr[20].partition('@')
head21, sep21, tail21 = prueba_arr[21].partition('@')
head22, sep22, tail22 = prueba_arr[22].partition('@')
head23, sep23, tail23 = prueba_arr[23].partition('@')
head24, sep24, tail24 = prueba_arr[24].partition('@')
head25, sep25, tail25 = prueba_arr[25].partition('@')
head26, sep26, tail26 = prueba_arr[26].partition('@')
head27, sep27, tail27 = prueba_arr[27].partition('@')
head28, sep28, tail28 = prueba_arr[28].partition('@')
head29, sep29, tail29 = prueba_arr[29].partition('@')
head30, sep30, tail30 = prueba_arr[30].partition('@')
head31, sep31, tail31 = prueba_arr[31].partition('@')
head32, sep32, tail32 = prueba_arr[32].partition('@')
head33, sep33, tail33 = prueba_arr[33].partition('@')
head34, sep34, tail34 = prueba_arr[34].partition('@')
head35, sep35, tail35 = prueba_arr[35].partition('@')
head36, sep36, tail36 = prueba_arr[36].partition('@')
head37, sep37, tail37 = prueba_arr[37].partition('@')
head38, sep38, tail38 = prueba_arr[38].partition('@')
head39, sep39, tail39 = prueba_arr[39].partition('@')

a_0 = set(head0)
a_1 = set(head1)
a_2 = set(head2)
a_3 = set(head3)
a_4 = set(head4)
a_5 = set(head5)
a_6 = set(head6)
a_7 = set(head7)
a_8 = set(head8)
a_9 = set(head9)
a_10 = set(head10)
a_11 = set(head11)
a_12 = set(head12)
a_13 = set(head13)
a_14 = set(head14)
a_15 = set(head15)
a_16 = set(head16)
a_17 = set(head17)
a_18 = set(head18)
a_19 = set(head19)
a_20 = set(head20)
a_21 = set(head21)
a_22 = set(head22)
a_23 = set(head23)
a_24 = set(head24)
a_25 = set(head25)
a_26 = set(head26)
a_27 = set(head27)
a_28 = set(head28)
a_29 = set(head29)
a_30 = set(head30)
a_31 = set(head31)
a_32 = set(head32)
a_33 = set(head33)
a_34 = set(head34)
a_35 = set(head35)
a_36 = set(head36)
a_37 = set(head37)
a_38 = set(head38)
a_39 = set(head39)

t_0 = tail0
t_1 = tail1

lst = list(a_0 & a_1) #& a_2 & a_3 & a_4 & a_5 & a_6 & a_7 & a_8 & a_9 & a_10 & a_11 & a_12 & a_13 & a_14 & a_15 & a_16 & a_17 & a_18 & a_19 & a_20 & a_21 & a_22 & a_23 & a_24 & a_25 & a_26 & a_27 & a_28 & a_29 & a_30 & a_31 & a_32 & a_33 & a_34 & a_35 & a_36 & a_37 & a_38 & a_39)

print('Common letters: {}'.format(lst))
print("-------------------------------")

#Cantidad de valores antes de la "@"
for i in prueba_arr[0]:
    if i == "@":
        print(n)
        largo_before = str(n)
    else:
        n = n+1

for i in lst:
    if i == ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z"):
        if not "a-z" in regex_0:
            regex_0.append("a-z")  
    if i == ("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z"):
        if not "A-Z" in regex_0:
            regex_0.append("A-Z")
    if i == ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
        if not "0-9" in regex_0:
            regex_0.append("0-9")
    if i == ("-"):
        if not "-" in regex_0:
            regex_0.append("-")
    if i == ("_"):
        if not "_" in regex_0:
            regex_0.append("_")

m = 0
palabras_igual = []
palabras_diff = []
largo_after = (len(t_0)-1)
print("Largo after: ")
print(largo_after)
print(t_0[0])
while m < largo_after:
    if t_0[m] == t_1[m]:
        palabras_igual.append(t_0[m])
        m = m+1
    else:
        palabras_igual.append("x")
        palabras_diff.append(t_0[m])
        m = m+1

largo_mid = len(palabras_diff)
largo_mid_str = str(largo_mid)

s_0_arr = []
for i in palabras_igual:
    if i == "x":
        break
    else:
        s_0_arr.append(i)

largo_2 = len(s_0_arr)


regex_1 = []

#print("-------- for diff ---------")
for i in palabras_diff:
    if i == ("a" or "b"or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z"):
        if not "a-z" in regex_1:
            regex_1.append("a-z")
    if i == ("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z"):
        if not "A-Z" in regex_1:
            regex_1.append("A-Z")
    if i == ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
        if not "0-9" in regex_1:
            regex_1.append("0-9")
    if i == ("-"):
        if not "-" in regex_1:
            regex_1.append("-")
    if i == ("_"):
        if not "_" in regex_1:
            regex_1.append("_")

#print("---------- akdfh ---------")
s_1_arr = []
suma_largo = largo_2+largo_mid
for i in palabras_igual:
    if suma_largo < largo_after:
        i = palabras_igual[suma_largo]
        suma_largo = suma_largo+1
        s_1_arr.append(i)


regex_final = "[" + concatenar_lista(regex_0, "") + "]" + "{" + largo_before + "}" + "@" + concatenar_lista(s_0_arr,"") + "[" + concatenar_lista(regex_1, "") + "]" + "{" + largo_mid_str + "}" + concatenar_lista(s_1_arr, "")

print("---- regex 0 ----")
print(regex_0)
print("---- palabras igual ----")
print(palabras_igual)
print("---- palabras diff ----")
print(palabras_diff)
print("---- regex 1 ----")
print(regex_1)
print("---- regex final ----")
print(regex_final)
print("------------------------")