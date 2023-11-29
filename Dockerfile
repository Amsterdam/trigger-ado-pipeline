# Container image that runs your code
FROM python:3.10-bookworm

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY trigger.py /trigger.py
RUN python3 -m pip install requests

# Code file to execute when the docker container starts up
ENTRYPOINT ["python3", "/trigger.py"]
