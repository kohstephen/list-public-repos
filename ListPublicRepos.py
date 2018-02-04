import requests
import sys


def get_public_repos(user):
    r = requests.get('https://api.github.com/users/{}/repos'.format(user))
    return (repo['name'] for repo in r.json())


def main():
    if len(sys.argv) != 2:
        raise ValueError('Must provide name of user as command-line argument!')
    user = sys.argv[1]
    repos = get_public_repos(user)
    [print(repo) for repo in repos]


if __name__ == "__main__":
    main()
