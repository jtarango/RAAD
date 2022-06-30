#!/usr/bin/python3
# -*- coding: utf-8 -*-
# *****************************************************************************/
# * Authors: Joseph Tarango
# *****************************************************************************/
from setuptools import setup, find_packages
import pathlib, os

here = os.path.abspath(__file__)
uphere = os.path.join(here, "..")
upHereJoe = os.path.abspath(uphere)
readJoe = pathlib.Path(upHereJoe).parent.resolve()
# Get the long description from the README file
super_long_description = (readJoe / "README.md").read_text(encoding="utf-8")

setup(name='RAAD',
      version='1.0.0',
      description="RAAD telemetry data analysis framework tools",
      long_description=str.join('Telemetry is the state space snapshot which tightly-couple specialists to pertinent data, remotely, '
                  'removing the cyber-physical challenges with interacting on complex platforms. The immediate benefit '
                  'is precise and rapid data extraction correlated to customer platforms. The purposeful subsequent '
                  'benefit is reactive-proactive real-time analytics for monitoring of client platforms and data '
                  'centers. The real-time processing of the data enables data mining, machine learning, and artificial '
                  'intelligence. The application of these techniques is given in an instance of Intel SSDs and can be '
                  'applied to technological eco-systems.\n', super_long_description),
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",  # https://pypi.org/classifiers/
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Tools",
          "Environment :: Console",
          "Operating System :: POSIX :: Linux",
          # "Operating System :: Microsoft :: Windows",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Unix Shell",
          "LICENSE :: OSI APPROVED :: APACHE SOFTWARE LICENSE"],
      keywords='raad, telemetry, NVMe, development tools',
      author='Joseph_Tarango',
      author_email='joseph.d.tarango@intel.com',
      license='APL 2.0',
      python_requires=">=3.8, <4",
      packages=find_packages('../src'),
      package_dir={'': '../src'},
      include_package_data=True,
      url='https://github.com/intel/RAAD.git',
      platforms=['linux'],  # , 'win32'],
      install_requires=[],
      entry_points={
                    'console_scripts': [
                                        # "raad" will be added to the installing-environment's text mode shell, eg `bash -c raad`
                                        'raad=main.mainFaultContext()',
                                       ]
                   },
      )
