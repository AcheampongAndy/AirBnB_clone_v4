#!/usr/bin/python3
"""States API routes"""
from models import storage, storage_t
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.state import State


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def show_states():
    """Shows all states in storage
           Returns:
               A list of JSON dictionaries of all states in a
               200 response body
    """
    states = list(storage.all('State').values())
    states_list = []
    for state in states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def show_state(state_id):
    """Shows a specific state based on id from storage
           Parameters:
               state_id [str]: the id of the state to display

           Returns:
               A JSON dictionary of the state in a 200 response
               A 404 response if the id does not match
    """
    all_states = storage.all(State).values()
    if state_id:
        res = list(filter(lambda x: x.id == state_id, all_states))
        if res:
            return jsonify(res[0].to_dict())
        raise NotFound()
    all_states = list(map(lambda x: x.to_dict(), all_states))
    return jsonify(all_states)


@app_views.route(
    '/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a specific state based on id from storage
           Parameters:
               state_id [str]: the id of the state to delete

           Returns:
               A JSON empty dictionary in a 200 response
               A 404 response if the id does not match
    """
    all_states = storage.all(State).values()
    res = list(filter(lambda x: x.id == state_id, all_states))
    if res:
        storage.delete(res[0])
        storage.save()
        return jsonify({}), 200
    raise NotFound()


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a state object
           Returns:
               A JSON dictionary of the new state in a 200 response
               A 400 response if not a valid JSON or if missing parameters
    """
    data = request.get_json()
    if type(data) is not dict:
        raise BadRequest(description='Not a JSON')
    if 'name' not in data:
        raise BadRequest(description='Missing name')
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates an existing state object based on id
           Parameters:
               state_id [str]: the id of the state to update

           Returns:
               A JSON dictionary of the udpated state in a 200 response
               A 400 response if not a valid JSON
               A 404 response if the id does not match
    """
    xkeys = ('id', 'created_at', 'updated_at')
    all_states = storage.all(State).values()
    res = list(filter(lambda x: x.id == state_id, all_states))
    if res:
        data = request.get_json()
        if type(data) is not dict:
            raise BadRequest(description='Not a JSON')
        old_state = res[0]
        for key, value in data.items():
            if key not in xkeys:
                setattr(old_state, key, value)
        old_state.save()
        return jsonify(old_state.to_dict()), 200
    raise NotFound()
