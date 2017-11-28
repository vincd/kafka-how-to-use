from kafka import KafkaConsumer

TOPIC_NAME = 'kafkaesque'
BOOTSTRAP_SERVERS = 'localhost:9092'

if __name__ == '__main__':
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ssl_ctx.load_cert_chain(certfile="./cert.pem")
    
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BOOTSTRAP_SERVERS, ssl_context=ssl_ctx)
    print '[+] Consuming topic "%s" from %s' % (TOPIC_NAME, BOOTSTRAP_SERVERS)

    for msg in consumer:
        print msg
