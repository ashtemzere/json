import requests
import json

def scrape_apps():
    # ئەو لینکە سەرەکییەی زانیارییەکانی تێدایە (لێرەدا پەڕەی ١ دەهێنین)
    url = "https://ipasoon.icu/apps/apps.php?page=1&search="
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://ipasoon.icu/apps/'
    }
    
    try:
        # هێنانی زانیارییەکان لە وێبسایتەکەوە
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # چونکە وێبسایتەکە خۆی JSON دەداتەوە، ڕاستەوخۆ وەریدەگرین
        data = response.json()
        
        # پاشەکەوتکردنی لە فایلی apps.json
        with open('apps.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print("سەرکەوتوو بوو! زانیارییەکانی API یەکە وەرگیران و خەزن کران.")
        
    except Exception as e:
        print(f"هەڵەیەک ڕوویدا: {e}")

if __name__ == "__main__":
    scrape_apps()
