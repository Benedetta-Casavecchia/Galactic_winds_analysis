def Temp_pdf(T, T_0, mini, maxi):

#Generate Tempreature PDF
    
    s = np.log10(T/T_0)
    mini = math.log10(mini)
    maxi = math.log10(maxi)
    
    hist_T, bins_T = np.histogram(s, bins = 50, range = (mini, maxi))
    
    center = (bins_T[:-1] + bins_T[1:]) / 2
    width = 0.8*(bins_T[1] - bins_T[0])
    #plt.bar(center, hist_T, align='center', alpha = 0.6, width = width)
    plt.show()
