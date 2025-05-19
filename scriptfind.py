import os

# Set the path to your portfolio folder
folder_path = r"C:\Users\ASUS\Downloads\VenkatJaswanth_Portfolio_Updated"

# Suspect placeholder terms to search for
suspect_terms = ['<h3 class="mb-4">Contact Number</h3>']

# Store matches
matches = {}

# Walk through the directory
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(('.html', '.js')):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for term in suspect_terms:
                    if term in content:
                        if file_path not in matches:
                            matches[file_path] = []
                        matches[file_path].append(term)

# Output results
for file, terms in matches.items():
    print(f"\nIn file: {file}")
    for term in terms:
        print(f"  Found: {term}")
