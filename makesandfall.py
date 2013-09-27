# Made by DrRadical15.
# Modify and redistribute as you wish.
from pymclevel.materials import alphaMaterials
displayName = "Make Sand Fall"
def perform(level, box, options):
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if level.blockAt(x,y,z) == 13 and level.blockAt(x,y-1,z) == 0:
					Y = y - 1
					while level.blockAt(x,Y,z) == 0:
						Y += -1
					level.setBlockAt(x,Y+1,z,ID_fall)
					level.setBlockDataAt(x,Y+1,z,data_fall)
					level.setBlockAt(x,y,z,0)
	level.markDirtyBox(box)
