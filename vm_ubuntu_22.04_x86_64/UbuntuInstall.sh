# source .bashrc
sudo apt-get update && sudo apt-get upgrade -y
swapooff -a
sudo apt-get install -f -y cmake gcc valgrind libssl-dev build-essential autoconf automake gdb git libffi-dev zlib1g-dev curl ssh ipmctl libipmctl-dev ledmon ndctl zfs-initramfs zfsutils-linux zfs-initramfs libzfslinux-dev zfs-auto-snapshot libvirt-daemon-driver-storage-zfs python3-pyzfs pyzfs-doc golang-go-zfs-dev libgtk-3-dev golang git nfs-common golang-github-gotk3-gotk3-dev btrfs-progs e2fsprogs f2fs-tools dosfstools hfsutils hfsprogs jfsutils mdadm util-linux cryptsetup dmsetup lvm2 util-linux nilfs-tools nilfs-tools ntfs-3g ntfs-3g reiser4progs reiserfsprogs reiserfsprogs udftools xfsprogs xfsdump gpart gedit samba rsync grsync rar unrar p7zip-full p7zip-rar openconnect libncurses5 libtinfo5 libz1 openvpn vpnc-scripts net-tools network-manager-openvpn network-manager-l2tp-gnome postfix libsasl2-modules ca-certificates mailutils ubuntu-mate-desktop mate-desktop-environment-extras mate-tweak gnome-tweaks wine texlive-pictures texlive-science texlive-latex-extra imagemagick secure-delete wipe bleachbit preload cpupower-gui indicator-cpufreq numad mdadm tuned redshift nvme-cli fio python-sphinx* linux-tools-virtual linux-tools-common linux-tools-generic linux-tools-`uname -r` libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 open-vm-tools-sdmp
sudo snap install pycharm-community --classic
sudo snap install clion --classic
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y
sudo ./ubuntuPackages.sh
sudo preload cpupower-gui indicator-cpufreq sysv-rc-conf numad
# Optional Performance setup guide
# sudo sysctl vm.swappiness=1
# sudo gedit /etc/sysctl.conf 
# sudo gedit /etc/fstab
# sudo ufw logging off
# sudo chmod +x /etc/rc.local
# sudo gedit  /etc/pam.d/common-session
# sudo gedit /etc/pam.d/common-session-noninteractive
# sudo gedit /etc/security/limits.conf
# sudo gedit /etc/sysctl.conf
# sudo  sysctl -p
# Update Anti-Virus
sudo ps ax | grep freshclamd
sudo ps ax | grep [c]lamd
sudo apt-get update
sudo apt-get install clamav clamav-daemon
sudo chown -R clamav:clamav /var/log/clamav
sudo killall clamav
sudo killall freshclam
sudo service clamav-daemon stop
sudo service clamav-freshclam stop
sudo freshclam
sudo service clamav-freshclam start
sudo service clamav-daemon start
sudo service --status-all | grep clamav
sudo ps ax | grep freshclamd
sudo ps ax | grep [c]lamd
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y
# Enable Swap
swapon -a
# Anaconda
sudo mkdir -p /opt/anaconda
sudo chmod -R 770 /opt/anaconda
wget -c https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O condaInstall.sh
chmod +x *.sh
./condaInstall.sh -b -p /opt/anaconda
# Setup Anaconda to shell
__conda_setup="$('/opt/anaconda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda/bin:$PATH"
    fi
fi
unset __conda_setup
# Anaconda Prepare profile
conda activate base
conda config --add channels conda-forge
conda config --set channel_priority true
conda config --set always_yes true
conda config --set allow_conda_downgrades true
conda config --set auto_activate_base False
conda config --set show_channel_urls true
conda config --set auto_update_conda true
conda config --set update_dependencies true
conda config --set pip_interop_enabled false
conda config --set ssl_verify true
conda config --set allow_other_channels true
conda config --set default_threads 8
conda config --set verify_threads 8
conda config --set execute_threads 8
conda config --set repodata_threads 8
conda config --set auto_activate_base true
conda config --set report_errors false
conda config --set allow_conda_downgrades true
# Perform upgrades
sudo ./updateConda.sh
sudo ./getPkgsConda.sh
sudo ./raadConda.sh
sudo chmod -R 770 /opt/anaconda
# Put system in low power mode
sudo tuned-adm profile laptop-battery-powersave

