import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches

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
    file = open(filename, 'r')
    lines = file.readlines()

    data = dict()

    data["f"] = []
    data["abs"] = []
    data["pha"] = []
    print(lines)

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
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data
data = read_file_spice("Ejercicio 1 - Pasabajo.txt")


fmed=[10,500,1*10**3,1.2*10**3,1.8*10**3,3*10**3,5*10**3,8*10**3,10*10**3,14*10**3,16*10**3,18*10**3,20*10**3,22*10**3, 30*10**3, 50*10**3,80*10**3,0.12*10**6,0.15*10**6 ,0.18*10**6 ,0.20*10**6 ,0.25*10**6 ,0.30*10**6 ,0.50*10**6 ,1*10**6]
hmed=[0.00, 0.00,-0.04,-0.12, -0.17, -0.21,-0.33, -0.69, -1.13, -1.84, -2.47, -3.17, -3.31, -3.66,-5.33, -8.80, -12.30, -15.28, -16.67, -18.32, -18.77, -21.66, -24.87, -26.96, -30.29]
fase=[-1,-1,-3,-4,-6,-10,-15,-25,-30,-39,-42,-45,-50,-52,-59,-71,-76,-79,-81,-82,-83,-83,-84,-85,-86]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('|H($)| [dB]')
ax1.plot(fmed, hmed, "blue", linestyle='-', label='Módulo de la Transferencia (Empírico)')
ax1.plot(data["f"], data["abs"], "red", linestyle='-', label='Módulo de la Transferencia (Simulado)')
ax1.set_xscale("log", basex=10,subsx=[1,2,3,4,5,6])
ax1.tick_params(axis='y')


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('Fase [°]')  # we already handled the x-label with ax1
ax2.plot(fmed, fase, "blue", linestyle=':', label='Fase(Empírica)')
ax2.plot(data["f"], data["pha"], "red", linestyle=':', label='Fase (Simulada)')
ax2.tick_params(axis='y')

ax1.set_yticks([5,0,-5,-10,-15,-20,-25,-30])
ax2.set_yticks([-90,-75,-60,-45,-30,-15,0])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
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
ax1.xaxis.grid(True)
plt.grid(which='major', axis='both', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.1, color='black')
plt.grid(True, which="both")

plt.show()
