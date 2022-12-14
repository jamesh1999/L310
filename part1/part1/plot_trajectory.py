from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pylab as plt
from rclpy.node import Node
import rclpy
import sys
import os
from ament_index_python.packages import get_package_share_directory

if __name__ == '__main__':

    share_tmp_dir = os.path.join(get_package_share_directory('part1'), 'tmp')
    file_path = os.path.join(share_tmp_dir, 'webots_exercise.txt')

    data = np.genfromtxt(file_path, delimiter=',')

    plt.figure()
    plt.plot(data[:, 0], data[:, 1], 'b', label='true')
    # For the localization exercise.
    if data.shape[1] == 6:
        plt.plot(data[:, 3], data[:, 4], 'g', label='estimated')
    # Cylinder.
    a = np.linspace(0., 2 * np.pi, 20)
    x = np.cos(a) * .3 + .5
    y = np.sin(a) * .3 + .6
    plt.plot(x, y, 'k')
    # Walls.
    plt.plot([-2, 2], [-2, -2], 'k')
    plt.plot([-2, 2], [2, 2], 'k')
    plt.plot([-2, -2], [-2, 2], 'k')
    plt.plot([2, 2], [-2, 2], 'k')
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([-2.5, 2.5])
    plt.ylim([-2.5, 2.5])

    if data.shape[1] == 6:
        plt.figure()
        error = np.linalg.norm(data[:, :2] - data[:, 3:5], axis=1)
        plt.plot(error, c='b', lw=2)
        plt.ylabel('Error [m]')
        plt.xlabel('Timestep')

    plt.show()
