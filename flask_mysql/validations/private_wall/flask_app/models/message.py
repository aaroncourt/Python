from pickle import APPEND
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import app
from flask import flash, redirect, session
from flask_app.models.user import User
import re

class Message:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.creator = None
        self.message = db_data['message']
        self.recipient = None
        # self.deleted = db_data['deleted']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_messages(cls, data):
        query = 'SELECT * FROM users AS sender JOIN messages ON creator_id = sender.id JOIN users AS recipient ON recipient.id = recipient_id WHERE messages.recipient_id = %(user_id)s;'
        results = MySQLConnection('private_wall').query_db(query, data)
        pprint.pprint(results)

        message_list = []

        for result in results:
            sender = User(result)
            message_info = {
                'id' : result['messages.id'],
                'message' : result['message'],
                'created_at' : result['messages.created_at'],
                'updated_at' : result['messages.updated_at'],
            }
            message = cls(message_info)
            message.creator = sender
            message_list.append(message)

        return message_list

    @classmethod
    def get_sent_msgs(cls, data):
        query = 'SELECT * FROM messages WHERE creator_id = %(user_id)s'
        results = MySQLConnection('private_wall').query_db(query, data)

        msg_ids_list = []

        for result in results:
            id = cls(result)
            msg_ids_list.append(id)

        return msg_ids_list

    @classmethod
    def new_message(cls, data):
        query = 'INSERT INTO messages (creator_id, message, recipient_id) VALUES (%(creator_id)s, %(message)s, %(recipient_id)s)'

        return MySQLConnection('private_wall').query_db(query, data)

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id = %(message_id)s"

        return MySQLConnection('private_wall').query_db(query, data)