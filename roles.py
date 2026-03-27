def get_role_permissions(role):
    if role == "Admin":
        return ["generate", "approve", "publish"]
    if role == "Reviewer":
        return ["approve"]
    return []
