class Key:
    def __init__(self, objectSize, serialNumber, material, color = "without color"):
        self.__size = objectSize # Обеьект класса 'ObjectSize'
        self.__serialNumber = serialNumber
        self.__material = material
        self.color = color # Поле без использования инкапсуляции (например, так как ключ можно перекрасить вручную)

    def getObjectSize(self):
        return self.__size

    def setObjectSize(self, newLength, newWidth, newThickness):
        size = self.getObjectSize()
        size.setLength(newLength)
        size.setWidth(newWidth)
        size.setThickness(newThickness)

    def getSerialNumber(self):
        return self.__serialNumber

    def getMaterial(self):
        return self.__material

    def setMaterial(self, newMaterial):
        self.__material = newMaterial

    def showCharacteristics(self):
        size = self.getObjectSize()
        size.showCharacteristics()
        print(f"Серийный номер:\t{str(self.getSerialNumber())}", f"\nМатериал:\t{str(self.getMaterial())}" + f"\nЦвет:\t{str(self.color)}")

    def openLock(self):
        size = self.getObjectSize()
        if 0.1 < size.getLength() and 0.1 < size.getWidth() and 0.1 < size.getThickness():
            print(f"Lock opened! Serial number of key:\t{str(self.getSerialNumber())}")
        else:
            print("Lock didn't open! The key is wrong!")