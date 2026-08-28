from datetime import datetime,UTC 
from sqlalchemy.orm import DeclarativeBase,MappedColumn,mapped_column
from sqlalchemy import String,Boolean,DateTime
import uuid 

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"
    id:MappedColumn[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    email:MappedColumn[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    username:MappedColumn[str] = mapped_column(String(12),unique=True,nullable=False)
    password: MappedColumn[str] = mapped_column(String(255),unique=True,nullable=False)
    is_active : MappedColumn[bool] = mapped_column(Boolean,default=True)
    created_at : MappedColumn[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda : datetime.now(UTC)
    )  
    updated_at : MappedColumn[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(UTC),
        onupdate=lambda:datetime.now(UTC)
    )


