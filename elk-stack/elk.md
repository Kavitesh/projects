# Introduction to ELK Stack

## What is ELK Stack?
ELK Stack is a powerful collection of three open-source tools used for log management and analysis:

1. **Elasticsearch** - A search and analytics engine that stores and indexes data.
2. **Logstash** - A data processing pipeline that ingests and transforms logs before sending them to Elasticsearch.
3. **Kibana** - A visualization tool that helps users explore and analyze the data stored in Elasticsearch.

The ELK Stack is widely used for log monitoring, real-time data analysis, and centralized logging solutions.

---

## Setting Up a Simple ELK "Hello World" Example

### Prerequisites
Ensure you have Docker installed, as we'll use Docker Compose to set up ELK quickly.

### Step 1: Create a Docker Compose File
Create a `docker-compose.yml` file with the following content:

```yaml
dversion: '3.7'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.0
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"

  logstash:
    image: docker.elastic.co/logstash/logstash:7.17.0
    container_name: logstash
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro
    ports:
      - "5044:5044"
      - "9600:9600"

  kibana:
    image: docker.elastic.co/kibana/kibana:7.17.0
    container_name: kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    ports:
      - "5601:5601"
```

### Step 2: Create Logstash Configuration File
Create a file named `logstash.conf` with the following content:

```plaintext
input {
  stdin {}
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
  }
  stdout {
    codec => rubydebug
  }
}
```

### Step 3: Start ELK Stack
Run the following command in the directory where the `docker-compose.yml` file is located:

```sh
docker-compose up -d
```

### Step 4: Send "Hello World" to Logstash
Once the containers are running, execute the following command to send a message to Logstash:

```sh
docker exec -it logstash bin/logstash -e 'input { stdin {} } output { stdout {} }'
```

Then type:

```sh
Hello World
```

Press **Enter**, and you should see the log appear in the terminal and be indexed in Elasticsearch.

### Step 5: View in Kibana
1. Open Kibana at `http://localhost:5601`
2. Navigate to **Discover** and select the `logstash-*` index pattern.
3. You should see the "Hello World" message indexed in Elasticsearch.

---

## Conclusion
This simple setup demonstrates how the ELK Stack can be used to process and visualize logs. It is a foundational step towards building more complex log analysis and monitoring solutions.

