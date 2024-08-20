##########################
# Capstone GUI Functions #
##########################
import numpy as np
from icecream import ic 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
##############################
#
def READ_IN(Asteroid_Name):
    """_summary_

    Args:
        Asteroid_Name (.out file): This is the output file from 
                                    Asteroid_CM.py

    Returns:
        Array: The x-y-z points of each Center of Mass for 
                asteroid tetrahedrons 
    """
    #######################
    # Load data file      ###################################### 
    data = np.loadtxt(Asteroid_Name, delimiter=' ', dtype=str) #
    ############################################################
    Tetra_CM = data.astype(float)
    return Tetra_CM


def OBJ_READ_IN(Asteroid_Name,scale):
    """ This reads in .obj files and creates the face mesh
     That is used for plotting around the Center of Masses
     
    Args:
        Asteroid_Name (.obj file):  Asteroid Shape model File
    
    Returns:
        Mesh: Asteroid face mesh 
    """
    #######################
    # Load data file      ###################################### 
    data = np.loadtxt(Asteroid_Name, delimiter=' ', dtype=str) #
    ############################################################
    ###############################################################
    # Set Vertex/Faces denotaed as v or f in .obj format to array #
    vertex_faces = data[:,0]                                      #
    # Get Length of the Vertex/Faces array for range counting     #
    V_F_Range = vertex_faces.size                                 #
    # Define varibale for number of vertices & faces              #
    numb_vert = 0                                                 #
    numb_face = 0                                                 #
    # Scan Data for v & f and count the numbers of each.          #
    #  Used for sorting x, y, & z as vertices                     #
    for i in range(0,V_F_Range):                                  #
        if vertex_faces[i] == 'v':                                #
            numb_vert += 1                                        #
        else:                                                     #
            numb_face += 1                                        #
    ###############################################################
    #########################
    # Assigning Vertex Data #
    #########################
    # Vertex data assigned to x, y, & z
    #  then cpnverts to float type
    ########################################
    # Assign 2nd row of .txt as x input    #
    x_input = data[range(0,numb_vert),1]   #
    # Assign 3rd row of .txt as y input    #
    y_input = data[range(0,numb_vert),2]   #
    # Assign 4th row of .txt as z input    #
    z_input = data[range(0,numb_vert),3]   #
    # Convert Vertices data to float type  #
    x_0 = x_input.astype(float)            #
    y_0 = y_input.astype(float)            #
    z_0 = z_input.astype(float)            #
    ########################################
    #
    ##############################################
    # Fill zero indecies with dummy values       #
    #  to allow faces to call vertices 1 to 1014 #
    x = np.append(0,x_0)  ########################
    y = np.append(0,y_0)  #
    z = np.append(0,z_0)  #
    #######################
    #
    #######################
    # Assigning Face Data #
    #######################
    # Face data assigned to fx, fy, & fz
    #  then cpnverts to float type
    #############################################
    # Range count for face data                 #
    row_tot = numb_face + numb_vert             #
    # Assign 2nd row of .txt as x input         #
    fx_input = data[range(numb_vert,row_tot),1] #
    # Assign 3rd row of .txt as y input         #
    fy_input = data[range(numb_vert,row_tot),2] #
    # Assign 4th row of .txt as z input         #
    fz_input = data[range(numb_vert,row_tot),3] #
    # Convert Vertices data to float type       #
    fx = fx_input.astype(int)                   #
    fy = fy_input.astype(int)                  #
    fz = fz_input.astype(int)                 #
    ##########################################
    #
    ##########################
    # Creating Output Arrays #
    ##########################
    #    Number of Vertex is (N-1)             
    #     numb_vert += 1
    #########################################
    # Number of Vertex set to array         #
    numb_vert_array = []                    #
    numb_vert_array.append(numb_vert)       #
    # Number of Faces set to array          #
    numb_face_array = []                    #
    numb_face_array.append(numb_face)       #
    # Stacking Columns of Vertex Data       #################
    Vert_Data_Out_0 = np.column_stack((x, y))               #
    Vert_Data       = np.column_stack((Vert_Data_Out_0, z)) #
    # Stacking Columns of Face Data                         #
    Face_Data_Out_0 = np.column_stack((fx,fy))              #
    Face_Data       = np.column_stack((Face_Data_Out_0,fz)) #
    #########################################################
    Vert_Data_mesh = Vert_Data*scale
    ##:)                                                 
    # Let's put a Happy little Asteroid right in there        
    Asteroid_Mesh = Poly3DCollection([Vert_Data_mesh[ii] for ii in Face_Data], 
                            edgecolor='#FFC107',
                            facecolors="white",
                            linewidth=0.1,
                            alpha=0.0)
    ######################################
    return Asteroid_Mesh



