from Key import *
from ObjectSize import *

if __name__ == "__main__":
    size1 = ObjectSize(80, 22, 4)
    key1 = Key(size1, "*AF12547*","aluminum", "red")
    key1.showCharacteristics()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    size2 = ObjectSize(70, 30, 5)
    key2 = Key(size2, "#K-79342","stainless")
    key2.showCharacteristics()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    key1.openLock()
    key2.openLock()