
import time
import numpy as np

import jigsawpy


def make_mesh():

    opts = jigsawpy.jigsaw_jig_t()              # jigsaw data structures
    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

    opts.geom_file = "tmp/geom.msh"             # setup jigsaw files
    opts.jcfg_file = "tmp/opts.jig"
    opts.mesh_file = "out/mesh.msh"

    geom.mshID = "ellipsoid-mesh"               # a simple "unit" sphere
    geom.radii = np.ones(+3)
    jigsawpy.savemsh(opts.geom_file, geom)

    opts.verbosity = +1                         # setup user-defined opt
    opts.optm_iter = +512
    opts.optm_qtol = +1.E-08
    opts.optm_kern = "odt+dqdx"
#   opts.optm_kern = "cvt+dqdx"

    ttic = time.time()

    jigsawpy.cmd.cubedsphere(opts, 6, mesh)     # mesh with n bisections

#   keep = mesh.quad4["IDtag"] == +1            # only keep single face?
#   mesh.quad4 = mesh.quad4[keep]

    ttoc = time.time()

    print("CPUSEC =", (ttoc - ttic))

    jigsawpy.savevtk("mesh.vtk", mesh)          # to open in paraview...

    return


if __name__ == "__main__": make_mesh()
