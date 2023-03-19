import io
import os
import tqdm
import traceback
import psycopg2
import pymongo
import gridfs
import bson
from bson.objectid import ObjectId
from flask import Flask, request
from zipfile import ZipFile
from multiprocessing.pool import ThreadPool
from embeddings import get_embeddings
import pickle
import glob


class MongoDB:

    def __init__(self, cred):
        self.mongo_cred = cred
        self.mongo_client = pymongo.MongoClient(self.mongo_cred)
        self.mongo_db = self.mongo_client.dummy
        self.mongo_col = self.mongo_db["data"]
        self.mongo_fs = gridfs.GridFS(self.mongo_db, collection='full_images')

    def put_to_fs(self, im_bytes, meta=False):
        if meta:
            meta_data = bson.Binary(pickle.dumps(meta))
        else:
            meta_data = None
        fid = self.mongo_fs.put(im_bytes, metadata=meta_data)
        return fid


class PostGresDB:

    def __init__(self, database, user, password, host, port):
        self.conn = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def insert_record(self, name, embedding, path):
        sql_query = '''insert into image_embeddings(name, embedding, path) 
                        values(%s, %s, %s) RETURNING id;'''
        self.cur.execute(sql_query, (name, embedding, path))
        row = self.cur.fetchone()
        return row[0]


def handle_image(im_path, mongo_db_obj, postgres_db_obj):
    try:
        im_name = os.path.basename(im_path).split(".")[0]
        with open(im_path, "rb") as f:
            im_bytes = f.read()
        data = get_embeddings(im_name)
        key_value = postgres_db_obj.insert_record(im_name, data, im_path)
        data_to_store = {"id": key_value, "image_name": im_name}
        id_ = mongo_db_obj.put_to_fs(im_bytes, meta=data_to_store)
        return id_
    except:
        pass
    return False


mongo_db_obj = MongoDB('postgres')

postgres_db_obj = PostGresDB(database='postgres', user='postgres', 
                             password='asd123', host='localhost', 
                             port='5432')

zips_dest_dirs = "extracted_zips"

if not os.path.exists(zips_dest_dirs):
    os.mkdir(zips_dest_dirs)

app = Flask(__name__)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    try:
        zip_file = request.files.get("archive")
        with ZipFile(zip_file, "r") as zipObj:
            zipObj.extractall(zips_dest_dirs)

        im_paths = glob.glob(zips_dest_dirs + "/**/*.jpg", recursive=True)
        pool = ThreadPool()
        results = list(
            tqdm.tqdm(pool.imap_unordered(lambda x: handle_image(x, mongo_db_obj, postgres_db_obj), im_paths), total=len(im_paths))
        )
        no_of_inserted_images = sum([1 for r in results if r])
        return {"status": f"{no_of_inserted_images} images done"}
    except Exception as e:
        return {"status": str(traceback.format_exc())}

