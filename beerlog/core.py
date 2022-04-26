import sqlite3
from typing import Optional, List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer

def and_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,

) -> bool:
     with get_session() as session:
         beer = Beer(
             name=name,
             stye=style,
             flavor=flavor,
             image=image,
             cost=cost,
         )
         session.add(beer)
         session.commit()

    ##return True

def get_from_database() -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        return session.exec(sql) 