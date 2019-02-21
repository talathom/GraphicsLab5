# Solar.py
#
# Simulates a solar system using a hierarchical model.

import viz
from solarUtil import *

class Solar( viz.EventClass):
	
	def __init__(self):
		viz.EventClass.__init__(self)
		
		self.callback(viz.TIMER_EVENT, self.onTimer)
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.starttimer(0, (1.0/10.0), viz.FOREVER)
		
		# Call the addCircle function in solarUtil.py to initialize
		# these variables to circle layers
		self.sun = addCircle(50, viz.YELLOW)
		self.moon = addCircle(5, viz.GRAY)
		self.earth = addCircle(20, viz.BLUE)
		self.mercury = addCircle(5, viz.ORANGE)
		
		# distances between orbs
		self.distMercurySun = 100
		self.distEarthSun = 400
		self.distMoonEarth = 45
		
		# location of the sun in the world coordinate system
		self.sunX = 0
		self.sunY = 0
		
		# current day of the simulation
		self.day = 0
		
		self.earth.setParent(self.sun)
		self.mercury.setParent(self.sun)
		self.moon.setParent(self.earth)
		self.setTransformations()
		
	# sets the transformation matices of the nodes in the scene graph	
	def setTransformations(self):
		sunM = viz.Matrix()
		sunM.postTrans(self.sunX, self.sunY)
		self.sun.setMatrix(sunM)
		
		earthM = viz.Matrix()
		earthM.postTrans(0, 400, 0)
		earthM.postAxisAngle(0, 0, 1, 1.0138*self.day)
		self.earth.setMatrix(earthM)
		
		mercuryM = viz.Matrix()
		mercuryM.postTrans(0, 100, 0)
		mercuryM.postAxisAngle(0, 0, 1, 1.607*self.day)
		self.mercury.setMatrix(mercuryM)
		
		moonM = viz.Matrix()
		moonM.postTrans(0, 45, 0)
		moonM.postAxisAngle(0, 0, 1, 12*self.day)
		self.moon.setMatrix(moonM)
		
	def onTimer(self, num):
		self.day = self.day + 1
		self.setTransformations()
		
	def onKeyDown(self, key):
		if key == 'a' or key == viz.KEY_LEFT:
			self.sunX -= 5
		if key == 'd' or key == viz.KEY_RIGHT:
			self.sunX += 5
		if key == 's' or key == viz.KEY_DOWN:
			self.sunY -= 5
		if key == 'w' or key == viz.KEY_UP:
			self.sunY += 5
		
		
		
		
		
		
	
		
	
		
		