from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        print("Going to test.html...")
        page.goto("http://localhost:8125/test.html")
        page.wait_for_timeout(10000)
        browser.close()

if __name__ == "__main__":
    run()