def MASCON_Orbit_3D(Initial_Conditions, MASCON_Choice, Center_of_mass, a, File_OBJ_Dir,scale):
  """MASCON Orbital plot in 3-Dimensions
        Used to plot simulated orbit around the tetrahedron center of masses,
        contianed within the asteroid's outer mesh.
  Args:
      Initial_Conditions (array): Tetrahedron center of masses.
      MASCON_Choice (int): This is a selection integer 1, 3, & 8 ONLY!!
      Center_of_mass (array): Polyhedron center of mass.
      a (array): State Vector of Orbit.
      File_OBJ_Dir (path & file name): The path & name of the .obj file, for the mesh.
      scale (float): mesh scale for the asteroid.

  Returns:
      plot: 3D plot of the orbit around the asteorid shape model. Don't forget to call the plot with `plt.show()` !!
  """
  ############
  # Settings #
  ############
  # CM point size in %
  Cm_plot_p_size   = 25
  # CM marker
  Cm_plot_mark_typ = '.'
  #####################
  # Colors
  grid_col   = '#0200FF'
  Space      = "#000000"
  orbit_line = "#F70101"
  Mesh_Color = '#FFB000'
  #############################
  Mascon_Color_Bank = ['#9600FF',
                      '#2600FF',
                      '#00D9FF',
                      '#00FF43',
                      '#D9FF00',
                      '#FFD500',
                      '#FFA700',
                      '#FFBB7D']
  ####################
  # 3D Plot of Orbit ######################
  # Grid Color                            #
  plt.rcParams['grid.color'] = grid_col   #
  #########################################
  # Set plot                              
  fig = plt.figure('Orbit')               
  # Set axis                              
  axis = plt.axes(projection='3d')           
  # Set Window Size                       
  fig.tight_layout()              
  # Plot CM of Asteroid                   
  cm_x = Center_of_mass[0]
  cm_y = Center_of_mass[1]
  cm_z = Center_of_mass[2]
  axis.scatter3D(cm_x,cm_y,cm_z,
                  marker='o',
                  color='#D41159')
  ############################
  # CM MASCON I, III, & VIII #
  ##########################################
  ################ MASCON I ################
  if MASCON_Choice == '1':
      axis.scatter3D(Initial_Conditions[:,0],
                  Initial_Conditions[:,1],
                  Initial_Conditions[:,2],
                  marker='o',
                  alpha=1,
                  s=Cm_plot_p_size, 
                  edgecolor=Mascon_Color_Bank[2])
  ############################################
  ################ MASCON III ################
  elif MASCON_Choice == '3':
      ###########
      # M1
      axis.scatter3D(Initial_Conditions[:,0],
                  Initial_Conditions[:,1],
                  Initial_Conditions[:,2],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[3])
      ##########
      # M2
      axis.scatter3D(Initial_Conditions[:,3],
                  Initial_Conditions[:,4],
                  Initial_Conditions[:,5],
              marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[4])
      ##########
      # M3
      axis.scatter3D(Initial_Conditions[:,6],
                  Initial_Conditions[:,7],
                  Initial_Conditions[:,8],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[5])
  #############################################
  ################ MASCON VIII ################
  else:
      ###########
      # M1
      axis.scatter3D(Initial_Conditions[:,0],
                  Initial_Conditions[:,1],
                  Initial_Conditions[:,2],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[0])
      ##########
      # M2
      axis.scatter3D(Initial_Conditions[:,3],
                  Initial_Conditions[:,4],
                  Initial_Conditions[:,5],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[1])
      ##########
      # M3
      axis.scatter3D(Initial_Conditions[:,6],
                  Initial_Conditions[:,7],
                  Initial_Conditions[:,8],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[2])
      ##########
      # M4
      axis.scatter3D(Initial_Conditions[:,9],
                  Initial_Conditions[:,10],
                  Initial_Conditions[:,11],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[3])
      ##########
      # M5
      axis.scatter3D(Initial_Conditions[:,12],
                  Initial_Conditions[:,13],
                  Initial_Conditions[:,14],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[4])
      ##########
      # M6
      axis.scatter3D(Initial_Conditions[:,15],
                  Initial_Conditions[:,16],
                  Initial_Conditions[:,17],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[5])
      ##########
      # M7
      axis.scatter3D(Initial_Conditions[:,18],
                  Initial_Conditions[:,19],
                  Initial_Conditions[:,20],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[6])
      ##########
      # M8
      axis.scatter3D(Initial_Conditions[:,21],
                  Initial_Conditions[:,22],
                  Initial_Conditions[:,23],
                  marker=Cm_plot_mark_typ,
                  s=Cm_plot_p_size,
                  color=Mascon_Color_Bank[7])
  #########################################
  # Set Aspect
  axis.set_box_aspect([1,1,1])
  # Add Asteroid MEsh
  # Read in OBJ file and assign as a 3D mesh of faces
  Asteroid_Mesh =OBJ_2_Mesh(
                            File_OBJ_Dir,
                            scale,
                            Mesh_Color)
  axis.add_collection3d(Asteroid_Mesh)
  #########################################
  # Set x data to position, i. given by a #
  xline = a[:,0]                          #
  # Set y data to position, j. given by a #
  yline = a[:,1]                          #
  # Set z data to position, k. given by a #
  zline = a[:,2]                          #
  # Plot line and asteroid                #
  axis.plot3D(xline, yline, zline,        #
          color=orbit_line )              #
  # Axis Labels                           #
  axis.set_xlabel('x (km)')                 #
  axis.set_ylabel('y (km)')                  #
  axis.set_zlabel('z (km)')                   #
  axis.tick_params(axis='x', colors=grid_col) #
  axis.tick_params(axis='y', colors=grid_col) #
  axis.tick_params(axis='z', colors=grid_col) #
  axis.yaxis.label.set_color(grid_col)        #  
  axis.xaxis.label.set_color(grid_col)       #  
  axis.zaxis.label.set_color(grid_col)      #
  # Background Color                      # 
  fig.set_facecolor(Space)                #
  axis.set_facecolor(Space)                #
  # Grid Pane Color/set to clear          #
  axis.xaxis.set_pane_color((0.0, 0.0,     #
                              0.0, 0.0))  #
  axis.yaxis.set_pane_color((0.0, 0.0,     #
                              0.0, 0.0))  #
  axis.zaxis.set_pane_color((0.0, 0.0,     #
                              0.0, 0.0))  # 
  #########################################
  return
############################################