import re
import os

# --- CONFIGURATION ---
README_FILE = "README.md"
# ---------------------

def load_readme():
    """Loads the README file content."""
    if not os.path.exists(README_FILE):
        print(f"❌ Error: {README_FILE} not found in the current directory.")
        return None
    with open(README_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def parse_tasks(lines):
    """Finds all task checkboxes in the markdown lines."""
    tasks = []
    # Regex finds '- [ ]' or '- [x]' followed by text
    pattern = re.compile(r"^\s*-\s*\[([ xX])\]\s*(.*)")
    
    for i, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            is_checked = match.group(1).lower() == 'x'
            raw_text = match.group(2).strip()
            # Clean up links for display (remove [text](url))
            display_text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", raw_text)
            
            tasks.append({
                "index": i,
                "checked": is_checked,
                "text": display_text
            })
    return tasks

def update_badge(lines, percent):
    """Updates the Shields.io progress badge color and percentage."""
    # Determine color based on progress
    if percent < 30: color = "red"
    elif percent < 70: color = "yellow"
    else: color = "success" # Green
    
    # Regex to find the badge line
    # Matches: ![Progress](https://img.shields.io/badge/Progress-NUMBER%-COLOR...)
    badge_pattern = re.compile(r"!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-[a-zA-Z]+")
    new_badge = f"![Progress](https://img.shields.io/badge/Progress-{percent}%25-{color}"
    
    updated_lines = []
    found = False
    for line in lines:
        if "img.shields.io/badge/Progress" in line:
            # Replace the old badge URL with the new one
            new_line = badge_pattern.sub(new_badge, line)
            updated_lines.append(new_line)
            found = True
        else:
            updated_lines.append(line)
            
    if found:
        return updated_lines
    return lines

def save_readme(lines, tasks):
    """Writes changes back to the README file."""
    
    # 1. Update Checkboxes in the text
    for task in tasks:
        mark = "x" if task["checked"] else " "
        original_line = lines[task["index"]]
        # robust replacement of [ ] or [x]
        lines[task["index"]] = re.sub(r"\[([ xX])\]", f"[{mark}]", original_line, count=1)

    # 2. Calculate Stats
    total = len(tasks)
    completed = sum(1 for t in tasks if t["checked"])
    percent = int((completed / total) * 100) if total > 0 else 0

    # 3. Update the Badge
    lines = update_badge(lines, percent)

    # 4. Save File
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
    
    print(f"\n✅ README updated! Progress: {percent}% ({completed}/{total} tasks)")

def main():
    lines = load_readme()
    if not lines: return

    while True:
        tasks = parse_tasks(lines)
        if not tasks:
            print("No tasks found in README.md. Make sure you have '- [ ]' items.")
            break

        # Display Interface
        print("\n" + "="*50)
        print(f" 🚀 ROADMAP TRACKER ")
        print("="*50)
        
        for i, task in enumerate(tasks):
            icon = "✅" if task["checked"] else "⬜"
            # Format: 1. ✅ Learn Python
            print(f"{i+1:2}. {icon} {task['text']}")
        
        print("\nCommands:")
        print("• Type number (e.g. '1') to toggle.")
        print("• Type 'q' to save and quit.")
        
        choice = input("\nSelect Action: ").strip().lower()
        
        if choice == 'q':
            save_readme(lines, tasks)
            break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(tasks):
                # Toggle status in memory
                tasks[idx]["checked"] = not tasks[idx]["checked"]
                
                # Update the specific line in 'lines' immediately so loop reflects it
                mark = "x" if tasks[idx]["checked"] else " "
                lines[tasks[idx]["index"]] = re.sub(r"\[([ xX])\]", f"[{mark}]", lines[tasks[idx]["index"]], count=1)
            else:
                print("❌ Invalid number.")
        except ValueError:
            print("❌ Invalid input.")

if __name__ == "__main__":
    main()
