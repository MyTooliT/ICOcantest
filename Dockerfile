FROM python:3.11

# Install required tools
RUN apt-get update && \
    apt-get install -y python3-venv

# Activate virtual environment
# Source: https://pythonspeed.com/articles/activate-virtualenv-dockerfile
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin":"$PATH"

# Install ICOc
RUN pip3 install icoc==1.7.0

COPY cantest /cantest

ENTRYPOINT ["bash"]
