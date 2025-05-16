
## Selenium Web Driver 

- type 
- click 
  


## Basic CSS Selector Syntax
- .className — selects elements with a specific class.
- #idName — selects an element with a specific id.
- tag — selects all elements with a specific tag (e.g., div, a, span).
- parent child — selects all child elements inside parent.
- .class1.class2 — selects elements with both class1 and class2.
- tag.class — selects elements with a specific tag and class.
  

we can find an element by its class name
- last_name_form = driver.find_element(By.CLASS_NAME, "form-control")


## Keep the browser open 
```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
```


## Using selenium-stealth to Avoid Detection

[`selenium-stealth`](https://github.com/diprajpatra/selenium-stealth) is a Python package that helps Selenium mimic real user behavior and avoid detection by anti-bot systems.

### Installation

```bash
pip install selenium-stealth
```

### Example Usage

```python
from selenium import webdriver
from selenium_stealth import stealth

driver = webdriver.Chrome()
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

driver.get("https://example.com")
```

### What does it do?
- Modifies browser fingerprinting properties (like `navigator.webdriver`, languages, vendor, etc.)
- Makes Selenium harder to detect as a bot.

> **Note:**  
> This does not guarantee bypassing all anti-bot systems, but it helps for many sites.  
> Use responsibly and respect website terms of service.