import re

def is_valid_user(user):
    return re.match(r'^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*$', user) is not None

def is_valid_host(host):
    return re.match(r'^[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+$', host) is not None

def extract_emails(text):
    pattern = r'\b([a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*)@([a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+)\b'
    return re.findall(pattern, text)

def main():
    input_string = input()
    emails = extract_emails(input_string)

    for email in emails:
        user, host = email[0], email[2]
        if is_valid_user(user) and is_valid_host(host):
            print(f'{user}@{host}')

if __name__ == "__main__":
    main()
