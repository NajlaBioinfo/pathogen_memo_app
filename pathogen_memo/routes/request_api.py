"""The Endpoints to manage the PATHOGEN_REQUESTS"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint


REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


PATHOGEN_REQUESTS = {
    "652": {
        'organism': u'Aeromonas schubertii',
        'taxonid': u'652',
        'rank': u'species',
        'aerobe': u'NA',
        'gram': u'Gram-negative',
        'habitat': u'Human, Animal, Vegetal',
        'isolation' : u'fish, meat, milk, vegetables',
        'pathostate': u'Pathogen',
        'timestamp': (datetime.today() - timedelta(1)).timestamp()
    },
    "673": {
        'organism': u'Grimontia hollisae',
        'taxonid': u'673',
        'rank': u'species',
        'aerobe': u'Aerobic',
        'gram': u'Gram-negative',
        'habitat': u'NA',
        'isolation' : u'undercooked/contaminated seafood',
        'pathostate': u'Pathogen',
        'timestamp': (datetime.today() - timedelta(2)).timestamp()
    }
}


@REQUEST_API.route('/getallpathogens', methods=['GET'])
def get_records():
    """Return all pathogen requests
    @return: 200: an array of all known PATHOGEN_REQUESTS as a \
    flask/response object with application/json mimetype.
    """
    return jsonify(PATHOGEN_REQUESTS)


@REQUEST_API.route('/getpathogenbyid/<string:_id>', methods=['GET'])
def get_record_by_id(_id):
    """Get pathogen request details by it's id
    @param _id: the id
    @return: 200: a PATHOGEN_REQUESTS as a flask/response object \
    with application/json mimetype.
    @raise 404: if pathogen request not found
    """
    if _id not in PATHOGEN_REQUESTS:
        abort(404)
    return jsonify(PATHOGEN_REQUESTS[_id])


@REQUEST_API.route('/createpathogen', methods=['POST'])
def create_record():
    """Create a pathogen request record
    @param organism: post : the requesters organism name
    @param taxonid: post : the taxon id of the pathogen requested
    @param rank: post : the rank of the pathogen requested
    @param aerobe: post : the aerobe state  of the pathogen requested
    @param gram: post : the gram state  of the pathogen requested
    @param habitat: post : the habitat of the pathogen requested
    @param isolation: post : the isolation env of the pathogen requested
    @param pathostate: post : the pathogenicity state of the pathogen requested
    @return: 201: a new_uuid as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('organism'):
        abort(400)

    if not data.get('taxonid'):
        abort(400)

    if not data.get('rank'):
        abort(400)

    if not data.get('aerobe'):
        abort(400)

    if not data.get('gram'):
        abort(400)
 
    if not data.get('habitat'):
        abort(400)

    if not data.get('isolation'):
        abort(400)

    if not data.get('pathostate'):
        abort(400)
         
    new_uuid = str(uuid.uuid4())
    pathogen_request = {
        'organism': data['organism'],
        'taxonid': data['taxonid'],
        'rank': data['rank'],
        'aerobe': data['aerobe'],
        'gram': data['gram'],
        'habitat': data['habitat'],
        'isolation' :data['isolation'],
        'pathostate':data['pathostate'],   
        'timestamp': datetime.now().timestamp()
    }
    PATHOGEN_REQUESTS[new_uuid] = pathogen_request
    # HTTP 201 Created
    return jsonify({"id": new_uuid}), 201


@REQUEST_API.route('/updatepathogen/<string:_id>', methods=['PUT'])
def edit_record(_id):
    """Edit a pathogen request record
    @param organism: post : the requesters organism name
    @param taxonid: post : the taxon id of the pathogen requested
    @param rank: post : the rank of the pathogen requested
    @param aerobe: post : the aerobe state  of the pathogen requested
    @param gram: post : the gram state  of the pathogen requested
    @param habitat: post : the habitat of the pathogen requested
    @param isolation: post : the isolation env of the pathogen requested
    @param pathostate: post : the pathogenicity state of the pathogen requested
    @return: 200: a pathogen_request as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if _id not in PATHOGEN_REQUESTS:
        abort(404)

    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('organism'):
        abort(400)

    if not data.get('taxonid'):
        abort(400)

    if not data.get('rank'):
        abort(400)

    if not data.get('aerobe'):
        abort(400)

    if not data.get('gram'):
        abort(400)
 
    if not data.get('habitat'):
        abort(400)

    if not data.get('isolation'):
        abort(400)

    if not data.get('pathostate'):
        abort(400)           
    new_uuid = str(uuid.uuid4())
    pathogen_request = {
        'organism': data['organism'],
        'taxonid': data['taxonid'],
        'rank': data['rank'],
        'aerobe': data['aerobe'],
        'gram': data['gram'],
        'habitat': data['habitat'],
        'isolation' :data['isolation'],
        'pathostate':data['pathostate'],   
        'timestamp': datetime.now().timestamp()
    }

    PATHOGEN_REQUESTS[_id] = pathogen_request
    return jsonify(PATHOGEN_REQUESTS[_id]), 200


@REQUEST_API.route('/deletepathogen/<string:_id>', methods=['DELETE'])
def delete_record(_id):
    """Delete a pathogen request record
    @param id: the id
    @return: 204: an empty payload.
    @raise 404: if pathogen request not found
    """
    if _id not in PATHOGEN_REQUESTS:
        abort(404)

    del PATHOGEN_REQUESTS[_id]

    return '', 204