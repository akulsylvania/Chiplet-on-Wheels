V=1.8         #voltage supplied(Vin)
Vth=0.47      #Vthreshold
C=15e-9       #(approximately)
F=1.5e9       #Frequency of operation of an SoC
T=10e-9       #T rise or fall in a gate
A=150e3       #Switching frequency
B=0.4         #Gain Constant in a transistor
I=15e-9       #leakage current per transistor
T_Density=100e6  #per mm2
F_compute=2e9
F_GPU=1.5e9
F_IO=1.5e9
F_SoC=0.5e9
A_compute=39.92                  
#size in mm2(CPU=39.92 I/O=9.87 SOC=94.9 GPU=23.4)
A_GPU=23.4
A_IO=9.87
A_SoC=94.9
V_compute=1.08
V_GPU=1.08
V_IO=0.9
V_SoC=0.9
def calculate_power():
     p_switch_SoC=A*C*F*V**2
     p_short_SoC=A*(B/12)*F*T*(V-2*Vth)**3
     p_leakage_per_transistor=I*V
     p_leakage_SoC= p_leakage_per_transistor
     *T_Density*858
     power_total_SoC=p_switch_SoC
     +p_short_SoC
     +p_leakage_SoC 
     p_switch_chiplet=
     A*C(F_compute*V_compute**2+
     F_GPU*V_GPU**2+F_IO*V_IO**2+F_SoC*V_SoC**2)
     p_short_chiplet=
     A*(B/12)*T*
     (F_compute*(V_compute-2*Vth)**3
     +F_GPU*(V_GPU-2*Vth)**3+F_IO*(V_IO-2*Vth)**3
     +F_SoC*(V_SoC-2*Vth)**3)
     p_leakage_per_transistor=I*V
     p_leakage_chiplet= 
     p_leakage_per_transistor*
     T_Density*(168.09)*4           
     #perchiplet combination
     power_total_chiplet=p_switch_chiplet+
     p_short_chiplet+p_leakage_chiplet
     print(power_total_chiplet/power_total_SoC)
calculate_power()