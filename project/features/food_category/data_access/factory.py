from ..settings.development import Development
from ..settings.options import OrmSqlalchemyOption

from .orm_sqlalchemy import OrmSqlalchemyFoodCategory

class FactoryDataAccess:

    @staticmethod
    def build_object(service = Development.ORMSQLALCHEMY):
        if service == OrmSqlalchemyOption.ORM_SQLALCHEMY:
            return OrmSqlalchemyFoodCategory()
        raise NotImplementedError()