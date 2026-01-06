from flask_frozen import Freezer
from app import app
import os
import shutil

# Configure the frozen app
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = False
app.config['FREEZER_BASE_URL'] = 'https://www.gradecalc.online/'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    # Clean the docs directory if it exists
    if os.path.exists('docs'):
        shutil.rmtree('docs')

    # Generate static files
    freezer.freeze()

    # Copy CNAME file to root of docs folder for GitHub Pages custom domain
    if os.path.exists('static/CNAME'):
        shutil.copy('static/CNAME', 'docs/CNAME')
        print("✅ CNAME file copied to docs/")

    print("✅ Static site generated successfully in 'docs' folder!")
    print(f"📁 Generated {len(list(freezer.all_urls()))} pages")
