from fastapi import Depends, status, HTTPException, Response, APIRouter
from .. import models, schemas, oauth2
from .. database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all() 
    
    return results


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db:Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
            
    return post


@router.post("/", response_model=schemas.PostCreate, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostBase, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    new_post = models.Post(
        title=post.title, 
        content= post.content, 
        published=post.published,
        owner_id = get_current_user.id
        )
    
    db.add(new_post); db.commit(); db.refresh(new_post)
    return new_post


@router.delete("/{id}")
def delete_post(id: int, db:Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")

    if post.first().owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you are not the owner of this post")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostOut)
def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    post_to_edit = db.query(models.Post).filter(models.Post.id == id)
    
    if not post_to_edit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    if post_to_edit.first().owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you are not the owner of this post")

    post_to_edit.update(post.model_dump())
    db.commit()
    post = post_to_edit.first()

    return post
