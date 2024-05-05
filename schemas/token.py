from marshmallow import Schema, fields


class TokenSchema(Schema):
    token_type = fields.Str(required=True)
    token_id = fields.Str(required=True)
