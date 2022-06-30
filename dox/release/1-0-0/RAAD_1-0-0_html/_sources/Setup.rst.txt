Documentation Sphinx Generator for Linux
#########################################

A simple generator for using Sphinx to document small Python modules.

reStructured Text cheat sheet
    - http://github.com/#index

Python documentation cheat sheet

.. code-block:: console

    module/__init__.py

Installation
**************************

.. code-block:: console

    $ sudo apt-get install python-sphinx
    $ sudo pip install sphinx
    # Depends on which version you prefer ...
    $ sudo pip3 install sphinx

Quickstart
**************************
Sphinx offers an easy quickstart

.. code-block:: console

    $ mkdir docs
    $ cd docs
    # Quickstart, select yes for apidoc and mathjax and for splitting build and source.
    $ sphinx-quickstart
    $ sphinx

Choose to separate source and build directories, choose project name and version and the autodoc extension.

If the code/module to be documentation is accessible from the root directory, edit

.. code-block:: console

    docs/source/conf.py

as follows

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../'))

Then the modules can be automatically documented using:

.. code-block:: console

    $ sphinx-apidoc -f -o source/ ../
    $ make html

Python 3.8
**************************

For modules or dependencies not supporting Python 3, `docs/Makefile` can ba adapted:

.. code-block:: python

    SPHINXBUILD   = python -c "import sys,sphinx;sys.exit(sphinx.main(sys.argv))"

Instruction Commands
*********************

New development should have a unit test capability built in to ensure there are no regressions.

* Auto doxygen location
    * RAAD/dox/build/index.html
    * RAAD/dox/build/epub/RAAD.epub
* Docstring Style
    * https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
* Example documentation execute order:

.. code-block:: python

   cd RAAD/dox/source/
   python findClasses.py
   cd ..
   make clean
   make

Operating System, Virtural Machine, Container Setup Options
#############################################################

