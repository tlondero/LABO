import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_med=[10,100,1*10**3,5*10**3,10*10**3,20*10**3,30*10**3,50*10**3,75*10**3,100*10**3,200*10**3,400*10**3,450*10**3,500*10**3,550*10**3,600*10**3,650*10**3,700*10**3,725*10**3,750*10**3,775*10**3,800*10**3,825*10**3,850*10**3,855*10**3,862.5*10**3,870*10**3,875*10**3,900*10**3,925*10**3,950*10**3,1*10**6,1.1*10**6,1.2*10**6,1.3*10**6,1.4*10**6,2*10**6,4*10**6,10*10**6]

z_med=[0.96,0.32,3.02,15.23,30.32,60.11,89.35,146.7,217.8,289.2,589.5,1368,1635,1954,2344,2829,3442,4217,4664,5147,5633,6089,6456,6672,6698,6715,6718,6705,6563,6282,5921,5146,3884,3068,2531,2159,1179,498.4,181.9]

fase_med=[70,72,86,87.76,87.78,87.58,87.38,87.04,86.55,86.01,83.40,76.44,74.05,71.16,67.60,63.06,57.10,49.05,43.99,37.96,30.99,22.93,13.96,4.38,2.45,-0.46,-3.40,-5.28,-14.43,-22.89,-30.30,-42.08,-56.67,-64.80,-69.82,-73.18,-81.50,-86.56,-87.87]

R_s_medida=[0.91,0.1,0.18,0.59,1.16,2.52,4.04,7.50,13.00,20.00,67.70,322,450,632,893,1281,1868,2763,3356,4060,4831,5608,6264,6653,6692,6715,6706,6677,6356,5787,5114,3820,2132,1306,874,626,175,29.60,6.70]

Q_medida=[0.0,3.0,16.6,25.8,26.0,23.8,22.1,19.5,16.7,14.4,8.6,4.1,3.5,2.9,2.4,2.0,1.5,1.2,1.0,0.8,0.6,0.4,0.2,0.1,0.0,0.0,0.1,0.1,0.3,0.4,0.6,0.9,1.5,2.1,2.7,3.3,6.7,16.8,27.3]

Q_calculada=[0.03,
3.02,
16.76,
25.82,
26.11,
23.84,
22.10,
19.56,
16.73,
14.43,
8.65,
4.13,
3.49,
2.93,
2.43,
1.97,
1.55,
1.15,
0.97,
0.78,
0.60,
0.42,
0.25,
0.08,
0.04,
0.08,
0.59,
0.09,
0.26,
0.42,
0.58,
0.90,
1.52,
2.13,
2.72,
3.30,
6.66,
16.80,
27.13]

Ls_medida=[0.49*10**(-3),0.480*10**(-3),0.480*10**(-3),0.485*10**(-3),0.482*10**(-3),0.4781*10**(-3),0.4736*10**(-3),0.467*10**(-3),0.4616*10**(-3),0.4593*10**(-3),0.4661*10**(-3),0.529*10**(-3),0.556*10**(-3),0.589*10**(-3),0.627*10**(-3),0.669*10**(-3),0.708*10**(-3),0.7243*10**(-3),0.7110*10**(-3),0.6713*10**(-3),0.5949*10**(-3),0.4718*10**(-3),0.3012*10**(-3),0.0940*10**(-3),0.0527*10**(-3),-0.100*10**(-3),-0.719*10**(-3),-0.1114*10**(-3),-0.2898*10**(-3),-0.4204*10**(-3),-0.500*10**(-3),-0.5488*10**(-3),-0.4697*10**(-3),-0.3682*10**(-3),-0.2908*10**(-3),-0.2349*10**(-3),-0.0928*10**(-3), -19.79*10**(-6), -2.893*10**(-6)]


##Impedancia y fase vs frecuencia (Empírica y Simulada)##
fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Factor de calidad (Q)')
ax1.plot(frecuencia_med, Q_medida, "blue", linestyle='-', label='Factor de calidad(Empírico)')
ax1.plot(frecuencia_med, Q_calculada, "red", linestyle=':', label='Factor de calidad(Calculado)')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax1.tick_params(axis='y')


ax1.set_yticks([0,5,10,15,20,25,30])
fig.tight_layout()  # otherwise the right y-label is slightly clipped

ax2 = ax1.twinx()  # agrego otro eje para hardcodear el error de la doble impresión
ax2.set_yticks([])





#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Factor de calidad (Medido)'),
    mpatches.Patch(color="red", linestyle='-', label='Factor de calidad (Simulado)'),
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


