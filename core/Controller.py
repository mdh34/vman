import sys

class Controller():
    """docstring for Controller"""

    def model(self):
        controller = self.__class__.__name__[:-10]
        path = self.getPath(controller)
        print path
        print controller

        if not path:
            #should throw exception
            return path
            pass

        #Dynamically import and instantiate an object from a class
        import imp
        imp.load_source(controller, path)
        this = self.my_import(controller + '.' + controller)
        this = this()

        # if sys.argv != []:
        #     if sys.argv[0] + 'Action' in dir(this):
        #         self._action = sys.argv[0]
        #         sys.argv.pop(0)


        modelFile = 'file model'
        print "include modelFile"
        return this
        pass


    def getPath(self, arg):
        import os
        path = os.path.dirname(os.path.realpath(__file__))[:-4]
        path += 'resources/'
        path += arg + '/'
        path += arg + 'Model.py'

        if os.path.isfile(path):
            self._controller = arg + 'Model'
            return path

        sys.argv.append(arg)
        return False#self.getPath(self._controller)

    def my_import(self, name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
