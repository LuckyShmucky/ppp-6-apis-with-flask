
from flask import (Blueprint, jsonify, request, make_response)
from . import models
reptile_bp = Blueprint('reptiles', __name__, url_prefix='/reptiles')

@reptile_bp.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']
        new_reptile = models.Reptile( common_name=common_name,scientific_name=scientific_name, 
        conservation_status=conservation_status,native_habitat=native_habitat,fun_fact=fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return {
             'common_name': new_reptile.common_name,
        'scientific_name': new_reptile.scientific_name,
        'conservation_status': new_reptile.conservation_status,
        'native_habitat': new_reptile.native_habitat,
        'fun_fact': new_reptile.fun_fact
        }
    results = models.Reptile.query.all()
    res = {
        'list':[]
    }
    for result in results:
        new_obj = {
        'common_name': result.common_name,
        'scientific_name': result.scientific_name,
        'conservation_status': result.conservation_status,
        'native_habitat': result.native_habitat,
        'fun_fact': result.fun_fact
        }
        res['list'].append(new_obj)

    
    return res
        # return jsonify(result_dict)
  
            
            
