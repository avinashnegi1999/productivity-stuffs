import re
import os

readme_path = "README.md"

def main():
    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 1. Calculate Progress
    total_tasks = 0
    completed_tasks = 0
    
    # We join lines to count tasks properly in case of formatting oddities, 
    # but counting line-by-line is usually safer for Markdown lists
    content = "".join(lines)
    total_tasks = len(re.findall(r"-\s\[[xX ]\]", content))
    completed_tasks = len(re.findall(r"-\s\[[xX]\]", content))

    if total_tasks > 0:
        percent = int((completed_tasks / total_tasks) * 100)
    else:
        percent = 0

    print(f"Detected: {completed_tasks}/{total_tasks} tasks ({percent}%)")

    # 2. Determine Color
    if percent == 100: color = "success" # Green
    elif percent > 50: color = "yellow"
    else: color = "red"

    # 3. generate New Badge Line
    new_badge_line = f"![Progress](https://img.shields.io/badge/Progress-{percent}%25-{color}?style=for-the-badge)\n"

    # 4. Find and Replace the Badge Line
    updated_lines = []
    badge_found = False

    for line in lines:
        # Check if this line looks like the progress badge
        if "![Progress]" in line and "img.shields.io" in line:
            updated_lines.append(new_badge_line)
            badge_found = True
            print("Badge line found and updated.")
        else:
            updated_lines.append(line)

    # 5. If no badge existed, add it to the top
    if not badge_found:
        print("No badge found. Adding to top.")
        updated_lines.insert(1, new_badge_line) # Insert after title (usually line 1 or 2)

    # 6. Save File
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    main()
