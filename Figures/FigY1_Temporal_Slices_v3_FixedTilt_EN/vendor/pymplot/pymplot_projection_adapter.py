# Extracted unchanged from lanl/pymplot, BSD-3-Clause.
# Copyright (c) 2020-2026, Los Alamos National Laboratory.
# The complete BSD-3-Clause notice is retained in pymplot_LICENSE.
import numpy as np

def isometric_projection(x, y, z, angles):
    alpha = angles[0]
    beta = angles[1]
    bx = x * np.cos(alpha * np.pi / 180.0) - y * np.cos(beta * np.pi / 180.0)
    by = z + x * np.sin(alpha * np.pi / 180.0) + y * np.sin(beta * np.pi / 180.0)
    return bx, by
