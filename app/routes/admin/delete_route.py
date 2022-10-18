''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Rota: [ delete_route ]
    descrição: 
    
    Testes:
        1. curl localhost:5000/user/delete/1
        2. curl localhost:5000/game/delete/1
        3. curl localhost:5000/giftcard/delete/1
        4. curl localhost:5000/medal/delete/1
        5. curl localhost:5000/screenshot/delete/1
        6. curl localhost:5000/purchase/delete/1
'''
@app.route("/<string:class_type>/delete/<int:id>")
@jwt_required()
def delete_route(class_type:str, id:int):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 

        for type in class_list:    
            if type.__tablename__ == class_type:
                data = db_query_by_id(type,id)
                db_delete(data)
                response = jsonify({"result":"ok", "details": "Sucess"})
                return response
                
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response

''' Rota: [ drop_database_route ]
    descrição: 
    
    Teste:
        1. curl localhost:5000/drop_database
'''
@app.route("/drop_database")
def drop_database_route():
    try:
        db_drop_database()
        response = jsonify({"result":"ok", "details": "Drop database Success! Obs: Reload back-end."})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response