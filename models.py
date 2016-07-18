from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 											#for using django user as authors and voters
#from django.template.defaultfilters import slugify

'''
	# Important Note:-
	 -	Although we could directly work with the poll model only for keeping track of votes but in that case, user-validation would be very difficult
		because it would be difficult to store which voter have voted and when on the poll.
	 -	It doesn’t matter which model has the ManyToManyField, but you should only put it in one of the models – not both.

	# Fields Present in auth.models.User :-
	 -	username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined

	# Methods Present in auth.models.User :-
	 -	get_username(), is_anonymous(), is_authenticated(), get_full_name(), get_short_name(), set_password(raw_password), has_perms(perm, obj=None),
		set_unusable_password(), has_usable_password(), get_group_permissions(obj=None), get_all_permissions(obj=None), check_password(raw_password),
		has_module_perms(package_name), email_user(subject, message, from_email=None, **kwargs)
'''

class Poll(models.Model):
	ACCESS_TO_VOTE_CHOICES = (
		('PUBLIC','PUBLIC'),				#anyone can see the poll and vote if wish
		('DEFAULT','DEFAULT'),				#anyone with link of poll can vote
		('PROTECTED','PROTECTED'),			#anyone with link can see the poll but only specific people(either matched-email or auth code) can vote
		('PRIVATE','PRIVATE'),				#only specific/white-listed people can see and vote(if not logged in, must give auth code)
	)
	AUTHOR_DISPLAY_CHOICES = (
		('A', 'Anonymous'),
		('N', 'NameOnly'),
		('NE', 'NameAndEmail')
	)
	poll_id = models.AutoField(primary_key=True)										#vote_id for easy reference of polls using an id
	headline = models.CharField(max_length=160)											#heading of the poll
	description = models.TextField(blank=True, null=True)								#detailed description of poll
	total_votes = models.BigIntegerField(default=0)										#total number of votes on the poll
	creation_date = models.DateTimeField(default=timezone.now)							#date of creation of poll. Will not show online
	publish_date = models.DateTimeField(blank=True, null=True)							#date of publishing. Will show on poll
	author = models.ForeignKey(User, related_name="author")								#authors of poll - 'auth.User'
	author_privacy = models.CharField(max_length=2, choices=AUTHOR_DISPLAY_CHOICES)		#display of creator of vote
	vote_access = models.CharField(max_length=9, choices=ACCESS_TO_VOTE_CHOICES)		#who can see the poll and vote on the poll
	invited_voters = models.ManyToManyField(User, related_name="invited_voters")		#compulsory for protected/private polls. Create user from email
	slug = models.SlugField(max_length=50,unique=True)									#slug url of poll
	#def save(self, *args, **kwargs):
	#	self.slug = slugify(self.truncate(headline))
	#	super(Idea, self).save(*args, **kwargs)
	def publish(self):
		self.publish_date = timezone.now()
		self.save()
	def __str__(self):
		return self.headline

class Choice(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice = models.CharField(max_length=160)
	def __str__(self):
		return self.choice

class Tag(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	tag = models.CharField(max_length=25)
	def __str__(self):
		return self.tag

class Vote(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)							#poll on which a vote is casted
	user = models.OneToOneField(User, on_delete=models.CASCADE)							#voter of the poll
	choice_selected = models.ForeignKey(Choice, on_delete=models.CASCADE)				#selecting more than one choice is irrelevant
	voting_time = models.DateTimeField(default=timezone.now)							#voting time. Just for the record
	def __str__(self):
		return self.poll.headline