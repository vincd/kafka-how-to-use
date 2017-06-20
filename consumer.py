from kafka import KafkaConsumer

TOPIC_NAME = 'kafkaesque'
BOOTSTRAP_SERVERS = 'localhost:9092'

if __name__ == '__main__':
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BOOTSTRAP_SERVERS)
    print '[+] Consuming topic "%s" from %s' % (TOPIC_NAME, BOOTSTRAP_SERVERS)

    for msg in consumer:
        print msg
