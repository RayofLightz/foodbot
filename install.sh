#!/bin/bash

echo What is the bots email ?

read bot_email

echo What is the bots password ?

read bot_password

echo Who should the emails be sent to ?

read user_email

echo Creating the config file

mkdir $HOME/.config/
cp foodbot.json $HOME/.config/

sed -i "s/<0>/$bot_email/" "$HOME/.config/foodbot.json"
sed -i "s/<1>/$bot_password/" "$HOME/.config/foodbot.json"
sed -i "s/<2>/$user_email/" "$HOME/.config/foodbot.json"
