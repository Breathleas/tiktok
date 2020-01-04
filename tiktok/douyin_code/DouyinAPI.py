import asyncio
import json
from aiohttp import ClientSession


class DouyinAPI(object):
    """ Wrapper interface around Douyin's API
    """

    def __init__(self, domain: str = "open.douyin.com", protocol: str = "https"):
        self.base_url = f"{protocol}://{domain}"

    async def get_posts(self, open_id: str, access_token: str, count: int, cursor: int) -> list:
        """ Retrieve list of posts from a user, desc-sorted by create_time.
            Official documentation: https://open.douyin.com/platform/doc/OpenAPI-video-list

        Args:
            open_id: (string). 通过/oauth/access_token/获取，用户唯一标志.
            access_token: (string). 调用/oauth/access_token/生成的token，此token需要用户授权.
            count: (int). 每页数量. 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 
                            同时response还会返回has_more来表明是否有更多的数据.
            cursor: (int). 第几页的游标

        Return:
            (list). List of `count` number of posts by user.
        """
        endpoint = "/video/list/?"
        params = f'cursor={cursor}&count={count}&open_id={open_id}&access_token={access_token}'
        url = self.base_url + endpoint + params
        Request_Record = 0

        while Request_Record < 5:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    response_text = await response.read()
                    if response.status == 200:
                        break
            Request_Record += 1
        return json.loads(response_text)

        # TODO: make request and return list of posts.

    async def get_post(self, open_id: str, access_token: str, item_ids: list):
        """ 该接口用于查询用户特定视频的数据, 如点赞数, 播放数等，返回的数据是实时的。
            Official documentation: https://open.douyin.com/platform/doc/OpenAPI-video-data

        Args:
            open_id: (string). 通过/oauth/access_token/获取，用户唯一标志
            access_token: (string). 调用/oauth/access_token/生成的token，此token需要用户授权。
            item_ids: (list). item_id数组，仅能查询access_token对应用户上传的视频

        Return:
            (list). List of post data corresponding to item_ids.
        """

        endpoint = "/video/data/"
        params = f'open_id={open_id}&access_token={access_token}'
        data = {
            "item_ids": item_ids
        }
        url = self.base_url + endpoint + params
        Request_Record = 0

        while Request_Record < 5:
            async with ClientSession() as session:
                async with session.post(url, data=data) as response:
                    response_text = await response.read()
                    if response.status == 200:
                        break
                Request_Record += 1
        return json.loads(response_text)
        # TODO: make request and return list of posts.

    def run_get_posts(self, open_id: str, access_token: str, count: int, cursor: int) -> list:
        tasks = []
        loop = asyncio.get_event_loop()
        for i in range(5):
            task = asyncio.ensure_future(
                DouyinAPI().get_posts(open_id=open_id, access_token=access_token, count=count, cursor=cursor))
            tasks.append(task)
        result = loop.run_until_complete(asyncio.gather(*tasks))
        return result


# if __name__ == "__main__":
#     douyin_api = DouyinAPI()
