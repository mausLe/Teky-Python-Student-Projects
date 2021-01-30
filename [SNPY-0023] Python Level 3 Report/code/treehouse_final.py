from mcpi.minecraft import Minecraft
from mcpi import block
import time, random
mc = Minecraft.create()

mc.postToChat("Building a tree house!")

# building a tree
x, y, z = (20, 0, 0)
mc.setBlocks(x + 10, y, z + 5, x + 20, y + 20, z + 15, block.WOOD)
mc.setBlocks(x+11,y + 1,z+6,x+19,y+18,z+14,block.AIR)
3
# Tree
# mc.setBlocks(x, y+20,z-5,x+30,y+22,z+35,block.AIR)

for i in range(10):
	mc.setBlocks(x+5 - 17 + i*2, y+20+i,z - 17 + i*2,x+24 + 17 - i*2,y+21+i,z+19 + 17 - i*2,block.LEAVES)

# Door
# mc.setBlock (35,0,14,block.DOOR_DARK_OAK)

mc.setBlocks (38,10,15, 39,11,15, block.GLASS)

mc.setBlocks (31,10,15, 32,11,15, block.GLASS)

mc.setBlocks (33,0,15, 37,7,15, block.AIR)


height = 20
center = 25,21,10  #x,y,z
for i in range(height*height):
	randomx = random.randint(center[0] - height, center[0] + height)
	randomz = random.randint(center[2] - height, center[2] + height)
	mc.setBlock(randomx,center[1] + 1, randomz,block.LEAVES)