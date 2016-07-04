#import sys

class View():
    """docstring for View"""

##reference code for now
class otherClass:
	def __init__(self):
		pass

	def functionToRun(self,s):
		print "functionToRun"

	def anotherfunctionToRun(self,s):
		print "anotherfunctionToRun"

other = otherClass()

indicatorObject = IndicatorClass('id')

indicatorObject.setDependency(other)

indicatorObject.setIcon('some/path/to/a/picture')

indicatorObject.menuItem('itemName', 'functionToRun')

indicatorObject.separator()

indicatorObject.menuItem('anotherItemName','anotherfunctionToRun')

indicatorObject.show()

#read file from glade
#and tie everything together

#I need more xp on this I need to build some apps wih parakeet to be sure what to do :)
