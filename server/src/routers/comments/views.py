from typing import Annotated

from fastapi import APIRouter, Depends, Query

from server.src.database_helper import get_db
from server.src.model.Schemas import CommentRead, CommentCreate

from sqlalchemy.orm import Session


comment_router = APIRouter(tags=['Comment'])



@comment_router.post('/', response_model=CommentRead)
def create_comments(comment_in: CommentCreate, db: Session = Depends(get_db())):
    return create_comments(db, comment_in=comment_in)


@comment_router.get('/', response_model=list[CommentRead])
def get_comments(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    return get_comments(db, limit=limit)


@comment_router.get('/{id}', response_model=CommentRead)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    return get_comment(db, comment_id=comment_id)


@comment_router.put('/{id}', response_model=CommentRead)
def update_comment(comment_id: int, comment_in: CommentCreate, db: Session = Depends(get_db)):
    return update_comment(db, comment_id=comment_id, comment_in=comment_in)


@comment_router.delete('/{id}', response_model=CommentRead)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return delete_comment(db, comment_id=comment_id)