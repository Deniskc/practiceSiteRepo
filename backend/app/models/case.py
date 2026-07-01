from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.core.database import Base

class TrustLevel(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class CaseStatus(str, enum.Enum):
    DRAFT = "draft"
    UNDER_REVIEW = "under_review"
    VERIFIED = "verified"
    PUBLISHED = "published"
    REJECTED = "rejected"

class Case(Base):
    __tablename__ = "cases"
    
    # Основные поля
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    
    # Внешние ключи
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    technology_id = Column(Integer, ForeignKey("technologies.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    verifier_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Информация о компании
    company = Column(String(200), nullable=False)
    industry = Column(String(100), nullable=False)
    facility_type = Column(String(100), nullable=False)
    
    # Проблема
    business_problem = Column(String(200), nullable=False)
    problem_description = Column(Text, nullable=False)
    
    # Решение
    it_systems = Column(String(200), nullable=True)
    solution_description = Column(Text, nullable=False)
    implementation_stages = Column(Text, nullable=True)
    
    # Результат
    measurable_result = Column(String(100), nullable=True)
    result_unit = Column(String(50), nullable=True)
    result_period = Column(String(50), nullable=True)
    initial_value = Column(String(50), nullable=True)
    final_value = Column(String(50), nullable=True)
    
    # Ограничения
    limitations = Column(Text, nullable=True)
    applicability = Column(Text, nullable=True)
    
    # Источник
    source_url = Column(String(500), nullable=False)
    source_type = Column(String(100), nullable=False)
    trust_level = Column(Enum(TrustLevel), nullable=False)
    source_date = Column(DateTime, nullable=True)
    is_vendor_case = Column(Boolean, default=False)
    
    # Статус и проверка
    status = Column(Enum(CaseStatus), default=CaseStatus.DRAFT)
    verification_date = Column(DateTime, nullable=True)
    
    # Даты
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Связи (relationships)
    country = relationship("Country", back_populates="cases")
    technology = relationship("Technology", back_populates="cases")
    author = relationship("User", foreign_keys=[author_id])
    verifier = relationship("User", foreign_keys=[verifier_id])