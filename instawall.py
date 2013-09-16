# Made by DrRadical15.
# Modify and redistribute as you wish.
from pymclevel.materials import alphaMaterials
displayName = "Insta-Wall"
inputs = (
	("Thickness", 1),
	("Block", alphaMaterials.StoneBricks),
	("Block Being Replaced", alphaMaterials.Air),
	("Replace Any Block", False),
)
def perform(level, box, options):
	block = options["Block"].ID
	data = options["Block"].blockData
	thickness = options["Thickness"]
	replace = options["Block Being Replaced"].ID
	replaceData = options["Block Being Replaced"].blockData
	anyBlock = options["Replace Any Block"]

	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if (x <= box.minx - 1 + thickness or x >= box.maxx - thickness or z <= box.minz - 1 + thickness or z >= box.maxz - thickness) and (anyBlock or (level.blockAt(x,y,z) == replace and level.blockDataAt(x,y,z) == replaceData)):
					level.setBlockAt(x, y, z, block)
					level.setBlockDataAt(x, y, z, data)
	level.markDirtyBox(box)
