
import collections

class EntityMeta(type):
    
    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()
    
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '{}#{}'.format(type_name, key)
                cls._field_names.append(key)
