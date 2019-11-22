FROM ubuntu
RUN apt-get update && apt-get install -y -q --no-install-recommends build-essential libtiff5-dev libjpeg-turbo8-dev
RUN apt-get install -y -q --no-install-recommends wget

RUN wget --no-check-certificate 'https://sourceforge.net/projects/iipimage/files/IIP%20Server/iipsrv-1.1/iipsrv-1.1.tar.bz2'
RUN tar xvf iipsrv-1.1.tar.bz2
WORKDIR iipsrv-1.1
RUN ./configure
RUN make
WORKDIR /

ENV URI_MAP="iiif=>IIIF"
RUN mkdir /var/log/iipsrv
ENV LOGFILE="/var/log/iipsrv/iipsrv.log"

CMD /iipsrv-1.1/src/iipsrv.fcgi --bind 0.0.0.0:9000
