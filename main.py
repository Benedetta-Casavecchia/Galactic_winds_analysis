# In order to analyse one simulation

input_directory = 'Wind_cloud/Wind-Cloud-MHD-Al/'

list = os.listdir(input_directory)
number_files = len(list)
#print(number_files)

## DEFINE NORMALIZATION FACTORS (c.g.s)

rho_0  = 1.115*10**(-26) 
L_0    = 3.086*10**19
v_0    = 10**7
mu     = 0.67
gamma  = 5/3

## DEFINE VARIABLES

step          = np.arange(0, 51, 1)
time_step     = np.zeros(51)
dens_average  = np.zeros(51)
n_average     = np.zeros(51)
vel_wind_mean = np.zeros(51)
mass          = np.zeros(51)
average_Temp  = np.zeros(51)
cloud_radius  = np.zeros(51)
mix_num       = np.zeros(51)
coo_CM        = np.zeros((51,3))
eff_radius    = np.zeros((51,3))

for i in range(number_files):
    
    file_name  = 'data.' + str(i).zfill(4) + '.vtk'
    file_name1 = 'Wind_cloud/vtk.out'
    
    time_step = time_computer(file_name1, v_0, L_0)
    time_step = time_step*3.17098*10**(-14)
    #start = time.time()
    
    rho, vx1, vx2, vx3, Bx1, Bx2, Bx3, prs, tr1 = pload_vtk(file_name, input_directory)
    dens_average[i], n_average[i], mass[i], vel_wind_mean[i], average_Temp[i], Temp, coo_CM[i][0],coo_CM[i][1],\
coo_CM[i][2],eff_radius[i][0], eff_radius[i][1], eff_radius[i][2], mix_num[i], n_cloud, mass_cloud =\
diagnostics_cgs(rho, vx1, vx2, vx3, Bx1, Bx2, Bx3, prs, tr1, file_name, input_directory, v_0, L_0, rho_0, mu, gamma)
    
    #MAKE COLUMN DENSITY PLOTS
    
    column_density(i, file_name, input_directory, rho_0, mu, L_0)
    plt.savefig('Wind_cloud/snapshots_columndensity/coldens.' + str(i) + '.jpeg')
    plt.close()
    
    density_downthebarrel(i, file_name, input_directory, rho_0, mu, L_0)
    plt.savefig('Wind_cloud/snapshots_downthebarrel/downthebarrel.' + str(i) + '.jpeg')
    plt.close()

    #COMPUTE TEMPERATURE PDF
    
    if(i == 0):

        T_0   = np.average(Temp)
        #T_min = np.amin(Temp)
        #T_max = np.amax(Temp)
        T_min = 10**(-3.6)
        T_max = 10**(1.5)
                    
    #Temp_pdf(Temp, T_0, T_min, T_max)
    
    make_2D_hist(i, rho, prs, tr1, vx1, vx2, vx3)
    plt.savefig('Wind_cloud/snapshots_hist2d/hist2d.' + str(i) + '.jpeg')
    plt.close()
    
    #end = time.time()
    #print('time = ', end - start, 'sec')

#mass_tot      = np.mean(mass)
#print('total mass = ', mass_tot)

## CLOUD_CRUSHING TIME

cloud_radius = np.sqrt(eff_radius[:][0]**2 + eff_radius[:][1]**2 + eff_radius[:][2]**2)
t_cc         = 2*(eff_radius[0][0]/(math.sqrt(0.006947657)*vel_wind_mean[0]))*3.17098*10**(-14)

print('eff_radius = ', eff_radius[0][0], 'cm')
print('t_cc = ', t_cc, 'Myr')

init_mass  = mass[0]
final_mass = mass[50]

## MIXING PARAMETER

mix_num = mix_num/mass[0]

## CHECKING

print('initial cloud density = ', n_average[0])
print('initial cloud temperature = ', average_Temp[0])
print('initial mass = ', init_mass)
print('final mass = ', final_mass)
print('wind vel = ', vel_wind_mean[0], 'cm/s')
#print(mass)
#print(coo_CM)
#print(np.shape(time_step))
#print(np.shape(eff_radius[:,0]))

## MAKE PLOTS

plt.plot(time_step, np.log10(n_average), 'r')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$\log_{10}(n \ [cm^{-3}])$', fontsize=13)
plt.show()

plt.plot(time_step, mass, 'b')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$mass \ [g]$', fontsize=13)
plt.show()

plt.plot(time_step, np.log10(average_Temp), 'g')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$\log_{10}(T \ [K])$', fontsize=13)
plt.show()

plt.plot(time_step, eff_radius[:,0]*10/L_0, 'g')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$r_{eff,X} \ [pc]$', fontsize=13)
plt.show()

plt.plot(time_step, eff_radius[:,1]*10/L_0, 'g')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$r_{eff,Y} \ [pc]$', fontsize=13)
plt.show()

plt.plot(time_step, eff_radius[:,2]*10/L_0, 'g')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$r_{eff,Z} \ [pc]$', fontsize=13)
plt.show()

plt.plot(time_step, mix_num, 'b')
plt.xlabel('t (Myr)', fontsize=13)
plt.ylabel(r'$f_{mix}$', fontsize=13)
plt.show()

## SAVE OUTPUT
#output = np.column_stack([step, time_step, dens_average, n_average, mass, mix_num])
#np.savetxt('Wind_cloud/WC_mass&density&mixfraction.txt', output, fmt=['%d','%4e','%4e','%4e','%4e','%4e'])

#output = np.column_stack([step, time_step, vel_wind_mean, average_Temp])
#np.savetxt('Wind_cloud/WC_velocity&Temp.txt', output, fmt=['%d','%4e','%4e','%4e'])

#output = np.column_stack([step, time_step, coo_CM[:,0],coo_CM[:,1], coo_CM[:,2],\
#eff_radius[:,0], eff_radius[:,1], eff_radius[:,2]])
#np.savetxt('Wind_cloud/WC_CM&eff_radius.txt', output, fmt=['%d','%4e','%4e','%4e','%4e','%4e','%4e','%4e'])
