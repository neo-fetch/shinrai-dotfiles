#!/bin/bash
playerctl metadata | \
	grep artUrl | \
	sed -e "s/spotify mpris:artUrl              //g"
