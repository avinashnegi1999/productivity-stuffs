import re
import os

readme_path = "README.md"

if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Count tasks
    # Finds '- [ ]' or '- [x]'
    total_tasks = len(re.findall(r"-\s\[[xX ]\]", content))
    completed_tasks = len(re.findall(r"-\s\[[xX]\]", content))
    
    # 2. Calculate Math
    if total_tasks > 0:
        percent = int((completed_tasks / total_tasks) * 100)
    else:
        percent = 0

    # 3. Determine Color
    if percent < 30: color = "red"
    elif percent < 70: color = "yellow"
    else: color = "success"

    # 4. Update the Badge Link
    # Looks for: ![Progress](https://img.shields.io/badge/Progress-NUMBER%-COLOR...)
    new_badge = f"![Progress](https://img.shields.io/badge/Progress-{percent}%25-{color}?style=for-the-badge)"
    
    new_content = re.sub(
        r"!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-[a-zA-Z]+\?style=for-the-badge\)",
        new_badge,
        content
    )

    # 5. Save ONLY if changed
    if new_content != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated progress to {percent}%")
    else:
        print("No changes needed.")
