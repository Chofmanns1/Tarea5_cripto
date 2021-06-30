import imaplib
import re

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
n = 0
a = "movistar" #Aqui se debe cambiar el nombre que llevaran los txt 

# CH: noreply@steampowered.com ; info@twitter.com ; no-reply@new.papajohns.cl ; no-reply@duolingo.com 
# C.h: movistarfijo@emailmovistar.cl 

imap.login('', '')
imap.select('Inbox')
typ, data = imap.search(None,'FROM', 'movistarfijo@emailmovistar.cl')

file_datito = open(a+'_file_datito.txt', 'w')
file_received = open(a+'file_received.txt', 'w')
#file_penultimo = open(a+'_file_penultimo.txt', 'w')
file_UTC = open(a+'_file_UTC.txt', 'w')
file_from = open(a+'_file_from.txt', 'w')
file_substring = open(a+'_file_substring.txt', 'w')


for num in data[0].split():
    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print("\n--------------------------------- Message-ID ---------------------------------\n")
    print(datito)
    file_datito.write(datito+"\n")
    
    #Received
    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    received_arr = None
    r= data[0][1].decode()
    received_arr = r.split("Received:")
    largo_received = len(received_arr)
    print("--------------------------------- Received first ---------------------------------\n")
    primero = received_arr[largo_received-1]
    print(primero)
    file_received.write(primero+"\n")
    print("--------------------------------- Received penultimo ---------------------------------\n")
    penultimo = received_arr[2]
    if primero == penultimo:
        print(received_arr[largo_received-2])
        file_received.write(received_arr[largo_received-2]+"\n")
    else:
        print(penultimo)
        file_received.write(penultimo+"\n") 
    print("--------------------------------- Received todo ---------------------------------\n")
    print(r)
    #print("\n--------------------------------- Received arr ---------------------------------\n")
    #print(received_arr)

    #Date
    #typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    #dates= data[0][1].decode()
    print("--------------------------------- UTC (PDT) ---------------------------------\n")
    UTC_var = primero.split(" ")
    largo_UTC = len(UTC_var)
    UTC_print = UTC_var[largo_UTC-2]+UTC_var[largo_UTC-1]
    print(UTC_print)
    file_UTC.write(UTC_print)
    #print(dates)

    #From
    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    from_r= data[0][1].decode()
    form_var = from_r
    print("--------------------------------- From ---------------------------------\n")
    print(form_var)
    file_from.write(form_var)

    #Correo
    largo_correo = len(form_var)
    print("--------------------------------- Correo ---------------------------------\n")
    start = form_var.find("<") + len("<")
    end = form_var.find(">")
    substring = form_var[start:end]
    print(substring)
    file_substring.write(substring+"\n")

    #print(form_var[])
    #print(n)
    #n = 40 para los 40 correos
    n = n+1
    if n == 40:
        break

file_datito.close()
file_received.close()
#file_penultimo.close()
file_UTC.close()
file_from.close()
file_substring.close()
imap.close()