#!/bin/bash

echo "HELLO SHELL SCRIPT WORLD!"
echo ---------------------------------------
cpu_temp0=$(cat /sys/class/thermal/thermal_zone0/temp)

cpu_temp1=$(($cpu_temp0/1000))
cpu_temp2=$(($cpu_temp0/100))
cpu_tempM=$(($cpu_temp2 % $cpu_temp1))

echo CPU Temp"="$cpu_temp1"."$cpu_tempM "C"
echo GPU $(vcgencmd measure_temp)
echo ----------------------------------------
echo
echo RPI Intro......
echo
echo Ver. $(vcgencmd version)

echo
echo Config
echo $(vcgencmd get_config int)
