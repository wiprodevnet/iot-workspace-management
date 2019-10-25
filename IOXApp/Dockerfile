FROM alpine:3.5
RUN apk add --update \
 python3
RUN pip3 install requests
RUN pip3 install flask
EXPOSE 8000
COPY main.py /main.py
CMD python3 /main.py
