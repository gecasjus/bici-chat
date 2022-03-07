from fastapi import APIRouter, Depends
from api.routes.chat import router as chat_router
from api.routes.item import router as item_router
from api.routes.message import router as message_router
from services.auth import auth_service

router = APIRouter()

router.include_router(chat_router, tags=["chat"], prefix="/chat", dependencies=[Depends(auth_service.get_auth_header)])
router.include_router(item_router, tags=["item"], prefix="/item", dependencies=[Depends(auth_service.get_auth_header)])
router.include_router(message_router, tags=["message"], prefix="/message", dependencies=[Depends(auth_service.get_auth_header)])