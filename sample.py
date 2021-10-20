import requests


def send_request():
    # Request (8)
    # GET https://github.com/trending/python

    try:
        response = requests.get(
            url="https://github.com/trending/python",
            params={
                "since": "weekly",
            },
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8, \
                    application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
            },
        )
        print(
            "Response HTTP Status Code: {status_code}".format(
                status_code=response.status_code
            )
        )
        print("Response HTTP Response Body: {content}".format(content=response.content))
    except requests.exceptions.RequestException:
        print("HTTP Request failed")


if __name__ == "__main__":
    send_request()
