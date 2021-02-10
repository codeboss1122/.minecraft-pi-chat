# minecraft-pi-chat
This a simple chat app written in python for Minecraft pi.

how to install:

1) open terminal on your raspberry pi.
2) run the following commands:

sudo git clone https://github.com/codeboss1122/.minecraft-pi-chat.git

sudo mv /home/pi/.minecraft-pi-chat/chat /home/pi/

sudo chmod 777 chat

3) make sure that minecraft is open and you are in a world, press the 'tab' key to release your mouse.
4) run:

./chat

5) type your in game username.
6) you can now chat.
7) to update:

cd .minecraft-pi-chat

sudo git pull

notes: There is a 3 second delay between sending a chat message and it showing in chat. this is to stop spamming. If the same message is sent in chat 3 times in a row it will exit the program. This is also a measure to stop spam.
