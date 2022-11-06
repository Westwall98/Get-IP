FROM ethan1st/python:alpine
WORKDIR /dockerfile
COPY /dockerfile/files/ /getip
EXPOSE 8000/tcp
CMD ["python", "/getip/getip.py"]
