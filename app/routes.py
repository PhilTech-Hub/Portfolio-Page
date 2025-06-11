import os
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Project, Certification
from flask_login import login_required, current_user
from flask import send_from_directory

# Define a Blueprint for routes
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/profile')
def profile():
    return render_template('profile.html', user=current_user)


@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)

@bp.route('/certifications')
def certifications():
    all_certifications = Certifications.query.all()
    return render_template('certifications.html', certifications=all_certifications)


@bp.route('/blog')
def blog():
    return render_template('blog.html')


@bp.route('/download_cv')
def download_cv():
    return send_from_directory(
        os.path.join(bp.root_path, 'static/files'),
        'My_CV.pdf',
        as_attachment=True
    )




@bp.route('/upload_project', methods=['GET', 'POST'])
@login_required
def upload_project():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        technologies = request.form.get('technologies')
        status = request.form.get('status')

        # Basic validation
        if not all([name, description, technologies, status]):
            return "All fields are required", 400

        new_project = Project(
            name=name,
            description=description,
            technologies=technologies,
            status=status
        )
        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('main.projects'))  # Redirect to projects listing page

    return render_template('upload_project.html')


@bp.route('/upload_certification', methods=['GET', 'POST'])
@login_required
def upload_certification():
    if request.method == 'POST':
        title = request.form['title']
        issued_by = request.form['issued_by']
        file = request.files['file']

        if not file:
            return "No file uploaded", 400

        # Secure and unique file name (optional)
        filename = file.filename
        cert_dir = os.path.join('static', 'certifications')

        if not os.path.exists(cert_dir):
            os.makedirs(cert_dir)

        save_path = os.path.join(cert_dir, filename)
        file.save(save_path)

        # Save only the relative path
        relative_path = os.path.join('certifications', filename)

        new_cert = Certification(title=title, issued_by=issued_by, file_path=relative_path)
        db.session.add(new_cert)
        db.session.commit()

        return redirect(url_for('main.projects'))  # Optional: redirect to see uploaded cert
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

