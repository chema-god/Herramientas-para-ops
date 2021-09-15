# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 02:46:21 2021

@author: HOME
"""

import gmsh


gmsh.initialize()

gmsh.option.setNumber("General.Terminal", 1)

gmsh.model.add("Modelo 1")

tmr=0.1
nPoints=50

gmsh.model.geo.addPoint(0, 0, 0, tmr,1)

gmsh.model.geo.addPoint(-1, 0, 0, tmr,2)

gmsh.model.geo.addPoint(0, 1, 0, tmr,3)

gmsh.model.geo.addCircleArc(2, 1, 3, 4)

gmsh.model.geo.mesh.setTransfiniteCurve(4, nPoints)

gmsh.model.addPhysicalGroup(1, [4],101)

gmsh.model.setPhysicalName(1, 101, "Carga")

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(1)

gmsh.option.setNumber("Mesh.Points", 1)

filename="malla arco.msh"

gmsh.write(filename)

gmsh.fltk.run()

gmsh.finalize()