# from abc import ABC,abstractmethode

# class Ide(ABC):

#     @abstractmethode
#     def debug(self):
#         pass


# class Pycharm(Ide):

#     def debug(self):
#         print("pycharm debug method")

# class Eclipse(Ide):

#     def debug(self):
#         print("Eclipse debug")

# pyc=Pycharm()
# pyc.debug()

#or

from abc import ABC,abstractmethod
class Ide(ABC):
    @abstractmethod
    def debug(self):
        pass

class Pycharm(Ide):
    def debug(self):
        print("Pycharm debug method")

class Eclipse(Ide):
    def debug(self):
        print("Eclipse debug method")

pyc=Pycharm()
pyc.debug()