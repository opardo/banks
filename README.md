# banks

## Author

Carlos Omar Pardo Gomez (cop2108@columbia.edu)

## Overview

Web application made using Django. It optimizes the ROI of the investors, given the interest rate and the minimum and maximum investments for a group of banks.

### User Page

In the upper part, the available investment banks are shown, with their corresponding information.

![Image of info](https://github.com/opardo/banks/blob/master/images/info.png)

Then, the suggestion of each user is presented such that, among all the possible solutions, it is the one that maximizes its ROI.

![Image of info](https://github.com/opardo/banks/blob/master/images/suggestion.png)

### Register Page

Here, banks and investors can be modified.

![Image of info](https://github.com/opardo/banks/blob/master/images/admin_menu.png)

For the banks, interest rate and constraints must be filled.

<img src="https://github.com/opardo/banks/blob/master/images/add_bank.png" width="500">

In the investor section, the administrator saves the amount of money available to each user and chooses which banks to invest in.

<img src="https://github.com/opardo/banks/blob/master/images/add_investor.png" width="500">

Finally, both sections can be modified.

<img src="https://github.com/opardo/banks/blob/master/images/change_investor.png" width="500">

## Requirements

python: 2.7.14, django 1.8.0, MySQL-python: 1.2.5, cvxopt: 1.1.9

## Running the project

The following instructions are intended to be carried out on the command line.

First, you must open a MySQL session to create the project database and grant the user _mocks_ all the privileges on it.

```
mysql> CREATE DATABASE banks;
mysql> CREATE USER 'mocks'@'localhost' IDENTIFIED BY 'mocks';
mysql> GRANT ALL PRIVILEGES ON banks . * TO 'mocks'@'localhost';
```

Then, the models defined by the project must be translated into different tables and variables within the newly created database, with the following command:

```
python manage.py migrate
```

Next, one superuser must be created, which is going to be used in the Log In window.

```
python manage.py createsuperuser --username=superusername
```

Finally, you can run the project with the command

```
python manage.py runserver
```

Some lines will appear in the shell. There, the project's direction will appear.

<img src="https://github.com/opardo/banks/blob/master/images/runserver.png" width="500">

You have to type such direction, adding _/users/_, and then you will be ready to start playing with the application.
