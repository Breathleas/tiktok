schema = {
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
}
