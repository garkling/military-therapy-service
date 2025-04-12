from pydantic import BaseModel
from pydantic import computed_field


class Auth0UserInfo(BaseModel):
    sub: str
    name: str | None = None
    email: str
    phone_number: str | None = None
    email_verified: bool = False
    phone_number_verified: bool = False

    updated_at: str | None = None

    @computed_field
    @property
    def id(self) -> str:
        return self.get_id(self.sub)

    @staticmethod
    def get_id(sub: str):
        return sub.split("|")[-1]
