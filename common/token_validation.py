def validate_token(token_type, token_id):
    if token_type == "google_token":
        if "Bearer test" in token_id:
            return True
        return False
