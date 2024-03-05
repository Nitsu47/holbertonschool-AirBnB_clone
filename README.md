<div align="center">

![AirBnB_Clone](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/assets/135637506/f1f3b282-0acb-4f0a-ba79-5f1678859dbf)
  
<h1> AirBnB Clone </h1>


════════════════════════════════════════ 

This repository contains the AirBnB Clone project for Holberton School as a pair programming group.


Contains the initial stage of a student project to build a clone of the AirBnB website. 


</div>

<div align="center">

════════════════════════════════════════ 

</div>

<br>

## Table of contents
* [About](#about)
* [Resources](#resources)
* [Files](#files)
* [Usage](#usage)
* [Examples](#examples)
* [Authors](#authors)

<h2>About</h2>
In this project we are aiming to create a clone of AirBnB web site, part by part.

This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

All necessary classes are contempled for the future improve of the project.

The project counts with a file storage and tests for all models.

<h2>Resources</h2>
  
- [Python packages](https://intranet.hbtn.io/concepts/66)
- [AirBnB clone](https://intranet.hbtn.io/concepts/74)
- [HBNB project overview](https://youtu.be/E12Xc3H2xqo)
- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
</details>

<h2>Files</h2>

| Poject Files | Description |
| ----- | ------ |
|[README.md](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/README.md) | Code for this incredible readme! |
|[AUTHORS](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/AUTHORS.txt) | Project authors |
|[/tests](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/tree/master/tests) | All tests for modules and engine |
|[/models](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/tree/master/models) | All class models used |
|[console.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/console.py) | Command interpreter to manage project classes, allows to create, show, list, destroy and update classes |

| Models Files | Description |
| ----- | ------ |
|[/models/base_model.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
|[/models/user.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/user.py) | User subclass|
[/models/place.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/place.py) | Place subclass|
[/models/city.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/city.py) | City subclass|
[/models/amenity.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/amenity.py) | Amenity subclass |
[/models/state.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/state.py) | State subclass |
[/models/review.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/review.py) | Review |
[/models/engine/file_storage.py](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py) | serializes instances to a JSON file |

| Test Files | Description |
| ----- | ------ |
|[/tests/test_models/test_base_model](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_base_model.py)| Test for BaseModel class |
|[/tests/test_models/test_amenity](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_amenity.py)| Test for Amenity subclass |
|[/tests/test_models/test_city](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_city.py)| Test for City subclass |
|[/tests/test_models/test_place](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_place.py)| Test for Place subclass |
|[/tests/test_models/test_review](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_review.py)| Test for Review subclass |
|[/tests/test_models/test_state](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/tests/test_models/test_state.py)| Test for State subclass |

</details>

<h2>Usage</h2>
<center> <h2>General Use</h2> </center>

1. First clone this repository "https://github.com/Nitsu47/holbertonschool-AirBnB_clone.git".

3. Once the repository is cloned locate the "console.py" file and run it:
```
/AirBnB_clone$ ./console.py
```
4. Once the command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.
##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

</details>

<h2>Examples</h2>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
</details>
<div align="center">


## Authors
  
&ensp;[<img src="https://img.shields.io/badge/Nitsu47-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Nitsu47)[<img src="https://img.shields.io/badge/Baguvix-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Baguvix)
<br>
════════════════════════════════════════
<br>

Last updated: March 5, 2024

</div>
