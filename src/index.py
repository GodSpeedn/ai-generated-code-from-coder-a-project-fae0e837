# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24) # Required for flashing messages

# --- Routes ---

@app.route('/')
def index():
    """Renders the homepage with hero, features, and contact form."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handles contact form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic server-side validation
        if not name or not email or not message:
            flash('All fields are required!', 'danger')
            return redirect(url_for('index'))
        
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'danger')
            return redirect(url_for('index'))

        # In a real application, you would process this data:
        # - Send an email
        # - Save to a database
        # - Integrate with a CRM
        print(f"New Contact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print("-" * 30)

        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact_success'))
    
    # If someone tries to access /contact directly via GET, redirect to home
    return redirect(url_for('index'))

@app.route('/contact-success')
def contact_success():
    """Renders a success page after contact form submission."""
    return render_template('contact_success.html')

# --- Main execution ---
if __name__ == '__main__':
    # Create static directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('templates', exist_ok=True)

    # Placeholder for static/css/style.css
    with open('static/css/style.css', 'w') as f:
        f.write("""
/* Custom styles for AI Startup Landing Page */
body {
    font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
}

.navbar {
    background-color: #0d1a26 !important; /* Dark blue/black for nav */
    padding: 1rem 0;
}

.navbar-brand {
    font-weight: bold;
    color: #00bcd4 !important; /* Cyan for brand */
    font-size: 1.8rem;
}

.nav-link {
    color: #e0e0e0 !important;
    margin-left: 1rem;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #00bcd4 !important;
}

