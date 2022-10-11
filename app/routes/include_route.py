''' Config import '''
from services.config import *

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard

'''Route tests

1. User

    Windows: 
    curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/user/include

    curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Emanoela Rodrigues Erthal\",\"username\":\"manu_erthal\",\"email\":\"manu@gmail.com\",\"password\":\"manu\"}" http://localhost:5000/user/include

    Linux:
    curl -H \Content-Type: application/json\ -X POST --d "{"name":"Alex Vieira Dias","username":"alexvieirasdias","email":"alexvieirasdias@gmail.com","password":"teste"}" http://localhost:5000/user/include

    curl -H \Content-Type: application/json\ -X POST --d "{"name":"Emanoela Rodrigues Erthal","username":"manu_ertha","email":"manu@gmail.com","password":"manu"}" http://localhost:5000/user/include

2. Game

    Windows: 
    curl -H \Content-Type:application/json\ -X POST --data "{\"title\":\"The test\",\"description\":\"this game...\",\"categorie\":\"aventura\",\"price\":\"2\",\"required_age\":\"0\",\"launch_date\":\"24/01/2005\",\"developer\":\"The Tester\"}" http://localhost:5000/game/include

    Linux: 
    curl -H \Content-Type: application/json\ -X POST --d "{"title":"The test","description":"this game...","categorie":"aventura","price":"2","required_age":"0","launch_date":"24/01/2005","developer":"The Tester"}" http://localhost:5000/user/include

'''
@app.route("/<string:class_type>/include", methods = ['POST'])
def include_route(class_type):
    try:
        if request.method == "POST":
            class_type = class_type.title()
            class_list = [ User, Game, GiftCard ] 
            datas = request.get_json(force=True)


            for type in class_list:    
                if type.__tablename__ == class_type:
                    new_data = type(**datas)
                    db.session.add(new_data)
                    db.session.commit()
                    
                    response = jsonify({"result":"ok", "details": 'Success'})
                    return response
        
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})

    return response