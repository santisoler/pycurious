"""
Copyright 2018 Ben Mather, Robert Delhaye

This file is part of PyCurious.

PyCurious is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or any later version.

PyCurious is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PyCurious.  If not, see <http://www.gnu.org/licenses/>.
"""

# -*- coding: utf-8 -*-
from .documentation import install_documentation
from .grid import CurieGrid, bouligand2009, tanaka1999, maus1995, ComputeTanaka
from .optimise import CurieOptimise
from .mapping import transform_coordinates
from .mapping import convert_extent
from .mapping import trim
from .mapping import grid
from .mapping import import_geotiff