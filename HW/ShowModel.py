# Matt Pigliavento
# Siena College, Fall 2017

import viz
import vizcam

viz.window.setSize( 640, 480 )
viz.window.setName( "Model Viewer" )

window = viz.MainWindow

viz.MainWindow.clearcolor( [0,255,0] ) 

viz.eyeheight(0)

viz.add('room.dae')

vizcam.PanoramaNavigate()

vizcam.KeyboardCamera(forward='w',
                                 backward='s',
                                 left='q',
                                 right='e',
                                 up='r',
                                 down='f',
                                 turnRight='d',
                                 turnLeft='a',
                                 pitchDown='h',
                                 pitchUp='y',
                                 rollRight='j',
                                 rollLeft='g',
                                 moveMode=viz.REL_LOCAL,
                                 moveScale=1.0,
                                 turnScale=1.0)
viz.go()