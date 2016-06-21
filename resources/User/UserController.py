#!/usr/bin/python
from core.Controller import Controller

class UserController(Controller):
    """docstring for UserController"""
    # def __init__(self):
    #     super(UserController, self).__init__()
    #     #self.arg = arg

    def indexAction(self):
        print "this is the User Controller indexAction"
        print self.model()
        pass

    def createAction(self):
        print "this is the User Controller createAction"
        pass
