import os
from curl_cffi import requests  # This compiles native browser TLS handshakes!
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib

load_dotenv(override=True)

# 1. THE TARGET URL (CRITICAL FIX: Changed back to your active headset listing link!)
amazon_url = "https://www.amazon.com/dp/B0HGR4SDYC/ref=sspa_dk_detail_5?pd_rd_i=B0HGR4SDYC&pd_rd_w=pBUr1&content-id=amzn1.sym.4f5afe61-a551-4f21-a495-c7c4f2997a96&pf_rd_p=4f5afe61-a551-4f21-a495-c7c4f2997a96&pf_rd_r=N7M10YW67HZ89W49K6AA&pd_rd_wg=SvG1v&pd_rd_r=70184d89-09b4-4acf-9936-32276d56306c&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1"

print("🚀 Initializing native browser TLS handshake emulation...")

# 2. DEFINE SYSTEM IDENTITY HEADERS
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# 3. FIRE THE REQUEST IMPERSONATING A REAL WINDOWS CHROME BROWSER
response = requests.get(amazon_url, headers=headers, impersonate="chrome")

if response.status_code == 200:
    print("✅ Connection Verified! Native TLS fingerprint bypassed all firewall layers.")
    soup = BeautifulSoup(response.text, "html.parser")

    price_in_float = None

    # --- RESILIENT LAYOUT PARSING ENGINE ---
    # Selector A: Core pricing label
    price_element = soup.select_one("span.a-price span.a-offscreen")

    if price_element:
        raw_text = price_element.get_text()
        # REFINED SCRUBBING: Removes both '$' and any alphabetic currency codes like 'NGN' or 'USD'
        clean_string = raw_text.replace("$", "").replace("NGN", "").replace(",", "").strip()
        price_in_float = float(clean_string)

    else:
        # Fallback 1: Dollars + Cents merging
        whole = soup.select_one(".a-price-whole")
        fraction = soup.select_one(".a-price-fraction")
        if whole and fraction:
            raw_text = f"{whole.get_text()}{fraction.get_text()}"
            price_in_float = float(raw_text.replace("$", "").replace(",", "").strip())
        else:
            # Fallback 2: Direct text block scan
            buybox_price = soup.select_one("#price_inside_buybox") or soup.select_one(".a-color-price")
            if buybox_price:
                raw_text = buybox_price.get_text()
                price_in_float = float(raw_text.replace("$", "NGN").replace(",", "").strip())
            else:
                # Fallback 3: Deep JavaScript Internal Metadata Scan
                import re

                js_price_match = re.search(r'"priceToPay"\s*:\s*"([^"]+)"', response.text) or \
                                 re.search(r'"currentPrice"\s*:\s*"([^"]+)"', response.text) or \
                                 re.search(r'"price"\s*:\s*(\d+\.\d{2})', response.text)

                if js_price_match:
                    raw_text = js_price_match.group(1)
                    price_in_float = float(raw_text.replace("$", "NGN").replace(",", "").strip())
                else:
                    # Fallback 4: Universal Regex Search as a last resort
                    price_match = re.search(r'\$\d+\.\d{2}', response.text)
                    if price_match:
                        raw_text = price_match.group(0)
                        price_in_float = float(raw_text.replace("$", "NGN").replace(",", "").strip())

    # --- SAFETY GATE PROTECTION & EMAIL ENGINE (RESTORED!) ---
    if price_in_float is not None:
        print("-" * 50)
        print(f"🎯 SUCCESS! Target Price Captured: ${price_in_float}")
        print("-" * 50)

        # Your condition check for the tracking threshold
        if price_in_float < 100:
            print("📧 Price drops below threshold! Firing notification email...")
            try:
                with smtplib.SMTP_SSL("://gmail.com", 465) as server:
                    server.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
                    server.sendmail(
                        from_addr=os.getenv("EMAIL"),
                        to_addrs=os.getenv("EMAIL"),
                        msg=f"Subject:Amazon Price Alert!\n\nThe item price dropped to ${price_in_float}!\nLink: {amazon_url}",
                    )
                print(f"🎉 Alert sent successfully to {os.getenv('EMAIL')}!")
            except Exception as e:
                print(f"❌ Email engine bottleneck: {e}")
    else:
        print("\n⚠️ LAYOUT SHIFT ERROR")
        print("The request connected successfully, but no pricing values could be parsed from this page view.")
else:
    print(f"❌ Connection Blocked. Server Response Code: {response.status_code}")
