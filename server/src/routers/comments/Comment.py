from typing import Annotated

from fastapi import Depends, Query, status, HTTPException

from server.src.database_helper import get_db
from server.src.model.Schemas import CommentCreate
from server.src.model.Database import Comment

from sqlalchemy.orm import Session


def create_comment(comment_in: CommentCreate, db: Session = Depends(get_db())):
    db_comment = Comment(**comment_in.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    if limit is None:
        return db.query(Comment).all()

    return db.query(Comment).limit(limit).all()


def get_comment(comment_id: int, db: Session = Depends(get_db)):
    if comment := db.query(Comment).get(comment_id):
        return comment

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


def update_comment(comment_id: int, comment_in: CommentCreate, db: Session = Depends(get_db)):
    comment = get_comment(comment_id, db)
    for key, value in comment_in.dict().items():
        setattr(comment, key, value)

    db.commit()
    db.refresh(comment)
    return comment


def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = get_comment(comment_id, db)
    db.delete(comment)
    db.commit()
    return {"detail": "Comment deleted"}