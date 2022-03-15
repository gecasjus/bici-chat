from fastapi import HTTPException
from sqlalchemy import exc

def database_error(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exc.SQLAlchemyError as err:
            raise HTTPException(status_code=500, detail=str(err.__dict__['orig']))

    return handler