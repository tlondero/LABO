import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

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

scriptfile = os.path.dirname(__file__)

########################HIGHPASS
###CSV
df = pd.read_csv(scriptfile +  '/CSV/HIGHPASS.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])
###SPICE
data = read_file_spice(scriptfile + '/Spice/HP/HP.txt')
###TEORICO$$$$$$############################################################
L = 500*10**(-6)
C = 33*10**(-9)
rc = 0
R = 82

fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc

Hcalc = (((s*np.sqrt(L*C))**2)/np.sqrt(((s*R*C)**2+(1-(s*np.sqrt(L*C))**2)**2)))
Hcalc = 20*np.log10(Hcalc)

Hphcalc=np.rad2deg(np.arctan(-rc/(s*L)))-np.rad2deg(np.arctan(s*(rc+R)*C/(-(s**2)*L*C+1)))
for x in range(len(Hphcalc)):
    if(Hphcalc[x] <0):
        Hphcalc[x]=Hphcalc[x]+180

####################################################################################

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud Medido')
plt.plot(data["f"],data["abs"],'r-',label = 'Amplitud Simulado')
plt.plot(fc,Hcalc,'g-',label = 'Amplitud Calculado')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()


plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase Medido')
plt.plot(data["f"],data["pha"],'r-.',label = 'Fase Simulado')
plt.plot(fc,Hphcalc,'g-.',label = 'Fase Calculado')
plt.legend()
plt.grid()
plt.show()

########################BANDPASS

#####CSV
df = pd.read_csv(scriptfile +  '/CSV/LABOPASABANDA.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])
#####SPICE
data = read_file_spice(scriptfile + '/Spice/BP/BP.txt')
###TEORICO$$$$$$############################################################
fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc
Hcalc = (s*R*C/np.sqrt(((s*R*C)**2+(1-((s*np.sqrt(L*C))**2))**2)))
Hcalc = 20*np.log10(Hcalc)

Hphcalc = [np.arctan(-tt*2*np.pi*np.sqrt(L*C))*180/(np.pi) for tt in fc]
Hphcalc =np.asarray(Hphcalc)*2+90

####################################################################################


plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud Medido')
plt.plot(data["f"],data["abs"],'r-',label = 'Amplitud Simulado')
plt.plot(fc,Hcalc,'g-',label = 'Amplitud Calculado')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()


plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase Medido')
plt.plot(data["f"],data["pha"],'r-.',label = 'Fase Simulado')
plt.plot(data["f"],data["pha"],'g-.',label = 'Fase Calculado')
plt.legend()
plt.grid()
plt.show()

########################NOTCH
####CSV
df = pd.read_csv(scriptfile +  '/CSV/NOTCH.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

###SPICE
data = read_file_spice(scriptfile + '/Spice/BR/BR.txt')

###TEORICO$$$$$$############################################################
L = 500*10**(-6)
C = 33*10**(-9)
rc = 0
R = 82

fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc
Hcalc = (np.sqrt(((1-(s*np.sqrt(L*C))**2)**2+(s*C*rc)**2)/((s*C*(rc+R))**2+(1-(s*np.sqrt(L*C))**2)**2)))
Hcalc = 20*np.log10(Hcalc)

Hphcalc=np.rad2deg(np.arctan(-rc/(s*L)))-np.rad2deg(np.arctan(s*(rc+R)*C/(-(s**2)*L*C+1)))

####################################################################################

plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud Medido')
plt.plot(data["f"],data["abs"],'r-',label = 'Amplitud Simulado')
plt.plot(fc,Hcalc,'g-',label = 'Amplitud Calculado')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase Medido')
plt.plot(data["f"],data["pha"],'r-.',label = 'Fase Simulado')
plt.plot(fc,Hphcalc,'g-.',label = 'Fase Calculado')
plt.legend()
plt.grid()
plt.show()


########################LOWPASS

###CSV
df = pd.read_csv(scriptfile +  '/CSV/PASABAJOPS.csv',sep = ';')
H = np.asarray(df['MAG'])
f = np.asarray(df['frequency'])
ph = np.asarray(df['PHA'])

###SPICE
data = read_file_spice(scriptfile + '/Spice/LP/LP.txt')

###TEORICO$$$$$$############################################################
fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc
Hcalc = (1/np.sqrt(((s*R*C)**2+(1-((s*np.sqrt(L*C))**2))**2)))
Hcalc = 20*np.log10(Hcalc)

Hphcalc = [-np.arctan(-tt*2*np.pi*R*C/(1-(tt*2*np.pi*np.sqrt(L*C))**2))*180/(np.pi) for tt in fc]
Hphcalc = np.asarray(Hphcalc) *-1
for x in range(len(Hphcalc)):
    if(x >3908):
        Hphcalc[x]=Hphcalc[x]-180
####################################################################################


plt.xscale('log')
plt.plot(f,H,'b-',label = 'Amplitud Medido')
plt.plot(data["f"],data["abs"],'r-',label = 'Amplitud Simulado')
plt.plot(fc,Hcalc,'g-',label = 'Amplitud Calculado')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'b-.',label = 'Fase Medido')
plt.plot(data["f"],data["pha"],'r-.',label = 'Fase Simulado')
plt.plot(fc,Hphcalc,'g-.',label = 'Fase Calculado')

plt.legend()
plt.grid()
plt.show()





