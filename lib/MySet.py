class MySet:

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}

    def __str__(self):
        keysList = self.dictionary.keys()
        returnString = ""
        if len(keysList) == 0:
            returnString = "MySet: {}"
            return returnString
        else:
            index = 1
            returnString = 'MySet: {'
            for key in keysList:
                if (index == len(keysList)):
                    returnString += str(key) + '}'
                    return returnString
                returnString += str(key) + ','
                index += 1
