conda activate base
conda clean --all
conda create --name raad python==3.8
conda activate raad
./getPkgsConda.sh
conda env update -f ../environment_ubuntu-x86_64.yml

