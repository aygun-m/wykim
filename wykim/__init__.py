import os
import time

class Wykim:
    def __init__(self):
        self.cwdPath = os.getcwd()
        self.dbPath = self.cwdPath + "/wykim/database.db"
        self.mainPath = self.cwdPath + "/wykim.py"
        self.corePath = self.cwdPath +  "/wykim/core.py"
        self.packagePath = self.cwdPath + "/wykim/"
