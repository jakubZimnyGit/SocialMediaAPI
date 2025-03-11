from fastapi import Depends, status, HTTPException, Response, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

@router.post("/")
def create_vote(vote: schemas.Vote, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    found_vote = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == get_current_user.id).first()

    if vote.dir == 1:    
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Vote already registered")
        
        new_vote = models.Vote(
            post_id=vote.post_id,
            user_id=get_current_user.id,
        )
        db.add(new_vote); db.commit(); db.refresh(new_vote)
        return new_vote

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        db.delete(vote); db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)