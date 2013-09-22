# coding unicode-escape
# Made by DrRadical15
# Modify and redistribute as you wish

from pymclevel import TAG_String

displayName = "Sectional and Newline Placeholders"

inputs = (
	("Sectional Sign Placeholder", ("string","value=%")),
	("Newline Sequence Placeholder", ("string","value=%n")),
)

def perform(level, box, options):

	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			x = t["x"].value
			y = t["y"].value
			z = t["z"].value
      
			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				if t["id"].value == "Control":
					newcmd = t["Command"].value.replace(options["Newline Sequence Placeholder"], "\n").replace(options["Sectional Sign Placeholder"], unichr(167))

					t["Command"] = TAG_String(newcmd)
					chunk.dirty = True
