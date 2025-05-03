from typing import Optional

from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        
    async def load(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.email = form.get("email")
        self.password = form.get("password")
        
        if not self.name or self.name.strip():
            self.error = "Name is required"
        elif not self.email or self.email.strip():
            self.error = "Email is required"
        elif not self.password or len(self.password) < 8:
            self.error = "Must have a password and be at least 8 characters long"
        