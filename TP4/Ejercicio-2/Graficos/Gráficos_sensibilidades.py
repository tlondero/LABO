import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches


frecuencia_medida=[1.00E+01,
1.50E+01,
2.00E+01,
2.50E+01,
3.00E+01,
3.50E+01,
4.00E+01,
4.50E+01,
5.00E+01,
5.50E+01,
6.00E+01,
6.50E+01,
7.00E+01,
7.50E+01,
8.00E+01,
8.50E+01,
9.00E+01,
9.50E+01,
1.00E+02,
1.05E+02,
1.10E+02,
1.15E+02,
1.20E+02,
1.25E+02,
1.30E+02,
1.35E+02,
1.40E+02,
1.45E+02,
1.50E+02,
1.55E+02,
1.60E+02,
1.65E+02,
1.70E+02,
1.75E+02,
1.80E+02,
1.85E+02,
1.90E+02,
1.95E+02,
2.00E+02]


Sensibilidad_16K_R_1=[0.0197411902,
0.0296117853,
0.0394823804,
0.0493529755,
0.0592235705,
0.0690941656,
0.0789647607,
0.0888353558,
0.0987059509,
0.1085765460,
0.1184471411,
0.1283177362,
0.1381883313,
0.1480589264,
0.1579295215,
0.1678001165,
0.1776707116,
0.1875413067,
0.1974119018,
0.2072824969,
0.2171530920,
0.2270236871,
0.2368942822,
0.2467648773,
0.2566354724,
0.2665060675,
0.2763766625,
0.2862472576,
0.2961178527,
0.3059884478,
0.3158590429,
0.3257296380,
0.3356002331,
0.3454708282,
0.3553414233,
0.3652120184,
0.3750826135,
0.3849532086,
0.3948238036
]

Sensibilidad_16K_R_3=[0.0197411902,
0.0296117853,
0.0394823804,
0.0493529755,
0.0592235705,
0.0690941656,
0.0789647607,
0.0888353558,
0.0987059509,
0.1085765460,
0.1184471411,
0.1283177362,
0.1381883313,
0.1480589264,
0.1579295215,
0.1678001165,
0.1776707116,
0.1875413067,
0.1974119018,
0.2072824969,
0.2171530920,
0.2270236871,
0.2368942822,
0.2467648773,
0.2566354724,
0.2665060675,
0.2763766625,
0.2862472576,
0.2961178527,
0.3059884478,
0.3158590429,
0.3257296380,
0.3356002331,
0.3454708282,
0.3553414233,
0.3652120184,
0.3750826135,
0.3849532086,
0.3948238036
]

Sensibilidad_K8_R_1=[0.001,
0.002,
0.002,
0.002,
0.003,
0.003,
0.004,
0.004,
0.004,
0.005,
0.005,
0.005,
0.006,
0.006,
0.006,
0.007,
0.007,
0.007,
0.007,
0.008,
0.008,
0.008,
0.008,
0.009,
0.009,
0.009,
0.009,
0.009,
0.010,
0.010,
0.010,
0.010,
0.010,
0.010,
0.011,
0.011,
0.011,
0.011,
0.011,
]

Sensibilidad_K8_R_3=[0.023,
0.024,
0.024,
0.025,
0.026,
0.026,
0.027,
0.027,
0.028,
0.028,
0.029,
0.029,
0.030,
0.031,
0.031,
0.032,
0.032,
0.033,
0.033,
0.034,
0.034,
0.035,
0.036,
0.036,
0.037,
0.037,
0.038,
0.038,
0.039,
0.039,
0.040,
0.041,
0.041,
0.042,
0.042,
0.043,
0.043,
0.044,
0.044
]

Sensibilidad_8K_R_1=[0.007,
0.010,
0.011,
0.012,
0.013,
0.014,
0.015,
0.015,
0.016,
0.016,
0.017,
0.017,
0.017,
0.018,
0.018,
0.018,
0.018,
0.018,
0.019,
0.019,
0.019,
0.019,
0.019,
0.019,
0.019,
0.019,
0.019,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020,
0.020
]

