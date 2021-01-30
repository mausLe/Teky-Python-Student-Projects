from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,math,random

x, y, z = 0, 0, 0
mc.player.setTilePos(x, y, z)

time.sleep(3)

base_height = 60
middle_height =  base_height / 2
top_height = base_height / 4

# TREE
def tree(x,y,z):
    mc.setBlocks(x-1,y,z-1,x+1,y+5,z+1,17)
    mc.setBlocks(x-2,y+5,z-2,x+2,y+6,z+2,18)
    mc.setBlocks(x-4,y+7,z-4,x+4,y+9,z+4,18)
    mc.setBlocks(x-3,y+10,z-3,x+3,y+10,z+3,18)
    mc.setBlocks(x-2,y+11,z-2,x+2,y+12,z+2,18)
    mc.setBlocks(x-1,y+13,z-1,x+1,y+13,z+1,18)
    
def amazon(x,y,z):
    for i in range(10):
        for k in range(10):
            tree(x+12*i,y,z+12*k)

# SKYSCRAPERS

def base(x, y, z):
    mc.setBlocks(x - 5, y, z - 5, x + 15, y + 10, z + 15, 1)

def floor(x,y,z):
    mc.setBlocks(x,y,z,x+10,y+8,z+10,95,3)
    mc.setBlocks(x+1,y+1,z+1,x+9,y+7,z+9,0)
    mc.setBlocks(x,y+8,z,x+10,y+8,z+10,41)

def skyscraper(x,y,z, nb_floor):
    # base(x, y, z)
    for i in range(nb_floor):
        floor(x,y+i*9,z)

# x,y,z = mc.player.getPos()
x, y, z = 0, 0, 110
for i in range(2):
    skyscraper(x + 20*i,y,z, i*4)

x, y, z = -20, 0, 0

floorX = x - 2
floorY = 0
floorZ = z - 2

width = 20
length = 10
block_id = 41

mc.setBlocks(floorX, floorY, floorZ, floorX, floorY, floorZ + length, block_id)

if block_id == 41:
    block_id = 57
else:
    block_id = 41
mc.setBlocks(floorX, floorY, floorZ, floorX, floorY, floorZ + length, block_id)

block_type = 155

xs2, ys2, zs2 = 40, 0, 110
# base
mc.setBlocks(xs2, ys2, zs2, xs2 + 9 - 1, ys2 + base_height - 1, zs2 + 9 - 1, block_type)
# Middle
mc.setBlocks(xs2 + 2, ys2 + base_height , zs2 + 2, xs2 + 2 + 5 - 1, ys2 + base_height + middle_height - 1, zs2 + 2 + 5 - 1, block_type)
# top
mc.setBlocks(xs2 + 4, ys2 + base_height + middle_height, zs2 + 4, xs2+ 4 + 1 - 1, ys2 + base_height + middle_height + top_height - 1, zs2 + 4 + 1 - 1, block_type)

xs3, ys3, zs3 = 0, 0, 110
# base
mc.setBlocks(xs3, ys3, zs3, xs3 + 9 - 1, ys3 + base_height - 1, zs3 + 9 - 1, block_type)
# Middle
mc.setBlocks(xs3 + 2, ys3 + base_height , zs3 + 2, xs3 + 2 + 5 - 1, ys3 + base_height + middle_height - 1, zs3 + 2 + 5 - 1, block_type)
# top
mc.setBlocks(xs3 + 4, ys3 + base_height + middle_height, zs3 + 4, xs3 + 4 + 1 - 1, ys3 + base_height + middle_height + top_height - 1, zs3 + 4 + 1 - 1, block_type)

# HOUSE

width = 20
height = 7
length = 10

block_type = 5 # cobblestone
air = 0

xh, yh, zh = 4, 0, 155
# house block
mc.setBlocks(xh, yh, zh, xh + width - 1, yh + height - 1, zh + length - 1, block_type)

# space in house
mc.setBlocks(xh + 1, yh + 1, zh + 1, xh + width - 1 - 1, yh + height - 1 - 1, zh + length - 1 - 1, air)

# door
dw = 2
dh = 3
dl = 1
mc.setBlocks(xh + width/2 - dw/2, yh, zh, xh + width/2 + dw/2 - 1, yh + dh - 1, zh + dl - 1, air)

# right window
ww = 2
wh = 2
wl = 1
mc.setBlocks(xh + 1 , yh + 4, zh, xh + 1 + ww - 1 , yh + 4 + wh - 1 , zh - wl - 1 , air)

# left window
mc.setBlocks(xh + width - 1 - ww , yh + 4, zh, xh + width - 1 - 1 , yh + 4 + wh - 1 , zh - wl - 1 , air)

