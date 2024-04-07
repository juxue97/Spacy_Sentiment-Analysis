# Use the Python 3.9 base image
FROM python:3.10

# Copy files into the desired directory
COPY . /code

# Set the working directory inside the container
WORKDIR /code

# Download the dependencies
RUN pip install -r requirements.txt

# Install the SpaCy model 'en_core_web_md'
RUN python -m spacy download en_core_web_md

# Expose the port
EXPOSE $PORT

# Start the application using Gunicorn
CMD uvicorn --workers=4 --bind 0.0.0.0:$PORT main:app