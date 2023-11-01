#!/usr/bin/env python
import pika
import json
import os, time
from dotenv import load_dotenv
load_dotenv()

start = time.time()

RABBITMQ_SERVER = os.getenv("RABBITMQ_SERVER")
RABBITMQ_PORT   = os.getenv("RABBITMQ_PORT")
RABBITMQ_USER   = os.getenv("RABBITMQ_USER")
RABBITMQ_PASS   = os.getenv("RABBITMQ_PASS")

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER, RABBITMQ_PORT, '/', credentials))

properties = pika.BasicProperties(content_type='application/json')

channel = connection.channel()

names =  ["Emily","Hannah","Madison","Ashley","Sarah","Alexis","Samantha","Jessica","Elizabeth","Taylor","Lauren","Alyssa","Kayla","Abigail","Brianna","Olivia","Emma","Megan","Grace","Victoria","Rachel","Anna","Sydney","Destiny","Morgan","Jennifer","Jasmine","Haley","Julia","Kaitlyn","Nicole","Amanda","Katherine","Natalie","Hailey","Alexandra","Savannah","Chloe","Rebecca","Stephanie","Maria","Sophia","Mackenzie","Allison","Isabella","Amber","Mary","Danielle","Gabrielle","Jordan","Brooke","Michelle","Sierra","Katelyn","Andrea","Madeline","Sara","Kimberly","Courtney","Erin","Brittany","Vanessa","Jenna","Jacqueline","Caroline","Faith","Makayla","Bailey","Garland","Garrett","Gavin","Geisha","Genny","Gerardo","Gila","Gissella","Graciana","Gracianna","Gwenivere","Halea","Halina","Hanh","Hannelore","Harnoor","Harshita","Harsimran","Helayna","Herminia","Heydy","Hollee","Malisha","Manaal","Marc","Marcedes","Marchelle","Margarette","Mariea","Marili","Marionna","Mariposa","Mariska","Zafirah","Zailey","Zakoria","Zakya","Zalaya","Zamanta","Zamariah","Zamiah","Zamiyah","Zanaii","Zanaria","Zanayah","Zareah","Zareen","Zarelia","Zarreah","Zaryia","Zawadi","Zayanna","Zaydee","Zaylee","Zehava","Zeltzin","Zhariah","Zikiria","Zineb","Zionah","Ziyana","Zlata","Zlaty","Zobia","Zoei","Zona","Zophia","Zori","Zorina","Zorriah","Zorya","Zoye","Zsazsa","Zyah","Zyaira","Zykeia","Zykeriah","Zykiera","Zyonna","Zyra"];


count = 1
for y in range(10):   
    for x in range(len(names)):
        body = {"id": count, "name": names[x]}
        count=count+1
        channel.queue_declare(queue='newRecord')

        channel.basic_publish(exchange='', routing_key='newRecord', body=json.dumps(body), properties=properties)
        print(" [x] Sent 'JSON to RabbitMQ:::'", count, ',', names[x])
connection.close()