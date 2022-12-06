from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self): 
        return f"<{type(self).__name__}(id={self.id})>" # pragma: no cover

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(BaseModel):
    __tablename__ = "items"

    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Models(BaseModel):
    __tablename__ = "models"

    product_id = Column(ForeignKey('product.id'), nullable=False)
    name = Column(String, index=True)
    price = Column(Integer, nullable = False)
    product_models = relationship('Product', back_populates ='models_product')
    supply_models = relationship('Supply', back_populates = 'models_supply')

class Product(BaseModel):
    __tablename__ = "product"

    name = Column(String, index=True)
    models_product = relationship('Models', back_populates ='product_models')


class WhoAccepted(BaseModel):
    __tablename__ = 'whoaccepted'
    
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    supply_whoaccepted = relationship('Supply', back_populates = 'whoaccepted_supply')

class Supply(BaseModel):
    __tablename__ = 'supply'
    
    models_id = Column(ForeignKey('models.id'),nullable = False)
    whoaccepted_id = Column(ForeignKey('whoaccepted.id'),nullable = False)
    date_supply = Column(DateTime, nullable=False)
    count_product = Column(Integer, nullable=False)

    models_supply = relationship('Models', back_populates = 'supply_models')
    whoaccepted_supply = relationship('WhoAccepted', back_populates = 'supply_whoaccepted')
