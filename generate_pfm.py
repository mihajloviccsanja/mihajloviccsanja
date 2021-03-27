"""
This file serves as data generator for test_project_sanja_mihajlovic.py file,
since it's input has to be .pfm file. In order to check if requested function 
for reading from .pfm file is implemented properly, raw values of chosen function
over matrix of (x, y) coordinates of desired dimensions are saved inside .csv file, which
is going to be checked against inside main project file.

"""

import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import csv

"""
Saves function(x, y), where x and y ranges up to width, height dimensions of matrix in .pfm file
function(x, y) = image argument
"""
def save_pfm(file, image, scale = 1):
  color = None

  if image.dtype.name != 'float32':
    raise Exception('Image dtype must be float32.')

  if len(image.shape) == 3 and image.shape[2] == 3: # color image
    color = True
  elif len(image.shape) == 2 or len(image.shape) == 3 and image.shape[2] == 1: # greyscale
    color = False
  else:
    raise Exception('Image must have H x W x 3, H x W x 1 or H x W dimensions.')

  file.write('PF\n' if color else 'Pf\n')
  file.write('%d %d\n' % (image.shape[1], image.shape[0]))  #dimensions of matrix 

  endian = image.dtype.byteorder
  if endian == '<' or endian == '=' and sys.byteorder == 'little':  #check for endianess of bytes to write
    scale = -scale

  file.write('%f\n' % scale)
  image = np.flipud(image)  #should be saved from bottom to top, per definition of format
  image.tofile(file) 

"""
For given matrix size, generates values of desired function
in (x, y) points, where (x, y) are matrix indices.
"""
def generate_function_data(width, height):

  X = np.arange(0, width)
  Y = np.arange(0, height)
 

  X, Y = np.meshgrid(X, Y)

  R = np.sqrt(X**2 + Y**2)  #user can define desired function
  Z = np.sin(R)

  return X, Y, Z

"""
Writes values of function inside .csv file, alongside with
height and width of matrix over which function values are calculated.
"""
def write_values_to_csv(height, width, array):

  with open('coordinates.csv', 'w', newline='') as csvfile:
      fieldnames = ['height', 'width', 'z']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

      writer.writeheader()
      writer.writerow({'height':height,'width': width})
      for i in range(0, height):
        for j in range(0, width):
          writer.writerow({'z': array[i][j]})


"""
3D graphical representation of given function, over given matrix
of (x, y) coordinates.
"""
def plot_surface(X, Y, Z):
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

  # Customize the z axis.
  #ax.set_zlim(-1.01, 1.01)
  ax.zaxis.set_major_locator(LinearLocator(10))
  # A StrMethodFormatter is used automatically
  ax.zaxis.set_major_formatter('{x:.02f}')

  # Add a color bar which maps values to colors.
  fig.colorbar(surf, shrink=0.5, aspect=5)

  plt.show()

"""
Values of arbitrary function over desired matrix are generated, plotted and 
written  to .pfm and .csv file.
"""
def main():
  # Make data.
  width = 5
  height = 5
  X, Y, Z = generate_function_data(width, height)
  # Plot the surface.
  plot_surface(X, Y, Z)


  f = open("demofile.pfm", "w")
  z = np.float32(Z)
  array = np.reshape(z, newshape = (height, width))
  save_pfm(f, array)
  write_values_to_csv(height, width, array)


if __name__ == '__main__':
    main()



