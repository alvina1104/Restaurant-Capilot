from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import (Boolean, DateTime, ForeignKey,String, func)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base
from app.main import restaurant_app


class Restaurant(Base):
    __tablename__ = "restaurant"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True,default=uuid4)
    rest_name: Mapped[str] = mapped_column(String(250), nullable=False)
    timezone: Mapped[str] = mapped_column(String(50),default="UTC")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(),onupdate=func.now())

    users: Mapped[list["User"]] = relationship(back_populates="restaurant",
                                               cascade="all, delete-orphan")




class UserProfile(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),primary_key=True, default=uuid4)
    restaurant_id: Mapped[UUID] = mapped_column(ForeignKey("restaurant_id", ondelete="CASCADE"),
                                                nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(250),nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
