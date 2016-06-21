#!/usr/bin/python
import os
import sqlite3 as lite
#from config.database import Database

class Database():
    """
        docstring for Database
        This class takes care of the connection to the database
        as Well as retrieve and write into the db.

        This probably will have to be renamed to Query,
        in order to get single responsibility
    """
    data = {}
    db = ''

    def __init__(self):
        #Database.__init__(self)
        #Gets the connection to te DB from the config
        #and creates that connection.
        home = os.path.expanduser("~")
        #self.db = lite.connect(home + '/.vman/boxes')
        #self.db = lite.connect(Database.database)
        # this is what I am aiming to do
        pass

    #this is a private method , notice the __
    #^this is more of a personal note
    #inserts data to the DB
    def __insert(self, keys, variables):
        className = self.__class__.__name__

        query = "INSERT INTO " + className.lower() + "("

        for key in keys:
            query +=  key +", "
            pass

        query = query[:-2]
        query += ") VALUES ("

        for key in keys:
            query +=  variables[key] + ", "
            pass
        query = query[:-2]
        query += ")"

        return query

    #this is a private method , notice the __
    #^this is more of a personal note
    #updates data to the DB
    def __update(self, keys, variables):
        className = self.__class__.__name__

        query = "UPDATE " + className.lower() + " SET VALUES "#"<list columns format: 'colName=?,'>

        for key in keys:
            query +=  key +"= " + variables[key] + ", "#") VALUES (<list values>)"
            pass

        query = query[:-2]
        query += " WHERE id = " + variables["id"]

        return query

    #saves data to the DB
    def save(self):
        #good for debug I should put this lines
        #as a function somewhere globally acessible
        #[still do not know how to do it yet :P]
        # from pprint import pprint
        # pprint (vars(self))

        #Extracts the variables in the 'model' in order to
        #have the correct order of items in the queries
        variables = {}
        keys = []
        for key, value in vars(self).items():
            if key != 'db':
                variables[str(key)] = str(value)
                keys.append(str(key))
                pass
            pass

        idKey = keys.index("id")
        keys.pop(idKey)

        query = self.__insert(keys, variables)

        if self.id != None:
            print "update entry"
            query = self.__update(keys, variables)

        print "query: \n " + query
        print "save model to the db" #execute the query
        return "last object inserted"

    #deletes data to the DB
    def delete(self):
        className = self.__class__.__name__
        query = "DELETE FROM " + className.lower() + " WHERE id = " + str(self.id)
        print query

    #this can be seperated in different methoods for each model
    #for now this will work
    def findOneBy(self, column, param):
        table = self.__class__.__name__
        query = "SELECT * FROM " + table + " WHERE " + column + " = " + param
        print query

    def findAll(self):
        table = self.__class__.__name__

        print "SELECT * FROM " + table
        #print "delete model from the db"

    def findAllFromWith(self, table, param):
        query = "SELECT * FROM " + table + " WHERE " + params
        print query
        print "find " + this + " from the table " + table + " on the db"
