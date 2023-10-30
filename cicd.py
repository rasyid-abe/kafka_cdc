import argparse
import logging
import json
import os
import requests
import difflib

logging.basicConfig(
    format='%(asctime)-15s: %(name)s - %(levelname)s: %(message)s')
LOGGER = logging.getLogger('connectors-deploy')
LOGGER.setLevel(logging.INFO)

API_ROOT_TEMPLATE = {
    "dev": os.environ['HOST_DEV'],
    "staging": os.environ['HOST_STAGING'],
    "prod": os.environ['HOST_PROD']
}

CONNECTORS_CONFIG_ROOT_TEMPLATE = f"./configs/cdc"
CONNECTOR_EXT = ".json"


def main():
    args = parse_args()

    LOGGER.info("Starting...")

    raw_config_filenames = find_files(get_connectors_config_root(args))

    LOGGER.info(
        f"Found {len(raw_config_filenames)} connectors: " \
        f"{raw_config_filenames}")

    processed_configs = process_config_files(raw_config_filenames)

    update_or_create_connectors(processed_configs, args)

    LOGGER.info("Completed")


def find_files(path_to_use):
    config_filenames = []

    for path, dirs, files in os.walk(path_to_use):
        for file in files:
            if file.endswith(CONNECTOR_EXT):
                config_filenames.append(os.path.abspath(path + "/" + file))

    return config_filenames


def process_config_files(raw_config_filenames):
    configs = []

    for filename in raw_config_filenames:
        with open(filename) as f:
            configs.append(f.read())

    return configs


def get_connectors_config_root(args):
    return f"{CONNECTORS_CONFIG_ROOT_TEMPLATE}/{args.env}"


def get_api_root(args):
    return API_ROOT_TEMPLATE[args.env]


def update_or_create_connectors(configs, args):
    api_root = get_api_root(args)
    headers = {"Accept": "application/json",
               "Content-Type": "application/json"}
    
    url = f"{api_root}/connectors"
    current_configs = requests.get(url).json()

    for config in configs:
        config_json = json.loads(config)

        if args.dry_run:
            if config_json['name'] not in current_configs:
                LOGGER.info(f"{config_json['name']} is a new connector")
            else:
                LOGGER.info(f"Showing diff {config_json['name']}")
                LOGGER.info(f"+++ is added in new config, " \
                    "--- is removed in new config")
                current_configs.remove(config_json['name'])
                url = f"{api_root}/connectors/{config_json['name']}/config"
                response = json.dumps(
                    requests.get(url).json(), 
                    sort_keys=True, 
                    indent=4)
                new = json.dumps(config_json, 
                    sort_keys=True, 
                    indent=4)
                for text in difflib.unified_diff(response.split("\n"), new.split("\n")):
                    if text[:3] not in ('+++', '---', '@@ '):
                        print(text)
        else:
            # Update or Create a connector
            LOGGER.info(f"Adding/updating {config_json['name']} connector")
            url = f"{api_root}/connectors/{config_json['name']}/config/"
            response = requests.put(
                url,
                data=config,
                headers=headers)

            LOGGER.info(f"Response: {response.status_code}")

            if 400 <= response.status_code < 600:
                LOGGER.error(f"{response.json()}")       

            response.raise_for_status()

    if args.dry_run:
        LOGGER.warning(
            f"These connectors not having json file config yet: {current_configs}")


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--env',
        required=True,
        choices=['dev', 'staging', 'prod'],
        help='Kafka Connect environment')

    parser.add_argument(
        '--dry-run',
        dest='dry_run',
        default=False,
        action='store_true',
        help='Dry-run mode')

    return parser.parse_args()


if __name__ == "__main__":
    main()
