from instagrapi import Client
from sqlalchemy.orm import Session
import models
from instagrapi.exceptions import LoginRequired, ClientConnectionError, UserNotFound
from sqlalchemy.exc import IntegrityError
import os
from dotenv import load_dotenv


load_dotenv()


def get_user_and_media_by_username(username: str, db: Session):
    result = [db.query(models.UserDB).filter(models.UserDB.username == username).first(),
              db.query(models.MediaDB).filter(models.MediaDB.username == username).all()]
    if not result[1]:
        return result[0]
    return result


def add_user_and_media_by_username(username: str, amount: int, db: Session) -> str:
    try:
        client = Client(proxy=os.getenv('PROXY'))
        user_info = client.user_info_by_username(username)
        db_user = models.UserDB(pk=user_info.pk,
                                username=user_info.username,
                                full_name=user_info.full_name,
                                is_private=user_info.is_private,
                                is_verified=user_info.is_verified,
                                media_count=user_info.media_count,
                                follower_count=user_info.follower_count,
                                following_count=user_info.following_count,
                                biography=user_info.biography,
                                public_email=user_info.public_email,
                                contact_phone_number=user_info.contact_phone_number,
                                public_phone_number=user_info.public_phone_number,
                                city_name=user_info.city_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        if amount > 0:
            media_info = client.user_medias(user_id=int(user_info.dict()['pk']), amount=amount)
            for post in media_info:
                db_post = models.MediaDB(pk=post.pk,
                                         username=user_info.username,
                                         id=post.id,
                                         code=post.code,
                                         taken_at=post.taken_at,
                                         media_type=post.media_type,
                                         comment_count=post.comment_count,
                                         like_count=post.like_count,
                                         caption_text=post.caption_text)
                db.add(db_post)
                db.commit()
                db.refresh(db_post)
            return f'User {user_info.dict()["username"]} and {amount} post(s) were added'
        return f'User {user_info.dict()["username"]} was added'
    except LoginRequired as e:
        return f'Error: {e}. Please, try again'
    except ClientConnectionError as e:
        return f'Error: {e}. Maybe a problem with the proxy'
    except UserNotFound as e:
        return f'Error: {e}. This user does not exist'
    except IntegrityError as e:
        return f'User {username} already exist'
    # except Exception as e:
    #     return f'Error: {e}'
