# Docker Date API

A simple Docker application that serves the current time with even/odd second indication via HTTP.

## Description

This project creates a Docker container that responds to HTTP requests on the `/date` endpoint, returning the current time in HH:MM:SS format along with whether the seconds value is EVEN or ODD.

## Technologies Used

- **Python 3.9** - Programming language
- **Flask** - Web framework
- **Docker** - Containerization

## API Endpoint

- `GET /date` - Returns current time with even/odd indication

### Example Response
```
21:59:25 ODD
21:59:26 EVEN
```

## How to Build and Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/docker-date-app.git
   cd docker-date-app
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t my-date-app .
   ```

3. **Run the container:**
   ```bash
   docker run -d -p 8080:80 --name date-container my-date-app
   ```

4. **Test the application:**
   ```bash
   curl http://localhost:8080/date
   ```

## Project Structure

```
├── app.py              # Flask application
├── Dockerfile          # Docker build instructions
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Logic Implementation

The application uses Python's `datetime` module to get the current time and the modulo operator (`%`) to determine if seconds are even or odd:

- Even: `seconds % 2 == 0`
- Odd: `seconds % 2 == 1`

## Clean Up

To stop and remove the container:
```bash
docker stop date-container
docker rm date-container
docker rmi my-date-app
```
