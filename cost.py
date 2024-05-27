def cost_compute_soc():
  x=858               #size in mm2
  Ndie= 3.14*150*150/x
  d0=0.004            # per mm2
  alpha= 3            #cluster parameter
  die_yield= (1+d0*x/alpha)**(-alpha)
  costwafer=16988/Ndie #cost of 300mm wafer
  costdie=costwafer/die_yield
  Ng=70695/40         #AND gate size=40mm2
  assembly_yield= (0.999**Ndie)*(0.999999**Ng)     
                    #Rent's rule
  total_cost= Ndie*costdie/assembly_yield
  return total_cost/Ndie
def cost_compute_chiplet():
  x=168.09          #size in mm2 
  Ndie=3.14*150*150/x
  d0=0.004          # per mm2
  alpha=3 
  die_yield= (1+d0*x/alpha)**(-alpha)
  costwafer=16988/Ndie #cost of 300mm wafer 
  costdie=costwafer/die_yield
  Ng=70695/40   
  assembly_yield= (0.999**Ndie)*(0.999999**Ng)     
                   #Rent's rule
  total_cost= Ndie*costdie/assembly_yield
  return 4*total_cost/Ndie