# Made by DrRadical15.
# Modify and redistribute as you wish.
from pymclevel.materials import alphaMaterials
displayName = "Make Blocks Fall"
inputs = (
	("Block to Make Fall",alphaMaterials.Sand),
	("Any Data Value",False),
	("Block to Take Place of Fallen Block",alphaMaterials.Air),
	(" Any Data Value ",False),
	("Block to Fall Through",alphaMaterials.Air),
	("  Any Data Value  ",False),
)
def perform(level, box, options):
	ID_fall = options["Block to Make Fall"].ID
	data_fall = options["Block to Make Fall"].blockData
	anyData_fall = options["Any Data Value"]

	ID_place = options["Block to Take Place of Fallen Block"].ID
	data_place = options["Block to Take Place of Fallen Block"].blockData
	anyData_place = options[" Any Data Value "]

	ID_through = options["Block to Fall Through"].ID
	data_through = options["Block to Fall Through"].blockData
	anyData_through = options["  Any Data Value  "]

	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if level.blockAt(x,y,z) == ID_fall and (level.blockAt(x,y-1,z) == data_fall or anyData_fall == True):
					Y = y - 1
					while level.blockAt(x,Y,z) == ID_through and (level.blockDataAt(x,Y,z) == data_through or anyData_through):
						Y += -1
					level.setBlockAt(x,Y+1,z,ID_fall)
					level.setBlockDataAt(x,Y+1,z,data_fall)
					level.setBlockAt(x,y,z,ID_place)
					level.setBlockDataAt(x,y,z,data_place)
	level.markDirtyBox(box)
