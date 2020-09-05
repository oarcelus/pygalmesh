# https://github.com/pybind/pybind11/issues/1004
from _pygalmesh import (Ball, Cone, Cuboid, Cylinder, Difference, DomainBase,
                        Ellipsoid, Extrude, HalfSpace, Intersection, Polygon2D,
                        RingExtrude, Rotate, Scale, SizingFieldBase, Stretch,
                        Tetrahedron, Torus, Translate, Union)

from .__about__ import __version__
from .main import (generate_from_array,
                   generate_from_array_with_subdomain_sizing,
                   generate_from_inr, generate_from_inr_with_subdomain_sizing,
                   generate_mesh, generate_periodic_mesh,
                   generate_surface_mesh,
                   generate_volume_mesh_from_surface_mesh,
                   generate_with_sizing_field, remesh_surface, saveinr)

__all__ = [
    "__version__",
    #
    "DomainBase",
    "SizingFieldBase",
    "Translate",
    "Rotate",
    "Scale",
    "Stretch",
    "Intersection",
    "Union",
    "Difference",
    "Extrude",
    "Ball",
    "Cuboid",
    "Ellipsoid",
    "Tetrahedron",
    "Cone",
    "Cylinder",
    "Torus",
    "HalfSpace",
    "Polygon2D",
    "RingExtrude",
    #
    "generate_mesh",
    "generate_with_sizing_field",
    "generate_periodic_mesh",
    "generate_surface_mesh",
    "generate_volume_mesh_from_surface_mesh",
    "generate_from_array",
    "generate_from_array_with_subdomain_sizing",
    "generate_from_inr",
    "generate_from_inr_with_subdomain_sizing",
    "remesh_surface",
    "saveinr",
]
