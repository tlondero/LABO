import matplotlib.pyplot as plt
import numpy

fmed=[1,2,3,5,10,100,1*10**3,10*10**3,100*10**3,1*10**6,2*10**6,4*10**6,6*10**6,10*10**6, 12*10**6, 13*10**6,14*10**6, 15*10**6]
vmed=[19,19.7,19.9,19.8,19.8,19.8,19.8,20,19.8,20.3,20.2,19.96,19.3,17.4,16.1,15.4,14.5,13.6]
vgen=20
transf=[]
gain=[]
for i in range(len(vmed)):
    transf.append(vmed[i]/vgen)
for i in range(len(transf)):
    gain.append(20*numpy.log10(transf[i]))
phase=[]
print(transf)
print(gain)
print(len(gain))
print(len(fmed))
plt.xscale("log")
plt.title("Comparacion de Modulos")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia modulo')
plt.plot(fmed,gain,"blue" , label="Bode de amplitud medido [dB]")
plt.show()
#plt.plot(fmed,phase,"red" , label="Bode de fase medido [grad]")
#plt.show()