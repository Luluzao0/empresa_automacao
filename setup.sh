#!/bin/bash

# Instalar Xvfb
apt-get update
apt-get install -y xvfb

# Iniciar Xvfb
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99
