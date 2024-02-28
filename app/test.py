from fastapi import  Path, Query, APIRouter, Body
from typing import Annotated
from pydantic import BaseModel,Field


class Item(BaseModel):
    name: int = Field(description="It is the name what else you expect", title="Name (did you expect something else)", gt=2, lt=5)
    price : str


app = APIRouter(tags=["Learnings"])

@app.put('/item/{item_id}')
def site_data( *,item_id: Annotated[int, Path(title = "The id of the item entered" )], q: Annotated[str, Query(max_length=1000)]=None,
              item: Item, y: Annotated[int, Query(ge=2)]= None):
    results = {"items_id": item_id}
    if q and y :
        results.update({'q': q,'y': y })
    if item:
        results.update({'item': item})
    
    return results


@app.post('/item/foo/{item_id}')
def site_data(*, item_id: Annotated[int, Path(title = "The id of the item entered", ge=0, le=10 )],
               q: Annotated[str, Query(max_length=1000)]=None,
                 item: Item, importance : Annotated[int, Body()],
                 single_item: Annotated[Item, Body(embed=True)]):
    results = {"items_id": item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update(item)

    if importance:
        results.update({'importance': importance})

    if single_item:
        results.update({'single_item' : single_item})
    
    return results


@app.post("/items/fooo/{item_id}")
def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"items_id": item_id}
    if item:
        results.update(item)
    return results