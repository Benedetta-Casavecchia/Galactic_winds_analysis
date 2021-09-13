## PLOTS MAKER ##

# 1) READ ALL FILES AND CREATE LISTS

f=open('Wind_cloud/WC_mass&density&mixfraction.txt',"r")
lines=f.readlines()

time_step       = []
mass_cloud      = []
n_cloud         = []
mix_ratio_cloud = []

for x in lines:
    time_step.append(x.split()[1])
    mass_cloud.append(x.split()[4])
    n_cloud.append(x.split()[3])
    mix_ratio_cloud.append(x.split()[5])
f.close()

#####################################

f=open('Wind_cloud_turb/WCturb_mass&density&mixfraction.txt',"r")
lines=f.readlines()

mass_cloud_turb      = []
n_cloud_turb         = []
mix_ratio_cloud_turb = []

for x in lines:
    mass_cloud_turb.append(x.split()[4])
    n_cloud_turb.append(x.split()[3])
    mix_ratio_cloud_turb.append(x.split()[5])
f.close()

#####################################

f=open('Wind_cloud/WC_velocity&Temp.txt',"r")
lines=f.readlines()

Temp_cloud = []

for x in lines:
    Temp_cloud.append(x.split()[3])
f.close()

#####################################

f=open('Wind_cloud_turb/WCturb_velocity&Temp.txt',"r")
lines=f.readlines()

Temp_cloud_turb = []

for x in lines:
    Temp_cloud_turb.append(x.split()[3])
f.close()

#####################################

f=open('Wind_cloud/WC_CM&eff_radius.txt',"r")
lines=f.readlines()

CM_x = []
CM_y = []
CM_z = []
r_x  = []
r_y  = []
r_z  = []

for x in lines:
    CM_x.append(x.split()[2])
    CM_y.append(x.split()[3])
    CM_z.append(x.split()[4])
    r_x.append(x.split()[5])
    r_y.append(x.split()[6])
    r_z.append(x.split()[7])
f.close()

#####################################

f=open('Wind_cloud_turb/WCturb_CM&eff_radius.txt',"r")
lines=f.readlines()

CM_x_turb = []
CM_y_turb = []
CM_z_turb = []
r_x_turb  = []
r_y_turb  = []
r_z_turb  = []

for x in lines:
    CM_x_turb.append(x.split()[2])
    CM_y_turb.append(x.split()[3])
    CM_z_turb.append(x.split()[4])
    r_x_turb.append(x.split()[5])
    r_y_turb.append(x.split()[6])
    r_z_turb.append(x.split()[7])
f.close()

# 2) CREATE ARRAYS

time_step            = np.array(time_step).astype(np.float)
n_cloud              = np.array(n_cloud).astype(np.float)
n_cloud_turb         = np.array(n_cloud_turb).astype(np.float)
mass_cloud           = np.array(mass_cloud).astype(np.float)
mass_cloud_turb      = np.array(mass_cloud_turb).astype(np.float)
Temp_cloud           = np.array(Temp_cloud).astype(np.float)
Temp_cloud_turb      = np.array(Temp_cloud_turb).astype(np.float)
mix_ratio_cloud      = np.array(mix_ratio_cloud).astype(np.float)
mix_ratio_cloud_turb = np.array(mix_ratio_cloud_turb).astype(np.float)
r_x                  = np.array(r_x).astype(np.float)
r_x_turb             = np.array(r_x_turb).astype(np.float)
r_y                  = np.array(r_y).astype(np.float)
r_y_turb             = np.array(r_y_turb).astype(np.float)
r_z                  = np.array(r_z).astype(np.float)
r_z_turb             = np.array(r_z_turb).astype(np.float)

# 3) PLOTS

plt.plot(time_step, np.log10(n_cloud), 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, np.log10(n_cloud_turb), 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$\log_{10}(n_{\rm cl} \ [cm^{-3}])$', fontsize=13)
plt.legend()
plt.show()

plt.plot(time_step, np.log10(Temp_cloud), 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, np.log10(Temp_cloud_turb), 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$\log_{10}(T_{\rm cl} \ [K])$', fontsize=13)
plt.legend()
plt.show()

plt.plot(time_step, mass_cloud, 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, mass_cloud_turb, 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$m_{\rm cl} \ [g]$', fontsize=13)
plt.legend()
plt.show()

plt.plot(time_step, mix_ratio_cloud, 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, mix_ratio_cloud_turb, 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.axvline(x = 0.5,linestyle = ':')
plt.axvline(x = 2.2, linestyle = ':')
plt.figtext(0.2, 0.3, r'Compression', fontsize = 15, rotation=90)
plt.figtext(0.33, 0.67, r'Stripping + Expansion', fontsize = 15)
plt.figtext(0.82, 0.3, r'Break-up', fontsize = 15, rotation=90)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$f_{\rm mix}$', fontsize=13)
plt.legend(loc = 2)
plt.show()

plt.plot(time_step, r_x*3.24*10**(-19), 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, r_x_turb*3.24*10**(-19), 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.axvline(x = 0.5, linestyle = ':')
plt.axvline(x = 2.2, linestyle = ':')
plt.figtext(0.2, 0.3, r'Compression', fontsize = 15, rotation=90)
plt.figtext(0.33, 0.67, r'Stripping + Expansion', fontsize = 15)
plt.figtext(0.82, 0.3, r'Break-up', fontsize = 15, rotation=90)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$\iota_x \ [pc])$', fontsize=13)
plt.legend(loc = 2)
plt.show()

plt.plot(time_step, r_y*3.24*10**(-19), 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, r_y_turb*3.24*10**(-19), 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.axvline(x = 0.5, linestyle = ':')
plt.axvline(x = 2.2, linestyle = ':')
plt.figtext(0.2, 0.3, r'Compression', fontsize = 15, rotation=90)
plt.figtext(0.33, 0.3, r'Stripping + Expansion', fontsize = 15)
plt.figtext(0.82, 0.3, r'Break-up', fontsize = 15, rotation=90)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$\iota_y \ [pc])$', fontsize=13)
plt.legend(loc = 2)
plt.show()

plt.plot(time_step, r_z*3.24*10**(-19), 'r', label = 'MHD-Al', linewidth = 2)
plt.plot(time_step, r_z_turb*3.24*10**(-19), 'b', label = 'MHD2AlTurb', linestyle = '--', linewidth = 2)
plt.axvline(x = 0.5, linestyle = ':')
plt.axvline(x = 2.2, linestyle = ':')
plt.figtext(0.2, 0.3, r'Compression', fontsize = 15, rotation=90)
plt.figtext(0.33, 0.67, r'Stripping + Expansion', fontsize = 15)
plt.figtext(0.82, 0.3, r'Break-up', fontsize = 15, rotation=90)
plt.xlabel('t [Myr]', fontsize=13)
plt.ylabel(r'$\iota_z \ [pc])$', fontsize=13)
plt.legend(loc = 2)
plt.show()

print(n_cloud[4])