xh2, yh2, zh2 = 26, 0, 155
# house block
mc.setBlocks(xh2, yh2, zh2, xh2 + width - 1, yh2 + height - 1, zh2 + length - 1, block_type, 1)

# space in house
mc.setBlocks(xh2 + 1, yh2 + 1, zh2 + 1, xh2 + width - 1 - 1, yh2 + height - 1 - 1, zh2 + length - 1 - 1, air)

# door
dw = 2
dh = 3
dl = 1
mc.setBlocks(xh2 + width/2 - dw/2, yh2, zh2, xh2 + width/2 + dw/2 - 1, yh2 + dh - 1, zh2 + dl - 1, air)

# right window
ww = 2
wh = 2
wl = 1
mc.setBlocks(xh2 + 1 , yh2 + 4, zh2, xh2 + 1 + ww - 1 , yh2 + 4 + wh - 1 , zh2 - wl - 1 , air)

# left window
mc.setBlocks(xh2 + width - 1 - ww , yh2 + 4, zh2, xh2 + width - 1 - 1 , yh2 + 4 + wh - 1 , zh2 - wl - 1 , air)

# LAVA POOL

xp, yp, zp = (0, 0,0)
lava = 11
# Original x, z
mc.setBlock(xp, yp - 1, zp, lava)
# Front of player
mc.setBlock(x, y - 1, z + 1, lava)
# Back of player
mc.setBlock(x, y - 1, z - 1, lava)
# Left of player
mc.setBlock(x + 1, y - 1, z, lava)
# Right of player
mc.setBlock(x - 1, y - 1, z, lava)
# Left forward of player
mc.setBlock(x + 1, y - 1, z + 1, lava)
# Left backward of player
mc.setBlock(x + 1, y - 1, z - 1, lava)
# Right forward of player
mc.setBlock(x - 1, y - 1, z + 1, lava)
# Right back of player
mc.setBlock(x - 1, y - 1, z - 1, lava)

# SWIMMING POOL

# pool dimensions
d = 3
# The width is twice the depth
w = d * 2
# The length to be three times to depth
l = d * 4

# Define the block types
block_type = 41
water = 9
xp, yp, zp = 1, 0, 132
# pool outer walls
mc.setBlocks(xp , yp - 1 , zp, xp + w - 1, yp - 1 - d + 1, zp + l - 1, block_type)

# water part
mc.setBlocks(xp + 1 , yp - 1 , zp + 1, xp + w - 1 - 1, yp - 1 - d + 1 + 1, zp + l - 1 - 1, water)

xp2, yp2, zp2 = 7, 0, 132
# pool outer walls
mc.setBlocks(xp2 , yp2 - 1 , zp2, xp2 + w - 1, yp2 - 1 - d + 1, zp2 + l - 1, block_type)

# water part
mc.setBlocks(xp2 + 1 , yp2 - 1 , zp2 + 1, xp2 + w - 1 - 1, yp2 - 1 - d + 1 + 1, zp2 + l - 1 - 1, water)

xp3, yp3, zp3 = 13, 0, 132
# pool outer walls
mc.setBlocks(xp3 , yp3 - 1 , zp3, xp3 + w - 1, yp3 - 1 - d + 1, zp3 + l - 1, block_type)

# water part
mc.setBlocks(xp3 + 1 , yp3 - 1 , zp3 + 1, xp3 + w - 1 - 1, yp3 - 1 - d + 1 + 1, zp3 + l - 1 - 1, water)

xp4, yp4, zp4 = 19, 0, 132
# pool outer walls
mc.setBlocks(xp4 , yp4 - 1 , zp4, xp4 + w - 1, yp4 - 1 - d + 1, zp4 + l - 1, block_type)

# water part
mc.setBlocks(xp4 + 1 , yp4 - 1 , zp4 + 1, xp4 + w - 1 - 1, yp4 - 1 - d + 1 + 1, zp4 + l - 1 - 1, water)

xp5, yp5, zp5 =25, 0, 132
# pool outer walls
mc.setBlocks(xp5 , yp5 - 1 , zp, xp5 + w - 1, yp5 - 1 - d + 1, zp5 + l - 1, block_type)

# water part
mc.setBlocks(xp5 + 1 , yp5 - 1 , zp5 + 1, xp5 + w - 1 - 1, yp5 - 1 - d + 1 + 1, zp5 + l - 1 - 1, water)

xp6, yp6, zp6 = 31, 0, 132
# pool outer walls
mc.setBlocks(xp6 , yp6 - 1 , 6, xp6 + w - 1, yp6 - 1 - d + 1, zp6 + l - 1, block_type)

