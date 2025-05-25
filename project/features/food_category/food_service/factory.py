from ..settings.development import Development
from ..settings.options import DefaultServiceOption
from .default import DefaultFoodService



class FactoryFoodService():
    @staticmethod
    def build_object(data_access, service=Development.DEFAULT_SERVICE):
        if service == DefaultServiceOption.DEFAULT:
            return DefaultFoodService(data_access)
        raise NotImplementedError()
    


