from flask_frozen import Freezer
from app import app
import os
import shutil

# Configure the frozen app
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = False
app.config['FREEZER_BASE_URL'] = 'https://joehill06.github.io/PassiveProject/'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    # Clean the docs directory if it exists
    if os.path.exists('docs'):
        shutil.rmtree('docs')

    # Generate static files
    freezer.freeze()

    print("✅ Static site generated successfully in 'docs' folder!")
    print(f"📁 Generated {len(list(freezer.all_urls()))} pages")
