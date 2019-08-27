import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches

fmed=[10,500,1*10**3,1.2*10**3,1.8*10**3,3*10**3,5*10**3,8*10**3,10*10**3,14*10**3,16*10**3,18*10**3,20*10**3,22*10**3, 30*10**3, 50*10**3,80*10**3,0.12*10**6,0.15*10**6 ,0.18*10**6 ,0.20*10**6 ,0.25*10**6 ,0.30*10**6 ,0.50*10**6 ,1*10**6]
V=[9.94,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81,9.81]
Vr=[0.173,0.171,0.514,0.692,1.034,1.705,2.539,4.149,4.906,6.181,6.564,6.937,7.525,7.74,8.4127,9.282,9.518,9.631,9.689,9.716,9.737,9.766,9.758,9.777,9.79,]
Vc=[9.94,9.81,9.77,9.68,9.62,9.58,9.44,9.0,8.61,7.94,7.38,6.81,6.7,6.44,5.31,3.56,2.38,1.69,1.44,1.1,1.13,0.81,0.56,0.44,0.3]

fig, ax1 = plt.subplots()


ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Tensión [V]')
ax1.plot(fmed, V, "yellow", linestyle='-', label='Tensión de entrada')
ax1.plot(fmed, Vr, "green", linestyle='-', label='Tensión en la resistencia')
ax1.plot(fmed, Vc, "violet", linestyle='-', label='Tensión en el capacitor')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax1.tick_params(axis='y')

ax1.set_yticks([0,1,2,3,4,5,6,7,8,9,10])

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# agregamos patches
patches = [
    mpatches.Patch(color="yellow", linestyle='-', label='$V$'),
    mpatches.Patch(color="green", linestyle='-', label='$V_R$'),
    mpatches.Patch(color="violet", linestyle='-', label='$V_C$'),
]
# agregamos leyenda
plt.legend(handles=patches)



#plt.ylabel('|H($)| [dB]')
#plt.xlabel('Frecuencia[Hz]')
#plt.plot(fmed, hmed, "blue", label='Módulo de la Transferencia (Empírico)')
#plt.plot(fmed, fase, "blue", linestyle=':', label='Fase')


# pongo una grilla
plt.minorticks_on()
ax1.xaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")


plt.show()
