# XML Site Scraper & Link Evaluator

A robust, production-grade Python web scraper built to perform automated batch extraction and evaluation of structured XML data endpoints. This project was developed based on a real-world client requirement on Upwork to fetch, validate, and parse thousands of structured XML data instances safely and efficiently.

## 📋 Project Overview

The core objective of this project is to sequentially parse sequentially indexed XML nodes (ranging from index 10 to 55,000), extract key nested datasets (`Exercise Name` and compiled `Instructions/Purposes`), filter out bad/redirected endpoints, and compile the final sanitized data into a structured CSV file.

## 🚀 Key Features

- **Smart Link Evaluation (Redirect Filtering):** Dynamically tracks response headers to detect and skip broken or dead links that auto-redirect back to the main site domain.
- **Deep XML Tree Traversal:** Utilizes `BeautifulSoup` with an XML parser to precisely target specific structural elements (`<exercise>`, `<instruction>`, `<purpose>`).
- **Anti-Scraping Resilience:** Simulates authentic mobile/desktop browser headers (`User-Agent`, `Accept-Language`, etc.) paired with randomized throttle delays (`1.5s to 3.5s`) to mitigate IP bans and rate limits.
- **Network Failsafe Mechanism:** Built-in connection monitoring that catches `ConnectionError` instantly and terminates executions gracefully without generating redundant error loops.
- **Automated CSV Data Pipeline:** Automatically checks for pre-existing tracking datasets and sequentially streams new clean outputs to prevent data overwrite.

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.x
- **Libraries Used:** 
  - `requests` (HTTP Networking Engine)
  - `beautifulsoup4` (XML/HTML DOM Parsing)
  - `time` & `random` (Humanized Delay Simulators)
  - `csv` & `os` (File I/O & Data Structuring)
  - `sys` (Process Controls)

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tuhin-cybersec/python-xml-scraper.git
   cd python-xml-scraper
