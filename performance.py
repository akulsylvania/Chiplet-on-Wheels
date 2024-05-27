F=1.5e9         #Hyperparameters
F_compute=2e9
F_GPU=1.5e9
F_IO=1.5e9
F_SoC=0.5e9
T_delay=60e-12  #60ps
bi=64
def performance_calculate():
  #Ri= Frequency
  #FLOPS_chiplet=F_compute
  #FLOPS_SoC=F_SoC
  Ri_chp=F_compute*2/1000  
               #in mega hertz  
  Ri_SoC= F*2/1000
  Ti_SoC= T_delay*F*5/1000     
#assume path IO->CORE->CACHE->CORE->IO
  c=1000
  Ti_chp=T_delay*(3*F_compute+2*F_IO)/c
  Latency_chiplet=(bi/Ri_chp)+Ti_chp
  Latency_SoC=(bi/Ri_SoC)+Ti_SoC
  lat_ratio=Latency_chiplet/Latency_SoC
  thrpt_ratio= F_compute*4/F*1            
  perfo_ratio=thrpt_ratio/lat_ratio
  print(perfo_ratio)
performance_calculate()