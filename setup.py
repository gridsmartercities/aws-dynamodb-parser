from setuptools import setup, find_packages

LONG_DESCRIPTION = open("README.md").read()

setup(name="aws-dynamodb-parser",
      version="0.1.2",
      description="AWS DynamoDB utility for parsing DynamoDB responses",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/gridsmartercities/aws-dynamodb-parser",
      author="Grid Smarter Cities",
      author_email="open-source@gridsmartercities.com",
      license="MIT",
      classifiers=[
          "Intended Audience :: Developers",
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Natural Language :: English"
      ],
      keywords="aws lambda decorator",
      packages=find_packages(exclude=("tests")),
      zip_safe=False)
