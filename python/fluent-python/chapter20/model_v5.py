import abc

class AutoStorage:
    __counter = 0
    
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter__
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validated(abc.ABC, AutoStorage):
    
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)
    
    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""
        
    
class Quantity(Validated):
    
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
            
        return value

class BonBlank(Validated):
    
    def validate(self, isinstance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
            
        return value