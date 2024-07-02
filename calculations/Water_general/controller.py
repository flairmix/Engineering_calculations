from litestar import Controller, get, post, put, patch, delete
from litestar.dto import DTOData
from pydantic import UUID4

from .model import User, PartialUserDTO


class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User: ...

    @get()
    async def list_users(self) -> list[User]: ...

    @patch(path="/{user_id:uuid}", dto=PartialUserDTO)
    async def partial_update_user(
        self, user_id: UUID4, data: DTOData[User]
    ) -> User: ...

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User: ...

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User: ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None: ...