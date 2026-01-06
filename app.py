from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Tools
@app.route('/tools/')
def tools():
    return render_template('tools/index.html')

@app.route('/tools/degree-classification-calculator.html')
def degree_calculator():
    return render_template('tools/degree-classification-calculator.html')

@app.route('/tools/gpa-calculator.html')
def gpa_calculator():
    return render_template('tools/gpa-calculator.html')

@app.route('/tools/exam-score-calculator.html')
def exam_score_calculator():
    return render_template('tools/exam-score-calculator.html')

@app.route('/tools/revision-timetable-generator.html')
def revision_timetable():
    return render_template('tools/revision-timetable-generator.html')

@app.route('/tools/module-grade-calculator.html')
def module_grade_calculator():
    return render_template('tools/module-grade-calculator.html')

# Guides
@app.route('/guides/')
def guides():
    return render_template('guides/index.html')

@app.route('/guides/how-degree-classifications-work-uk.html')
def guide_degree_classifications():
    return render_template('guides/how-degree-classifications-work-uk.html')

@app.route('/guides/how-to-get-a-first.html')
def guide_get_first():
    return render_template('guides/how-to-get-a-first.html')

@app.route('/guides/exam-grading-explained.html')
def guide_exam_grading():
    return render_template('guides/exam-grading-explained.html')

# Static Pages
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/privacy-policy.html')
def privacy():
    return render_template('privacy-policy.html')

@app.route('/terms.html')
def terms():
    return render_template('terms.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# SEO files
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt', mimetype='text/plain')

@app.route('/ads.txt')
def ads():
    return send_from_directory('static', 'ads.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
