def time_computer(name_file, v_0, L_0):
    
    'Convert the code-time in sec'

    f = open(name_file, "r")
    lines=f.readlines()
    time_simul=[]
    for x in lines:
        time_simul.append(float(x.split(' ')[1]))
    f.close()

    time_real   = np.asarray(time_simul)*L_0/v_0
    
    return time_real #in sec
