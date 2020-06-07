from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser
# Defines the model component of the MVC pattern.

# Customized model defining a user
class User(AbstractUser):
    user_avatar = ProcessedImageField(
        upload_to='static/pics/users',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

# Model defining a post
class Post(models.Model):
    # Django field offers different field options
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/pics/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

    # Create multi (Posts) to one (user) relationship with ForeignKey
    # delete all all posts owned by the user when deleting a user with CASCADE deletes.
    # related_name: defines the relationship between the object operating on the object containing
    #               the foreign key and the foreign key object
    #               in this case it allows us to find all posts by a given user
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owns')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

# Model defining a like, essentially a relationship object
class Like(models.Model):
    # Create multi (Likes) to one (user/post) relationship with ForeignKey
    # delete all all likes by the user/of the post when deleting a user/post with CASCADE deletes.
    user = models.ForeignKey('User', on_delete=models.CASCADE) # there is no related_name for user because nothing
                                                               # is operating on the user
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['user', 'post'] # only allows the user to like a post once

    # bind user and post keys together with __str__ function with every like object to enable unique_together
    def __str__(self):
        return self.user.username + ' likes ' + self.post.post_id
