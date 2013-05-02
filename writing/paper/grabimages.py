#!/usr/bin/python
import os
import subprocess
def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()

call_command('../shargynxsecs/composites/shargynfault/make_composite.py')
call_command('../shargynxsecs/composites/bogdfault/make_composite.py')
call_command('../shargynxsecs/composites/intersectionwedge/make_composite.py')
call_command('../shargynxsecs/composites/khantaishir/make_composite.py')


files = dict()
files['./shargynfault.png'] = '../shargynxsecs/composites/shargynfault/final.png'
files['./bogdfaultxsecs.png'] = '../shargynxsecs/composites/bogdfault/final.png'
files['./intersectionwedgexsecs.png'] = '../shargynxsecs/composites/intersectionwedge/final.png'
files['./khantaishir.png'] = '../shargynxsecs/composites/khantaishir/final.png'
files['./gravity.ps.png'] = '../gravity/gravity.ps.png'
files['./magnetic.ps.png'] = '../magnetic/magnetic.ps.png'
files['./broad.png'] = '../broadfiguremine/broad.png'
files['./regional.png'] = '../regionalfigure/regional.png'
files['./basins.png'] = '../basintypesfigure/basins.png'
files['./asia.png'] = '../asiafigure/asia.png'
files['./bedrock.png'] = '../bedrockfigure/bedrockfigure.png'
files['./grain.png'] = '../grainfigure/grain.png'
files['./faultzones.png'] = '../faultscollage/faultscollage.png'
files['./schematic.png'] = '../schematicfaults/schematic.png'
files['./faultmap.png'] = '../maps/markedupfaultmap.png'

for key,value in files.iteritems():
	cmd = 'cp ' + value + ' ' + key
	print cmd
	call_command(cmd)

