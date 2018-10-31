from abc import abstractmethod


class IEntity:

    @abstractmethod
    def Deserialize(self,data): raise NotImplementedError("The method - \"deserialize\" wasn't implemented")
