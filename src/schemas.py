from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    """
    Базовый класс для Item
    """
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Item(ItemBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    owner_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


class UserBase(BaseModel):
    """
    Базовый класс для User
    """
    email: str


class UserCreate(UserBase):
    """
    Класс для создания User. Пароль мы не должны нигде отображать, поэтому
    это поле есть только в классе для создания.
    """
    password: str


class User(UserBase):
    """
    Класс для отображения информации о User. Все значения полей будут браться
    из базы данных
    """
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        orm_mode = True

class WhoAcceptedBase(BaseModel):
    name: str
    phone : str

class WhoAcceptedCreate(WhoAcceptedBase):
    pass

class WhoAccepted(WhoAcceptedBase):
    id: int
    # supply_whoaccepted : list[Supply] =[]
    class Config:
        orm_mode = True


class ModelsBase(BaseModel):
    name: str
    price : int
    product_id : int

class ModelsCreate(ModelsBase):
    pass

class Models(ModelsBase):
    id: int
    # product_models : list[Product] = []
    # models_supply : list[Models] = []
    class Config:
        orm_mode = True



class SupplyBase(BaseModel):
    date_supply : datetime
    count_product : int
    models_id : int
    whoaccepted_id : int

class SupplyCreate(SupplyBase):
    pass

class Supply(SupplyBase):
    id: int
 
    class Config:
        orm_mode = True