from enum import Enum
from typing import Optional
from urllib import response
from xmlrpc.client import boolean
from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get('/')
def home():
    return {'mesage': "Hellow world"}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'mesage': "All blogs provided"}

@app.get('/blog/all', tags=['blog'], summary='Retrieve all blogs', description='This api call simulates fetching all blogs.')
def get_all_blogs(page = 1, page_size = 10): # default values
    return {'mesage': f"All {page_size} blogs ont page {page}"}

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter

    """
    return {'message': f'blog_id {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}
     
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id>10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'mesage': f"Blog with {id}"}
