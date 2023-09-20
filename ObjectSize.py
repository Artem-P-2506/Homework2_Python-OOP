class ObjectSize:
    def __init__(self, length = 0.1, width = 0.1, thickness = 0.1):
        self.__length = length
        self.__width = width
        self.__thickness = thickness

    def getLength(self):
        return self.__length

    def setLength(self, newLength):
        self.__length = newLength

    def getWidth(self):
        return self.__width

    def setWidth(self, newWidth):
        self.__width = newWidth

    def getThickness(self):
        return self.__thickness

    def setThickness(self, newThickness):
        self.__thickness = newThickness

    def showCharacteristics(self):
        print(f"Длина:\t{str(self.getLength())}" + "мм" +
              f"\nШирина:\t{str(self.getWidth())}" + "мм" +
              f"\nВысота:\t{str(self.getThickness())}" + "мм")