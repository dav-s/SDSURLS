from sqlalchemy import Column, String
from sqlalchemy.orm import clear_mappers, mapper
from SDSURLS import Base


def gen_subdomain_table(subdomain):
    return type(subdomain, (Base,),
                {"__tablename__": subdomain,
                 "hash": Column(String(10), primary_key=True),
                 "link": Column(String(512))})
