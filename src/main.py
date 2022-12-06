from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal() # pragma: no cover
    try: # pragma: no cover
        yield db # pragma: no cover
    finally: # pragma: no cover
        db.close() # pragma: no cover


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Создание пользователя, если такой email уже есть в БД, то выдается ошибка
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users





@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    """
    Добавление пользователю нового предмета
    """
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка предметов
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items



@app.post("/productCreate/", response_model=schemas.Product)
def create_user(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product = product)

@app.post("/whoAcceptedCreate/", response_model=schemas.WhoAccepted)
def create_user(
    whoaccepted: schemas.WhoAcceptedCreate, 
    db: Session = Depends(get_db)):
   
    return crud.create_whoAccepted(db=db, whoaccepted = whoaccepted )

@app.post("/ModelsCreate/", response_model=schemas.Models)
def create_user(
    model: schemas.ModelsCreate, 
    db: Session = Depends(get_db)):
   
    return crud.create_models(db=db, model = model )

@app.post("/SupplyCreate/", response_model=schemas.Supply)
def create_user(
    supply: schemas.SupplyCreate, 
    db: Session = Depends(get_db)):
   
    return crud.create_Supply(db=db, supply = supply )




@app.get("/productFull/", response_model=list[schemas.Product])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка предметов
    """
    items = crud.get_product(db, skip=skip, limit=limit)
    return items

@app.put('/productsName/', response_model=schemas.Product)
def update_product_price(product: schemas.Product, new_name: str, db:Session=Depends(get_db)):
    db_product = crud.get_product_by_id(db=db, product_id=product.id) # pragma: no cover
    if db_product is None: # pragma: no cover
        raise HTTPException(status_code=404, detail='product not found') # pragma: no cover
    return crud.update_product_name(db=db,product=product,new_name=new_name) # pragma: no cover


@app.get("/whoAcceptedFull/", response_model=list[schemas.WhoAccepted])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_whoAccepted(db, skip=skip, limit=limit)
    return items

@app.get("/SupplyFull/", response_model=list[schemas.Supply])
def read_supply(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_Supply(db, skip=skip, limit=limit)
    return items

@app.get("/ModelsFull/", response_model=list[schemas.Models])
def read_supply(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_Model(db, skip=skip, limit=limit)
    return items 


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    return db_user