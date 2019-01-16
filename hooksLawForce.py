from H3DInterface import *
from math import sqrt

di = getActiveDeviceInfo()
if di:
  hd = di.device.getValue()[0]
  
class CalcForce(TypedField((SFVec3f), (SFVec3f, MFBool))):
	center = Vec3f(0,0,0)
	rad = 0.05
	
	def dist(self, deviceX, deviceY, deviceZ):
		return sqrt(pow(deviceX, 2) + pow(deviceY, 2) + pow(deviceZ, 2))
	
	def update(self, event):
		#Spring constant, gradually increase from 100
		k = 200
	
#		x = event.getValue().x
#		y = event.getValue().y
#		z = event.getValue().z
		
#		dist = self.dist(x, y, z)	
		
		#If device is inside of sphere
#		if dist <= self.rad and dist != 0:
#			displacement = self.rad - dist
#			forceX = (x/dist) * displacement * k
#			forceY = (y/dist) * displacement * k
#			forceZ = (z/dist) * displacement * k
#			return Vec3f(forceX, forceY, forceZ)
#		else:
#			return Vec3f(0, 0, 0)
		
		#DEVICE ORIENTATION
		negativeZ = Vec3f(0,0,-1)
		newTouchPos = 0.02 * (Matrix3f(hd.trackerOrientation.getValue()) * negativeZ) + event.getValue()
		dist = self.dist(newTouchPos.x, newTouchPos.y, newTouchPos.z)
		if dist <= self.rad and dist != 0:
			displacement = self.rad - dist
			forceX = (newTouchPos.x/dist) * displacement * k
			forceY = (newTouchPos.y/dist) * displacement * k
			forceZ = (newTouchPos.z/dist) * displacement * k
			return Vec3f(forceX, forceY, forceZ)
		else:
			return Vec3f(0, 0, 0)
		
calcForce = CalcForce()
			