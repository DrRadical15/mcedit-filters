# Made by DrRadical15.
# Parts of this code include some of SethBling's code from Sandify. If you use, modify, or share this, please accredit him. (http://www.youtube.com/user/SethBling)
# The concept of making any block a slab was SimplySarc's. Please accredit him for the design and concept. (http://www.youtube.com/user/SimplySarc)

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Float
from pymclevel import TAG_Double
from pymclevel import TAG_String

displayName = "Slabify"

inputs = (
	("Can be stood on", True),
)

def perform(level, box, options):
	solid = options["Can be stood on"]
	for x in xrange(box.minx, box.maxx):
		for z in xrange(box.minz, box.maxz):
				y = box.maxy - 1
				block = level.blockAt(x, y, z)
				if block != 0:
					data = level.blockDataAt(x, y, z)
					te = level.tileEntityAt(x, y, z)
					
					if solid:
						level.setBlockAt(x, y, z, 140)
						level.setBlockDataAt(x, y, z, 0)
					else:
						level.setBlockAt(x, y, z, 0)
						level.setBlockDataAt(x, y, z, 0)

					sand = createSandEntity(x, y, z, block, data, 1)
					
					chunk = level.getChunk(x/16, z/16)

					if te != None:
						sand["TileEntityData"] = te
						chunk.TileEntities.remove(te)
					
					chunk.Entities.append(sand)

					y = y - 1
					level.setBlockAt(x, y, z, 36)
					level.setBlockDataAt(x, y, z, 0)

					y = y - 1
					level.setBlockAt(x, y, z, 85)
					level.setBlockDataAt(x, y, z, 0)

					chunk.dirty = True

def createSandEntity(x, y, z, block, data, time):
	sand = TAG_Compound()
	sand["id"] = TAG_String("FallingSand")
	sand["Motion"] = TAG_List()
	sand["Motion"].append(TAG_Double(0))
	sand["Motion"].append(TAG_Double(0))
	sand["Motion"].append(TAG_Double(0))
	sand["OnGround"] = TAG_Byte(1)
	sand["DropItem"] = TAG_Byte(0)
	sand["Dimension"] = TAG_Int(0)
	sand["Air"] = TAG_Short(300)
	sand["Pos"] = TAG_List()
	sand["Pos"].append(TAG_Double(x+0.5))
	sand["Pos"].append(TAG_Double(y))
	sand["Pos"].append(TAG_Double(z+0.5))
	sand["Data"] = TAG_Byte(data)
	sand["TileID"] = TAG_Int(block)
	if block >= 128:
		block = block - 256
	sand["Tile"] = TAG_Byte(block)
	sand["Time"] = TAG_Byte(time)
	sand["Fire"] = TAG_Short(-1)
	sand["FallDistance"] = TAG_Float(0)
	sand["Rotation"] = TAG_List()
	sand["Rotation"].append(TAG_Float(0))
	sand["Rotation"]. append(TAG_Float(0))
	
	return sand