# water part
mc.setBlocks(xp6 + 1 , yp6 - 1 , zp6 + 1, xp6 + w - 1 - 1, yp6 - 1 - d + 1 + 1, zp6 + l - 1 - 1, water)

xp7, yp7, zp7 = 37, 0, 132
# pool outer walls
mc.setBlocks(xp7 , yp7 - 1 , zp7, xp7 + w - 1, yp7 - 1 - d + 1, zp7 + l - 1, block_type)

# water part
mc.setBlocks(xp7 + 1 , yp7 - 1 , zp7 + 1, xp7 + w - 1 - 1, yp7 - 1 - d + 1 + 1, zp7 + l - 1 - 1, water)

xp8, yp8, zp8 =43, 0, 132
# pool outer walls
mc.setBlocks(xp8 , yp8 - 1 , zp8, xp8 + w - 1, yp8 - 1 - d + 1, zp8 + l - 1, block_type)

# water part
mc.setBlocks(xp8 + 1 , yp8 - 1 , zp8 + 1, xp8 + w - 1 - 1, yp8 - 1 - d + 1 + 1, zp8 + l - 1 - 1, water)

# SMALL RAINBOW STRUCTURE

wool = 35

xr, yr, zr = 10, 0, 125
# purple wool in original x
mc.setBlock(xr, yr - 1, zr, wool,10)
mc.setBlock(xr + 1, yr, zr, wool,10)
mc.setBlock(xr + 2, yr - 1, zr, wool,10)

# Increase y to place next block above
yr = yr + 1

# Place the blue wool
mc.setBlock(xr, yr - 1, zr, wool,11)
mc.setBlock(xr + 1, yr, zr, wool,11)
mc.setBlock(xr + 2, yr - 1, zr, wool,11)

# Increase y to place next block above
yr = yr + 1

# green wool
mc.setBlock(xr, yr - 1, zr, wool,13)
mc.setBlock(xr + 1, yr, zr, wool,13)
mc.setBlock(xr + 2, yr - 1, zr, wool,13)

# Increase y to place next block above
yr = yr + 1
# yellow wool
mc.setBlock(xr, yr - 1, zr, wool,4)
mc.setBlock(xr + 1, yr, zr, wool,4)
mc.setBlock(xr + 2, yr - 1, zr, wool,4)

# Increase y to place next block above
yr = yr + 1

# orange wool
mc.setBlock(xr, yr - 1, zr, wool,1)
mc.setBlock(xr + 1, yr, zr, wool,1)
mc.setBlock(xr + 2, yr - 1, zr, wool,1)

# Increase y to place next block above
yr = yr + 1

# red wool block
mc.setBlock(xr, yr - 1, zr, wool,14)
mc.setBlock(xr + 1, yr, zr, wool,14)
mc.setBlock(xr + 2, yr - 1, zr, wool,14)

# 2

xr2, yr2, zr2 = 25, 0, 125
# purple wool in original x
mc.setBlock(xr2, yr2 - 1, zr2, wool,10)
mc.setBlock(xr2 + 1, yr2, zr2, wool,10)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,10)

# Increase y to place next block above
yr2 = yr2 + 1

# Place the blue wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,11)
mc.setBlock(xr2 + 1, yr2, zr2, wool,11)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,11)

# Increase y to place next block above
yr2 = yr2 + 1

# green wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,13)
mc.setBlock(xr2 + 1, yr2, zr2, wool,13)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,13)

# Increase y to place next block above
yr2 = yr2 + 1
# yellow wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,4)
mc.setBlock(xr2 + 1, yr2, zr2, wool,4)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,4)

# Increase y to place next block above
yr2 = yr2 + 1

# orange wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,1)
mc.setBlock(xr2 + 1, yr2, zr2, wool,1)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,1)

# Increase y to place next block above
yr2 = yr2 + 1

# red wool block
mc.setBlock(xr2, yr2 - 1, zr2, wool,14)
mc.setBlock(xr2 + 1, yr2, zr2, wool,14)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,14)

# 3

xr3, yr3, zr3 = 40, 0, 125
# purple wool in original x
mc.setBlock(xr3, yr3 - 1, zr3, wool,10)
mc.setBlock(xr3 + 1, yr3, zr3, wool,10)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,10)

# Increase y to place next block above
yr3 = yr3 + 1

# Place the blue wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,11)
mc.setBlock(xr3 + 1, yr3, zr3, wool,11)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,11)

# Increase y to place next block above
yr3 = yr3 + 1

# green wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,13)
mc.setBlock(xr3 + 1, yr3, zr3, wool,13)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,13)

# Increase y to place next block above
yr3 = yr3 + 1
# yellow wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,4)
mc.setBlock(xr3 + 1, yr3, zr3, wool,4)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,4)

