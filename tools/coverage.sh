#!/bin/bash

coverage run --branch --source='aws_dynamodb_parser' -m unittest tests/test_*.py
coverage report -m --fail-under=100 --omit=*/__init__.py,tests/*,setup.py,env/*
