
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
import urllib.parse
import json
from jsonschema import validate as validate_schema
from datetime import datetime, timezone
import random

from schemas.douyin import save_post, save_post_statistics, \
                save_normie_profile, save_comment, save_normie_follow

class DouyinDB:
    def __init__(self, host, port, username, password, db_name):
        username = urllib.parse.quote_plus(username)
        password = urllib.parse.quote_plus(password)
        client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))
        self.db = client[db_name]

    def get_posts_fresher_than(self, hours=72, days=0):
        pass

    def save_post(self, shangol_profile_id: str, post_json: dict):
        """ Insert Douyin post into DouyinDB. 

        Args:
            profile_id: id of the Douyin user profile.
            post_json: the JSON representation of a single post, as obtained from the Douyin API (must match schema defined below).

        Return:
            _id of the inserted object in the DB. 
        """

        schema = save_post.schema
        
        try:
            validate_schema(instance=post_json, schema=schema)
        except Exception as e:
            print("JSON is incorrect.")
            raise e

        post_json["_id"] = post_json.pop("item_id")
        post_json["create_time"] = datetime.utcfromtimestamp(post_json["create_time"])
        post_json["shangol_profile_id"] = shangol_profile_id
        post_json["statistics"]["dt"] = datetime.now(timezone.utc)
        post_json["latest_stats"] = post_json["statistics"]
        post_json["statistics"] = [post_json["statistics"]]
        

        try:
            post_id = self.db.posts.insert_one(post_json).inserted_id
        except Exception as e:
            raise e

        return post_id

    def save_post_statistics(self, post_id: str, statistics_json: dict):
        """ Save statistics data point about a post into the DB.

        Args:
            post_id: the ID of the post (as found from the official Douyin API).
            statistics_json: the JSON representation of the statistics block in a post object, 
                             as obtained from the Douyin API (must match schema defined below).

        Returns:
            None
        """
        schema = save_post_statistics.schema
        
        try:
            validate_schema(instance=statistics_json, schema=schema)
        except Exception as e:
            raise e

        statistics_json["dt"] = datetime.now(timezone.utc)

        self.db.posts.update_one(
            { "_id": post_id},
            { 
                "$push": {"statistics": statistics_json},
                "$set": {
                    "latest_stats": statistics_json,
                    "last_updated": datetime.now(timezone.utc)
                }
            }
        )

    def save_normie_profile(self, kol_profile_id: str, normie_search_id: str, 
                            normie_unique_id: str, normie_uid: str,
                            normie_json: dict):

        schema = save_normie_profile.schema

        try:
            validate_schema(instance=normie_json, schema=schema)
        except Exception as e:
            raise e

        normie_json.pop('cover_url', None)
        normie_json.pop('video_icon', None)
        normie_json.pop('story_open', None)
        normie_json.pop('video_cover', None)
        normie_json.pop('ad_cover_url', None)
        normie_json.pop('ad_cover_url', None)
        normie_json.pop('avatar_medium', None)
        normie_json.pop('avatar_168x168', None)
        normie_json.pop('avatar_300x300', None)

        normie_json["kol_profile_id"] = kol_profile_id
        normie_json["search_id"] = normie_search_id
        normie_json["unique_id"] = normie_unique_id
        normie_json["_id"] = normie_uid

        try:
            normie_id = self.db.normies.insert_one(normie_json).inserted_id
        except Exception as e:
            raise e

        return normie_id

    def save_comment(self, commenter_id: str, post_id: str,
                    commenter_search_id: str, comment_json: dict):
        
        schema = save_comment.schema

        try:
            validate_schema(instance=comment_json, schema=schema)
        except Exception as e:
            raise e

        comment_json.pop('cover_url', None)
        comment_json.pop('video_icon', None)
        comment_json.pop('story_open', None)
        comment_json.pop('video_cover', None)
        comment_json.pop('ad_cover_url', None)
        comment_json.pop('ad_cover_url', None)
        comment_json.pop('avatar_medium', None)
        comment_json.pop('avatar_168x168', None)
        comment_json.pop('avatar_300x300', None)

        try:
            comment_id = self.db.comments.insert_one(comment_json).inserted_id
        except Exception as e:
            raise e

        return comment_id

    def save_normie_follows(self, shangol_profile_id: str, normie_id: str, followee_normie_id: str,
                            followee_json: dict):

        relation = {
            "shangol_profile_id": shangol_profile_id,
            "normie_id": normie_id,
            "followee_normie_id": followee_normie_id
        }

        relation_id = self.db.normie.follows.insert_one(relation).inserted_id

        schema = save_normie_follows.schema

        try:
            validate_schema(instance=followee_json, schema=schema)
        except Exception as e:
            raise e

        followee_json.pop('cover_url', None)
        followee_json.pop('video_icon', None)
        followee_json.pop('avatar_medium', None)
        followee_json.pop('avatar_168x168', None)
        followee_json.pop('avatar_300x300', None)

        try:
            normie_id = self.db.normies.insert_one(followee_json).inserted_id
        except Exception as e:
            raise e

        return normie_id


if __name__ == '__main__':
    host = '54.223.192.102'
    port = '27017'
    user = 'admin'
    password = '!5Gf7Au8Zq5SKYIy#@$v'
    db = 'DouyinDB'

    douyin = DouyinDB(host, port, user, password, db)

    with open('./samples/douyin/posts.json', 'r') as f:
        post = json.load(f)

    p = post["data"]["list"][0]

    p_id = douyin.save_post('abcdef', p)

    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

    prev_statistics = {
            "comment_count": 0,
            "digg_count": 0,
            "download_count": 0,
            "forward_count": 0,
            "play_count": 0,
            "share_count": 0,
        }


    for _ in range(144 * 3):

        #douyin.find_one({"_id": p_id})

        try:
            prev_statistics = douyin.db.posts.find_one( 
                {"_id": p_id}, 
                {"statistics": { "$slice": -1 } }
            )["statistics"][0]
        except Exception as xxx:
            print(xxx)

        curr_stats = {
            "comment_count": a - prev_statistics["comment_count"],
            "digg_count": b - prev_statistics["digg_count"],
            "download_count": c - prev_statistics["download_count"],
            "forward_count": d - prev_statistics["forward_count"],
            "play_count": e - prev_statistics["play_count"],
            "share_count": f - prev_statistics["share_count"],
        }

        douyin.save_post_statistics(p_id, curr_stats)

        

        a += 10
        b += 20
        c += 3
        d += 5
        e += 30
        f += 2
