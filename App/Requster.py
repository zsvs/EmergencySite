import requests
import json

class HTTPClient:
    __Payload = None
    __Headers = None
    __URL = None
    __Answer = None

    def __init__(self, URL):
        self.__Headers = {
                            "Content-type": "application/json",
                            "Accept": "*/*",
                            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                            "Content-Encoding": "utf-8",
                            "Keep-Alive": "timeout=600, max=10000"
                        }
        self.__URL = URL
    def SetPayload(self, Data):
        """
        Setting up HTTP payload.
        Mandatory attribute <Data>, preferred to be a dict()
        """
        self.__Payload = json.dumps(Data)

    def GetPayload(self):
        """
        Getting active request payload
        """
        return self.__Payload

    def PostRequest(self):
        """
        Sending POST request to web-server
        """
        if self.__Payload:
            self.__Answer = requests.post(self.__URL, data = self.__Payload, headers = self.__Headers)
            print(self.GetAnswer())
        else:
            raise Exception("Payload must be setted")

    def GetRequest(self):
        """
        Sending GET request to web-server
        """
        if self.__Payload:
            self.__Answer = requests.get(self.__URL, data = self.__Payload, headers = self.__Headers)
            print(self.GetAnswer())
        else:
            raise Exception("Payload must be setted")

    def GetAnswer(self):
        """
        Returns HTTP code of response
        """
        return self.__Answer