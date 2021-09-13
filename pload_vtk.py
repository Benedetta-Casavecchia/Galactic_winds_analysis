def pload_vtk(file_name, input_directory):
    """Read VTK file and returns the variables as 1D vectors"""

    file_name = file_name

    reader= vtk.vtkDataSetReader()
    reader.SetFileName(input_directory+file_name)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()
    
    #print(data)
    dens = data.GetCellData().GetArray("rho")
    vel1 = data.GetCellData().GetArray("vx1")
    vel2 = data.GetCellData().GetArray("vx2")
    vel3 = data.GetCellData().GetArray("vx3")
    Bx1  = data.GetCellData().GetArray("Bx1")
    Bx2  = data.GetCellData().GetArray("Bx2")
    Bx3  = data.GetCellData().GetArray("Bx3")
    prs  = data.GetCellData().GetArray("prs")
    tr1  = data.GetCellData().GetArray("tr1")
    
    rho = np.array(dens)
    vx1 = np.array(vel1)
    vx2 = np.array(vel2)
    vx3 = np.array(vel3)    
    Bx1 = np.array(Bx1)
    Bx2 = np.array(Bx2)
    Bx3 = np.array(Bx3)
    prs = np.array(prs)    
    tr1 = np.array(tr1)
    
    #print(tr1.shape)
    
    return rho, vx1, vx2, vx3, Bx1, Bx2, Bx3, prs, tr1
