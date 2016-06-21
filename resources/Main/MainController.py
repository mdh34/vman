#!/usr/bin/python
from core.Controller import Controller

class MainController(Controller):
    """docstring for UserController"""
    # def __init__(self):
    #     super(UserController, self).__init__()
    #     #self.arg = arg

    def indexAction(self):
        print "this is the Main Controller indexAction"
        print self.model()

        pass

    def createAction(self):
        print "this is the Main Controller createAction"
        pass
