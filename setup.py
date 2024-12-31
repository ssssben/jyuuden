<<<<<<< HEAD
# SPDX-FileCopyrightText: 2024 Ben
# SPDX-License-Identifier: BSD-3-Clause
from setuptools import setup
import os
from glob import glob
=======
from setuptools import setup
>>>>>>> Initial commit

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bun',
    maintainer_email='vlongbf@gmail.com',
<<<<<<< HEAD
    description='充電残量を知らせる',
=======
    description='充電残量を表示',
>>>>>>> Initial commit
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'batterytalker = mypkg.batterytalker:main',
        ],
    },
)
