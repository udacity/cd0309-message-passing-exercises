## Usage
### Create a new virtual environment
`python3 -m venv venv`

### Activate the environment
`source venv/bin/activate`

### Start Kafka broker (Kraft mode)
```
docker run -d \
  --name kafka \
  -p 9092:9092 \
  -e KAFKA_PROCESS_ROLES=broker,controller \
  -e KAFKA_NODE_ID=1 \
  -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT \
  -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -e KAFKA_LOG_DIRS=/tmp/kraft-combined-logs \
  apache/kafka:3.7.0
```

### Open interactive shell
`docker exec --workdir /opt/kafka/bin/ -it broker sh`

### Installation
`pip install kafka-python==2.2.10`
### Load Consumer
`python consumer.py`
### Run Producer
`python producer.py`
