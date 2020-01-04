schema = {
    "type": "object",
    "properties": {
        "cover": {"type": "string"},
        "create_time": {"type": "integer"},
        "is_reviewed": {"type": "boolean"},
        "is_top": {"type": "boolean"},
        "item_id": {"type": "string"},
        "share_url": {"type": "string"},
        "statistics": {
            "type": "object",
            "properties": {
                "comment_count": {"type": "integer"},
                "digg_count": {"type": "integer"},
                "download_count": {"type": "integer"},
                "forward_count": {"type": "integer"},
                "play_count": {"type": "integer"},
                "share_count": {"type": "integer"},
            },
            "required": ["comment_count", "digg_count", "download_count", "forward_count", "play_count", "share_count"]
        },
        "title": {"type": "string"}
    },
    "required": ["cover", "create_time", "item_id", "share_url", "statistics"]
}