import subprocess
import os
def days7(country, page_id, date_range='7', output_file='7.json'):
    """
    Scrape the Facebook Ad Library for a specific page.

    :param country: Country code (e.g., 'DE' for Germany)
    :param page_id: Facebook Page ID
    :param date_range: '7' for last 7 days, '30' for last 30 days, '90' for last 90 days, or 'ALL' for all time
    :param output_file: Name of the output file
    """
    # Validate date_range
    valid_ranges = ['7', '30', '90', 'ALL']
    if date_range not in valid_ranges:
        raise ValueError(f"Invalid date_range. Must be one of {valid_ranges}")
    # Get cookies from environment variables
    datr = os.environ.get('FB_DATR', '')
    sb = os.environ.get('FB_SB', '')
    c_user = os.environ.get('FB_C_USER', '')
    xs = os.environ.get('FB_XS', '')
    dpr = os.environ.get('FB_DPR', '')
    fr = os.environ.get('FB_FR', '')
    oo = os.environ.get('FB_OO', '')
    wd = os.environ.get('FB_WD', '')
    # Construct the cookie string
    cookie = f"datr={datr}; sb={sb}; c_user={c_user}; xs={xs}; dpr={dpr}; fr={fr}; oo={oo}; wd={wd}"
    # Construct the curl command
    curl_command = f'''curl "https://www.facebook.com/ads/library/?active_status=active&ad_type=political_and_issue_ads&country={country}&media_type=all&search_type=page&view_all_page_id={page_id}&date_preset=LAST_{date_range}_DAYS" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7" -H "accept-language: en-GB,en;q=0.5" -H "cache-control: max-age=0" -H "cookie: {cookie}" -H "dpr: 1.5" -H "priority: u=0, i" -H "sec-ch-prefers-color-scheme: light" -H "sec-ch-ua: \\"Google Chrome\\";v=\\"129\\", \\"Not=A?Brand\\";v=\\"8\\", \\"Chromium\\";v=\\"129\\"" -H "sec-ch-ua-full-version-list: \\"Google Chrome\\";v=\\"129.0.6668.90\\", \\"Not=A?Brand\\";v=\\"8.0.0.0\\", \\"Chromium\\";v=\\"129.0.6668.90\\"" -H "sec-ch-ua-mobile: ?0" -H "sec-ch-ua-model: \\"\\""  -H "sec-ch-ua-platform: \\"Windows\\"" -H "sec-ch-ua-platform-version: \\"15.0.0\\"" -H "sec-fetch-dest: document" -H "sec-fetch-mode: navigate" -H "sec-fetch-site: same-origin" -H "sec-fetch-user: ?1" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36" -H "viewport-width: 423"'''
    # Run the curl command and capture the output
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    # Save the result output to the specified file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result.stdout)
    # print(f"The output has been saved to {output_file}")

# Example usage:
# days7('DE', '248913988520756', date_range='30', output_file='facebook_ads_30days.txt')
# Example usage:
# scrape_facebook_ad_library('DE', '248913988520756', date_range='30', output_file='facebook_ads_30days.txt')
