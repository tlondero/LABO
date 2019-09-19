import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_medida=[10,100,1*10**3,5*10**3,10*10**3,20*10**3,30*10**3,50*10**3,75*10**3,100*10**3,200*10**3,400*10**3,450*10**3,500*10**3,550*10**3,650*10**3,750*10**3,800*10**3,900*10**3,1*10**6,1.2*10**6,2*10**6,4*10**6,7*10**6,9*10**6,11*10**6,12*10**6,13*10**6]

C_p_medida=[2.2*10**(-9),2.27*10**(-9),2.26*10**(-9),2.25*10**(-9),2.24*10**(-9),2.23*10**(-9),2.23*10**(-9),2.22*10**(-9),2.21*10**(-9),2.21*10**(-9),2.19*10**(-9),2.176*10**(-9),2.174*10**(-9),2.17*10**(-9),2.117*10**(-9),2.166*10**(-9),2.164*10**(-9),2.16*10**(-9),2.16*10**(-9),2.16*10**(-9),2.157*10**(-9),2.157*10**(-9),2.203*10**(-9),2.296*10**(-9),2.43*10**(-9),2.63*10**(-9),2.76*10**(-9),2.91*10**(-9)]

fase_medida=[90,89.9,89.8,89.6,89.56,89.42,89.35,89.28,89.22,89.21,89.3,89.08,89.07,89.06,89.06,89.04,89.03,89.02,89.01,89,88.97,88.9,88.68,88.16,87.7,87.1,86.7,86.3]

R_p_medida=[0,0,0.05*10**(-6),0.49*10**(-6),0.0011*10**(-3),0.0028*10**(-3),0.0047*10**(-3),0.0088*10**(-3),0.0142*10**(-3),0.019*10**(-3),0.042*10**(-3),0.088*10**(-3),0.1*10**(-3),0.111*10**(-3),0.124*10**(-3),0.149*10**(-3),0.173*10**(-3),0.186*10**(-3),0.21*10**(-3),0.24*10**(-3),0.29*10**(-3),0.52*10**(-3),1.27*10**(-3),3.2*10**(-3),0.005,0.009,0.012,0.015]

D_medida=[0,0.01,0.0035,0.007,0.007,0.01,0.0113,0.0126,0.0136,0.0138,0.0152,0.0161,0.0162,0.0163,0.0165,0.0168,0.017,0.017,0.0173,0.0175,0.0179,0.0193,0.023,0.0317,0.039,0.05,0.057,0.065]

Z_medida=[0.14*10**(-6),1.43*10**(-6),14.22*10**(-6),70.73*10**(-6),0.1410*10**(-3),0.2808*10**(-3),0.42*10**(-3),0.6971*10**(-3),1.04*10**(-3),1.38*10**(-3),2.753*10**(-3),5.47*10**(-3),6.146*10**(-3),6.821*10**(-3),7.4*10**(-3),8.84*10**(-3),10.2*10**(-3),10.87*10**(-3),12.22*10**(-3),13.57*10**(-3),16.27*10**(-3),27.12*10**(-3),55.38*10**(-3),101.05*10**(-3),0.1308,0.182,0.208,0.239]

D_calc=[0.0072,
0.0071,
0.0035,
0.0069,
0.0078,
0.0100,
0.0112,
0.0126,
0.0136,
0.0137,
0.0153,
0.0161,
0.0163,
0.0163,
0.0169,
0.0168,
0.0170,
0.0171,
0.0172,
0.0177,
0.0178,
0.0192,
0.0229,
0.0317,
0.0364,
0.0495,
0.0577,
0.0631
]


##Impedancia y fase vs frecuencia (Empírica y Simulada)##
fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Factor de pérdida (D)')
ax1.plot(frecuencia_medida, D_medida, "blue", linestyle='-', label='Factor de pérdida(Empírico)')
ax1.plot(frecuencia_medida, D_calc, "red", linestyle=':', label='Factor de pérdida (Simulado)')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
#ax1.set_yscale("log", basey=10,subsy=[1,0.1,0.01])
ax1.tick_params(axis='y')



ax1.set_yticks([0.001,0.01,0.025,0.05,0.075,0.1])

ax2 = ax1.twinx()  # agrego otro eje para hardcodear el error de la doble impresión
ax2.set_yticks([])

fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Factor de pérdida (Medido)'),
    mpatches.Patch(color="red", linestyle=':', label='Factor de pérdida (Simulado)'),
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
ax1.yaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")

plt.show()


