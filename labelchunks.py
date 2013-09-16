# Made by DrRadical15.
# Modify and redistribute as you wish.
from pymclevel.materials import alphaMaterials
displayName = "Label Chunks"
inputs = (
	("Border Block", alphaMaterials.Stone),
)
def perform(level, box, options):
	block = options["Border Block"].ID
	data = options["Border Block"].blockData

	for x in xrange(box.minx, box.maxx):
		for z in xrange(box.minz, box.maxz):
			if (x / 16) * 16 == x or ((x + 1) / 16) * 16 == x + 1 or (z / 16) * 16 == z or ((z + 1) / 16) * 16 == z + 1:
				level.setBlockAt(x, box.miny, z, block)
				level.setBlockDataAt(x, box.miny, z, data)
	level.markDirtyBox(box)
