# Budget App

The Budget App is a web application designed to help users manage their finances by tracking their budget, expenses, and savings goals. It provides a user-friendly interface for setting a budget, adding expenses, and calculating savings contributions based on various parameters.

## Features

- **Set Budget**: Users can set their budget for a specific period.
- **Add Expenses**: Users can add expenses by specifying the title and amount, which helps in tracking where the money is going.
- **View Expenses**: The app lists all added expenses for easy monitoring and management.
- **Calculate Savings Contribution**: Users can calculate their savings contributions based on their savings goal, starting balance, saving time, and interest rate from selected banks or custom rates.

## Technologies Used

- **HTML/CSS**: For structuring and styling the web pages.
- **Bootstrap**: For responsive design and pre-designed components.
- **Flask/Django**: (Assuming from the Python-related `.gitignore` content) For backend logic, handling requests, and rendering templates.
- **Docker**: For containerizing the application and ensuring consistent deployment across different environments.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.x
- Flask or Django (depending on the backend framework used)
- Docker

### Installation

1. Clone the repository
    ```sh
    git clone https://github.com/bravosixgoingdark/fintech-hackathon
    ```

2. Build the Docker image:
    ```sh
    docker build -t budget-app .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 5000:5000 budget-app
    ```

4. Open your web browser and navigate to `http://localhost:5000` to access the Budget App.




