# assault

A simple CLI load testing tool.

## Installation

Install using `pip`:

```
$ pip install assault
```

## Usage

The simplest usage of `assault` requires only a URL to test against and 500 requests synchronously (one at a time). This is what it would look like:

```
$ assault https://example.com
.... Done!
--- Results ---
Successful requests     500
Slowest                 0.010s
Fastest                 0.001s
Average                 0.003s
Total time              0.620s
Requests Per Minute     48360
Requests Per Second     806
```

If we want to add concurrency, we'll use the `-c` option, and we can use the `-r` option to specify how many requests that we'd like to make:

```
$ assault -r 3000 -c 10 https://example.com
.... Done!
--- Results ---
Successful requests     3000
Slowest                 0.010s
Fastest                 0.001s
Average                 0.003s
Total time              2.400s
Requests Per Minute     90000
Requests Per Second     1250
```

If you'd like to see these results in JSON format, you can use the `-j` option with a path to a JSON file:

```
$ assault -r 3000 -c 10 -j output.json https://example.com
.... Done!
```

## Development

For working on `assult`, you'll need to have Python >= 3.7 (because we'll use `asyncio`) and [`pipenv`][1] installed. With those installed, run the following command to create a virtualenv for the project and fetch the dependencies:

```
$ pipenv install --dev
...
```

Next, activate the virtualenv and get to work:

```
$ pipenv shell
...
(assault) $
```

[1]: https://docs.pipenv.org/en/latest/
With our documentation in place, we at least have something to come back to if we lose track of what we should be working towards.

The setup.py
Some of the other files that we'll want to have before we dig into the code are the setup.py and the .gitignore. These files can be written by hand, but there are some pretty great starting points out there.

For the setup.py, we can use the setup.py for Humans. We'll need to make some modifications, but this file will save us a lot of time.

Let's download the file and start modifying it:

$ curl -O https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py
As for our modifications, we'll want to change things in the # Package meta-data section to be about assault:

setup.py (partial)

# Package meta-data.
NAME = 'assault'
DESCRIPTION = 'A Python based web load testing tool.'
URL = 'https://github.com/example/assault'
EMAIL = 'me@example.com'
AUTHOR = 'Example Person'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1.0'
We'll also want to change any mention of Python 3.6.0 to Python 3.7.0.

The .gitignore
For our .gitignore file, we're going to use the one for Python maintained by GitHub. We can pull it down using the following curl command:

$ curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -o .gitignore
At this point it makes sense to also intialize our project as a Git repository, so let's do that:

$ git init
Using Pipenv for our Virtual Environment
Finally, we're going to use Pipenv to manage our virtual environment and development dependencies. Since we're creating an installable library, we'll also need to add dependencies to the setup.py later on, but Pipenv is still useful for us while we're developing.

Let's initialize our environment using Python 3.7 and install twine as a development dependency as specified by the setup.py to get the python setup.py upload feature:

$ pipenv install --python python3.7 twine --dev
...
Now we're ready to make our first commit and then start developing our tool:

$ git add --all .
$ git commit -m 'Initial commit'
How do you feel about this video?
Flash Cards
Notes
Downloads
