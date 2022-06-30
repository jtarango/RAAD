# dpkg --get-selections > thisList.txt
sudo dpkg --clear-selections
sudo apt-get install dselect -y 
sudo dselect update
sudo apt-get update
sudo dpkg --set-selections < install_list.txt
sudo apt-cache dumpavail | sudo dpkg --merge-avail > clean.txt
sudo dpkg --set-selections < clean.txt
sudo apt-get deselect-upgrade
sudo dselect update
sudo apt-get upgrade -y
#rm -f clean.txt
