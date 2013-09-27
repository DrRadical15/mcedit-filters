# Modified by DrRadical15.
# Created by SethBling.
# http://youtube.com/SethBling

import random

displayName = "Random Blocks 2"

inputs = (
	("One Block Per", 16),
	("Block", "blocktype"),
	("Block to Replace", "blocktype"),
	("Any Subtype of Block to Replace", False),
	("Replace any Block", False),
)

def perform(level, box, options):
	invFreq = options["One Block Per"]
	freq = 1.0 / invFreq
	block = options["Block"].ID
	data = options["Block"].blockData
	replace = options["Block to Replace"].ID
	replaceData = options["Block to Replace"].blockData
	anyData = options["Any Subtype of Block to Replace"]
	anyBlock = options["Replace any Block"]
	
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if anyBlock == False and (level.blockAt(x, y, z) == replace and (anyData == True or level.blockDataAt(x, y, z) == replaceData)) == False:
					continue
				if random.random() < freq:
					level.setBlockAt(x, y, z, block)
					level.setBlockDataAt(x, y, z, data)
	
	level.markDirtyBox(box)
