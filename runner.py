import subprocess
import yaml


def main():
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    print(config['env'])
    if 'env' not in config.keys():
        raise Exception('config.yml need to setup env')

    borg_repo = config['env'].get('borg_repo', 'default')

    process = subprocess.Popen(['ls', '-l'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stderr.decode('utf-8'))
    print(stdout.decode('utf-8'))
    print(borg_repo)


if __name__ == '__main__':
    main()
