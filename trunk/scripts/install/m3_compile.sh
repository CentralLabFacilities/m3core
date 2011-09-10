#!/bin/bash

echo "Starting M3 compile."

#cd ~/mekabot/m3

make proto_base
sudo make proto_base_install
make base
sudo make base_install
make rt_system
sudo make rt_system_install
make proto
sudo make proto_install
make toolbox
sudo make toolbox_install
make hardware
sudo make hardware_install
make chains
sudo make chains_install
make
sudo make install

echo "compile finished."

exit 0

