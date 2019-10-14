import click


@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output JSON file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    print(f"Requests: {requests}")
    print(f"Concurrency {concurrency}")
    print("JSON File: {}".format(json_file))
    print("URL: {}".format(url))
    pass


if __name__ == "__main__":
    cli()