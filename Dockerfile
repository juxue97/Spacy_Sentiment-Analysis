# Use the Python 3.9 base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file to the container
COPY ./requirements.txt /code/requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install the SpaCy model 'en_core_web_md'
RUN python -m spacy download en_core_web_md

# Copy the application code to the container
COPY ./app /code/app

# Set the default command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]