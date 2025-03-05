# section comprises of all the utility methods for dataM/zlow
import json
import datetime
import logging
import os 
import datetime



class Configs:
    def __init__(self):
        with open('dm_v1/zflow-env/configuration.json', 'r') as jsonFile:
            tempConf = json.load(jsonFile)
        self.conf = tempConf
        # printing json while initialization
        print("conf file loaded", "\n", tempConf)
    

    def read_configuration(self, ser_name=None, app_name=None):
        if ser_name == None and app_name == None:
            rc_message= "service name missing"
            tempConf = {}
        elif ser_name is not None and app_name == None:
            for elements in self.conf:
                if elements["service"] == ser_name:
                    tempConf = elements["applications"]
                else:
                    rc_message = "service name not found"
        else:
            rc_message= "service name missing"
            tempConf = {}
        return rc_message, tempConf
            


        










class Read_data:
    pass


    # def get_service_client_token_credential(self, account_name) -> DataLakeServiceClient:
    #     account_url = f"https://{account_name}.dfs.core.windows.net"
    #     token_credential = DefaultAzureCredential()

    #     service_client = DataLakeServiceClient(account_url, credential=token_credential)

    #     return service_client