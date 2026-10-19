# SkillConnect — Local Job & Skill Matching Portal for Daily-Wage Workers

A modern, premium, professional web platform designed to connect unskilled and semi-skilled daily-wage workers with nearby job opportunities based on skills, location, availability, and fair wages.

---

## 🌟 Key Features

1. **Design & Brand Identity**:
   - **Primary Dark Navy**: `#062B63`
   - **Primary Green**: `#08A84F`
   - **Secondary Green**: `#16B85A`
   - **Accent Yellow**: `#F5B400`
   - **Light Surface**: `#F7FAFC`
   - **Typography**: Poppins (Modern Rounded Sans-Serif) + Kalam (Handwritten Community Annotation)

2. **Hero Section**:
   - Headline:
     > **Find Work.**  
     > **Find Workers.**  
     > **Build Your Future.**
   - Hero Image Composition: High-resolution realistic photography featuring diverse local Indian tradespeople (construction supervisor with yellow helmet & orange vest, electrician, gardener, plumber, carpenter, painter, mechanic, chef).
   - Handwritten Annotation: *"Local Skills Create Stronger Communities"* with hand-drawn SVG underline and arrow.
   - Dual Large Rounded CTAs: **Find a Job** (Green pill) & **Find a Worker** (Navy outline pill) with subtle lift and arrow hover animations.

3. **Bottom Feature Strip**:
   - **Local Opportunities** (Green Location Pin Icon) — *Jobs and workers near you*
   - **Trusted Profiles** (Blue Shield / Checkmark Icon) — *Verified and reliable*
   - **Quick & Easy** (Yellow Lightning Icon) — *Simple and fast process*
   - **Build Communities** (Purple People Icon) — *Support local employment*

4. **Functional Multi-Page Routing**:
   - `/` or `index.html`: Landing Page
   - `/jobs` or `jobs.html`: Find Jobs & Daily Shifts (with live search, category pills, and Quick Apply modal)
   - `/workers` or `workers.html`: Find & Hire Skilled Local Workers (with verification badges, daily rates, and Hire modal)
   - `/login` or `login.html`: Dual-mode Login (Mobile OTP for Workers & Password/Email for Contractors)
   - `/signup` or `signup.html`: Dual Registration (Worker vs Employer)
   - `/about` or `about.html`: Mission, Problem vs Solution (Labor Chowk vs SkillConnect), Core Values, and Evaluator Specs

---

## 🚀 How to Run

### Option 1: Run with Python Server (Recommended for Clean URLs)
Run the built-in clean-URL Python server:
```bash
python server.py
```
Then open your browser at:
- **Landing Page**: [http://localhost:5000/](http://localhost:5000/)
- **Find Jobs**: [http://localhost:5000/jobs](http://localhost:5000/jobs)
- **Find Workers**: [http://localhost:5000/workers](http://localhost:5000/workers)
- **Login**: [http://localhost:5000/login](http://localhost:5000/login)
- **Sign Up**: [http://localhost:5000/signup](http://localhost:5000/signup)
- **About**: [http://localhost:5000/about](http://localhost:5000/about)

### Option 2: Open Directly in Browser
You can also directly double-click `index.html` or open it with VS Code Live Server / any web browser. All navigation links and modals function out of the box without any external dependencies!

---

## 📁 File Structure
```
Job Project/
├── assets/
│   ├── css/
│   │   └── style.css            # Custom brand variables, typography, animations, handwritten badge
│   ├── js/
│   │   └── main.js              # Mobile menu, modals, filters, animated counters, toast alerts
│   └── images/
│       └── hero-workers.jpg     # Realistic Indian local workers photo composition
├── index.html                   # Landing page
├── jobs.html                    # Job listings & application portal
├── workers.html                 # Worker directory & hiring portal
├── login.html                   # Authentication with OTP & password
├── signup.html                  # Worker / Employer registration
├── about.html                   # Mission, labor chowk transformation, and academic notes
├── server.py                    # Lightweight Python HTTP server with clean routing
└── README.md                    # Project documentation
```
