
# BlogForge

BlogForge is a powerful and modular blog application built using Django and Django REST Framework (DRF). This project showcases the evolution of coding practices from Function-Based Views (FBVs) to Class-Based Views (CBVs) and finally to APIViews, with a focus on scalability, maintainability, and RESTful API development.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-3.2%2B-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.12%2B-red)
![Docker](https://img.shields.io/badge/Docker-19.03%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12%2B-blue)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)

## Features

- **Function-Based Views (FBVs):** Demonstrates straightforward implementation for simple use cases.
- **Class-Based Views (CBVs):** Implements object-oriented principles for better code reuse and maintainability.
- **RESTful API with APIViews:** Builds a robust API for interacting with blog functionalities.
- **Docker Support:** Provides consistent environments for development and deployment using Docker and Docker Compose.
- **Adherence to Coding Standards:** Ensures clean and maintainable code with Flake8.
- **Modular Design:** Organized code structure to facilitate scalability and ease of maintenance.

## Project Evolution

This repository highlights the progression in coding methodologies:

1. **Function-Based Views (FBVs):** Initial approach for handling HTTP requests in a simple and direct manner.
2. **Class-Based Views (CBVs):** Transition to leveraging Django's class hierarchy for improved maintainability.
3. **APIViews:** Integration with Django REST Framework to build a scalable and feature-rich API.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hesamhme/BlogForge.git
   cd BlogForge
   ```

2. Build and run the application using Docker:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Web app: `http://localhost:8000`
   - API endpoints: `http://localhost:8000/api/v1/`

## Directory Structure

```
core/
├── blog/
│   ├── views.py         # Contains FBVs and CBVs
│   ├── api/v1/views.py  # Contains APIViews
├── accounts/
│   ├── api/v1/views.py  # User authentication and management views
├── settings.py          # Django settings for the project
Dockerfile               # Docker configuration
docker-compose.yml       # Docker Compose configuration
requirements.txt         # Python dependencies
```

## API Documentation

The API supports the following endpoints:

- **GET /api/v1/posts/**: Retrieve a list of blog posts.
- **POST /api/v1/posts/**: Create a new blog post.
- **GET /api/v1/posts/<id>/**: Retrieve details of a specific post.
- **PUT /api/v1/posts/<id>/**: Update a specific post.
- **DELETE /api/v1/posts/<id>/**: Delete a specific post.

## Future Enhancements

- Implement token-based authentication for secure API access.
- Develop a frontend using modern frameworks like React or Vue.js.
- Add unit and integration tests to ensure code reliability.
- Automate testing and deployment pipelines using CI/CD tools.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the [MIT License](LICENSE).

---

Explore the project and feel free to suggest or contribute to its development!
