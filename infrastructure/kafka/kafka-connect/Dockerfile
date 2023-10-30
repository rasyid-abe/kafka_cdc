FROM confluentinc/cp-kafka-connect:6.2.0

USER root

RUN echo "===> Creating Kafka Connects logs dir ..." 
RUN mkdir -p /var/log/kafka-connect-logs
RUN chmod -R ag+w /var/log/kafka-connect-logs

COPY kafka-connect-log4j.properties /etc/confluent/docker/log4j.properties.template

COPY connect.sh /home/appuser/connect.sh

CMD ["bash", "/home/appuser/connect.sh"]