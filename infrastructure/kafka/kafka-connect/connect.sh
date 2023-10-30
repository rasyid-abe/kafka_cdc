#!/bin/bash

echo "Installing Connector"
confluent-hub install --no-prompt debezium/debezium-connector-mysql:1.8.1

echo "Installing JDBC Connector"
confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest

echo "Installing common transform"
confluent-hub install --no-prompt jcustenborder/kafka-connect-transform-common:latest

echo "Installing mongoDB connector"
confluent-hub install --no-prompt debezium/debezium-connector-mongodb:2.0.1

echo "Download JDBC drivers"
cd /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/lib
curl https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.27/mysql-connector-java-8.0.27.jar -o mysql-connector-java-8.0.27.jar

echo "Download Null character handler"
cd /usr/share/java
curl -L https://github.com/cyberjar09/StripUnicodeNullTransform/releases/download/0.0.2/StripUnicodeNullTransform-0.0.2.jar -o StripUnicodeNullTransform-0.0.2.jar

echo "Launching Kafka Connect worker"
/etc/confluent/docker/run &

sleep infinity
