# Reverse Vending Machine (Vegeta)

This repository contains the scripts and code for the Reverse Vending Machine project. This is a Data Science project where we used a RaspberryPI 3, and a Deep Learning model to create a reverse vending machine targeted for the tunisian market, specializing in the classification of plastic bottles and aluminum/metal cans. The users have the chance to receive points/vouchers for the type of object they insert into the vending machine.

####
For more information on how a reverse vending machine works :
* https://www.youtube.com/watch?v=i-AVw1gl6Xw
* https://www.youtube.com/watch?v=3dnJtUoCu2I

The "Vegeta Reverse Vending Machine" does not rely on expensive sensors to detect the type of the object inserted, it uses AI : Deep Learning to classify the object that is detected by a cheap 1080p HD IR camera.


####
The types of the objects which the deep learning model has been trained on :

* Plastic bottles, ranging from 25cl to 2 liters.
* Aluminum/Metal cans.

####

## Examples
![Data Examples Bottles](https://i.imgur.com/YCAkEfw.png)

## RasperryPI Setup :
A Raspberry PI 3 Model B running on Rasipan OS has been used for this project. The main code that has been used for taking the picture can be found in the __Vending_Machine_Python_Script.py__ file.

Here's how we setup the card and the components :
![Pi Connections](https://i.imgur.com/8yZzEPn.jpg)

For the Demo Videos :
* [Reverse Vending Machine Web Application](https://www.youtube.com/watch?v=i-AVw1gl6Xw&feature=youtu.be)
* [Reverse Vending Facial Recognition](https://youtu.be/3dnJtUoCu2I)
