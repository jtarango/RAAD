# Setup Options
 1. **Native OS Ubuntu 22.04 LTS**
 2. **Ubuntu 22.04 LTS Docker**
 3. **Create your own image of Ubuntu 22.04 LTS**
 4. **Use a partial make image of Ubuntu 22.04 LTS**
 5. **Intel Pre-made image of Ubuntu 22.04 LTS** (Not supported yet, pending release process)
 6. **Windows 10 x86_64 (Not Recommended)**

## Option 1: Ubuntu 22.04 LTS
4. Proceed to 'Clone Repository'
5. Proceed to 'Install RAAD Ubuntu Script for Requirements'
5. Proceed to 'Use default IDE to run RAAD main.py'

## Option 2: Ubuntu 22.04 LTS Docker

1. Setup Docker
   * https://docs.docker.com/engine/install/ubuntu/
2. Proceed to 'Clone Repository'
3. Run Docker
   ``` 
   cd RAAD/vm_ubuntu_22.04_x86_64
   docker build
   ```
4. Proceed to 'Install RAAD Ubuntu Script for Requirements'
5. Proceed to 'Use default IDE to run RAAD main.py'   

## Option 3: Create your own image of Ubuntu 22.04 LTS
1. Create Ubuntu download image at:
   * https://ubuntu-mate.org/download/amd64/jammy/
2. To use the virtual machine download VMWare workstation player
   * https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html
3. Follow steps:
   * https://kb.vmware.com/s/article/1018415
   * https://kb.vmware.com/s/article/1018414
4. Proceed to 'Clone Repository'
5. Proceed to 'Install RAAD Ubuntu Script for Requirements'
6. Proceed to 'Use default IDE to run RAAD main.py'

## Option 4: Use a partial make image of Ubuntu 22.04 LTS
1. To download semi-pre-made image:
   * https://sourceforge.net/projects/osboxes/files/v/vm/55-U--u/22.04/64bit.7z/download
2. Login info is located at:
   * https://www.osboxes.org/faq/what-are-the-credentials-for-virtual-machine-image/
3. Install vitural machine tools
   * https://kb.vmware.com/s/article/1018414
4. Proceed to 'Clone Repository'
5. Proceed to 'Install RAAD Ubuntu Script for Requirements'
6. Proceed to 'Use default IDE to run RAAD main.py'

## Option 5: Intel Pre-made image of Ubuntu 22.04 LTS
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
6. Proceed to 'Clone Repository'
7. Proceed to 'Install RAAD Ubuntu Script for Requirements'
8. Proceed to 'Use default IDE to run RAAD main.py'

## Option 6 Windows 10 x86_64 (Not Recommended)
1. Goto Setup section in /dox/source/setup.rst


# Clone Repository
Right click on desktop and select 'Open in Terminal'
```
cd ~/Desktop
mkdir -p github
cd github
git clone --recursive https://github.com/intel/RAAD.git
```

# Install RAAD Ubuntu Script for Requirements
1. Install script is at
   * https://github.com/intel/RAAD/blob/main/vm_ubuntu_22.04_x86_64/UbuntuInstall.sh
2. To install requirements run the script open a terminal and type
    ```
    cd RAAD
    chmod +x UbuntuInstall.sh
    ./UbuntuInstall.sh
    ```

# Use default IDE to run RAAD main.py
* A setup IDE is PyCharm community
    * Menu -> Programming -> PyCharm Community Edition
    * Within PyCharm select File-> Open 
      * I.E. '/home/raaduser/Desktop/github/RAAD/'
    * To run the entry point of RAAD is: 
      * I.E. '/home/raaduser/Desktop/github/RAAD/src/main.py'
    * Right click on main.py then Debug 'main.py
      * The default parameters will open the GUI interface.
      
      
# Docker Helpers
To use the docker scripts type:
```
cd raad/vm_ubuntu_22.04_x86_64
source dockerHelp.sh
```

## Show all docker containers running
```
dr-ps
```

## Run specific command inside docker container without login into a container
## syntax: cr-cmd <container> <command>
```
dr-cmd my-container ls -la
```

## Run a docker image
```
dr-run <image>
```

## Log in to specific docker container
```
dr-sh <container>
```

## Show container logs for docker container
```
dr-log <container>
```

## Build and run container on port 8080
```
dr-build <image:tag> <inside-port>
```

## Reset docker container and its image
```
dr-reset
```

## To run container that exited
```
dr-run-dead <image-name>
```

## Reset/truncate docker container logs
```
dr-reset-log
```

## Remove all unused images
```
dr-clean
```
