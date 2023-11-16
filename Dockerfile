FROM python:3.10.13-bookworm

COPY ./requirements.txt .

# Install required system packages
RUN pip install --no-cache-dir -r requirements.txt

# Install uvicorn
RUN pip install uvicorn

# Copy your application code into the container
COPY . .

# Expose the port that your application will run on
EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]