.hero-section {
    background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('/static/images/hero_bg.jpg') no-repeat center center;
    background-size: cover;
    color: white;
    padding: 100px 0;
    text-align: center;
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-section h1 {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: #00bcd4; /* Cyan for hero heading */
}

.hero-section p {
    font-size: 1.25rem;
    margin-bottom: 30px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.btn-primary-ai {
    background-color: #00bcd4; /* Cyan button */
    border-color: #00bcd4;
    padding: 12px 30px;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 50px;
    transition: all 0.3s ease;
}

.btn-primary-ai:hover {
    background-color: #00a8b8;
    border-color: #00a8b8;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 188, 212, 0.3);
}

.features-section {
    padding: 80px 0;
    background-color: #ffffff;
}

.features-section h2 {
    color: #0d1a26;
    font-weight: 700;
    margin-bottom: 50px;
}

.feature-item {
    text-align: center;
    padding: 30px;
    border-radius: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    background-color: #f8f9fa;
    margin-bottom: 30px;
}

.feature-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.feature-item i {
    font-size: 3rem;
    color: #00bcd4;
    margin-bottom: 20px;
}

.feature-item h3 {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 15px;
    color: #0d1a26;
}

.contact-section {
    padding: 80px 0;
    background-color: #e9ecef;
}

.contact-section h2 {
    color: #0d1a26;
    font-weight: 700;
    margin-bottom: 40px;
}

.form-control {
    border-radius: 0.5rem;
    padding: 0.75rem 1rem;
    border: 1px solid #ced4da;
}

.form-control:focus {
    border-color: #00bcd4;
    box-shadow: 0 0 0 0.2rem rgba(0, 188, 212, 0.25);
}

textarea.form-control {
    min-height: 150px;
    resize: vertical;
}

.footer {
    background-color: #0d1a26;
    color: #e0e0e0;
    padding: 40px 0;
    text-align: center;
    font-size: 0.9rem;
}

.footer a {
    color: #00bcd4;
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* About Page Specific */
.about-section {
    padding: 80px 0;
    background-color: #ffffff;
    min-height: calc(100vh - 180px); /* Adjust based on header/footer height */
}

.about-section h1 {
    color: #0d1a26;
    font-weight: 700;
    margin-bottom: 30px;
}

.about-section p {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}

/* Contact Success Page Specific */
.contact-success-section {
    padding: 80px 0;
    background-color: #ffffff;
    min-height: calc(100vh - 180px); /* Adjust based on header/footer height */
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.contact-success-section h1 {
    color: #28a745; /* Green for success */
    font-weight: 700;
    margin-bottom: 20px;
}

.contact-success-section p {
    font-size: 1.2rem;
    margin-bottom: 30px;
}

.alert {
    margin-top: 1rem;
    border-radius: 0.5rem;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .hero-section h1 {
        font-size: 2.5rem;
    }
    .hero-section p {
        font-size: 1rem;
    }
    .navbar-brand {
        font-size: 1.5rem;
    }
    .nav-link {
        margin-left: 0;
        text-align: center;
    }
    .feature-item {
        padding: 20px;
    }
    .feature-item h3 {
        font-size: 1.3rem;
    }
}
""")

    # Placeholder for static/js/script.js
    with open('static/js/script.js', 'w') as f:
        f.write("""
// Custom JavaScript for AI Startup Landing Page
// (Currently empty, but ready for future enhancements)

document.addEventListener('DOMContentLoaded', function() {
    // Example: Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
""")

    # Placeholder for static/images/hero_bg.jpg (replace with a real image)
    # For demonstration, we'll create a dummy file. In a real app, you'd place an actual image here.
    try:
        from PIL import Image
        img = Image.new('RGB', (1920, 1080), color = 'grey')
        img.save('static/images/hero_bg.jpg')
    except ImportError:
        print("Pillow not installed. Cannot create dummy image. Please place a 'hero_bg.jpg' in static/images manually.")
        with open('static/images/hero_bg.jpg', 'w') as f:
            f.write("Dummy image content - replace with actual image.")

    # Placeholder for static/favicon.ico
    # For demonstration, we'll create a dummy file. In a real app, you'd place an actual favicon here.
    with open('static/favicon.ico', 'w') as f:
        f.write("Dummy favicon content - replace with actual .ico file.")

    # base.html template
    with open('templates/base.html', 'w') as f:
        f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Cutting-edge AI solutions for your business. Explore our innovative products and services.">
    <meta name="keywords" content="AI, Artificial Intelligence, Startup, Technology, Machine Learning, Deep Learning, Innovation">
    <meta name="author" content="AI Startup">
    <title>AI Innovate - Intelligent Solutions for the Future</title>
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">AI Innovate</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{{ url_for('index') }}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('about') }}">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 AI Innovate. All rights reserved. | <a href="{{ url_for('about') }}">Privacy Policy</a></p>
        </div>
    </footer>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
""")

    # index.html template
    with open('templates/index.html', 'w') as f:
        f.write("""
{% extends "base.html" %}

{% block content %}
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <h1>Unlocking Tomorrow's Potential with AI</h1>
                    <p class="lead">We build intelligent solutions that transform businesses and enhance human capabilities. Discover the power of Artificial Intelligence with AI Innovate.</p>
                    <a href="#contact" class="btn btn-primary-ai btn-lg">Get Started</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features-section">
        <div class="container">
            <h2 class="text-center mb-5">Our Core AI Capabilities</h2>
            <div class="row text-center">
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-brain"></i>
                        <h3>Advanced Machine Learning</h3>
                        <p>Leverage cutting-edge ML algorithms for predictive analytics, data classification, and pattern recognition.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-robot"></i>
                        <h3>Intelligent Automation</h3>
                        <p>Automate complex tasks and workflows with AI-powered robots and smart systems, boosting efficiency.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-comments"></i>
                        <h3>Natural Language Processing</h3>
                        <p>Understand, interpret, and generate human language for chatbots, sentiment analysis, and content creation.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-eye"></i>
                        <h3>Computer Vision</h3>
                        <p>Enable machines to see and interpret visual information for object detection, facial recognition, and image analysis.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-chart-line"></i>
                        <h3>Data-Driven Insights</h3>
                        <p>Transform raw data into actionable intelligence with AI-powered analytics and visualization tools.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-item">
                        <i class="fas fa-cogs"></i>
                        <h3>Custom AI Development</h3>
                        <p>Tailored AI solutions built from the ground up to meet your unique business challenges and goals.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="container">
            <h2 class="text-center mb-5">Get in Touch</h2>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    {% with messages = get_flashed_messages(with_categories=true) %}
                        {% if messages %}
                            {% for category, message in messages %}
                                <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                                    {{ message }}
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                </div>
                            {% endfor %}
                        {% endif %}
                    {% endwith %}
                    <form action="{{ url_for('contact') }}" method="POST">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="message" class="form-label">Message</label>
                            <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                        </div>
                        <div class="d-grid gap-2">
                            <button type="submit" class="btn btn-primary-ai btn-lg">Send Message</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
{% endblock %}
""")

    # about.html template
    with open('templates/about.html', 'w') as f:
        f.write("""
{% extends "base.html" %}

{% block content %}
    <section class="about-section py-5">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <h1 class="text-center mb-4">About AI Innovate</h1>
                    <p>Welcome to AI Innovate, where we believe in the transformative power of Artificial Intelligence. Founded in 2024, our mission is to empower businesses and individuals with intelligent solutions that drive innovation, efficiency, and growth.</p>
                    <p>Our team comprises passionate AI researchers, data scientists, and software engineers dedicated to pushing the boundaries of what's possible. We specialize in developing custom AI models, integrating machine learning into existing systems, and providing expert consultation to help you navigate the complex world of AI.</p>
                    <p>From predictive analytics and natural language processing to computer vision and intelligent automation, we offer a comprehensive suite of services designed to meet the unique challenges of modern enterprises. We are committed to ethical AI development, ensuring our solutions are not only powerful but also responsible and fair.</p>
                    <p>Join us on our journey to build a smarter future. Let AI Innovate be your partner in harnessing the true potential of Artificial Intelligence.</p>
                    <h3 class="mt-5 mb-3 text-center">Our Vision</h3>
                    <p class="text-center">To be a global leader in AI innovation, creating intelligent systems that redefine industries and improve lives.</p>
                    <h3 class="mt-5 mb-3 text-center">Our Values</h3>
                    <ul class="list-unstyled text-center">
                        <li><i class="fas fa-lightbulb me-2 text-primary-ai"></i> Innovation</li>
                        <li><i class="fas fa-shield-alt me-2 text-primary-ai"></i> Integrity</li>
                        <li><i class="fas fa-users me-2 text-primary-ai"></i> Collaboration</li>
                        <li><i class="fas fa-chart-line me-2 text-primary-ai"></i> Excellence</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
{% endblock %}
""")

    # contact_success.html template
    with open('templates/contact_success.html', 'w') as f:
        f.write("""
{% extends "base.html" %}

{% block content %}
    <section class="contact-success-section py-5">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-lg-8 text-center">
                    <i class="fas fa-check-circle fa-5x text-success mb-4"></i>
                    <h1>Message Sent Successfully!</h1>
                    <p class="lead">Thank you for reaching out to AI Innovate. We have received your message and will get back to you as soon as possible.</p>
                    <p>In the meantime, feel free to explore our <a href="{{ url_for('index') }}" class="text-primary-ai">homepage</a> or learn more <a href="{{ url_for('about') }}" class="text-primary-ai">about us</a>.</p>
                </div>
            </div>
        </div>
    </section>
{% endblock %}
""")

    print("Flask app and templates/static files generated. Run 'python app.py' and navigate to http://127.0.0.1:5000")
    app.run(debug=True) # debug=True for development, set to False in production