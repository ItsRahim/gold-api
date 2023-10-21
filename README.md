
# Gold Price Web Scraper

Python application equipped with custom API endpoints. This application serves as a versatile web scraper, enabling users to extract gold price information from various websites. The scraped data is seamlessly transmitted to Apache Kafka, where it can be efficiently processed by a Java Spring Boot application, unlocking a range of possibilities for data analysis and utilisation and portfolio tracking


## Authors

- [Rahim Ahmed](https://www.github.com/ItsRahim)


## Installation

Clone the project & Install Python

```bash
  git clone https://github.com/ItsRahim/gold-price-api.git
```

Install pipenv
```bash
pip install pipenv
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pipenv install
```

## Feedback, Features & Support

If you have any feedback or feature requests, email me at rahim1605@gmail.com

For any issues, please create an issue in the repository


## FAQ

#### How do I solve ```ImportError: No module named six ```

Go into python-kafka's codec.py file and comment ```from kafka.vendor.six.moves import range ```

#### Question 2

Answer 2


## License

[MIT](https://choosealicense.com/licenses/mit/)

