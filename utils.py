# import requests
import os
import json

# def get_data(url):
#     headers={
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'cache-control': 'no-cache',
#         'cookie': '_ga=GA1.1.819952447.1728886326; __cf_bm=rgb92NtmmwYzMF7wS35ae5qZJsDJdGiUjQu7CM5YTXA-1728887213-1.0.1.1-sxn12Ca1Jvki5B_Ai53_GGqfFyB4HTVNKzvtklGwejSOSSAEi9V9rx0JB_wVFnOSERkV4PpR8G60gNySQ.LKZA; _ga_0XM0LYXGC8=GS1.1.1728886326.1.1.1728887529.0.0.0; cf_clearance=ROXj.357lzilweGudkbQUA8zkVftNtXI3LDbtQwDPTk-1728887685-1.2.1.1-vS2.WN97HH_mHeAWrLDllPCQ4yC4UebOQlTvVskh2OqnujoDCYNDTiFpP5XJhaYNXCDYVw2VtoGVj8kicyKOYhkfu2KcRhalzqI4oIz6tQn9V_Fmph_bmsNw3tfAsJZ_ANtr73h96xR0zXSICTH0d9OWsBwrly55Rfr4ESeteYFtQUEy4U0ieShr6TjHqzmTJPD1nrORvzTEe0._NBQzY8F9GCYchA6.ACqjVqWdqvdf24e5xmIVKpF08PBUqBRxeBhUHLTjrANSvat8GEx.2VwtZJMkYSffI3LjNcKwJqn3gWTCFxHrjrWi7eBRaNAH2M7fv5Qfoed8eX.6pGq8CP1MS5OqwQfKSix3kbM3FQCQZyAZDH0p06CuwGPlxXGdQUDm0QzRJ2bjqqtQMWjwPzccScZlQruONtZfZ8HhsFmHR7D3cWDHKNjmxyvyYZOr',
#         'pragma': 'no-cache',
#         'priority': 'u=0, i',
#         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#         'sec-ch-ua-arch': '"x86"',
#         'sec-ch-ua-bitness': '"64"',
#         'sec-ch-ua-full-version': '"129.0.6668.90"',
#         'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.90", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.90"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-model': '""',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-ch-ua-platform-version': '"13.7.0"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'none',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
#     }

#     # 发起 GET 请求，添加头部
#     response = requests.get(url, headers=headers)
#     # 检查请求是否成功
#     if response.status_code == 200:
#         # 读取 JSON 数据
#         data = response.json()
#         return data
#     else:
#         print(f"请求失败，url：{url},状态码：{response.status_code}")


def get_data(url):
    command = f'''curl '{url}' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _ga=GA1.1.819952447.1728886326; cf_clearance=K3g92DANycOZFbQvwsBFlrIcJqD_dozBwG17Ww_aGs8-1728888439-1.2.1.1-alwQEq4xqHB2vD_7qDiMxP6cRCLir4mxadUfYT94qf7CaedK8k1Krf9meK5bK_Kun17sFuOU12gOwdPRYJrX0QWdJROlYFkV0sS0vbkp17pdjmF7kIEmGMrpeXxip69udvB4pQbqtTUwkkFnHt4gezAjqahzQvOpwKUbdwAHztgDbgadad9qzmCl5uzubZFrS6sjRAg631h433LFYOIbzLcZVKS3Aped4HvA3y3E4jiAgnC3QrW7qr_Jtf__yFqjnLcjbzf.X3xu9WLwle4mATtZE7YucIDj2_ZI9GOi88marHUrycE7qXwo9j78UCmt.M2UkQwMC1jwn4YqBPeg6eo44rJ6VPvLDtK8qhn.dnqJG6jQmdQk5WlKf5t6FWD3AoLA0N0WQbmyG8hIP_74.BcORCR2OFAz9pZc8HQF5NyVXWK3hHyHm8Jp4.aeFck5; __cf_bm=aEpgmzbb5TOnOwA2lPFFfPk_f6SQbq9re09RFbxnyTE-1728890886-1.0.1.1-lrWGRH.euYZWK6XnJMG.q0lpLAFlEMVkh2w1evb2VHMt_LRYKlV6tkAXyxCdQUCG62Dsuu7OJ.jWv8ESWBRv9A; _ga_0XM0LYXGC8=GS1.1.1728891632.2.0.1728891632.0.0.0' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://gmgn.ai/?chain=sol' \
  -H 'sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
  -H 'sec-ch-ua-arch: "x86"' \
  -H 'sec-ch-ua-bitness: "64"' \
  -H 'sec-ch-ua-full-version: "129.0.6668.90"' \
  -H 'sec-ch-ua-full-version-list: "Google Chrome";v="129.0.6668.90", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.90"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-model: ""' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-ch-ua-platform-version: "13.7.0"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
  '''
    response = os.popen(command).read()
    response = json.loads(response)
    return response['data']