Choices for setups are:
 1. **Native OS Ubuntu 22.04 LTS** [#_Option_1]
 2. **Ubuntu 22.04 LTS Docker** [#_Option_2]
 3. **Create your own image of Ubuntu 22.04 LTS** [#_Option_3]
 4. **Use a partial make image of Ubuntu 22.04 LTS**  [#_Option_4]
 5. **Intel Pre-made image of Ubuntu 22.04 LTS**  [#_Option_5]
 6. **Windows 10 x86_64 (Not Recommended)** [#_Option_6]

.. [#_Option_1]

Option 1 Ubuntu 22.04 LTS
**************************
1. See [#_Clone_Repository-label]
2. See [#_Install_RAAD_Ubuntu_Script_for_Requirements-label]
3. See [#_Use_default_IDE_to_run_RAAD_main-label]

.. [#_Option_2]

Option 2 Ubuntu 22.04 LTS + Docker
***********************************

.. [#_Option_3]

Option 3 Create your own image of Ubuntu 22.04 LTS
**************************************************
1. Create Ubuntu download image at:
       * https://ubuntu-mate.org/download/amd64/jammy/
2. To use the virtual machine download VMWare workstation player
       * https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html
3. Follow steps:
       * https://kb.vmware.com/s/article/1018415
       * https://kb.vmware.com/s/article/1018414
4. See [#_Clone_Repository-label]
5. See [#_Install_RAAD_Ubuntu_Script_for_Requirements-label]
6. See [#_Use_default_IDE_to_run_RAAD_main-label]

.. [#_Option_4]

Option 4 Use a partial make image of Ubuntu 22.04 LTS
******************************************************
1. To download semi-pre-made image:
       * https://sourceforge.net/projects/osboxes/files/v/vm/55-U--u/22.04/64bit.7z/download
2. Login info is located at:
       * https://www.osboxes.org/faq/what-are-the-credentials-for-virtual-machine-image/
3. Install vitural machine tools
       * https://kb.vmware.com/s/article/1018414
4. Proceed to 'Clone Repository'
5. See [#_Clone_Repository-label]
6. See [#_Install_RAAD_Ubuntu_Script_for_Requirements-label]
7. See [#_Use_default_IDE_to_run_RAAD_main-label]

.. [#_Option_5]

Option 5 Intel Pre-made image of Ubuntu 22.04 LTS
**************************************************
1. Download VMWare workstation player
       * https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html
2. Decompress the image
       * To decompress the virtual machine download and install 7-Zip
       * https://www.7-zip.org/download.html
       * Decompress the image/RAAD/vm_ubuntu_22.04_x86_64/vm.7z
3. Run RAAD
       * Once installed open vmware workstation player and select File -> Open...
4. Select the file: RAAD/vm_ubuntu_22.04_x86_64/RAAD_Testing_U22LTSx8664/RAAD_Testing_U22LTSx8664.vmx
       * User and password pairs are:
       * raad_admin, raad
       * raaduser, raad
       * developer, raad_dev
       * tester, raad_tester
5. Login to raaduser
        * Note Anaconda is installed at: /opt/anaconda3
        * Symbolic link is: /home/raad/anaconda3 ->/opt/anaconda3
6. See [#_Clone_Repository-label]
7. See [#_Install_RAAD_Ubuntu_Script_for_Requirements-label]
8. See [#_Use_default_IDE_to_run_RAAD_main-label]

.. [#_Clone_Repository-label]

Clone Repository
========================================

Right click on desktop and select 'Open in Terminal'

    .. code-block::

        cd ~/Desktop
        mkdir -p github
        cd github
        git clone --recursive https://github.com/intel/RAAD.git

.. [#_Install_RAAD_Ubuntu_Script_for_Requirements-label]

Install RAAD Ubuntu Script for Requirements
============================================
1. Install script is at

    .. code-block::

        https://github.com/intel/RAAD/blob/main/vm_ubuntu_22.04_x86_64/UbuntuInstall.sh

2. To install requirements run the script open a terminal and type

    .. code-block::

        cd RAAD
        chmod +x UbuntuInstall.sh
        ./UbuntuInstall.sh

.. [#_Use_default_IDE_to_run_RAAD_main-label]

Use default IDE to run RAAD main.py
===================================
- A setup IDE is PyCharm community
    * Menu -> Programming -> PyCharm Community Edition
    * Within PyCharm select File-> Open
        + I.E. '/home/raaduser/Desktop/github/RAAD/'
    * To run the entry point of RAAD is:
        + I.E. '/home/raaduser/Desktop/github/RAAD/src/main.py'
    * Right click on main.py then Debug 'main.py
        + The default parameters will open the GUI interface.

.. [#_Option_6]

Option 6 Windows 10 x86_64 (Not Recommended)
**************************************************
.. include:: Anaconda_Windows.rst
.. include:: Anaconda_Windows_Installer.rst


Docker Helpers
===================================
To use the docker scripts type:

.. code-block::

	cd raad/vm_ubuntu_22.04_x86_64
	source dockerHelp.sh


Show all docker containers running
***************************************
.. code-block::

	dr-ps

Run specific command inside docker container without login into a container
*******************************************************************************
syntax: cr-cmd <container> <command>

.. code-block::

	dr-cmd my-container ls -la


Run a docker image
*******************

.. code-block::

	dr-run <image>


Log in to specific docker container
************************************

.. code-block::

	dr-sh <container>


Show container logs for docker container
********************************************
.. code-block::

	dr-log <container>

Build and run container on port 8080
*************************************

.. code-block::

	dr-build <image:tag> <inside-port>


Reset docker container and its image
*************************************

.. code-block::

	dr-reset

To run container that exited
********************************

.. code-block::

	dr-run-dead <image-name>


Reset/truncate docker container logs
****************************************

.. code-block::

	dr-reset-log

## Remove all unused images
****************************

.. code-block::

	dr-clean