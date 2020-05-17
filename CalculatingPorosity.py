import numpy as np

# all variables: Calculation is of spheres of equal size in BCC formation
R = 2     # radius sphere 1 in mm
r = R       # radius sphere 2 (All spheres the same size)
A = 0.96  # overlapping factor
X = 5       # Spheres in X direction
Y = 5       # Spheres in Y direction
Z = 8       # Spheres in Z direction

# calculation section
D = (R + r)*A   # distance between centre of 2 spheres
BCCdistance = float((4/(np.sqrt(3)))*R*A) # Bcc distance between spheres

# the equation for the radius of the overlap
WindowRadius = float((1/(2*D))*np.sqrt((-D+r-R)*(-D-r+R)*(-D+r+R)*(D+r+R)))
print('The window radius is', WindowRadius, 'mm')

# finding the volume of the removed lens common to the intersecting spheres
LensVolume = float(np.pi*((R+r-D)**2)*(D**2+2*D*r-3*r**2+2*D*R+6*r*R-3*R**2)/(12*D))

# volume of the removed lens if spheres have same radius
LensVolumeSimple = float((np.pi*(4*R+D)*((2*R-D)**2))/12)

# Volume of cube without any pores in mm3
CubeVolume = float((X-1)*BCCdistance*(Y-1)*BCCdistance*(Z-1)*BCCdistance)
print('The volume of the cube is', CubeVolume, 'mm^3')

# total BCC spheres in a given X Y Z configuration
TotalSpheres = (X*Y*Z)+((X-1)*(Y-1)*(Z-1)) # spheres in NxNxN + internal BCC spheres
# print('The total number of spheres  created is', TotalSpheres)

# there are always going to be 8 spheres in the corner (1/8 spheres) 1 window
Cornerspheres = 8
# edge spheres (1/4 spheres) 2 windows
EdgeSpheres = (X-2)*4 + (Y-2)*4 + (Z-2)*4
# external face spheres (1/2 spheres) 4 windows
FaceSpheres = (((X-2)*(Y-2))*2)+(((X-2)*(Z-2))*2)+(((Y-2)*(Z-2))*2)
# internal spheres (full spheres) have 8 windows
InternalSpheres = ((X-2)*(Y-2)*(Z-2))+((X-1)*(Y-1)*(Z-1))

# confirmation on total number of spheres
ConfirmationSpheres = Cornerspheres+EdgeSpheres+FaceSpheres+InternalSpheres
# print('Confirmation of number of spheres counting: edges, corners faces and internal', ConfirmationSpheres)

# Total number of inverted spheres within cube
TotalInvertedSpheresInCube = (Cornerspheres/8) + (EdgeSpheres/4) + (FaceSpheres/2) + InternalSpheres

# each full sphere has 8 windows but each window needs 2 spheres.
totalWindows = (TotalInvertedSpheresInCube*8)/2
# print('The total number for windows within the cube is', totalWindows)

# total volume of lenses (interaction of 2 spheres) = number of windows * Lens volume
TotalLensVolume = totalWindows*LensVolume

# total volume of the voids within the cube
CubeVoidVolume = TotalInvertedSpheresInCube*(float((4*np.pi*R**3)/3))-TotalLensVolume
print('Volume of pores', CubeVoidVolume, 'mm^3')

#Porosity of cube
Porosity = float(CubeVoidVolume/CubeVolume)
print('The volume fraction (porosity) of the cube is', Porosity)






