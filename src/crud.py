from sqlalchemy.orm import Session

from src import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    """
    Добавление нового пользователя
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """
    Добавление нового Item пользователю
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user(db: Session, user_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Получить пользователя по его email
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список предметов из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.User).offset(skip).limit(limit).all()



def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name)
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product_name(db:Session, product: schemas.Product, new_name : str):
    db_product = get_product_by_id(db=db, product_id=product.id) # pragma: no cover
    db_product.name = new_name # pragma: no cover
    db.commit() # pragma: no cover
    db.refresh(db_product)# pragma: no cover
    return db_product# pragma: no cover

def get_product_by_id(db: Session, product_id:int):
    return db.query(models.Product).filter(models.Product.id == product_id).first() # pragma: no cover

def get_whoAccepted_by_id(db: Session, whoaccepted_id:int):
    return db.query(models.WhoAccepted).filter(models.WhoAccepted.id == whoaccepted_id).first() # pragma: no cover






def update_product_name(db:Session, product: schemas.Product, new_name:str):
    db_product = get_product_by_id(db=db, product_id=product.id) # pragma: no cover
    db_product.name = new_name # pragma: no cover
    db.commit() # pragma: no cover
    db.refresh(db_product) # pragma: no cover
    return db_product # pragma: no cover

def get_product(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_whoAccepted(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WhoAccepted).offset(skip).limit(limit).all()

def get_Supply(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Supply).offset(skip).limit(limit).all()

def get_Model(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Models).offset(skip).limit(limit).all()

def create_whoAccepted(db: Session, whoaccepted: schemas.WhoAcceptedCreate):
    db_whoaccepted = models.WhoAccepted(name=whoaccepted.name,
                                        phone= whoaccepted.phone )
    
    db.add(db_whoaccepted)
    db.commit()
    db.refresh(db_whoaccepted)
    return db_whoaccepted


def create_models(db: Session, model: schemas.ModelsCreate):
    db_models = models.Models(name=model.name,
                                    price= model.price, 
                                    product_id = model.product_id)
    
    db.add(db_models)
    db.commit()
    db.refresh(db_models)
    return db_models

def create_Supply(db: Session, supply: schemas.SupplyCreate):
    db_supply = models.Supply(date_supply=supply.date_supply,
                            count_product= supply.count_product,
                            models_id= supply.models_id,
                            whoaccepted_id = supply.whoaccepted_id )
    
    db.add(db_supply)
    db.commit()
    db.refresh(db_supply)
    return db_supply