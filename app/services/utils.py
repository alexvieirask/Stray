from sqlalchemy import delete
from services.config import *

'''  Funções relacionadas á database '''

def db_query_all(schema:object) -> list:
    ''' Retorna uma lista com todos 
    os objetos de um determinado schema.
    '''
    return schema.query.all()

def db_query_by_id(schema:object,id:int) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o schema e id. 
    '''
    return schema.query.get(id)

def db_query_by_username(schema, username:str) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o username. 
    '''
    return schema.query.filter_by(username = username).first()

def db_query_by_email(schema, email:str) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o username. 
    '''
    return schema.query.filter_by(email = email).first()

def db_drop_database() -> None:
    ''' Destrói todas as tabelas.'''
    db.drop_all()

def db_add_many_objects(list:list):
    ''' Adiciona diversos itens na database através de uma lista '''
    for item in list:
        db.session.add(item)
    db.session.commit()

def db_delete_many_objects(list:list):
    ''' Remove diversos itens da database através de uma lista '''
    for item in list:
        db.session.delete(item)
    db.session.commit()
