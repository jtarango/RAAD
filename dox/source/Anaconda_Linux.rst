Linux Ubuntu Mate x64
*********************
.. include_anaconda_linux

Anaconda Installation
======================

1. Download file

    .. code-block:: console

        wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
        chmod 755 Anaconda3-2020.07-Linux-x86_64.sh
        ./Anaconda3-2020.07-Linux-x86_64.sh -b -p $HOME/anaconda3

#. Open Anaconda
#. Change to repository directory
#. Recreate and update the base environment with the best known method.
    - Please note environment_ubuntu-x86_64.yml should be `environment_{operating system}.yml`

    .. code-block:: console

        conda update --force conda -y
        conda update anaconda -y
        conda update --all
        conda update anaconda-navigator
        conda update python
        conda env create --file environment_ubuntu-x86_64.yml

#. To update use

    .. code-block:: console

        conda env update -f environment_ubuntu-x86_64.yml

Jet Brains PyCharm Debugger
=============================
- https://www.jetbrains.com/pycharm/

.. code-block:: console

    sudo snap install pycharm-community --classic
