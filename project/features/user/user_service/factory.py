from ..settings.options import UserServiceOption
from ..settings.development import Development
from .default import DefaultUserService



class FactoryUserService:

    @staticmethod
    def build_object(data_access,service=Development.USER_SERVICE):
        if service == UserServiceOption.DEFAULT:
            return DefaultUserService(data_access)
        
        raise NotImplementedError()