from pydantic import BaseModel, Field, field_validator, SecretStr
from pydantic import field_serializer, ValidationError, model_validator


class Blog(BaseModel):
    title: str = Field(..., min_length=5)
    is_active: bool
    password: SecretStr
    confirm_password: SecretStr

    @field_validator('title')
    def validate_no_sql_injection(cls, value):
        if 'delete from' in value:
            raise ValueError('Our term stricly prohobit SQLInject')
        return value

    @field_serializer('password', when_used='json')
    def dump_password(self, v):
        # Avoid serializing the password by default
        raise ValueError("Password serialization is forbidden for security reasons")
    
    @model_validator(mode='after')
    def verify_password_match(cls, model):
        password = model.password.get_secret_value()
        confirm_password = model.confirm_password.get_secret_value()

        if password != confirm_password:
            raise ValueError('The who password did not match')
        return model



    def get_password(self):
        return self.password.get_secret_value()

    def validate_password(self):
        plain_password = self.get_password()
        if len(plain_password) < 8:
            raise ValueError('Password must br a least 8 characters')
        return True


try:
    blog = Blog(
        title="Example Blog",
        is_active=True,
        password=SecretStr("StrongPass123!"),
        confirm_password=SecretStr("StrongPass123!")
    )
    print("Validation successful!")
    print("Password (masked):", blog.password)
    print("Password (plain):", blog.get_password())
    blog.validate_password()  # Validate password strength
except ValidationError as e:
    print("Validation failed:", e.errors())
