import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_med=[10,100,1*10**3,5*10**3,10*10**3,20*10**3,30*10**3,50*10**3,75*10**3,100*10**3,200*10**3,400*10**3,450*10**3,500*10**3,550*10**3,600*10**3,650*10**3,700*10**3,725*10**3,750*10**3,775*10**3,800*10**3,825*10**3,850*10**3,855*10**3,862.5*10**3,870*10**3,875*10**3,900*10**3,925*10**3,950*10**3,1*10**6,1.1*10**6,1.2*10**6,1.3*10**6,1.4*10**6,2*10**6,4*10**6,10*10**6]

z_med=[0.96,0.32,3.02,15.23,30.32,60.11,89.35,146.7,217.8,289.2,589.5,1368,1635,1954,2344,2829,3442,4217,4664,5147,5633,6089,6456,6672,6698,6715,6718,6705,6563,6282,5921,5146,3884,3068,2531,2159,1179,498.4,181.9]

fase_med=[70,72,86,87.76,87.78,87.58,87.38,87.04,86.55,86.01,83.40,76.44,74.05,71.16,67.60,63.06,57.10,49.05,43.99,37.96,30.99,22.93,13.96,4.38,2.45,-0.46,-3.40,-5.28,-14.43,-22.89,-30.30,-42.08,-56.67,-64.80,-69.82,-73.18,-81.50,-86.56,-87.87]

R_s_medida=[0.91,0.1,0.18,0.59,1.16,2.52,4.04,7.50,13.00,20.00,67.70,322,450,632,893,1281,1868,2763,3356,4060,4831,5608,6264,6653,6692,6715,6706,6677,6356,5787,5114,3820,2132,1306,874,626,175,29.60,6.70]

Q_medida=[0.0,3.0,16.6,25.8,26.0,23.8,22.1,19.5,16.7,14.4,8.6,4.1,3.5,2.9,2.4,2.0,1.5,1.2,1.0,0.8,0.6,0.4,0.2,0.1,0.0,0.0,0.1,0.1,0.3,0.4,0.6,0.9,1.5,2.1,2.7,3.3,6.7,16.8,27.3]

Q_calculada=[
72.937722429,
71.65588319,
86.58446161,
87.78248626,
87.8064765,
87.59816398,
87.40879202,
87.07342748,
86.57951759,
86.03483456,
83.40188116,
76.33934365,
73.95365855,
71.02939204,
67.42614086,
62.79916836,
56.70446318,
48.37728954,
43.11897583,
36.84465075,
29.61960355,
21.3269897,
12.15101576,
2.285760113,
0.36671649,
-6.704197521,
-32.5195809,
-7.350245954,
-16.53550015,
-24.8441393,
-32.04782808,
-43.47709715,
-57.56903965,
-65.38236777,
-70.21581168,
-73.46670081,
-81.59345044,
-86.63738222,
-87.91347479]

Ls_medida=[0.49*10**(-3),0.480*10**(-3),0.480*10**(-3),0.485*10**(-3),0.482*10**(-3),0.4781*10**(-3),0.4736*10**(-3),0.467*10**(-3),0.4616*10**(-3),0.4593*10**(-3),0.4661*10**(-3),0.529*10**(-3),0.556*10**(-3),0.589*10**(-3),0.627*10**(-3),0.669*10**(-3),0.708*10**(-3),0.7243*10**(-3),0.7110*10**(-3),0.6713*10**(-3),0.5949*10**(-3),0.4718*10**(-3),0.3012*10**(-3),0.0940*10**(-3),0.0527*10**(-3),-0.100*10**(-3),-0.719*10**(-3),-0.1114*10**(-3),-0.2898*10**(-3),-0.4204*10**(-3),-0.500*10**(-3),-0.5488*10**(-3),-0.4697*10**(-3),-0.3682*10**(-3),-0.2908*10**(-3),-0.2349*10**(-3),-0.0928*10**(-3), -19.79*10**(-6), -2.893*10**(-6)]

Z_cal=[0.94,
0.40,
3.20,
15.83,
31.44,
62.60,
93.31,
154.20,
230.50,
308.53,
652.88,
1644.70,
2010.56,
2463.19,
3027.74,
3749.32,
4668.77,
5796.97,
6402.48,
6985.64,
7447.59,
7671.81,
7520.26,
6891.68,
6723.19,
5973.25,
2734.19,
5868.87,
4594.66,
3279.92,
2102.76,
370.92,
1122.98,
1486.64,
1519.93,
1458.77,
1003.66,
473.34,
177.02
]

##Impedancia y fase vs frecuencia (Empírica y Simulada)##
fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('|Z| [\u03A9]')
ax1.plot(frecuencia_med, z_med, "blue", linestyle='-', label='Módulo de la Impedancia (Empírico)')
ax1.plot(frecuencia_med, Z_cal, "red", linestyle='-', label='Módulo de la Transferencia (Simulado)')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax1.tick_params(axis='y')


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('Fase [°]')  # we already handled the x-label with ax1
ax2.plot(frecuencia_med, fase_med, "blue", linestyle=':', label='Fase(Empírica)')
ax2.plot(frecuencia_med, Q_calculada, "red", linestyle=':', label='Fase (Simulada)')
ax2.tick_params(axis='y')

ax1.set_yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
ax2.set_yticks([-90,-75,-60,-45,-30,-15,0,15,30,45,60,75,90])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle=':', label='Fase (Medida)'),
    mpatches.Patch(color="blue", linestyle='-', label='Módulo de la Impedancia (Medido)'),
    mpatches.Patch(color="red", linestyle=':', label='Fase (Simulada)'),
    mpatches.Patch(color="red", linestyle='-', label='Módulo de la Impedancia (Simulado)'),
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

##
##Inductancia serie y resistencia serie vs frecuencia (Empírica y Simulada)##

fig1, ax3 = plt.subplots()

ax3.set_xlabel('Frecuencia [Hz]')
ax3.set_ylabel('$L_S$ [H]')
ax3.plot(frecuencia_med, Ls_medida, "blue", linestyle='-', label='Inductancia serie(Empírico)')
#ax1.plot(data["f"], data["abs"], "red", linestyle='-', label='Módulo de la Transferencia (Simulado)')
ax3.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax3.tick_params(axis='y')


ax4 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax4.set_ylabel('Resistencia serie [\u03A9]')  # we already handled the x-label with ax1
ax4.plot(frecuencia_med, R_s_medida, "blue", linestyle=':', label='Resistencia serie(Empírica)')
#ax2.plot(data["f"], data["pha"], "red", linestyle=':', label='Fase (Simulada)')
ax4.tick_params(axis='y')

ax3.set_yticks([-1*10**(-3),-0.75*10**(-3),-0.5*10**(-3),-0.25*10**(-3),0*10**(-3),0.25*10**(-3),0.5*10**(-3),0.75*10**(-3),1*10**(-3)])
ax4.set_yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
fig1.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle=':', label='Fase (Medida)'),
    mpatches.Patch(color="blue", linestyle='-', label='Módulo de la Transferencia (Medido)'),
    mpatches.Patch(color="red", linestyle=':', label='Fase (Simulada)'),
    mpatches.Patch(color="red", linestyle='-', label='Módulo de la Transferencia (Simulada)'),
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
