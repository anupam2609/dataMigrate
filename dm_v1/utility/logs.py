import datetime
import logging
import os 
import datetime


class Logs:
    """class refers to log build of all processes"""
    def __init__(self, process_name:str):
        self.process_name = process_name
        self.path = "./" + "logs/" + process_name
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
            print(f"{self.path} created!")
        print("Intialize logger-", "\n", "Choose level of log from options - DEBUG, ERROR, INFO, WARNING, CRITICAL!")


    def processDateTime(self):
        """sets process date and time while logging"""
        self.current_date = datetime.datetime.utcnow().date()
        self.current_time = datetime.datetime.utcnow().time()
        print(self.current_date, self.current_time)
        return self

    
    def setLoggerDate(self):
        """ creates date directory as per process date and time"""
        self.processDateTime()
        self.processDatePath = self.path + '/' + str(self.current_date)
        if not os.path.isdir(self.processDatePath):
            os.makedirs(self.processDatePath)
        return self 
    

    def setHandlers(self):
        """configure and sets handlers for logging"""
        self.file_log = self.processDatePath + '/' + self.process_name
        print(self.file_log)
        logging.basicConfig(level=self.level_name.upper())
        logger = logging.getLogger(__name__)
        print(f"Logger set to {self.level_name.upper()} level!")
        file_handler = logging.FileHandler(self.file_log, mode = "a", encoding= "utf-8")
        logger.addHandler(file_handler)
        self.logger = logger
        return self
        

    def intializeLogger(self, level_name:str):
        """initializes process"""
        self.level_name = level_name
        self.setLoggerDate()
        self.setHandlers()
        return self



  