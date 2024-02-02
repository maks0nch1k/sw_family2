import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Controller(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'controller'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    technical_description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    technical_description_img = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    interface_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    interface_img = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    extra_info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    warning = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    warning_img = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)