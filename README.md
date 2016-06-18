# Fractals

Program draws fractals given in ifs notation

To run the program:

1) Start terminal and enter the directory with program and input files

2) Type: python fractal.py -i file_name.ifs -n number -t type

3) Enjoy


file_name can be either of these: tree, carpet, fern, nebula, rectangle_cross, sierp_tri

number: number of iterations


type: there are two types

1) recursive reference rectangles drawing (type: r)

2) chaos game (type: c)


recommended number of iterations for:

1) r - 1, 2, 3, 4, 5 to understand how the fractal works above 5 it is very slow (exponential growth)

2) c - the bigger the more exact but also the longer it takes to draw,

optimal: 5000-25000 (this is the number of points that will be drawn)

# EXAMPLES

EXAMPLE #1:
python fractal.py -i tree.ifs -n 5000 -t c

EXAMPLE #2:
python fractal.py -i sierp_tri.ifs -n 5 -t r


More information (in Polish): http://regulomics.mimuw.edu.pl/wp/2015/12/zadanie-zaliczeniowe-nr-2-fraktale/
