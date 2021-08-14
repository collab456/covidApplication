"""#bookfrom typing import Collection
import pymongo
from pymongo import MongoClient
#from pymongo import collation
#from pymongo import collection

import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']


cluster = MongoClient('mongodb+srv://suraj:Suraj#$s1@cluster0.hiorx.mongodb.net/bookings?retryWrites=true&w=majority')
#mongodb+srv://suraj:<password>@cluster0.hiorx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

db = cluster["covidHelp"]
books = db["bookings"]


post =[ {"Hospital":"H1", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H1", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H1", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H1", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H1", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H2", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H2", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H2", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H2", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H2", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H3", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H3", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H3", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H3", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H3", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H4", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H4", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H4", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H4", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H4", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H5", "Bed_no":6, "cBed_no":6,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":1, "cBed_no":1,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":2, "cBed_no":2,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":3, "cBed_no":3,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":4, "cBed_no":4,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":5, "cBed_no":5,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":6, "cBed_no":6,"nTaken":False, "cTaken":False},
        {"Hospital":"H6", "Bed_no":7, "cBed_no":7,"nTaken":False, "cTaken":False}
]

#books.insert_many(post)
#print(books.find())
#books.delete_many({})
#print(books.find_one({"Hospital":"4"}))"""