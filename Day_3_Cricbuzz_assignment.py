
from playwright.sync_api import sync_playwright, TimeoutError
from datetime import datetime

print("Starting Playwright script...")
print(f"Script started at: {datetime.now()}")

with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(headless=False)

    page = browser.new_page(
        viewport={"width": 1366, "height": 768}
    )

    try:
        # STEP 1: Open Cricbuzz
        print("\nStep 1: Opening Cricbuzz...")

        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        page.screenshot(
            path="cricbuzz.png",
            full_page=True
        )

        # STEP 2: Capture Live Scores section
        print("\nStep 2: Finding Live Scores...")

        live_scores = page.get_by_text(
            "LIVE SCORES",
            exact=False
        ).first

        try:
            live_scores.wait_for(timeout=15000)
            print("Live Scores section found!")

        except TimeoutError:
            print("Live Scores heading not found. Continuing...")

        page.screenshot(
            path="live_scores.png",
            full_page=True
        )

        # STEP 3: Find Sri Lanka vs Pakistan match
        print("\nStep 3: Searching for Sri Lanka vs Pakistan...")

        match_links = page.locator("a").evaluate_all("""
            elements => elements.map(a => ({
                text: a.innerText.trim(),
                href: a.href
            }))
        """)

        match_url = None

        for item in match_links:

            match_text = item["text"].lower()

            if ("sri lanka" in match_text
                and "pakistan" in match_text):

                match_url = item["href"]
                break

        if match_url:

            print("Match found:", match_url)

            # STEP 4: Open match details
            page.goto(
                match_url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(5000)

            page.screenshot(
                path="srilanka_pakistan.png",
                full_page=True
            )

            print("\nStep 5: Extracting match details...")

            # Extract visible page text
            score = page.locator("body").inner_text()

            print("\nMATCH DETAILS:")
            print(score)

            # STEP 6: Save details in text file
            with open(
                "cricbuzz_match_details.txt",
                "w",
                encoding="utf-8"
            ) as file:

                file.write("CRICBUZZ MATCH DETAILS\n")
                file.write("======================\n")
                file.write(
                    f"Date: {datetime.now()}\n\n"
                )
                file.write(score)

            print("\nText file saved successfully!")

        else:

            print("\nSri Lanka vs Pakistan match not found.")

            # Display matching links for debugging
            for item in match_links:
                if ("sri lanka" in item["text"].lower()
                    or "pakistan" in item["text"].lower()):

                    print(item["text"], item["href"])

    except Exception as e:

        print("\nERROR OCCURRED:")
        print(e)

    finally:

        print("\nClosing browser...")
        browser.close()

print("\nScript completed!")
