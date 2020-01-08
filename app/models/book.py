

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Book(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  author = Column(String(50), default='未命名')
  isbn = Column(Integer, nullable=False,unique=True)
  binding = Column(Integer)
  desc = Column(String(1000))

  def sample(self):
    pass