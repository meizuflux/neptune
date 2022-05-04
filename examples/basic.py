import sys

sys.path.insert(0, "..")


from cion import Field, Options, Schema, types, validators
from cion.schema import ExtraFieldsOption

User = Schema(
    fields={
        "username": Field(
            type_=types.string(),
            validators=[validators.length(3, 64)],
            default="testing1234",
        ),
        "password": Field(
            type_=types.string(),
            validators=[validators.length(8, 1024)],
            required=True,
        ),
    },
)


data = {
    "username": "meizuflux",
    "password": "password",
}

print(User.validate_data(data))
