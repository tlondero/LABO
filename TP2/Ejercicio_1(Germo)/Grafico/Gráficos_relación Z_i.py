import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_med=[10,100,1*10**3,5*10**3,10*10**3,20*10**3,30*10**3,50*10**3,75*10**3,100*10**3,200*10**3,400*10**3,450*10**3,500*10**3,550*10**3,600*10**3,650*10**3,700*10**3,725*10**3,750*10**3,775*10**3,800*10**3,825*10**3,850*10**3,855*10**3,862.5*10**3,870*10**3,875*10**3,900*10**3,925*10**3,950*10**3,1*10**6,1.1*10**6,1.2*10**6,1.3*10**6,1.4*10**6,2*10**6,4*10**6,10*10**6]

C_p_medida=[2.2*10**(-9),2.27*10**(-9),2.26*10**(-9),2.25*10**(-9),2.24*10**(-9),2.23*10**(-9),2.23*10**(-9),2.22*10**(-9),2.21*10**(-9),2.21*10**(-9),2.19*10**(-9),2.176*10**(-9),2.174*10**(-9),2.17*10**(-9),2.117*10**(-9),2.166*10**(-9),2.164*10**(-9),2.16*10**(-9),2.16*10**(-9),2.16*10**(-9),2.157*10**(-9),2.157*10**(-9),2.203*10**(-9),2.296*10**(-9),2.43*10**(-9),2.63*10**(-9),2.76*10**(-9),2.91*10**(-9)]

fase_medida=[90,89.9,89.8,89.6,89.56,89.42,89.35,89.28,89.22,89.21,89.3,89.08,89.07,89.06,89.06,89.04,89.03,89.02,89.01,89,88.97,88.9,88.68,88.16,87.7,87.1,86.7,86.3]

R_p_medida=[0,0,0.05*10**(-6),0.49*10**(-6),0.0011*10**(-3),0.0028*10**(-3),0.0047*10**(-3),0.0088*10**(-3),0.0142*10**(-3),0.019*10**(-3),0.042*10**(-3),0.088*10**(-3),0.1*10**(-3),0.111*10**(-3),0.124*10**(-3),0.149*10**(-3),0.173*10**(-3),0.186*10**(-3),0.21*10**(-3),0.24*10**(-3),0.29*10**(-3),0.52*10**(-3),1.27*10**(-3),3.2*10**(-3),0.005,0.009,0.012,0.015]

D_medida=[0,0.01,0.0035,0.007,0.007,0.01,0.0113,0.0126,0.0136,0.0138,0.0152,0.0161,0.0162,0.0163,0.0165,0.0168,0.017,0.017,0.0173,0.0175,0.0179,0.0193,0.023,0.0317,0.039,0.05,0.057,0.065]

Z_medida=[0.14*10**(-6),1.43*10**(-6),14.22*10**(-6),70.73*10**(-6),0.1410*10**(-3),0.2808*10**(-3),0.42*10**(-3),0.6971*10**(-3),1.04*10**(-3),1.38*10**(-3),2.753*10**(-3),5.47*10**(-3),6.146*10**(-3),6.821*10**(-3),7.4*10**(-3),8.84*10**(-3),10.2*10**(-3),10.87*10**(-3),12.22*10**(-3),13.57*10**(-3),16.27*10**(-3),27.12*10**(-3),55.38*10**(-3),101.05*10**(-3),0.1308,0.182,0.208,0.239]

Zmedida=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Zmedida1pf=[0.980,
1.255,
1.058,
1.039,
1.037,
1.041,
1.044,
1.051,
1.058,
1.067,
1.108,
1.202,
1.230,
1.261,
1.292,
1.325,
1.356,
1.375,
1.373,
1.357,
1.322,
1.260,
1.165,
1.033,
1.004,
0.890,
0.407,
0.875,
0.700,
0.522,
0.355,
0.072,
0.289,
0.485,
0.601,
0.676,
0.851,
0.950,
0.973
]

Zmedida1nf=[0.980,
1.255,
1.058,
1.039,
1.035,
1.033,
1.026,
1.003,
0.955,
0.894,
0.609,
0.234,
0.184,
0.144,
0.113,
0.088,
0.068,
0.052,
0.046,
0.040,
0.036,
0.032,
0.029,
0.027,
0.027,
0.027,
0.026,
0.026,
0.026,
0.026,
0.026,
0.022,
0.043,
0.048,
0.053,
0.057,
0.073,
0.087,
0.096]

Zmedida1ff=[0.980,
1.255,
1.058,
1.039,
1.037,
1.041,
1.044,
1.051,
1.058,
1.067,
1.108,
1.207,
1.237,
1.270,
1.305,
1.344,
1.383,
1.411,
1.414,
1.403,
1.372,
1.310,
1.212,
1.072,
1.041,
0.919,
0.413,
0.904,
0.719,
0.532,
0.360,
0.072,
0.287,
0.479,
0.593,
0.667,
0.841,
0.939,
0.962
]

##Impedancia y fase vs frecuencia (Empírica y Simulada)##
fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Ratio Zs')
ax1.plot(frecuencia_med, Zmedida, "blue", linestyle='-', label='Impedancia empírica')
ax1.plot(frecuencia_med, Zmedida1pf, "red", linestyle='-', label='Impedancia con 1pf')
ax1.plot(frecuencia_med, Zmedida1nf, "yellow", linestyle='-', label='Impedancia con 1nf ')
ax1.plot(frecuencia_med, Zmedida1ff, "brown", linestyle='-', label='Impedancia con 1ff')

#ax1.plot(data["f"], data["abs"], "red", linestyle='-', label='Módulo de la Transferencia (Simulado)')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
#ax1.set_yscale("log", basey=10,subsy=[1,0.1,0.01])
ax1.tick_params(axis='y')



#ax1.set_yticks([0.001,0.01,0.025,0.05,0.075,0.1])

ax2 = ax1.twinx()  # agrego otro eje para hardcodear el error de la doble impresión
ax2.set_yticks([])

fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Referencia'),
    mpatches.Patch(color="red", linestyle='-', label='Impedancia usando capacitor de 1pF'),
    mpatches.Patch(color="yellow", linestyle='-', label='Impedancia usando capacitor de 1nF'),
    mpatches.Patch(color="brown", linestyle='-', label='Impedancia usando capacitor de 1fF'),
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


