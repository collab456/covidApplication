from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import MongoClient
#from utils import cluster
# Create your views here.

import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

cluster = MongoClient('mongodb+srv://suraj:Suraj#$s1@cluster0.hiorx.mongodb.net/bookings?retryWrites=true&w=majority')

db = cluster["covidHelp"]
books = db["bookings"]



def search(request):
    val = books.find() 
    condi = request.POST["Patient"]
    code = int(request.POST["pincode"])
    hospital = request.POST["hospital"]
    #print(condi, code, hospital)
    available = []

    if(condi=="Critical"): 
        
        for x in val:
            #print(x["Hospital"])
            if(x["Hospital"]==hospital and x["cTaken"]==False):
                available.append([hospital, x["cBed_no"]])
        #for i in available:   
            #print(i)
        #return render(request, 'avai_beds.html', {'available':available})
    
    elif(condi=="High" or condi=="Low"):
        for x in val:
            #print(x["Hospital"])
            if(x["Hospital"]==hospital and x["nTaken"]==False):
                available.append([hospital, x["Bed_no"]])
        #for i in available:   
            #print(i)
        #return render(request, 'avai_beds.html', {'available':available})

    return render(request, 'avai_beds.html', {'available':available}) 

def book(request):
    val = books.find() 
    condi = request.POST["Patient"]
    hospital = request.POST["hospital"]
    bed_no = int(request.POST["bed_no"])
    #print(condi, bed_no, hospital)

    cfind = books.find_one({"Hospital":hospital, "cBed_no":bed_no})
    nfind = books.find_one({"Hospital":hospital, "Bed_no":bed_no})
    msg=""
    if(condi=="Critical" and cfind["cTaken"]==False):
        books.update_one({"Hospital":hospital, "cBed_no":bed_no}, {"$set":{"cTaken":True}})
        msg = "Bed is allotted successfully"
    elif((condi=="High" or condi=="Low") and nfind["nTaken"]==False):
        books.update_one({"Hospital":hospital, "Bed_no":bed_no}, {"$set":{"nTaken":True}})
        msg = "Bed is allotted successfully"
    else:
        msg = "No bed available, find vacant beds"
        return render(request, 'index.html', {'alert': msg})
    return render(request, 'index.html', {'alert': msg})

def cancel(request):
    val = books.find()
    condi = request.POST["Patient"]
    hospital = request.POST["hospital"]
    bed_no = int(request.POST["bed_no"])
    #print(condi, bed_no, hospital)

    cfind = books.find_one({"Hospital":hospital, "cBed_no":bed_no})
    nfind = books.find_one({"Hospital":hospital, "Bed_no":bed_no})
    msg=""
    if(condi=="Critical" and cfind["cTaken"]==True):
        books.update_one({"Hospital":hospital, "cBed_no":bed_no}, {"$set":{"cTaken":False}})
        msg = "Booking is cancelled successfully"
    elif((condi=="High" or condi=="Low") and nfind["nTaken"]==True):
        books.update_one({"Hospital":hospital, "Bed_no":bed_no}, {"$set":{"nTaken":False}})
        msg = "Booking is cancelled successfully"
    else:
        msg = "No bed allotted to this booking"
        return render(request, 'index.html', {'msg': msg})
    return render(request, 'index.html', {'msg':msg})

def home(request):
    val = books.find() 
    #print(val)
    nb = int(0)
    cb = int(0)

    for x in val:
        #print(x["Bed_no"]) 
        if(x["nTaken"]==False):
           nb+=1
        if(x["cTaken"]==False):
           cb+=1  
    return render(request, 'index.html', {"val":val, "nb":nb+cb})

"""def add(request): 
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    sum = a+b
    return render(request,'index.html',{"answer":sum}) venv
""" 