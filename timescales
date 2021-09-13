def timescales(dens_contrast, r_cl, wind_vel, rho_cloud, average_Temp, n_cloud):
    
    'Compute the time-scales'
    
    #define all the paramenters in c.g.s units
    
    G          = 6.67259*10**(-8)
    Lambda     = 2.158000e-24
    k_b        = 1.38*10**(-16)
    sec_to_Myr = 3.17098*10**(-14)
    
    # CLOUD CRUSHING TIME
    
    t_cc = 2*math.sqrt(dens_contrast)*r_cl/wind_vel
    print('t_cc = ', t_cc*sec_to_Myr, 'Myr \n')
    
    # WIND PASSAGE TIME
    
    t_ws = 2*r_cl/wind_vel
    print('t_ws = ', t_ws*sec_to_Myr, 'Myr \n')
    
    # K-H INSTABILITY GROWTH TIME
    
    t_KH = t_cc/(2*math.pi)
    print('t_KH = ', t_KH*sec_to_Myr, 'Myr \n')
    
    # R-T INSTABILITY GROWTH TIME
    
    t_RT = t_cc/math.sqrt(0.8*math.pi)
    print('t_RT = ', t_RT*sec_to_Myr, 'Myr \n')
    
    # FREE-FALL TIME
    
    t_ff = math.sqrt((3*math.pi)/(32*G*rho_cloud))
    print('t_ff = ', t_ff*sec_to_Myr, 'Myr \n')
    
    # COOLING TIME
     
    t_cool  = (3*k_b*average_Temp)/(2*n_cloud*Lambda)
    print('t_cool = ', t_cool*sec_to_Myr, 'Myr \n')
