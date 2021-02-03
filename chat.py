from mcpi.minecraft import Minecraft

l = ','

n = (input('what is your minecraft username? >'))

b = 1
while True:

     mc = Minecraft.create()

     i = (input('>'))

     c = (n,  l,  i)

     mc.postToChat(c)
