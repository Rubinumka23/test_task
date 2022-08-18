from sqlalchemy import Boolean, Column, Integer, String, BigInteger, Date
from database import Base


class UserDB(Base):

    __tablename__ = 'Users'
    pk = Column(BigInteger, primary_key=True)
    username = Column(String)
    full_name = Column(String)
    is_private = Column(Boolean)
    is_verified = Column(Boolean)
    media_count = Column(Integer)
    follower_count = Column(Integer)
    following_count = Column(Integer)
    biography = Column(String)
    public_email = Column(String)
    contact_phone_number = Column(String)
    public_phone_number = Column(String)
    city_name = Column(String)


class MediaDB(Base):

    __tablename__ = 'Media'
    pk = Column(String, primary_key=True)
    username = Column(String)
    id = Column(String)
    code = Column(String)
    taken_at = Column(Date)
    media_type = Column(Integer)
    comment_count = Column(Integer)
    like_count = Column(Integer)
    caption_text = Column(String)
