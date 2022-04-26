from multiprocessing.sharedctypes import Value
from optparse import Values
from turtle import title
from wsgiref import headers
import typer 
from typing import Optional
from beerlog.core import add_beer_database, get_beers_from_database
from rich.table import Table
from

main = typer.Typer(help="Beer Management Application")

@main.command("add")
def add(
    name: str, 
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
    ):
    print(name, style)

@main.command("list")
def list_beers(style: Optional[str] = None):
    """List Beers in Database"""

    beers = get_beers_from_database()
    table = Table(title="Beerlog")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.and_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*Values)
        
        console.print(table)

    


