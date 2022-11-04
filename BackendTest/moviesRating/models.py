from django.db import models
 
class Movie(models.Model):
    id = models.UUIDField(primary_key=True)
    isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    name = models.CharField(max_length=1)
    image = models.TextField()
    url = models.TextField()
    language = models.CharField(max_length=1)
    summary = models.TextField()
    ratingid = models.OneToOneField('Rating', models.DO_NOTHING, db_column='ratingId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True)
    isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    comment = models.TextField()
    username = models.CharField(max_length=1)
    description = models.TextField(blank=True, null=True)
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movieId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class Rating(models.Model):
    id = models.UUIDField(primary_key=True)
    isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    average = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'rating'


class Reaction(models.Model):
    id = models.UUIDField(primary_key=True)
    isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    type = models.TextField()  # This field type is a guess.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movieId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reaction'