# Increase y to place next block above
yr3 = yr3 + 1

# orange wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,1)
mc.setBlock(xr3 + 1, yr3, zr3, wool,1)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,1)

# Increase y to place next block above
yr3 = yr3 + 1

# red wool block
mc.setBlock(xr3, yr3 - 1, zr3, wool,14)
mc.setBlock(xr3 + 1, yr3, zr3, wool,14)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,14)

# OTHER SIDE 

xr, yr, zr = 10, 0, 148
# purple wool in original x
mc.setBlock(xr, yr - 1, zr, wool,10)
mc.setBlock(xr + 1, yr, zr, wool,10)
mc.setBlock(xr + 2, yr - 1, zr, wool,10)

# Increase y to place next block above
yr = yr + 1

# Place the blue wool
mc.setBlock(xr, yr - 1, zr, wool,11)
mc.setBlock(xr + 1, yr, zr, wool,11)
mc.setBlock(xr + 2, yr - 1, zr, wool,11)

# Increase y to place next block above
yr = yr + 1

# green wool
mc.setBlock(xr, yr - 1, zr, wool,13)
mc.setBlock(xr + 1, yr, zr, wool,13)
mc.setBlock(xr + 2, yr - 1, zr, wool,13)

# Increase y to place next block above
yr = yr + 1
# yellow wool
mc.setBlock(xr, yr - 1, zr, wool,4)
mc.setBlock(xr + 1, yr, zr, wool,4)
mc.setBlock(xr + 2, yr - 1, zr, wool,4)

# Increase y to place next block above
yr = yr + 1

# orange wool
mc.setBlock(xr, yr - 1, zr, wool,1)
mc.setBlock(xr + 1, yr, zr, wool,1)
mc.setBlock(xr + 2, yr - 1, zr, wool,1)

# Increase y to place next block above
yr = yr + 1

# red wool block
mc.setBlock(xr, yr - 1, zr, wool,14)
mc.setBlock(xr + 1, yr, zr, wool,14)
mc.setBlock(xr + 2, yr - 1, zr, wool,14)

# OTHER SIDE 2

xr2, yr2, zr2 = 25, 0, 148
# purple wool in original x
mc.setBlock(xr2, yr2 - 1, zr2, wool,10)
mc.setBlock(xr2 + 1, yr2, zr2, wool,10)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,10)

# Increase y to place next block above
yr2 = yr2 + 1

# Place the blue wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,11)
mc.setBlock(xr2 + 1, yr2, zr2, wool,11)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,11)

# Increase y to place next block above
yr2 = yr2 + 1

# green wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,13)
mc.setBlock(xr2 + 1, yr2, zr2, wool,13)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,13)

# Increase y to place next block above
yr2 = yr2 + 1
# yellow wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,4)
mc.setBlock(xr2 + 1, yr2, zr2, wool,4)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,4)

# Increase y to place next block above
yr2 = yr2 + 1

# orange wool
mc.setBlock(xr2, yr2 - 1, zr2, wool,1)
mc.setBlock(xr2 + 1, yr2, zr2, wool,1)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,1)

# Increase y to place next block above
yr2 = yr2 + 1

# red wool block
mc.setBlock(xr2, yr2 - 1, zr2, wool,14)
mc.setBlock(xr2 + 1, yr2, zr2, wool,14)
mc.setBlock(xr2 + 2, yr2 - 1, zr2, wool,14)

# OTHER SIDE 3

xr3, yr3, zr3 = 40, 0, 148
# purple wool in original x
mc.setBlock(xr3, yr3 - 1, zr3, wool,10)
mc.setBlock(xr3 + 1, yr3, zr3, wool,10)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,10)

# Increase y to place next block above
yr3 = yr3 + 1

# Place the blue wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,11)
mc.setBlock(xr3 + 1, yr3, zr3, wool,11)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,11)

# Increase y to place next block above
yr3 = yr3 + 1

# green wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,13)
mc.setBlock(xr3 + 1, yr3, zr3, wool,13)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,13)

# Increase y to place next block above
yr3 = yr3 + 1
# yellow wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,4)
mc.setBlock(xr3 + 1, yr3, zr3, wool,4)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,4)

# Increase y to place next block above
yr3 = yr3 + 1

# orange wool
mc.setBlock(xr3, yr3 - 1, zr3, wool,1)
mc.setBlock(xr3 + 1, yr3, zr3, wool,1)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,1)

# Increase y to place next block above
yr3 = yr3 + 1

# red wool block
mc.setBlock(xr3, yr3 - 1, zr3, wool,14)
mc.setBlock(xr3 + 1, yr3, zr3, wool,14)
mc.setBlock(xr3 + 2, yr3 - 1, zr3, wool,14)