# Use the official Python image from the Docker Hub
FROM python:3.9

RUN apt-get update && apt-get install -y libssl3

# pievienoju, jo startējot ir kļūda
RUN 	pip install git+https://github.com/wbond/oscrypto.git && \
	 	pip install 'setuptools>=61.0.0' 'setuptools_scm>=8.0'


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt .


# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
#COPY /app/ .
COPY /app/ ./app/

#copy certs
COPY /test_certs ./app/cert/
COPY /test_trusted_ca ./app/trusted_ca/

# rename file
RUN mv app/app_config/__config_secrets.py app/app_config/config_secrets.py && \
	mv app/metadata_config/metadata_config.json app/metadata_config/metadata_config.json && \
	mv app/metadata_config/openid-configuration.json app/metadata_config/openid-configuration.json

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 5000

# Run the application
#CMD ["flask", "run", "--debug"]

ENTRYPOINT ["sh", "-c", "flask --app app run --debug"]
#
# Usage examples:
# flask --app app run --debug
# flask --app app run --debug --cert=app/certs/certHttps.pem --key=app/certs/key.pem --host=127.0.0.1 --port=4430
#
