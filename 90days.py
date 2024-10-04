import requests
import urllib.parse
import os
import json

def days90(page_id, timeframe='LAST_90_DAYS', output_file='90.json'):
    url = "https://www.facebook.com/api/graphql/"

    # Get cookies from environment variables
    cookies = {
        'datr': os.environ.get('FB_DATR', ''),
        'sb': os.environ.get('FB_SB', ''),
        'c_user': os.environ.get('FB_C_USER', ''),
        'dpr': os.environ.get('FB_DPR', ''),
        'oo': os.environ.get('FB_OO', ''),
        'xs': os.environ.get('FB_XS', ''),
        'fr': os.environ.get('FB_FR', ''),
        'presence': os.environ.get('FB_PRESENCE', ''),
        'wd': os.environ.get('FB_WD', '')
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.facebook.com',
        'priority': 'u=1, i',
        'referer': f'https://www.facebook.com/ads/library/?active_status=active&ad_type=political_and_issue_ads&country=DE&media_type=all&search_type=page&view_all_page_id={page_id}',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.90", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.90"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'AdLibraryPageAudienceTabQuery',
        'x-fb-lsd': 'm5Ztd_ujjCyN5yv_gqBil1',
    }

    data = {
        'av': cookies['c_user'],
        '__aaid': '0',
        '__user': cookies['c_user'],
        '__a': '1',
        '__req': 'h',
        '__hs': '20000.HYP:comet_plat_default_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1017067526',
        '__s': 'a70jdq:6pd2oq:amgjv84',
        '__hsi': '7422004002273257624',
        '__dyn': '7xeUmxa13yoS1syUbFp432m2q1Dxu13wqovzEdF8ixy360CEbo9E3-xS6Ehw2nVEK12wvk0gq78b87C2m3K2y11wBz81s8hwGwQwoEcE7O2l0Fwqo31wp8kwyx2cwAxq1izXwrUcUjwGzE2VKUbo5G4EG1MUlwhE2Lxiaw5rwSyES0gq0K-1Lwqp8aE2cwmo6O1Fw5VwtUbUaU',
        '__csr': 'hA-FiSyWkBvAV4uiEKGA8VVAmUHAGQvmimam8ACCGbxq78eo6y1bw-wywei0gq3O16w9m3K04uo00y9y00A0U',
        '__comet_req': '1',
        'fb_dtsg': 'NAcNhN8o08KXRHH6TlIqDpaICFpIelcXeOgqTdLUdStIqbwWL4Xj3sw:25:1728062778',
        'jazoest': '25546',
        'lsd': 'm5Ztd_ujjCyN5yv_gqBil1',
        '__spin_r': '1017067526',
        '__spin_b': 'trunk',
        '__spin_t': '1728069969',
        '__jssesw': '1',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdLibraryPageAudienceTabQuery',
        'variables': json.dumps({"audienceTimeframe": timeframe, "viewAllPageID": page_id}),
        'server_timestamps': 'true',
        'doc_id': '8579646815389930',
    }

    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    if response.status_code == 200:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        # print(f"Data has been successfully retrieved and saved to {output_file}")
        return response.json()
    else:
        # print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Example usage:
# result = days90('248913988520756', timeframe='LAST_90_DAYS', output_file='facebook_ad_data_90days.json')
# if result:
#     print(result)
