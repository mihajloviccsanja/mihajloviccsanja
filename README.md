
Run generate_pfm.py to produce test pfm file (demofile.pfm) and coordinates.csv file with values of desired function(x, y) 
where x, y are coordinates (indices) of matrix of desired width and height.

test_project_sanja_mihajlovic.py is using demofile.pfm as input for implemented reading from pfm file (and coordinates.csv for checking is file is read correctly). Later, surface which is obtained in this way is tesselated in two ways, with custom implemented function, and written to corresponding stl file (extracted_triangles.stl). Also, with Python's implementation of 2D Delaunay triangulation (test_triangles.stl). Obtained triangles are compared numerically, with test program. It is recommended to open resulting .stl files in some program for 3D model viewing (3D viewer for example was used) to visually check if program works as intented.



Prerequisites for running program:
-> Python 3.5 was used. Requirements.txt containes all python libraries currently installed on development computer.
But, besides basic python libraries (numpy, sys, matplotlib, scipy, re), only few are used:
-> opencv-python
->numpy-stl
->csv
 


