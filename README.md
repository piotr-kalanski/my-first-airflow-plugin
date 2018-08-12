# Introduction

Example airflow plugin with custom operator.

# Installation

Copy content of *plugins* directory to [plugins] directory in airflow home directory.

You can also copy example dag from directory [dags] to dags directory in airflow home folder.

# Testing

Check dags:

	airflow list_dags

Run task with custom operator:

	airflow test dag_with_custom_operator task_with_custom_operator 2018-08-11