Sensibilidad_8K_R_3=[0.033,
0.039,
0.045,
0.050,
0.056,
0.061,
0.067,
0.072,
0.078,
0.084,
0.089,
0.095,
0.100,
0.106,
0.112,
0.117,
0.123,
0.128,
0.134,
0.139,
0.145,
0.151,
0.156,
0.162,
0.167,
0.173,
0.179,
0.184,
0.190,
0.195,
0.201,
0.207,
0.212,
0.218,
0.223,
0.229,
0.234,
0.240,
0.246
]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [KHz]')
ax1.set_ylabel('$\Delta V_D $[mV]')
ax1.plot(frecuencia_medida, Sensibilidad_16K_R_1, "blue", linestyle='-', label='Sensibilidad $R_1$')
ax1.plot(frecuencia_medida, Sensibilidad_16K_R_3, "yellow", linestyle=':', label='Sensibilidad $R_3$')
ax1.set_xticks([10,25,50,75,100,125,150,175,200])
#ax1.tick_params(axis='y')


#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

#ax2.set_ylabel('Fase [°]')  # we already handled the x-label with ax1
#ax2.plot(frecuencia_medida, fase_medida, "blue", linestyle=':', label='Fase(Empírica)')
#ax2.plot(data["f"], data["pha"], "red", linestyle=':', label='Fase (Simulada)')
#ax2.tick_params(axis='y')

#ax1.set_yticks([])
#ax2.set_yticks([90,75,60,45,30,15,0])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()


#plt.yscale("linear")

#plt.title('Diagrama de Bode - Filtro Pasa-bajos')

# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Sensibilidad $R_1$'),
    mpatches.Patch(color="yellow", linestyle=':', label='Sensibilidad $R_3$'),
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


###############################
fig2, ax2 = plt.subplots()

ax2.set_xlabel('Frecuencia [Hz]')
ax2.set_ylabel('$\Delta V_D $[V]')
ax2.plot(frecuencia_medida, Sensibilidad_K8_R_1, "blue", linestyle='-', label='Sensibilidad $R_1$')
ax2.plot(frecuencia_medida, Sensibilidad_K8_R_3, "red", linestyle='-', label='Sensibilidad $R_3$')
ax2.set_xticks([10E3,25E3,50E3,75E3,100E3,125E3,150E3,175E3,200E3])

fig2.tight_layout()  # otherwise the right y-label is slightly clipped


# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Sensibilidad R_1'),
    mpatches.Patch(color="red", linestyle='-', label='Sensibilidad R_3'),
]
# agregamos leyenda
plt.legend(handles=patches)



# pongo una grilla
plt.minorticks_on()
ax2.xaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")

plt.show()

###############################
fig3, ax3 = plt.subplots()

ax3.set_xlabel('Frecuencia [Hz]')
ax3.set_ylabel('$\Delta V_D $[V]')
ax3.plot(frecuencia_medida, Sensibilidad_8K_R_1, "blue", linestyle='-', label='Sensibilidad $R_1$')
ax3.plot(frecuencia_medida, Sensibilidad_8K_R_3, "red", linestyle='-', label='Sensibilidad $R_3$')
ax3.set_xticks([10E3,25E3,50E3,75E3,100E3,125E3,150E3,175E3,200E3])


fig3.tight_layout()  # otherwise the right y-label is slightly clipped


# agregamos patches
patches = [
    mpatches.Patch(color="blue", linestyle='-', label='Sensibilidad R_1'),
    mpatches.Patch(color="red", linestyle='-', label='Sensibilidad R_3'),
]
# agregamos leyenda
plt.legend(handles=patches)


# pongo una grilla
plt.minorticks_on()
ax3.xaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")

plt.show()