from ..settings.options import OrmsqlalchemyOption
from ..settings.development import  Development
from .ormsqlachemy import OrmsqlalchemyDataAccess


class FactoryDataAccess:
 @staticmethod
 def build_object(service=Development.ORM_SQLALCHEMY):
  if service == OrmsqlalchemyOption.ORMSQLALCHEMY:
   return OrmsqlalchemyDataAccess()
  raise NotImplementedError()