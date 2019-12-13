FROM jrottenberg/ffmpeg
MAINTAINER Bobby Richter <secretrobotron@gmail.com>

RUN apt-get update && apt-get install -y --force-yes python3

ENV HOME /data
WORKDIR /data
VOLUME ["/data"]

RUN mkdir /processor
ADD process.py /processor

ENTRYPOINT ["python3", "/processor/process.py"]
CMD [""]
