#!/bin/bash
echo "Enter package name:";
read package;
PACK="Installing: ${package}";
line="beavis.zen blowfish bong bud-frogs bunny cheese cower daemon default dragon dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy supermilker surgery telebears three-eyes turkey turtle tux udder vader vader-koala www"
array=(`echo ${line}`)
size=${#array[@]}
index=$(($RANDOM % $size))
cowsay -f "${array[$index]}" $PACK; 
sudo pacman -S $package;
