
def isvoid(x,y,z):
    """check if block is air or water"""
    if mc.getBlock(x,y,z) == 0 or mc.getBlock(x,y,z) == 8 or mc.getBlock(x,y,z) == 9:
        return True
    else:
        return False


def lengthbridge(x,y,z,direction):
    l=0
    if direction is "North":
        if isvoid(x,y-1,z-1) is True or isvoid(x+1,y-1,z-1) is True:
#if at least one block is air or water the bridge must be built
#the block must be under the position of player
            i=1
            while isvoid(x,y-1,z-i) is True or isvoid(x+1,y-1,z-i) is True:
                i+=1
                if isvoid(x,y-1,z-i) is False and isvoid(x+1,y-1,z-i) is False:
#if both blocks are not air or water the bridge ends
                    l+=i-1
#length under the bridge aka void blocks
        else:
            lengthbridge(x,y,z-1,direction)
#if the player is not near void it searchs the nearest void block to begin the bridge
    if direction is "South":
        if isvoid(x,y-1,z+1) is True or isvoid(x-1,y-1,z+1) is True:
            i=1
            while isvoid(x,y-1,z+i) is True or isvoid(x-1,y-1,z+i) is True:
                i+=1
                if isvoid(x,y-1,z+i) is False and isvoid(x-1,y-1,z+i) is False:
                    l+=i-1
        else:
            lengthbridge(x,y,z+1,direction)
    if direction is "East":
        if isvoid(x+1,y-1,z) is True or isvoid(x+1,y-1,z+1) is True:
            i=1
            while isvoid(x+i,y-1,z) is True or isvoid(x+i,y-1,z+1) is True:
                i+=1
                if isvoid(x+i,y-1,z) is False and isvoid(x+i,y-1,z+1) is False:
                    l+=i-1
        else:
            lengthbridge(x+1,y,z,direction)
    if direction is "West":
        if isvoid(x-1,y-1,z) is True or isvoid(x-1,y-1,z-1) is True:
            i=1
            while isvoid(x-i,y-1,z) is True or isvoid(x-i,y-1,z-1) is True:
                i+=1
                if isvoid(x-i,y-1,z) is False and isvoid(x-i,y-1,z-1) is False:
                    l+=i-1
        else:
            lengthbridge(x-1,y,z,direction)
    print(l)
    return l


def bridge(x,y,z,direction,blocktype):
    l=lengthbridge(x,y,z,direction)
    if l>5:
#2 blocks of stairs 1 normal block and 2 blocks of stairs minimum
        if blocktype is "COBBLESTONE":
#block in order to have stairs and blcoks matching
            stairs=67
            block=4
        if blocktype is "WOOD":
            stairs=53
            block=5
#other stairs type not in pdf I have to search on internet
        i=1
        if direction is "North":
            while True:
#Find start point
                if isvoid(x,y-1,z-i) is True or isvoid(x+1,y-1,z-i) is True:
                    xs,ys,zs=x,y-1,z-i
                    break
                else:
                    i+=1
#1st stage
            mc.setBlock(xs-1,ys+1,zs+2,stairs,3)
            mc.setBlock(xs+2,ys+1,zs+2,stairs,3)
            mc.setBlocks(xs,ys+1,zs+1,xs+1,ys+1,zs+1,stairs,3)
            mc.setBlock(xs-1,ys+1,zs+1,block)
            mc.setBlock(xs+2,ys+1,zs+1,block)            
            mc.setBlocks(xs-1,ys+1,zs,xs+2,ys+1,zs,stairs,6)
            mc.setBlock(xs-1,ys+1,zs-l-1,stairs,2)
            mc.setBlock(xs+2,ys+1,zs-l-1,stairs,2)
            mc.setBlocks(xs,ys+1,zs-l,xs+1,ys+1,zs-l,stairs,2)
            mc.setBlock(xs-1,ys+1,zs-l,block)
            mc.setBlock(xs+2,ys+1,zs-l,block)
            mc.setBlocks(xs-1,ys+1,zs-l+1,xs+2,ys+1,zs-l+1,stairs,7)            
#2nd stage
            mc.setBlock(xs-1,ys+2,zs+1,stairs,3)
            mc.setBlock(xs+2,ys+2,zs+1,stairs,3)
            mc.setBlocks(xs,ys+2,zs,xs+1,ys+2,zs,stairs,3)
            mc.setBlock(xs-1,ys+2,zs,block)
            mc.setBlock(xs+2,ys+2,zs,block)
            mc.setBlock(xs-1,ys+2,zs-1,stairs,6)
            mc.setBlock(xs+2,ys+2,zs-1,stairs,6)
            mc.setBlock(xs-1,ys+2,zs-l,stairs,2)
            mc.setBlock(xs+2,ys+2,zs-l,stairs,2)
            mc.setBlock(xs-1,ys+2,zs-l+1,block)
            mc.setBlock(xs+2,ys+2,zs-l+1,block)
            mc.setBlock(xs-1,ys+2,zs-l+2,stairs,7)
            mc.setBlock(xs+2,ys+2,zs-l+2,stairs,7)
            mc.setBlocks(xs,ys+2,zs-l+1,xs+1,ys+2,zs-l+1,stairs,2)
            mc.setBlocks(xs,ys+2,zs-1,xs+1,ys+2,zs-l+2,block)
            mc.setBlocks(xs-1,ys+2,zs-2,xs-1,ys+2,zs-l+3,stairs,4)
            mc.setBlocks(xs+2,ys+2,zs-2,xs+2,ys+2,zs-l+3,stairs,5)
#3rd stage
            mc.setBlocks(xs-1,ys+3,zs,xs-1,ys+3,zs-l+1,block)
            mc.setBlocks(xs+2,ys+3,zs,xs+2,ys+3,zs-l+1,block)

            
            

            
##lengthbridge(xp,yp,zp,"North")


bridge(xp,yp,zp,"North","WOOD")