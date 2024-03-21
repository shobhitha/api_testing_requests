from uuid import uuid4

import requests
import pytest
import json
from assertpy.assertpy import assert_that, soft_assertions



Base_URI = 'http://0.0.0.0:5000/api/people'
def test_read_all_has_kent():
    people, response = get_all_users()
    #print(response)
    print(json.dumps(people))

    with soft_assertions():

        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        #fnames = [person['fname'] for person in people]

        assert_that(people).extracting('fname').contains('Kento')


def get_all_users():
    response = requests.get(Base_URI)
    people = response.json()
    return people, response


def test_new_person_can_be_added():
    unique_last_name = create_new_unique_user()

    people = requests.get(Base_URI).json()
    new_users = search_users_by_lname(people, unique_last_name)
    with soft_assertions():
        assert_that(new_users).is_not_empty()
        print(new_users)


def search_users_by_lname(people, unique_last_name):
    return [person for person in people if person['lname'] == unique_last_name]


def test_person_can_be_deleted():
    new_user_lname = create_new_unique_user()
    all_users, _ = get_all_users()
    new_user = search_users_by_lname(all_users, new_user_lname)[0]
    #print(new_user)
    person_to_be_deleted = new_user['person_id']
    delete_url = f'{Base_URI}/{person_to_be_deleted}'
    response = requests.delete(delete_url)

    with soft_assertions():

        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        people_after_deletion, _ = get_all_users()

        user_list =[person for person in people_after_deletion if person['person_id'] == person_to_be_deleted]

        assert_that(user_list).is_empty()



def create_new_unique_user():
    unique_last_name = f'User{str(uuid4())}'
    print(unique_last_name)
    payload = json.dumps({'fname': 'New',
                          'lname': unique_last_name})
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'

    }
    response = requests.post(url=Base_URI, data=payload, headers=headers)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.no_content)
    return unique_last_name
