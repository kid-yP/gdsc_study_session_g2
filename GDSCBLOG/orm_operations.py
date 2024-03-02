# Import necessary modules
from BlogApp.models import Post
from CommentApp.models import Comment

# Django setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
import django
django.setup()

# ORM operations for Posts

# Create posts
post1 = Post.objects.create(title='First Post', content='Content of the first post', category='General', image='path_to_image', tags=['tag1', 'tag2'])
post2 = Post.objects.create(title='Second Post', content='Content of the second post', category='Technology', image='path_to_image', tags=['tag3', 'tag4'])
post3 = Post.objects.create(title='Third Post', content='Content of the third post', category='Science', image='path_to_image', tags=['tag5', 'tag6'])

# Query and display all posts in a specific category
posts_in_category = Post.objects.filter(category='Technology')
for post in posts_in_category:
    print(post.title)

# Update the content of one post
post_to_update = Post.objects.get(title='First Post')
post_to_update.content = 'Updated content of the first post'
post_to_update.save()

# Delete a post
post_to_delete = Post.objects.get(title='Third Post')
post_to_delete.delete()

# ORM operations for Comments

# Create comments
comment1 = Comment.objects.create(content='Comment on the first post', author='John Doe', post=post1)
comment2 = Comment.objects.create(content='Comment on the second post', author='Jane Doe', post=post2)
comment3 = Comment.objects.create(content='Comment on the third post', author='Bob Smith', post=post2)

# Query and display all comments related to a specific post
comments_for_post2 = Comment.objects.filter(post=post2)
for comment in comments_for_post2:
    print(comment.content)

# Update the content of one comment
comment_to_update = Comment.objects.get(content='Comment on the first post')
comment_to_update.content = 'Updated comment on the first post'
comment_to_update.save()

# Delete a comment
comment_to_delete = Comment.objects.get(content='Comment on the second post')
comment_to_delete.delete()
