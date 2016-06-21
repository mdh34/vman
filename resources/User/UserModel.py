#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.Database import Database

# Initialize using Parent
#
class User(Database):
    table = 'user'

    id   = None
    name = None
    age  = None

    def __init__(self, id = None):
        Database.__init__(self)
        #self._Database__insert()

        self.id   = None
        self.name = None
        self.age  = None

        if id != None:
            print "USER OBJECT got this from the DB"
            self.id   = 19
            self.name = "Fernando"
            self.age  = 29
            return None

        print "this is a new USER"
