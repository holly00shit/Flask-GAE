
from flask import g, render_template, request, jsonify
from application.services.posts_service import *

def posts():
    try: index = int(request.args.get('index'))
    except: index = 0
    keyword = request.args.get('keyword')
    if keyword is None: keyword = ''
    g.view_model['keyword'] = keyword

    g.view_model['title'] = 'Board - '

    ps = PostsService()
    result, total = ps.get_posts(keyword, index)
    g.view_model['page'] = {
        'items': result,
        'total': total,
        'index': index,
        'size': config.page_size,
        'max': (total - 1) / config.page_size
    }

    return render_template('board.html', **g.view_model)

def post_add():
    title = request.form.get('title')
    content = request.form.get('content')

    ps = PostsService()
    success = ps.create_post(title, content)

    return jsonify({'success': success})

def post_delete(post_id=None):
    ps = PostsService()
    success = ps.delete_post(post_id)

    return jsonify({'success': success})