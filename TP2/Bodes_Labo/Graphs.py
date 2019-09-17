import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1


def read_file_spice(filename):
    file = open(filename,'r')
    lines = file.readlines()

    data = dict()

    data["f"] =   []
    data["abs"] = []
    data["pha"] = []
    #print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != 'd':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '°':
#            if lines[i][pnt]>0:
                c3 += lines[i][pnt]
                pnt += 1


        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)
 #       if(c3<360):
#            c3=c3-360

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data


df = pd.read_csv('HIGHPASS.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()


plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase')
plt.legend()
plt.grid()
plt.show()



df = pd.read_csv('LABOPASABANDA.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()


plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase')
plt.legend()
plt.grid()
plt.show()



df = pd.read_csv('NOTCH.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase')
plt.legend()
plt.grid()
plt.show()




df = pd.read_csv('PASABAJOPS.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase')
plt.legend()
plt.grid()
plt.show()






