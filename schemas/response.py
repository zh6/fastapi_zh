"""

统一响应状态码

"""
from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder


def success(*, data: Union[list, dict, str] = None, message: str = "Success", count: int = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 0,
            'message': message,
            'data': data,
            'count': count,
        })
    )
def error(*, data: Union[list, dict, str] = None, message: str = "Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 99,
            'message': message,
            'data': data,
        })
    )