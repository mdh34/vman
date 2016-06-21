#!/usr/bin/python
import os
import sys

#import sqlite3 as lite

class App():
    """App initializer"""

    _controller = 'Main'
    _action     = 'index'
    _parameters = []

    def __init__(self):
        sys.argv.pop(0)

        controller = self._controller
        if sys.argv != []:
            controller = sys.argv[0]
            sys.argv.pop(0)

        path = self.getPath(controller)
        #Dynamically import and instantiate an object from a class
        import imp
        imp.load_source(self._controller, path)
        this = self.my_import(self._controller + '.' + self._controller)
        this = this()

        if sys.argv != []:
            if sys.argv[0] + 'Action' in dir(this):
                self._action = sys.argv[0]
                sys.argv.pop(0)

        #Dynamically call method from above class
        methodToCall = getattr(this, self._action + 'Action')
        result = methodToCall()

        self._parameters = sys.argv
        #print self._parameters

    def my_import(self, name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    def getPath(self, arg):
        import os
        path = os.path.dirname(os.path.realpath(__file__))[:-4]
        path += 'resources/'
        path += arg + '/'
        path += arg + 'Controller.py'

        if os.path.isfile(path):
            self._controller = arg + 'Controller'
            return path

        sys.argv.append(arg)
        return self.getPath(self._controller)
