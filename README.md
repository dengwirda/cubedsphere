## `Cubedsphere`

Generate cubedsphere meshes using the `JIGSAW` mesh generator.

A hierarchy of "smooth" cubedsphere grids may be generated using "Optimal Delaunay Tessellation" (ODT) or "Centroidal Voronoi Tessellation" (CVT) like mesh optimisation techniques. Here, a new generalisation of these schemes is used to optimise quadrilateral grid-types.

### `Quickstart`

`Cubedsphere` requires the `JIGSAW` meshing package be installed. `JIGSAW`'s `Python` interface is available <a href="https://github.com/dengwirda/jigsaw-python">here</a>. Once installed, the example problem can be run via:

    clone/download + unpack this repository.
    python3 run.py

Note: installation of `JIGSAW` requires a `c++` compiler and the `cmake` utility. `JIGSAW` may also be installed as a `conda` package. See <a href="https://github.com/dengwirda/jigsaw">here</a> for details.

### `License`

This program may be freely redistributed under the condition that the copyright notices (including this entire header) are not removed, and no compensation is received through use of the software.  Private, research, and institutional use is free.  You may distribute modified versions of this code `UNDER THE CONDITION THAT THIS CODE AND ANY MODIFICATIONS MADE TO IT IN THE SAME FILE REMAIN UNDER COPYRIGHT OF THE ORIGINAL AUTHOR, BOTH SOURCE AND OBJECT CODE ARE MADE FREELY AVAILABLE WITHOUT CHARGE, AND CLEAR NOTICE IS GIVEN OF THE MODIFICATIONS`. Distribution of this code as part of a commercial system is permissible `ONLY BY DIRECT ARRANGEMENT WITH THE AUTHOR`. (If you are not directly supplying this code to a customer, and you are instead telling them how they can obtain it for free, then you are not required to make any arrangement with me.) 

`DISCLAIMER`:  Neither I nor: Columbia University, the Massachusetts Institute of Technology, the University of Sydney, nor the National Aeronautics and Space Administration warrant this code in any way whatsoever.  This code is provided "as-is" to be used at your own risk.

### `References`

Additional information and references regarding the formulation of the underlying `JIGSAW` mesh-generator can be found <a href="https://github.com/dengwirda/jigsaw">here</a>. If you make use of this work, please consider including a reference to the following: 

`[1]` - D. Engwirda: JIGSAW-GEO (1.0): locally orthogonal staggered unstructured grid generation for general circulation modelling on the sphere, Geosci. Model Dev., 10 (2017), 2117-2140.

`[2]` - L. Chen, J. C. Xu, Optimal Delaunay triangulations, Journal of Computational Mathematics (2004) 299–308.

`[3]` - Du, Q., Faber, V., Gunzburger, M. Centroidal Voronoi tessellations: applications and algorithms, SIAM Rev. 41 (1999) (4) 637–676.
