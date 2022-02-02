from fastapi import Path

def get_chats_by_id_from_path(item_id: str = Path(..., min_length=1)):
    
