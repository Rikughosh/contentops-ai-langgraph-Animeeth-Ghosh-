import uuid
def publish_to_linkedin(content):
    return {
        "platform": "LinkedIn",
        "post_id": str(uuid.uuid4()),
        "status": "published",
        "preview": content[:100]
    }
