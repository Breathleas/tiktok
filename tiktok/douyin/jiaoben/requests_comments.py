# -*- coding: utf-8 -*-#
# Name:         requests_comments
# Description:  
# Author:       Wang Junling
# Date:         2019/11/26

import requests
import time

print(time.strftime('%Y %m %d %H %M %S',time.localtime(1574913641)))

headers={
'Accept-Encoding': 'gzip',
'X-SS-REQ-TICKET': '1574751234495',
# 'X-SS-REQ-TICKET'
'sdk-version': '1',
'User-Agent': 'ttnet okhttp/3.10.0.2',
'Cookie': 'install_id=93500901858; ttreq=1$4740a66ae36c4080b2d7cc8a35baff2cb7b5f186; d_ticket=8639c6b72b716126d2bd826f0bedc4f304537; odin_tt=17d65079427af1f99e997d2583902b66f2be16a31569935a63ef80dc14857354e34280611c93f7a0d2eb3a60c2904b50; msh=pnNzJqRMt6fBKPaQ3Y36ZBDVQAg; sid_guard=13b4c5e67a2ba020b713f5dded16f59d%7C1574748339%7C5184000%7CSat%2C+25-Jan-2020+06%3A05%3A39+GMT; uid_tt=24c35b64034f73d3b23d176e5a972e8d; sid_tt=13b4c5e67a2ba020b713f5dded16f59d; sessionid=13b4c5e67a2ba020b713f5dded16f59d',
'x-tt-token': '0013b4c5e67a2ba020b713f5dded16f59d87f0aa8dbd7b5fa47ba9b07490b7271cb57068f9ebdf4cfd4726480e1bf0744317',
'X-Gorgon': '0301b0024001072e7fdc9c43631a6b42cbbeae803dd46cec7de6',
# 'X-Gorgon'
'X-Khronos': '1574751234',
#X-Khronos
'Host': 'aweme-hl.snssdk.com',
'Connection': 'Keep-Alive'
}
url='https://aweme-hl.snssdk.com/aweme/v2/comment/list/?aweme_id=6655454541699403020&cursor=0&count=20&address_book_access=1&gps_access=1&forward_page_type=1&openudid=13c46d80f289a105&version_name=8.8.0&ts=1574751233&device_type=google%20Pixel%202&ssmix=a&iid=93500901858&app_type=normal&os_api=19&mcc_mnc=46007&device_id=70018547270&resolution=720*1280&device_brand=google&aid=1128&manifest_version_code=880&app_name=aweme&_rticket=1574751234498&os_version=4.4.2&device_platform=android&version_code=880&update_version_code=8802&ac=wifi&dpi=240&uuid=865166011604629&language=zh&channel=tengxun_new'
  # "https://aweme-hl.snssdk.com/aweme/v1/user/follower/list/?user_id=82837571567&sec_user_id=MS4wLjABAAAAFp71FMEd0pI5b79w3g8U0RKC-eWWQbp0-66LPEWasmU&max_time=1574607282&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&openudid=13c46d80f289a105&version_name=8.8.0&ts=1574664300&device_type=google%20Pixel%202&ssmix=a&iid=93500901858&app_type=normal&os_api=19&mcc_mnc=46007&device_id=70018547270&resolution=720*1280&device_brand=google&aid=1128&manifest_version_code=880&app_name=aweme&_rticket=1574664292728&os_version=4.4.2&device_platform=android&version_code=880&update_version_code=8802&ac=wifi&dpi=240&uuid=865166011604629&language=zh&channel=tengxun_new"
  #max_time
  #ts
  #_rticket

# rp=requests.get(url,headers=headers,verify=False)
# print(rp.text)

