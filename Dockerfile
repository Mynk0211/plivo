# Use the official Python image from the Docker Hub
FROM python:3.9-slim
RUN apt-get update
RUN apt-get install -y build-essential default-libmysqlclient-dev pkg-config
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/
RUN python  manage.py makemigrations
RUN python manage.py migrate
# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

