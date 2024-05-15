import yaml
from scripts.plot import plot_map

def open_config():
    """Open config files.

    Returns
    -------
    dict
        A dictionary of config settings.
    """
    config = yaml.safe_load("config.yaml").read_text(encoding="utf8")

    return config

if __name__ == '__main__':
    config = open_config()
    plot_map(config)

    