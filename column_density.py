def column_density(i, name_file, input_directory, rho_0, mu, L_0):

#Make column density plot
    
    m_p = 1.67*10**(-24)
    
    rho, _, _, _, _, _, _, _, tr1 = pload_vtk(name_file, input_directory)
    
    n_cgs    = rho*rho_0*tr1/(mu*m_p)
    n_cgs_3d = np.reshape(n_cgs, (96, 192, 96))
    N_mc     = np.sum(n_cgs_3d*(L_0/8), axis = 0)
    
    ## CREATE PLOTS
    
    x1  = np.linspace(-60, 60, 96)
    y1  = np.linspace(-20, 220, 192)
    x,y = np.meshgrid(x1,y1)
    
    magma  = plt.get_cmap('magma_r')
    plt.figure(figsize=(4,8))
    plt.pcolormesh(x, y, N_mc, norm=matplotlib.colors.LogNorm(vmin=10**16, vmax=10**20), cmap = magma, shading = 'nearest')
    plt.colorbar(label = r'$N_{mc} \ [cm^{-3}]$',)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel(r'$x \ [pc]$', fontsize=13)
    plt.ylabel(r'$y \ [pc]$', fontsize=13)
    #if(name_file == 'data.0012.vtk'):
        #plt.figtext(0.17, 0.85, r'MHD2AlTurb-rad', fontsize = 13)
    #plt.show()
    
    #return N_mc
