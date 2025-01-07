import os
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Project, Certification

# Define a Blueprint for routes
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/projects')
def projects():
    return render_template('projects.html')

@bp.route('/certifications')
def certifications():
    return render_template('certifications.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')




@bp.route('/upload_project', methods=['GET', 'POST'])
def upload_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        technologies = request.form['technologies']
        status = request.form['status']
        new_project = Project(name=name, description=description, technologies=technologies, status=status)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('upload_project.html')

@bp.route('/upload_certification', methods=['GET', 'POST'])
def upload_certification():
    if request.method == 'POST':
        title = request.form['title']
        issued_by = request.form['issued_by']
        file = request.files['file']

        # Define the path where you want to save the uploaded files
        cert_dir = os.path.join('static', 'certifications')

        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(cert_dir):
            os.makedirs(cert_dir)

        file_path = os.path.join(cert_dir, file.filename)

        # Save the file to the specified directory
        file.save(file_path)

        # Save certification information to the database
        new_cert = Certification(title=title, issued_by=issued_by, file_path=file_path)
        db.session.add(new_cert)
        db.session.commit()

        return redirect(url_for('main.home'))
    return render_template('upload_certification.html')

@bp.route('/upload_resume', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume-file']
        file_path = f"static/resumes/{file.filename}"
        file.save(file_path)
        # Save resume information to the database, if needed
        return redirect(url_for('main.home'))
    return render_template('upload_certification.html')  # You can reuse the same template for both

