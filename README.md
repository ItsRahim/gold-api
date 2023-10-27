
# Gold Price Web Scraper

Python application equipped with custom API endpoints. This application serves as a versatile web scraper, enabling users to extract gold price information from various websites. The scraped data is seamlessly transmitted to Apache Kafka, where it can be efficiently processed by a Java Spring Boot application, unlocking a range of possibilities for data analysis and utilisation and portfolio tracking


## Authors

- [Rahim Ahmed](https://www.github.com/ItsRahim)


## Installation

Install Python

```bash
  https://www.python.org/downloads/
```

Download Kafka
```bash
  https://kafka.apache.org/downloads
```

Clone Repository

```bash
  git clone https://github.com/ItsRahim/gold-price-api.git
```

Install pipenv
```bash
pip install pipenv
```

Go to the project directory

```bash
  cd C:/.../gold-price-api
```

Install dependencies

```bash
  pipenv install
```

## Setup
#### Kafka and Zookeeper

```commandline
# Start Zookeeper
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

# Start Kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties

# Create Kafka Topic
.\bin\windows\kafka-topics.bat --create --topic gold-price-stream --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Start Consumer
.\bin\windows\kafka-console-consumer.bat --topic gold-price-stream --bootstrap-server localhost:9092 --from-beginning
```
<br>

#### Changing Host and Port (Optional)
By default, the API starts on ```localhost:8000```

This can be changed by altering ```app_config.yaml``` found in ```gold-project-api/app/resource/app_config.yaml```

```yaml
app:
  host: your_host_here
  port: your_port_here
```
<br>

#### Changing Topic Name (Optional)
Topic name by default is ```gold-price-stream```

If you wish to change this, you'll need to alter the Kafka commands above ```--topic your_topic_name```  edit the ```app_config.yaml```
```yaml
kafka:
  topic: your_topic_name
```
<br>

### Run Program
Whilst in the project directory
```commandline
pipenv run main.py
```

## Feedback, Features & Support

If you have any feedback or feature requests, email me at rahim1605@gmail.com

For any issues, please create an issue in the repository


## FAQ

#### 1) How do I solve ```ImportError: No module named six ```

Go into python-kafka's codec.py file and comment ```from kafka.vendor.six.moves import range ```


## License

[MIT](https://choosealicense.com/licenses/mit/)

