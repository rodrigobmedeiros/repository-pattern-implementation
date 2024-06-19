from src.domain.dto.user import ItemDTO, UserDTO


users = [
    UserDTO(user_id=1, user_name="Alice"),
]

items = [
    ItemDTO(item_id=1, user_id=1, item_name="Apple"),
    ItemDTO(item_id=2, user_id=1, item_name="OtherItem"),
]
