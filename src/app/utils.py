class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


truthy = {
    "t",
    "T",
    "true",
    "True",
    "TRUE",
    "on",
    "On",
    "ON",
    "y",
    "Y",
    "yes",
    "Yes",
    "YES",
    "1",
    1,
    True
}

falsy = {
    "f",
    "F",
    "false",
    "False",
    "FALSE",
    "off",
    "Off",
    "OFF",
    "n",
    "N",
    "no",
    "No",
    "NO",
    "0",
    0,
    False
}