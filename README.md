# GradeCalc - Passive Learning & Assessment Tools Website

A passive income website featuring educational calculators and planning tools for assessments, exams, and learning outcomes. Built with Python Flask and vanilla JavaScript.

## Features

### 🧮 Calculators
- **UK Degree Classification Calculator** - Calculate final degree classification (First, 2:1, 2:2, Third)
- **GPA Calculator** - Calculate GPA on 4.0 or 5.0 scales
- **Exam Score Calculator** - Calculate exam percentages and pass/fail status
- **Revision Timetable Generator** - Create personalized study plans
- **Module Grade Calculator** - Calculate current grades and required exam marks

### 📚 Educational Guides
- How Degree Classifications Work (UK)
- How to Get a First Class Degree
- Exam Grading Explained

### ✨ Key Features
- 100% free, no sign-up required
- Mobile-first responsive design
- Client-side calculations (no data storage)
- SEO optimized for organic traffic
- Accessible and user-friendly

## Tech Stack

- **Backend:** Python 3.x with Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Hosting:** Can be deployed to Vercel, Netlify, Heroku, or any Python hosting
- **Database:** None (static site with client-side calculations)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PassiveProject
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## Project Structure

```
PassiveProject/
├── app.py                  # Flask application with routes
├── requirements.txt        # Python dependencies
├── static/
│   └── css/
│       └── style.css      # Main stylesheet (mobile-first)
├── templates/
│   ├── base.html          # Base template with header/footer
│   ├── index.html         # Homepage
│   ├── about.html         # About page
│   ├── contact.html       # Contact page
│   ├── privacy-policy.html
│   ├── terms.html
│   ├── tools/
│   │   ├── index.html                           # Tools listing
│   │   ├── degree-classification-calculator.html
│   │   ├── gpa-calculator.html
│   │   ├── exam-score-calculator.html
│   │   ├── revision-timetable-generator.html
│   │   └── module-grade-calculator.html
│   └── guides/
│       ├── index.html                          # Guides listing
│       ├── how-degree-classifications-work-uk.html
│       ├── how-to-get-a-first.html
│       └── exam-grading-explained.html
└── README.md
```

## Deployment

### Option 1: Traditional Hosting (Heroku, PythonAnywhere)

1. Add a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Add `gunicorn` to requirements.txt:
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

3. Deploy following your hosting provider's instructions

### Option 2: Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Create `vercel.json`:
   ```json
   {
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. Deploy:
   ```bash
   vercel
   ```

## SEO Optimization

- ✅ Semantic HTML structure
- ✅ Meta descriptions and keywords for each page
- ✅ Open Graph tags
- ✅ Mobile-friendly (Google's mobile-first indexing)
- ✅ Fast loading (no heavy dependencies)
- ✅ Clean URL structure
- ✅ Internal linking between pages

### Adding Google Analytics

Replace the placeholder in `templates/base.html` with your Google Analytics 4 tracking code:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Adding Google AdSense

Add AdSense code to relevant pages for monetization (typically after calculator and in content sections).

## Customization

### Changing the Brand Name

The current brand is "GradeCalc". To change it:

1. Update `templates/base.html` - change the logo text
2. Update page titles and meta descriptions
3. Update About page content
4. Consider purchasing a domain matching your new brand

### Adding New Calculators

1. Add route to `app.py`
2. Create template in `templates/tools/`
3. Add JavaScript calculation logic
4. Link from tools index page
5. Add to navigation in base template

## Maintenance

This site is designed for minimal maintenance:
- No database to manage
- No user accounts to moderate
- All calculations client-side
- Static content (update guides occasionally)

### Regular Tasks
- Monitor Google Analytics for traffic insights
- Update content if grading systems change
- Add new calculators based on user demand
- Refresh guides with current information

## Legal

- Ensure Privacy Policy and Terms are reviewed by legal counsel
- Update contact information in all pages
- Add cookie consent banner if required by your jurisdiction (GDPR, etc.)

## License

This project is built for educational and commercial purposes. Modify as needed for your use case.

## Support

For issues or questions about the codebase, refer to the inline code comments and Flask documentation.

---

**Built with ❤️ for passive income and helping learners worldwide**
