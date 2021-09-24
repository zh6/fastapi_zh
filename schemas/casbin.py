from pydantic import BaseModel
# Casbin权限
class AuthCreate(BaseModel):
    role_id: str
    sys_id: str
    path: str
    method: str
