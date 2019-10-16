import click

from .http import assault
from .stats import Results
from typing import TextIO
import json
import sys

@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output JSON file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    if json_file:
        try:
            output_file = open(json_file, 'w')
        except:
            print(f"unable to write to {json_file}")
            sys.exit(1)

    total_time, request_dicts = assault(url, requests, concurrency)
    results = Results(total_time, request_dicts)
    display(results, output_file)

def display(results: Results, output_file: TextIO):
    if output_file:
        json.dump(
            {
                "successful_requests": results.successful_requests(),
                "slowest_request": results.slowest(),
                "fastest_request": results.fastest(),
                "total_time": results.total_time,
                "requests_per_minute": results.requests_per_minute(),
                "requests_per_second": results.requests_per_second()

            },
            output_file
        )
        print('.... Done!')
    else:
        print(".... Done!")
        print("--- Results ---")
        print(f"Successful Requests\t{results.successful_requests()}")
        print(f"Slowest            \t{results.slowest()}s")
        print(f"Fastest            \t{results.fastest()}s")
        print(f"Total time         \t{results.total_time}s")
        print(f"Requests Per Minute\t{results.requests_per_minute()}")
        print(f"Requests Per Second\t{results.requests_per_second()}")

if __name__ == "__main__":
    cli()
