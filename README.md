# Web Application

This project is a full-stack web application with a backend in Python and a frontend in React and Node.js. It allows users to input information through the frontend, which is then saved, searched, updated, and deleted via the backend.

## Features

- **Input Information:** Users can input their information through the frontend web interface.
- **Save Data:** Information is saved to the backend.
- **Search:** Users can search for specific information.
- **Update:** Users can update existing information.
- **Delete:** Users can delete information.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Node.js
- npm

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Install the necessary Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the backend server:
    ```bash
    python main.py
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install the necessary Node.js dependencies:
    ```bash
    npm install
    ```

3. Start the frontend development server:
    ```bash
    npm run dev
    ```

### Access the Application

Once both the backend and frontend servers are running, open your browser and navigate to `http://localhost:3000` to access the application.

## Environment Variables

Ensure to configure any required environment variables. Refer to the `.env.example` files in both the backend and frontend directories for guidance.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
