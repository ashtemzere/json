import requests
from bs4 import BeautifulSoup
import json

# لینکی وێبسایتەکە
url = "https://ipasoon.icu/apps/"

# بەکارهێنانی User-Agent بۆ ئەوەی وێبسایتەکە بلۆکمان نەکات
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_apps():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        apps_list = []
        
        # تێبینی: پێویستە ئەم کلاسانە (class) بگۆڕیت بەپێی کۆدی HTML ی وێبسایتەکە
        # چونکە لە وێنەکەدا تەنها ڕووکارەکە دیارە
        app_cards = soup.find_all('div', class_='app-card-class-name') 
        
        for card in app_cards:
            name = card.find('h3', class_='app-title-class').text.strip() if card.find('h3', class_='app-title-class') else "N/A"
            version = card.find('span', class_='version-class').text.strip() if card.find('span', class_='version-class') else "N/A"
            date = card.find('span', class_='date-class').text.strip() if card.find('span', class_='date-class') else "N/A"
            icon_url = card.find('img')['src'] if card.find('img') else ""
            
            app_data = {
                "name": name,
                "version": version,
                "date": date,
                "icon": icon_url
            }
            apps_list.append(app_data)
            
        # پاشەکەوتکردنی وەک فایلی JSON
        with open('apps.json', 'w', encoding='utf-8') as f:
            json.dump({"apps": apps_list}, f, ensure_ascii=False, indent=4)
            
        print(f"سەرکەوتوو بوو: {len(apps_list)} بەرنامە خەزن کرا.")
        
    except Exception as e:
        print(f"هەڵەیەک ڕوویدا: {e}")

if __name__ == "__main__":
    scrape_apps()
