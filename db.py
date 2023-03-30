from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class VilanderGay(Base):
    __tablename__ = "openai"

    openai_key: Mapped[str]

