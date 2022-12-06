from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_user():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/users/",
        json={"email": "email@example.com", "password": "qwe123"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "email@example.com"


def test_create_exist_user():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/users/",
        json={"email": "email@example.com", "password": "qwe123"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Email already registered"


def test_get_users():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/users/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["email"] == "email@example.com"


def test_get_user_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/users/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "email@example.com"



def test_add_item_to_user():
    """
    Тест на добавление Item пользователю
    """
    response = client.post(
        "/users/1/items/",
        json={"title": "SomeBook", "description": "foobar"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "SomeBook"
    assert data["description"] == "foobar"
    assert data["owner_id"] == 1


def test_get_items():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "SomeBook"
    assert data[0]["description"] == "foobar"
    assert data[0]["owner_id"] == 1

   
def test_create_productCreate():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/productCreate/",
        json={"name": "T-shirt"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "T-shirt"

#def test_get_productCreate():
    #"""
    #"""
    #response = client.get("/productCreate/")
    #assert response.status_code == 405, response.text
    #data = response.json()
    #assert data[0]["name"] == "T-shirt"

def test_get_productFull():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/productFull/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "T-shirt"

def test_create_whoAcceptedCreate():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/whoAcceptedCreate/",
        json={"name": "Сер гей", "phone": "89000000000"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Сер гей"
    assert data["phone"] == "89000000000"

def test_get_whoAcceptedFull():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/whoAcceptedFull/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "Сер гей"
    assert data[0]["phone"] == "89000000000"

def test_create_ModelsCreate():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/ModelsCreate/",
        json={"name": "Сланцы", "price": "1", "product_id": "1"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Сланцы"
    assert data["price"] == 1
    assert data["product_id"] == 1

def test_get_ModelsFull():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/ModelsFull/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "Сланцы"
    assert data[0]["price"] == 1
    assert data[0]["product_id"] == 1

def test_create_SupplyCreate():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/SupplyCreate/",
        json={"models_id": "1", "whoaccepted_id": "1", "date_supply": "1970-01-01T00:00:01", "count_product": "1"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["models_id"] == 1
    assert data["whoaccepted_id"] == 1
    assert data["date_supply"] == "1970-01-01T00:00:01"
    assert data["count_product"] == 1

def test_get_SupplyFull():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/SupplyFull/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["models_id"] == 1
    assert data[0]["whoaccepted_id"] == 1
    assert data[0]["date_supply"] == "1970-01-01T00:00:01"
    assert data[0]["count_product"] == 1


    
    

    








    

    



    

