# Contributing

To contribute to this project, please either submit an issue describing a bug or proposed change or [open a pull request](https://opensource.com/article/19/7/create-pull-request-github) and we will respond to you as soon as possible.

This project requires Python >=3.7

## Code standards

In order for a pull request to be accepted and merged, Grid Smarter Cities requires that all code pass our standard code standards.

Firstly we require all unit tests to be passing, and that test coverage is 100%. You can test this by running `./tools/coverage.sh`
```
$ ./tools/coverage.sh
.............
----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
Name                           Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------
aws_dynamodb_parser/utils.py      29      0     24      0   100%
```

We require all code to adhere to our linting style as defined in [pylintrc](https://github.com/gridsmartercities/aws-dynamodb-parser/blob/master/pylintrc). We use [prospector](https://pypi.org/project/prospector/) to run linting checks.
```sh
$ prospector
Check Information
=================
         Started: 2020-10-01 17:55:32.697915
        Finished: 2020-10-01 17:55:33.725397
      Time Taken: 1.03 seconds
       Formatter: text
        Profiles: .prospector.yaml, full_pep8, no_doc_warnings, strictness_veryhigh, no_member_warnings
      Strictness: from profile
  Libraries Used:
       Tools Run: dodgy, mccabe, pep8, profile-validator, pyflakes, pylint
  Messages Found: 0
 External Config: pylint: /Users/rob/Documents/code/grid/aws-dynamodb-parser/pylintrc
```

And lastly that [Bandit](https://pypi.org/project/bandit/) security checks pass
```sh
$ ./tools/bandit.sh
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.8.5
Run started:2020-10-01 14:58:17.950255

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 203
	Total lines skipped (#nosec): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
	Total issues (by confidence):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
Files skipped (0):
```

Once the changes are finished and the criteria for merging are met, simply create a pull request with a good title and description and it'll be reviewed as soon as possible

Thanks for contributing!