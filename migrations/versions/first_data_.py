"""empty message

Revision ID: first_data
Revises: 7193876b68ab
Create Date: 2022-11-28 21:50:11.989061

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime
from src.models import User, Item, Supply, Models, WhoAccepted, Product


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '7193876b68ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    ivanov = User(email='ivanov@mail.ru', hashed_password='qwerty')
    petrov = User(email='petrov@mail.ru', hashed_password='asdfgh')

    session.add_all([ivanov, petrov])
    session.flush()

    book_harry = Item(title='Harry Potter', description='Book', owner_id = ivanov.id)
    book_rings = Item(title='The Lord of The Rings', description='Book', owner_id = ivanov.id)
    doka = Item(title='Dota 2', description='Game', owner_id = petrov.id)
    game = Item(title='Half Life 3', description='Game', owner_id = petrov.id)

    session.add_all([book_harry, book_rings, doka, game])
    session.flush()

    prod_1 = Product(
        name = 'Product 1',
    )
    prod_2 = Product(
        name = 'Product 2',
    )
    session.add_all([prod_1, prod_2])
    session.flush()

    who_acc_1 = WhoAccepted(
        name = 'Саша Павлович',
        phone = '+790665555'
    )
    who_acc_2 = WhoAccepted(
        name = 'Сер Гей',
        phone = '+790000000'
    )

    session.add_all([who_acc_1, who_acc_2])
    session.flush()

    mod_1 = Models(
        name = 'Model 1',
        price = 444,
        product_id = prod_1.id
    )

    mod_2 = Models(
        name = 'Model 2',
        price = 44444,
        product_id = prod_2.id
    )

    session.add_all([mod_1, mod_2])
    session.flush()

    supl_1 = Supply(
        date_supply = datetime(2021,2,2,2,00),
        count_product = 2,
        models_id = mod_1.id,
        whoaccepted_id =  who_acc_1.id
    )

    supl_2 = Supply(
        date_supply = datetime(2022,1,1,1,00),
        count_product = 3,
        models_id = mod_2.id,
        whoaccepted_id =  who_acc_2.id
    )

    session.add_all([supl_1, supl_2])

    session.commit()

def downgrade() -> None:
    pass


