### Selecting Elements with Multiple Classes in Selenium

If you want to select an element that has **multiple classes**, use `By.CSS_SELECTOR` and prefix each class with a dot (`.`), with **no spaces** between class names for the same element.

**Example:**  
Suppose you want to select an element with all these classes:  
`artdeco-button artdeco-button--secondary ml5`

Use:
```python
follow_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--secondary.ml5")
```

**Important Notes:**
- Spaces in a CSS selector mean a descendant, not multiple classes on the same element.
- For multiple classes on the **same element**, use `.class1.class2.class3` (no spaces).
- If you use spaces, like `.follow .artdeco-button`, it means you're looking for `.artdeco-button` inside `.follow`.

**Summary:**
- **Single class:**  
  `driver.find_element(By.CLASS_NAME, "classname")`
- **Multiple classes:**  
  `driver.find_element(By.CSS_SELECTOR, ".class1.class2")`