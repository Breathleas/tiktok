# -*- coding: utf-8 -*-#
# Name:         request_chesi
# Description:  
# Author:       Wang Junling
# Date:         2019/11/25
# url=GET https://aweme-hl.snssdk.com/aweme/v1/user/follower/list/?user_id=82837571567&sec_user_id=MS4wLjABAAAAFp71FMEd0pI5b79w3g8U0RKC-eWWQbp0-66LPEWasmU&max_time=1573213013&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&openudid=13c46d80f289a105&version_name=8.8.0&ts=1574663582&device_type=google%20Pixel%202&ssmix=a&iid=93500901858&app_type=normal&os_api=19&mcc_mnc=46007&device_id=70018547270&resolution=720*1280&device_brand=google&aid=1128&manifest_version_code=880&app_name=aweme&_rticket=1574663576066&os_version=4.4.2&device_platform=android&version_code=880&update_version_code=8802&ac=wifi&dpi=240&uuid=865166011604629&language=zh&channel=tengxun_new

# tou={
# 'Accept-Encoding': 'gzip',
# 'X-SS-REQ-TICKET': '1574663576063',
# 'sdk-version': '1',
# 'User-Agent': 'ttnet okhttp/3.10.0.2',
# 'Cookie': 'install_id=93500901858; ttreq=1$4740a66ae36c4080b2d7cc8a35baff2cb7b5f186; d_ticket=7a3302b6b0c7ab05f297fc93ff7ce05904537; odin_tt=7e0dc3b0d764dce8a785ce7a6f17b0bdc1e54165c9e6bd4f1562289782ff2af36cdb8d48c1f0e71be46073c6eb31b8a28c66743e4cbcfc5e3b25890d50f28af9; sid_guard=51782efaf564fffddec65cb8cc7c9c14%7C1574662406%7C5184000%7CFri%2C+24-Jan-2020+06%3A13%3A26+GMT; uid_tt=cf77179c2829561bd5d2449d3223285a; sid_tt=51782efaf564fffddec65cb8cc7c9c14; sessionid=51782efaf564fffddec65cb8cc7c9c14',
#            install_id=93500901858; ttreq=1$4740a66ae36c4080b2d7cc8a35baff2cb7b5f186; d_ticket=7a3302b6b0c7ab05f297fc93ff7ce05904537; odin_tt=7e0dc3b0d764dce8a785ce7a6f17b0bdc1e54165c9e6bd4f1562289782ff2af36cdb8d48c1f0e71be46073c6eb31b8a28c66743e4cbcfc5e3b25890d50f28af9; sid_guard=51782efaf564fffddec65cb8cc7c9c14%7C1574662406%7C5184000%7CFri%2C+24-Jan-2020+06%3A13%3A26+GMT; uid_tt=cf77179c2829561bd5d2449d3223285a; sid_tt=51782efaf564fffddec65cb8cc7c9c14; sessionid=51782efaf564fffddec65cb8cc7c9c14
# 'x-tt-token': '0051782efaf564fffddec65cb8cc7c9c14ca3a392570b58821d82357bc3bbc96f42b25a1388d7eee6b2ae46ea1aaef7a6459',
#                0051782efaf564fffddec65cb8cc7c9c14ca3a392570b58821d82357bc3bbc96f42b25a1388d7eee6b2ae46ea1aaef7a6459
# 'X-Gorgon': '030100d741016b092274e377376454b71bbfeaf53dedc6a81893,
#              0301d0494001ab76e6fe247b7bfff88cdebc2033212b5f80a2ea
# 'X-Khronos': '1574664292',
# 'Host': 'aweme-hl.snssdk.com',
# 'Connection': 'Keep-Alive'
# }

import requests
headers={
'Accept-Encoding': 'gzip',
'X-SS-REQ-TICKET': '1574749938680',
# 'X-SS-REQ-TICKET'
'sdk-version': '1',
'User-Agent': 'ttnet okhttp/3.10.0.2',
'Cookie': 'install_id=93500901858; ttreq=1$4740a66ae36c4080b2d7cc8a35baff2cb7b5f186; d_ticket=8639c6b72b716126d2bd826f0bedc4f304537; odin_tt=17d65079427af1f99e997d2583902b66f2be16a31569935a63ef80dc14857354e34280611c93f7a0d2eb3a60c2904b50; msh=pnNzJqRMt6fBKPaQ3Y36ZBDVQAg; sid_guard=13b4c5e67a2ba020b713f5dded16f59d%7C1574748339%7C5184000%7CSat%2C+25-Jan-2020+06%3A05%3A39+GMT; uid_tt=24c35b64034f73d3b23d176e5a972e8d; sid_tt=13b4c5e67a2ba020b713f5dded16f59d; sessionid=13b4c5e67a2ba020b713f5dded16f59d',
'x-tt-token': '0013b4c5e67a2ba020b713f5dded16f59d87f0aa8dbd7b5fa47ba9b07490b7271cb57068f9ebdf4cfd4726480e1bf0744317',
'X-Gorgon': '030120da4101f3a9daa622031fb9b3da1d2b7c4b55e3891fbe8d',
# 'X-Gorgon'
'X-Khronos': '1574749938',
#X-Khronos
'Host': 'aweme-hl.snssdk.com',
'Connection': 'Keep-Alive'
}
url='http://aweme-hl.snssdk.com/aweme/v1/user/follower/list/?user_id=86462745631&sec_user_id=MS4wLjABAAAATcXaxd7WooDAiBWVMHx6DLxlz3jReQr4YgI_Il7qzBo&max_time=1564974669&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&openudid=13c46d80f289a105&version_name=8.8.0&ts=1574749941&device_type=google%20Pixel%202&ssmix=a&iid=93500901858&app_type=normal&os_api=19&mcc_mnc=46007&device_id=70018547270&resolution=720*1280&device_brand=google&aid=1128&manifest_version_code=880&app_name=aweme&_rticket=1574749938683&os_version=4.4.2&device_platform=android&version_code=880&update_version_code=8802&ac=wifi&dpi=240&uuid=865166011604629&language=zh&channel=tengxun_new'
  # "https://aweme-hl.snssdk.com/aweme/v1/user/follower/list/?user_id=82837571567&sec_user_id=MS4wLjABAAAAFp71FMEd0pI5b79w3g8U0RKC-eWWQbp0-66LPEWasmU&max_time=1574607282&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&openudid=13c46d80f289a105&version_name=8.8.0&ts=1574664300&device_type=google%20Pixel%202&ssmix=a&iid=93500901858&app_type=normal&os_api=19&mcc_mnc=46007&device_id=70018547270&resolution=720*1280&device_brand=google&aid=1128&manifest_version_code=880&app_name=aweme&_rticket=1574664292728&os_version=4.4.2&device_platform=android&version_code=880&update_version_code=8802&ac=wifi&dpi=240&uuid=865166011604629&language=zh&channel=tengxun_new"
  #max_time
  #ts
  #_rticket

rp=requests.get(url,headers=headers)
print(rp.text)