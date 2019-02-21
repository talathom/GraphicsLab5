import viz

class Arm( viz.EventClass):
	
	def __init__(self):
		viz.EventClass.__init__(self)
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		
		# create 3 layers here for base, upper arm, and lower arm
		viz.startLayer(viz.POLYGON)
		viz.vertex(0,0)
		viz.vertex(-25, 0)
		viz.vertex(-25, 10)
		viz.vertex(25, 10)
		viz.vertex(25, 0)
		self.base = viz.endLayer()
		
		viz.startLayer(viz.POLYGON)
		viz.vertex(0, 0)
		viz.vertex(0, 5)
		viz.vertex(40, 5)
		viz.vertex(40, 0)
		self.upperArm = viz.endLayer()
		
		viz.startLayer(viz.POLYGON)
		viz.vertex(0, 0)
		viz.vertex(0, 5)
		viz.vertex(20, 5)
		viz.vertex(20, 0)
		self.lowerArm = viz.endLayer()
		
		# starting configuration
		self.ua = 120
		self.la = 85
		self.baseX = 0
		self.baseY = 0
		
		self.upperArm.setParent(self.base)
		self.lowerArm.setParent(self.upperArm)
				
		self.setTransformations()
		
		
		
	def setTransformations(self):
		
		baseM = viz.Matrix()
		baseM.postTrans(self.baseX, self.baseY)
		self.base.setMatrix(baseM)
		
		upperArmM = viz.Matrix()
		upperArmM.postAxisAngle(0, 0, 1, self.ua)
		upperArmM.postTrans(25, 5)
		self.upperArm.setMatrix(upperArmM)
		
		lowerArmM = viz.Matrix()
		lowerArmM.postAxisAngle(0, 0, 1, self.la)
		lowerArmM.postTrans(40, 2.5)
		self.lowerArm.setMatrix(lowerArmM)
		
	def onKeyDown(self, key):
		if key == 'q':
			self.ua += 5
		if key == 'a':
			self.ua -= 5
		if key == 'w':
			self.la += 5
		if key == 's':
			self.la -= 5
		if key == viz.KEY_LEFT:
			self.baseX -= 5
		if key == viz.KEY_RIGHT:
			self.baseX += 5
		self.setTransformations()
		
	
		
		