#!/bin/bash

echo "Misc Install settings"

sudo rm -f /bin/sh
sudo ln -s /bin/bash /bin/sh

sudo apt-get remove apparmor
sudo apt-get install bum
sudo bum

exit 0