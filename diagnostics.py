def diagnostics_cgs(rho, vx1, vx2, vx3, Bx1, Bx2, Bx3, prs, tr1, name_file, input_directory, v_0, L_0, rho_0, mu, gamma):
  
  #Compute all the diagnostics 
    
    k_b = 1.38*10**(-16)
    m_p = 1.67*10**(-24)
    
    #rho, vx1, vx2, vx3, Bx1, Bx2, Bx3, prs, tr1 = pload_vtk(name_file, input_directory)
    
    num_cells = len(rho)

    ## DENFINE THE CLOUD TRACE
    
    tr1_3d      = np.reshape(tr1, (96,192,96))
    tr_cloud_3d = np.where(tr1_3d > 0)
    
    ## DENSITY FIELD & MASS
    
    rho_3d        = np.reshape(rho*rho_0, (96,192,96))
    rho_cells     = rho*rho_0*tr1
    rho_cloud     = rho[np.where(tr1>0)]*rho_0*tr1[np.where(tr1>0)]
    rho_cloud_1   = rho[np.where(tr1>0)]*rho_0
    rho_wind      = rho[np.where(tr1<1)]*(1-tr1[np.where(tr1<1)])*rho_0
    n_cloud       = rho_cloud/(mu*m_p)
    
    mass_cell      = rho*rho_0*(L_0/8)**3
    mass_cloud     = rho_cells[np.where(tr1>0)]*(L_0/8)**3
    mass_cloud_3d  = rho_cloud*(L_0/8)**3
    mass_wind      = rho_wind*(L_0/8)**3
    mass_cloud_tot = np.sum(mass_cloud)
    mass_tot       = np.sum(mass_cell)
    
    average_rho_cl = np.average(rho_cloud, weights = mass_cloud)
    average_rho_w  = np.average(rho_wind, weights = mass_wind)  
    dens_contrast  = average_rho_cl/average_rho_w
    
    ## PRESSURE
    
    prs_3d       = np.reshape(prs*rho_0*v_0**2, (96,192,96))
    prs_cloud    = prs[np.where(tr1>0)]*rho_0*(v_0**2)*tr1[np.where(tr1>0)]
    prs_cloud_1  = prs[np.where(tr1>0)]*rho_0*(v_0**2)
    prs_wind     = prs[np.where(tr1<1)]*(1-tr1[np.where(tr1<1)])*rho_0*(v_0**2)
        
    ## VELOCITY & MACH
    
    vel           = np.sqrt((vx1)**2 + (vx2)**2 + (vx3)**2)*v_0    
    mean_vel      = np.mean(vel)
    wind_vel      = vel[np.where(tr1<1)]*(1-tr1[np.where(tr1<1)])
    cloud_vel     = vel[np.where(tr1>0)]*tr1[np.where(tr1>0)]
    mean_wind_vel = np.mean(wind_vel)
    
    wind_cs       = np.sqrt(gamma*(1-tr1[np.where(tr1<1)])*prs_wind/rho_wind)
    wind_mach     = wind_vel/wind_cs
    
    mean_wind_mach = np.average(wind_mach)
        
    ## TEMPERATURE
    
    Temp         = (prs_cloud*m_p*mu)/(rho_cloud_1*k_b) #cloud temperature 
    average_Temp = np.average(Temp)
    log_Temp     = np.log10(Temp/average_Temp)
    
    ## CENTRE OF MASS
    
    x = np.arange(-6+0.125/2, 6+0.125/2, 0.125)
    y = np.arange(-2+0.125/2, 22+0.125/2, 0.125)
    z = np.arange(-6+0.125/2, 6+0.125/2, 0.125)
    
    coord_comb = cartesian((x,y,z))
    CM         = np.average(coord_comb[np.where(tr1>0)], axis=0, weights=rho_cloud)
    CM_rms     = np.average((coord_comb[np.where(tr1>0)])**2, axis=0, weights=rho_cloud)

    ## CLOUD EXTENSION
    
    eff_radius_x     = np.sqrt(5*(CM_rms[0] - CM[0]**2))*L_0
    eff_radius_y     = np.sqrt(5*(CM_rms[1] - CM[1]**2))*L_0
    eff_radius_z     = np.sqrt(5*(CM_rms[2] - CM[2]**2))*L_0
    
    #print(eff_radius_x, eff_radius_y, eff_radius_z)
    
    ## MIXING FRACTION
     
    mix_numerator = np.sum(mass_cell[np.where((tr1<0.99) & (tr1>0.01))]*tr1[np.where((tr1<0.99) & (tr1>0.01))])
    
    ## CREATE HISTOGRAM FOR THE TEMPERATURE
    
    #hist_T, bins_T = np.histogram(log_Temp, bins = 20, range = (-3.6, 1.5))
    
    #center = (bins_T[:-1] + bins_T[1:]) / 2
    #width = 0.8*(bins_T[1] - bins_T[0])
    #plt.bar(center, hist_T, align = 'center', alpha = 0.6, width = width)
    
    ## HISTOGRAM 3D n, T and mass (CLOUD)
    
    average_Temp    = np.average(Temp, weights = rho_cloud)
    log_Temp        = np.log10(Temp/average_Temp)
    n_cloud_average = np.average(n_cloud, weights = rho_cloud)
    
    n_cloud1D = rho[np.where(tr1>0)]*tr1[np.where(tr1>0)]*rho_0/(mu*m_p) 
    
    if(name_file == 'data.0000.vtk'):
        print('c_s = ', np.average(wind_cs), '\n')
        print('Mach Number = ', mean_wind_mach, '\n')
        print('dens contrast = ', dens_contrast, '\n')
        print('<Temp> = ', average_Temp, '\n')
        timescales(dens_contrast, eff_radius_x, mean_wind_vel, average_rho_cl, average_Temp, n_cloud_average)
    
    return average_rho_cl, n_cloud_average, mass_cloud_tot, mean_wind_vel, average_Temp, Temp, CM[0], CM[1], CM[2], \
eff_radius_x, eff_radius_y, eff_radius_z, mix_numerator, n_cloud1D, mass_cloud
