# Specify the base image
FROM ubuntu:22.04

# Set some appropriate metadata
LABEL maintainer="Intel Corporation"
LABEL version="1.0"
LABEL description="This is custom Docker Image built for running RAAD"

# Disable prompt during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Used for miniconda installation
ENV PATH="/opt/anaconda/bin:${PATH}"
ARG PATH="/opt/anaconda/bin:${PATH}"

# Updates, packages, get sudo
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y &&
    apt-get install sudo -y

# Add docker raaduser to sudo
RUN groupadd -g 999 raaduser && useradd -u 999 -g raaduser -G sudo -m -s /bin/bash raaduser && \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "raaduser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "Customized the sudoers file for passwordless access to the raaduser user!" && \
    echo "raaduser user:";  su - raaduser -c id

# Download all dependencies
RUN sudo apt-get install -f -y cmake gcc valgrind libssl-dev build-essential autoconf automake gdb git libffi-dev zlib1g-dev curl ssh ipmctl libipmctl-dev ledmon ndctl zfs-initramfs zfsutils-linux zfs-initramfs libzfslinux-dev zfs-auto-snapshot libvirt-daemon-driver-storage-zfs python3-pyzfs pyzfs-doc golang-go-zfs-dev libgtk-3-dev golang git nfs-common golang-github-gotk3-gotk3-dev btrfs-progs e2fsprogs f2fs-tools dosfstools hfsutils hfsprogs jfsutils mdadm util-linux cryptsetup dmsetup lvm2 util-linux nilfs-tools nilfs-tools ntfs-3g ntfs-3g reiser4progs reiserfsprogs reiserfsprogs udftools xfsprogs xfsdump gpart gedit samba rsync grsync rar unrar p7zip-full p7zip-rar openconnect libncurses5 libtinfo5 libz1 openvpn vpnc-scripts net-tools network-manager-openvpn network-manager-l2tp-gnome postfix libsasl2-modules ca-certificates mailutils ubuntu-mate-desktop mate-desktop-environment-extras mate-tweak gnome-tweaks wine texlive-pictures texlive-science texlive-latex-extra imagemagick secure-delete wipe bleachbit preload cpupower-gui indicator-cpufreq numad mdadm tuned redshift nvme-cli fio python-sphinx* linux-tools-virtual linux-tools-common linux-tools-generic linux-tools-`uname -r` libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 open-vm-tools-sdmp wget vim libpapi5.7 libpapi-dev papi-tools build-essential libssl-dev libz-dev time gdb clamav clamav-daemon
RUN sudo snap install pycharm-community --classic
RUN sudo snap install clion --classic

# Set working directory
RUN cd /home/raaduser
RUN sudo chmod -R 770 /home/raaduser
RUN git clone --recursive https://github.com/intel/RAAD.git RAAD
RUN sudo chmod -R 770 /home/raaduser/RAAD

# Update more Packages
RUN cd /home/raaduser/RAAD/vm_ubuntu_22.04_x86_64
RUN sudo chmod +x *
RUN bash -c 'sudo ./ubuntuPackages.sh'

# Prepare APPs
RUN sudo preload cpupower-gui indicator-cpufreq sysv-rc-conf numad    
RUN sudo ps ax | grep freshclamd
RUN sudo ps ax | grep [c]lamd
RUN sudo apt-get update
RUN sudo apt-get -y install clamav clamav-daemon
RUN sudo chown -R clamav:clamav /var/log/clamav
RUN sudo killall clamav
RUN sudo killall freshclam
RUN sudo service clamav-daemon stop
RUN sudo service clamav-freshclam stop
RUN sudo freshclam
RUN sudo service clamav-freshclam start
RUN sudo service clamav-daemon start
RUN sudo service --status-all | grep clamav
RUN sudo ps ax | grep freshclamd
RUN sudo ps ax | grep [c]lamd

# Install Anaconda
RUN cd /home/raaduser/RAAD/vm_ubuntu_22.04_x86_64
RUN sudo mkdir -p /opt/anaconda
RUN sudo chmod -R 770 /opt/anaconda
RUN wget -c https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O condaInstall.sh
RUN chmod +x *.sh
RUN bash -c 'condaInstall.sh -b -p /opt/anaconda'
RUN rm condaInstall.sh

# Setup Anaconda to shell
RUN cd /home/raaduser/RAAD/vm_ubuntu_22.04_x86_64
RUN bash -c './anacondaEnv.sh'

# Anaconda Prepare profile
RUN conda activate base
RUN conda config --add channels conda-forge
RUN conda config --set channel_priority true
RUN conda config --set always_yes true
RUN conda config --set allow_conda_downgrades true
RUN conda config --set auto_activate_base False
RUN conda config --set show_channel_urls true
RUN conda config --set auto_update_conda true
RUN conda config --set update_dependencies true
RUN conda config --set pip_interop_enabled false
RUN conda config --set ssl_verify true
RUN conda config --set allow_other_channels true
RUN conda config --set default_threads 4
RUN conda config --set verify_threads 4
RUN conda config --set execute_threads 4
RUN conda config --set repodata_threads 4
RUN conda config --set auto_activate_base true
RUN conda config --set report_errors false
RUN conda config --set allow_conda_downgrades true

# Perform upgrades
RUN cd /home/raaduser/RAAD/vm_ubuntu_22.04_x86_64
RUN bash -c 'sudo ./updateConda.sh'
RUN bash -c 'sudo ./getPkgsConda.sh'
RUN bash -c 'sudo ./raadConda.sh'
RUN bash -c 'sudo chmod -R 770 /opt/anaconda'
   
# Clean
RUN apt update \
    && apt clean
    
# Put system in low power mode
RUN sudo tuned-adm profile laptop-battery-powersave

# Prepare and run RAAD
RUN cd /home/raaduser/RAAD/src
RUN python main.py --help
