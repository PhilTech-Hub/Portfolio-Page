from flask import render_template, request, redirect, url_for
from app import db
from app.models import Project, Certification
from app import create_app

app = create_app()  # Use the create_app function to instantiate the app


@app.route('/')
def index():
    projects = Project.query.all()
    certifications = Certification.query.all()
    return render_template('index.html', projects=projects, certifications=certifications)

@app.route('/upload_project', methods=['GET', 'POST'])
def upload_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        technologies = request.form['technologies']
        status = request.form['status']
        new_project = Project(name=name, description=description, technologies=technologies, status=status)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload_project.html')

@app.route('/upload_certification', methods=['GET', 'POST'])
def upload_certification():
    if request.method == 'POST':
        title = request.form['title']
        issued_by = request.form['issued_by']
        file = request.files['file']
        file_path = f"static/certifications/{file.filename}"
        file.save(file_path)
        new_cert = Certification(title=title, issued_by=issued_by, file_path=file_path)
        db.session.add(new_cert)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload_certification.html')


