schema = {
    "type": "object",
    "properties": {
        "uid": {"type": "string"},
        "city": {"type": "string, null"},
        "gender": {"type": "integer"},
        "ins_id": {"type": "string, null"},
        "region": {"type": "string, null"},
        "secret": {"type": "integer"},
        "wx_tag": {"type": "integer"},
        "country": {"type": "string"},
        "is_star": {"type": "boolean"},
        "room_id": {"type": "integer"},
        "sec_uid": {"type": "string"},
        "activity": {
            "type": "object",
            "properties": {
                "digg_count": {"type": "integer"},
                "use_music_count": {"type": "integer"}
            },
            "required": ["digg_count", "use_music_count"]
        },
        "birthday": {"type": "string"},
        "district": {"type": "string"},
        "location": {"type": "string"},
        "nickname": {"type": "string"},
        "province": {"type": "string"},
        "short_id": {"type": "string"},
        "unique_id": {"type": "string"},
        "share_info": {
            "type": "object",
            "properties": {
                "share_url": {"type": "string"},
                "bool_persist": {"type": "boolean"},
                "share_qrcode_url": {
                    "type": "object",
                    "properties": {
                        "uri": {"type": "string"},
                        "url_list": {"type": "array"},
                    },
                }
            }
        },
        "aweme_count": {"type": "array"},
        "is_verified": {"type": "boolean"},
        "school_name": {"type": "string"},
        "user_period":0,
        "verify_info":"",
        "avatar_thumb": {
            "type": "object",
            "properties": {
                "uri": {"type": "string"},
                "url_list": {"type": "array"},
            }
        },
        "college_name": {"type": "string"},
        "avatar_larger": {
            "type": "object",
            "properties": {
                "uri": {"type": "string"},
                "url_list": {"type": "array"},
            }
        },
        "constellation": {"type": "integer"},
        "dongtai_count": {"type": "integer"},
        "follow_status": {"type": "integer"},
        "hide_location": {"type": "boolean"},
        "live_commerce": {"type": "boolean"},
        "follower_count": {"type": "integer"},
        "comment_setting": {"type": "integer"},
        "follower_status": {"type": "integer"},
        "following_count": {"type": "integer"},
        "total_favorited": {"type": "integer"},
        "with_shop_entry": {"type": "boolean"},
        "favoriting_count": {"type": "integer"},
        "followers_detail": {
            "type": "array",
            "items": {
                "icon": {"type": "string"},
                "name": {"type": "string"},
                "app_name": {"type": "string"},
                "apple_id": {"type": "string"},
                "open_url": {"type": "string"},
                "fans_count": {"type": "integer"},
                "download_url": {"type": "string"},
                "package_name": {"type": "string"}
            }
        },
        "is_activity_user": {"type": "boolean"},
        "is_effect_artist": {"type": "boolean"},
        "is_gov_media_vip": {"type": "boolean"},
        "share_qrcode_uri": {"type": "string"},
        "user_story_count": {"type": "integer"},
        "latest_order_time": {"type": "integer"},
        "original_musician": {
            "type": "object",
            "properties" : {
                "digg_count": {"type": "integer"},
                "music_count": {"type": "integer"},
                "music_used_count": {"type": "integer"}
            }
        },
        "has_activity_medal": {"type": "boolean"},
        "birthday_hide_level": {"type": "integer"},
        "commerce_user_level": {"type": "integer"},
        "with_commerce_entry": {"type": "boolean"},
        "unique_id_modify_time": {"type": "integer"},
        "with_fusion_shop_entry": {"type": "boolean"},
        "enterprise_verify_reason": {"type": "string"},
        "mplatform_followers_count": {"type": "integer"},
        "recommend_reason_relation": {"type": "string"},
        "hide_following_follower_list": {"type": "integer"},
        "with_commerce_enterprise_tab_entry": {"type": "boolean"},
    }
}