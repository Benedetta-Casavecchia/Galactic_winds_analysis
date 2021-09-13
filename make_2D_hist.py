def make_2D_hist(i, rho, prs, tr1, vx1, vx2, vx3):

#Generate 2D histograms of 'n' and 'T' PDFs

    rho=rho
    prs=prs
    tr1=tr1
    vx1=vx1
    vx2=vx2
    vx3=vx3
    temp=1.203E+6*prs*6.724418e-01/rho

    fig, ax = plt.subplots()
    #figh, axh = plt.subplots()

    data1 = np.log10(rho/100.)
    data2 = np.log10(temp)
    #data3 = vel

    h, xedges, yedges, image = ax.hist2d(data1, data2, bins=(160,160), range=[[-4, 4], [0, 8]], weights=(rho*tr1), cmap="jet",norm=matplotlib.colors.LogNorm())
    #hh, xedgesh, yedgesh, imageh = axh.hist2d(data1, data3, bins=(160,160), range=[[-4, 4], [0, 8]], weights=(rho*tr1), cmap="jet",norm=matplotlib.colors.LogNorm())
    fig.colorbar(image, ax=ax, label = r'$M/M_0$')   
    #fig.colorbar(imageh, ax=axh)   
    fig.tight_layout()
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel(r'$\log_{10}(n \ [cm^{-3}])$', fontsize=13)
    plt.ylabel(r'$\log_{10}(T \ [K])$', fontsize=13)
    #if(i==12):
     #   plt.figtext(0.12, 0.85, r'MHD2AlTurb-rad', fontsize = 13)
    #plt.show()
    
    return h, xedges, yedges, image
