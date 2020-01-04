schema = {
    "type": "object",
    "properties": {
        "uid": {"type": "string"},
        "gender": {"type": "integer"},
        "ins_id": {"type": "string"},
        "region": {"type": "string"},
        "sec_uid": {"type": "string"},
        "birthday": {"type": "string"},
        "nickname": {"type": "string"},
        "short_id": {"type": "string"},
        "unique_id": {"type": "string"},
        "avatar_uri": {"type": "string"},
        "has_orders": {"type": "boolean"},
        "weibo_name": {"type": "string"},
        "create_time": {"type": "integer"},
        "hide_search": {"type": "boolean"},
        "is_verified": {"type": "boolean"},
        "school_name": {"type": "string"},
        "school_type": {"type": "integer"},
        "avatar_thumb": {
            "type": "object",
            "properties": {
                "uri": {"type": "string"},
                "url_list": {"type": "array"},
            }
        },
        "avatar_larger": {
            "type": "object",
            "properties": {
                "uri": {"type": "string"},
                "url_list": {"type": "array"},
            }
        },
        "constellation": {"type": "integer"},
        "hide_location": {"type": "boolean"},
        "is_star_atlas": {"type": "integer"},
        "live_commerce": {"type": "boolean"},
        "authority_status": {"type": "integer"},
        "is_gov_media_vip": {"type": "boolean"},
        "share_qrcode_uri": {"type": "string"},
        "birthday_hide_level": {"type": "integer"},
        "commerce_user_level": {"type": "integer"},
        "with_commerce_entry": {"type": "boolean"},
        "unique_id_modify_time": {"type": "integer"},
        "enterprise_verify_reason": {"type": "string"}
    }
}