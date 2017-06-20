from kafka import KafkaProducer
from time import sleep
from datetime import datetime

TOPIC_NAME = 'kafkaesque'
BOOTSTRAP_SERVERS = 'localhost:9092'

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    print '[+] Producing messages on topic "%s" to %s' % (TOPIC_NAME, BOOTSTRAP_SERVERS)

    for _ in range(100):
      producer.send(TOPIC_NAME, 'A new message! ' + str(datetime.now().time()) )
      sleep(1)
