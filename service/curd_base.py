#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:59
# @Author  : CoderCharm
# @File    : curd_base.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
基础的CRUD类
"""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union,Tuple

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id, self.model.is_delete == 0).first()

    def get_multi(
            self,
            db: Session,
            *,
            filters: Tuple = tuple(),
            order_by=None,
            page: int = 1,
            limit: int = 10
    ) -> Optional[List[ModelType]]:
        offset = limit * (page - 1)
        query = db.query(self.model)
        if filters:
            query = query.filter(*filters)
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return query.all()

    def count(self, db: Session, *, filters=tuple()) -> Any:
        query = db.query(self.model)
        if filters:
            query = query.filter(*filters)
        return query.count()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, ids):
            if isinstance(ids, int):
                obj = db.query(self.model).get(ids)
                db.delete(obj)
                db.commit()
            elif isinstance(ids, list):
                for i in ids:
                    obj = db.query(self.model).get(i)
                    db.delete(obj)
                db.commit()
            else:
                raise ValueError
            return
