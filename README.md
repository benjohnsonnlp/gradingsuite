# gradingsuite

## Install/deploy

1. `pip install -r requirements.txt`
2. `cd gradingsuite`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`

## Administration

1. Log in to the admin ui (at http://whereveriam.com/admin)
2. Create an assignment
    1. Give it a name for users
    2. Add a path to where all the student submission folders are
    3. Take note of its id
3. To give the new assignment a rubric from a json file, run `python manage.py rubricfromfile [path_to_json] [assignment_id]`
4. [prereg:  give an assignment a rubric] To populate submissions for an assignment, select it in the admin tool and click the dropdown above and select populate submissions. 
