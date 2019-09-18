import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_med=[10,100,1*10**3,5*10**3,10*10**3,20*10**3,30*10**3,50*10**3,75*10**3,100*10**3,200*10**3,400*10**3,450*10**3,500*10**3,550*10**3,600*10**3,650*10**3,700*10**3,725*10**3,750*10**3,775*10**3,800*10**3,825*10**3,850*10**3,855*10**3,862.5*10**3,870*10**3,875*10**3,900*10**3,925*10**3,950*10**3,1*10**6,1.1*10**6,1.2*10**6,1.3*10**6,1.4*10**6,2*10**6,4*10**6,10*10**6]

z_med=[0.96,0.32,3.02,15.23,30.32,60.11,89.35,146.7,217.8,289.2,589.5,1368,1635,1954,2344,2829,3442,4217,4664,5147,5633,6089,6456,6672,6698,6715,6718,6705,6563,6282,5921,5146,3884,3068,2531,2159,1179,498.4,181.9]

fase_med=[70,72,86,87.76,87.78,87.58,87.38,87.04,86.55,86.01,83.40,76.44,74.05,71.16,67.60,63.06,57.10,49.05,43.99,37.96,30.99,22.93,13.96,4.38,2.45,-0.46,-3.40,-5.28,-14.43,-22.89,-30.30,-42.08,-56.67,-64.80,-69.82,-73.18,-81.50,-86.56,-87.87]

R_s_medida=[0.91,0.1,0.18,0.59,1.16,2.52,4.04,7.50,13.00,20.00,67.70,322,450,632,893,1281,1868,2763,3356,4060,4831,5608,6264,6653,6692,6715,6706,6677,6356,5787,5114,3820,2132,1306,874,626,175,29.60,6.70]

Q_medida=[0.0,3.0,16.6,25.8,26.0,23.8,22.1,19.5,16.7,14.4,8.6,4.1,3.5,2.9,2.4,2.0,1.5,1.2,1.0,0.8,0.6,0.4,0.2,0.1,0.0,0.0,0.1,0.1,0.3,0.4,0.6,0.9,1.5,2.1,2.7,3.3,6.7,16.8,27.3]

Ls_medida=[0.49,0.48,0.48,0.485,0.482,0.4781,0.4736,0.467,0.462,0.459,0.466,0.529,0.556,0.589,0.627,0.669,0.708,0.7243,0.7110,0.6713,0.5949,0.4718,0.3012,0.0940,0.0527,-0.100,-0.719,-0.1114,-0.2898,-0.4204,-0.500,-0.5488,-0.4697,-0.3682,-0.2908,-0.2349,-0.0928, -19.79*10**(-3), -2.893*10**(-3)]

R_s_calculada=[0.91,
0.10,
0.18,
0.59,
1.16,
2.52,
4.04,
7.50,
13.00,
20.00,
67.70,
322.00,
449.99,
631.98,
892.94,
1280.86,
1867.64,
2762.08,
3354.53,
4057.68,
4827.47,
5602.87,
6257.10,
6644.61,
6683.37,
6706.01,
6693.37,
6667.88,
6347.09,
5779.07,
5107.38,
3815.83,
2130.39,
1305.27,
873.61,
625.77,
174.96,
29.60,
6.70]

##Inductancia serie y resistencia serie vs frecuencia (Empírica y Simulada)##

fig1, ax3 = plt.subplots()

ax3.set_xlabel('Frecuencia [Hz]')
ax3.set_ylabel('$L_S$ [mH]')
ax3.plot(frecuencia_med, Ls_medida, "blue", linestyle='-', label='Inductancia serie(Empírico)')
#ax1.plot(data["f"], data["abs"], "red", linestyle='-', label='Módulo de la Transferencia (Simulado)')
ax3.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax3.tick_params(axis='y')


ax4 = ax3.twinx()  # instantiate a second axes that shares the same x-axis

ax4.set_ylabel('$R_S$ [\u03A9]')  # we already handled the x-label with ax1
ax4.plot(frecuencia_med, R_s_medida, "blue", linestyle=':', label='Resistencia serie(Empírica)')
ax4.plot(frecuencia_med, R_s_calculada, "red", linestyle=':', label='Resistencia serie (Simulada)')
ax4.tick_params(axis='y')

ax3.set_yticks([-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1])
ax4.set_yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
fig1.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle=':', label='Resistencia serie(Empírica)'),
    mpatches.Patch(color="blue", linestyle='-', label='Inductancia serie(Empírica)'),
    mpatches.Patch(color="red", linestyle=':', label='Resistencia serie(Simulada)'),

]
# agregamos leyenda
plt.legend(handles=patches)



#plt.ylabel('|H($)| [dB]')
#plt.xlabel('Frecuencia[Hz]')
#plt.plot(fmed, hmed, "blue", label='Módulo de la Transferencia (Empírico)')
#plt.plot(fmed, fase, "blue", linestyle=':', label='Fase')


# pongo una grilla
plt.minorticks_on()
ax3.xaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")

plt.show()
