import os
from datetime import datetime

def generate_blog_index(blog_dir="blog"):
    posts = []
    for file in sorted(os.listdir(blog_dir), reverse=True):
        if file.endswith(".html") and file.startswith("blog_"):
            date_part = file.split("_")[1]
            date = datetime.strptime(date_part, "%Y-%m-%d").strftime("%B %d, %Y")
            title = file.replace("blog_", "").replace(".html", "").replace("_", " ").title()
            posts.append(f"<li>📅 {date} — <a href='{file}'>{title}</a></li>")

    html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Blog – TollywoodAI</title>
  <link rel='stylesheet' href='../styles.css'>
</head>
<body>
  <h1>📝 TollywoodAI Blog</h1>
  <ul>
    {'\n'.join(posts)}
  </ul>
  <p><a href='/'>← Back to Home</a></p>
</body>
</html>"""

    with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_blog_index()