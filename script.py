import os

# 👉 Change this to the full path of your local portfolio folder
folder_path = r"C:\Users\ASUS\Downloads\VenkatJaswanth_Portfolio_Updated"

# Placeholder terms to replace
# suspect_terms = [
#     'I am a passionate developer skilled in Flutter, Java development, MySQL, and data structures and algorithms. With a strong foundation in Java and proficiency in Flutter, I have developed multiple projects showcasing my ability to create scalable applications with seamless user interfaces. My expertise in MySQL allows me to design robust databases, ensuring data integrity and accessibility. I am adept at writing efficient code and optimizing application performance, thanks to my solid understanding of data structures and algorithms.'
# ]

# # Replacement name
# replacement_name = 'This is about'
# suspect_terms = [
#     '<a href="https://www.linkedin.com/in/i-v-j" class="btn btn-primary py-3 px-3">LinkedIn</a>']

# # Replacement name
# replacement_name ='<a href="https://www.linkedin.com/in/i-v-j" class="btn btn-primary py-3 px-3">LinkedIn</a> <a href="https://leetcode.com/u/hxrdcoder21/" class="btn btn-primary py-3 px-3">LeetCode</a>'

suspect_terms = ['<a href="https://x.com/VatsaAditya1"><span class="icon-twitter"></span></a>']

# Replacement name
replacement_name ='<a href="https://www.linkedin.com/in/i_v_j/"><span class="icon-linkedin"></span></a>'

# Go through files and replace content
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(('.html', '.js')):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            original_content = content  # keep for comparison

            for term in suspect_terms:
                content = content.replace(term, replacement_name)

            # Write only if there was a change
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated: {file_path}")
