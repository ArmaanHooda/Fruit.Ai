

# Fruit.AI 🍇🍉🍎

**Fruit.AI** is a mobile-friendly web application designed to help users manage their fruit consumption in a healthy way. It offers a chatbot for fruit recommendations, a translator for regional languages, a FAQ section with CRUD operations, and an about page. The backend provides API support for managing fruit-related FAQs using **FastAPI/Flask** with full CRUD functionality.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Frontend Setup](#frontend-setup)
- [Backend Setup](#backend-setup)
- [API Endpoints](#api-endpoints)
- [Project Screenshots](#project-screenshots)
- [Future Enhancements](#future-enhancements)

## Project Overview

This is a health manager product designed to assist users in maintaining healthy fruit intake. It includes several functionalities like:
- A **chatbot** that displays a list of fruits as cards.
- A **translator** to convert English into a regional language.
- A **FAQ page** with full CRUD operations (Create, Read, Update, Delete) for managing fruit-related questions.
- An **about page** that explains the purpose of the app.

The app is responsive and user-friendly, ensuring a seamless experience on both mobile and desktop platforms.

## Features

- **Login Page**: A dummy login page with a placeholder for user credentials. Successful login redirects to the homepage.
- **Home Page**: Displays four services: Chatbot, Translator, FAQs, and About, each as interactive cards.
- **Chatbot Page**: List of fruits displayed as cards with individual fruit details.
- **Translator Page**: Translate any input text into a regional language.
- **FAQ Page**: Basic CRUD functionality allowing users to create, view, edit, and delete FAQs about fruits.
- **About Page**: Describes the purpose of the Fruit.AI application.
- **API Support**: Backend API developed using **FastAPI/Flask**, providing CRUD operations for FAQs.

## Technologies Used

### Frontend
- **HTML5**
- **CSS3** (for styling and responsiveness)
- **JavaScript** (for client-side functionality)

### Backend
- **FastAPI** or **Flask** (Python framework for handling the API)
- **SQLite** (or any other lightweight database for FAQ storage)


## Getting Started

### Prerequisites
- Ensure you have Python 3.x installed.
- Install Node.js and npm (if not already installed).
  
### Frontend Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ArmaanHooda/Fruit.Ai.git
   cd Fruit.Ai
   ```

2. **Open the `index.html` file in your browser**:
   - You can use any server (e.g., `live-server`) to launch the frontend.
   - Alternatively, open `index.html` directly in a browser.

3. **Run locally** (optional):
   If you are using a simple server for development, you can run the following command (if using Node.js):
   ```bash
   npm live-server
   ```

### Backend Setup

1. **Install Dependencies**:
   If you are using Flask, create a virtual environment and install the dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the Flask/ FastAPI app**:
   ```bash
   flask run  # for Flask
   uvicorn main:app --reload  # for FastAPI
   ```

3. **Access API**:
   The API will be available at:
   - `http://localhost:5000` for Flask
   - `http://localhost:8000` for FastAPI

### API Endpoints

#### Available CRUD Endpoints for FAQs

- **GET /faqs**: Fetch all FAQs.
- **GET /faqs/{id}**: Fetch an individual FAQ by ID.
- **POST /faqs**: Create a new FAQ.
- **PUT /faqs/{id}**: Update an existing FAQ by ID.
- **DELETE /faqs/{id}**: Delete an FAQ by ID.


## Project Screenshots

### Login Page
![Login Page](path-to-image)

### Home Page
![Home Page](path-to-image)

### Chatbot Page
![Chatbot Page](path-to-image)

### FAQ Page (CRUD)
![FAQ Page](path-to-image)

### About Page
![About Page](path-to-image)

## Future Enhancements
- **Authentication**: Implement real user authentication for login functionality.
- **Database Integration**: Replace the local SQLite database with a more robust cloud database solution (e.g., PostgreSQL).
- **More Services**: Extend the chatbot to include more fruit recommendations, interactive services, and AI-powered insights.
- **Improved UI/UX**: Further refine the UI for better aesthetics and usability across all devices.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
