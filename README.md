# My Portfolio - Django Project

## Project Overview
This is a **Django-based Portfolio Web Application** that consists of multiple apps, each serving a different purpose. The main app (`main`) serves as the root of the project, while other apps have specific functionalities such as showcasing portfolio, blogs, hobbies, work, and ventures.

## Features
- **Modular Structure**: 9 Django apps for different functionalities.
- **Static & Media Handling**: Each app has its own templates, CSS, JavaScript, and image directories.
- **URL Routing**: Each app is accessible via a unique URL.
- **Scalable**: Easily extendable for new functionalities.
- **Open Source**: Contributions are welcome!

## Project Structure
```
my_portfolio/
│── main_project/        # Django Project Configuration
│── portfolio/          # Portfolio App
│── personal/           # Personal App
│── blogs/              # Blogs App
│── hobby/              # Hobby App
│── help/               # Help App
│── manage/             # Manage App
│── work/               # Work App
│── venture/            # Venture App
│── main/               # Main App (Root)
│── static/             # Global Static Files
│── media/              # User Uploads
│── templates/          # Shared Templates
│── venv/               # Virtual Environment
│── db.sqlite3          # SQLite Database
│── manage.py           # Django Management Script
```

## Installation & Setup
### Prerequisites
- Python 3.x
- Git
- Virtual Environment (venv)
- Django (installed via pip)

### Steps to Run the Project

#### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/my_portfolio.git
cd my_portfolio
```

#### 2. Set Up Virtual Environment
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

#### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 4. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

#### 5. Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## URL Routing
| App Name    | URL Path            |
|------------|--------------------|
| Main       | `/`                |
| Portfolio  | `/portfolio/`       |
| Personal   | `/personal/`        |
| Blogs      | `/blogs/`           |
| Hobby      | `/hobby/`           |
| Help       | `/help/`            |
| Manage     | `/manage/`          |
| Work       | `/work/`            |
| Venture    | `/venture/`         |

## File Structure in Each App
Each app has the following structure:
```
app_name/
│── templates/
│   └── app_name/
│       └── home.html
│── static/
│   └── app_name/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── script.js
│       ├── images/
│           └── sample.jpg
```

## Contribution Guidelines
We welcome contributions! To contribute:
1. **Fork** the repository.
2. **Create a new branch** (`feature-branch`)
3. **Commit your changes** (`git commit -m "Added new feature"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Open a Pull Request**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any queries, feel free to reach out:
- **Email**: your.email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

---
Happy Coding! 🚀

