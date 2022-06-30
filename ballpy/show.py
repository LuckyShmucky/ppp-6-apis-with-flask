from flask import Blueprint, request
from . import models
show_bp = Blueprint(
    'show',
    __name__,
    url_prefix='/reptiles/<int:id>'
)

@show_bp.route('/')
def show(id):
    reptile = models.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name,
        'conservation_status': reptile.conservation_status,
        'native_habitat': reptile.native_habitat,
        'fun_fact': reptile.fun_fact
    }
    return  reptile_dict