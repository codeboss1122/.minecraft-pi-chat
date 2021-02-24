from mcpi.minecraft import Minecraft
import time
l = ''



n = (input('what is your minecraft username? >'))
k = 4


b = 1
while True:

     mc = Minecraft.create()

     i = (input('>'))

     c = (i)

     time.sleep(3)

     mc.postToChat(c)

     mca = Minecraft.create()

     inp = (input('>'))

     ca = (inp)

     time.sleep(3)

     mca.postToChat(ca)

     mcb = Minecraft.create()

     inpu = (input('>'))

     cb = (i)
     
     time.sleep(3)

     mcb.postToChat(cb)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     j = "was temp muted for spamming" 
     no = (n, ",,",  j, ",", inp)

     if i == inp == inpu:
         mc.postToChat(no)
         break



