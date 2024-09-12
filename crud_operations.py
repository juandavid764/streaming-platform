import requests
import json
from db import db
from couchdb.http import ResourceConflict

def get_document_templates(db):
    templates = {}
    for doc_id in db:
        if 'template_' in doc_id:  # Check if the document is a template"
            template = db[doc_id]
            templates[template['type']] = template['fields']
    return templates


def document_exists(db, doc_id):
    return doc_id in db


def create_record(record):
    try:
        db.save(record)
        print("document created")
    except ResourceConflict:
        print("document already exist")


def read_record(id):
    document = db.get(id)
    return document


def update_record(id, new_record):
    document = read_record(id)
    if document:
        try:
            for key, value in new_record.items():
                document[key] = value
            db.save(document)
            print("Document have been updated")
        except ResourceConflict:
            print("An error occurred")
    else:
        print("Document haven't found")


def delete_record(id):
    document = read_record(id)
    if document:
        db.delete(document)
        print("Successful elimination")
    else:
        print("Document haven't found")