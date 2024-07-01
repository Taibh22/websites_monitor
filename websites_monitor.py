import requests
import time
import configparser
import logging

# Setup logging
logging.basicConfig(filename='websites_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    settings = {
        'checking_period': int(config['settings']['checking_period'])
    }

    urls = {}
    for key, value in config.items('urls'):
        url, expected_content = value.split(',', 1)
        urls[url] = expected_content.strip()

    return settings, urls

def check_website(url, expected_content):
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time

        if response.status_code == 200:
            if expected_content in response.text:
                logging.info(f"{url} is up. Content matched. Response time: {response_time:.2f} seconds.")
            else:
                logging.warning(f"{url} is up. Content did not match. Response time: {response_time:.2f} seconds.")
        else:
            logging.error(f"{url} is up. Unexpected status code: {response.status_code}. Response time: {response_time:.2f} seconds.")
    
    except requests.exceptions.RequestException as e:
        logging.error(f"{url} is down. Error: {e}")

def main():
    config_file = 'config.ini'
    settings, urls = read_config(config_file)

    checking_period = settings['checking_period']

    while True:
        logging.info("Starting new round of checks...")
        for url, expected_content in urls.items():
            check_website(url, expected_content)
        logging.info(f"Sleeping for {checking_period} seconds before next check.")
        time.sleep(checking_period)

if __name__ == '__main__':
    main()
