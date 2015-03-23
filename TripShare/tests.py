from django.test import TestCase
from TripShare.models import Trip,User,UserProfile,Rating
import datetime
import time
from django.core.urlresolvers import reverse

class TripMethodTests(TestCase):
	"""
	   Checks if model Trip accepts number of passengers < 1
	"""
	def test_ensure_pass_num_is_less_than_1(self):
		user2 = User(id = 1)

		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate=datetime.datetime(2015,5,1,12,0,0),dateposted='2015-02-03')
		trip.save()
		self.assertEqual((trip.pass_num >= 1), True)
	"""
	   Checks if model Trip accepts cost < 0
	"""

	def test_ensure_cost_is_positive(self):
		user2 = User(id = 1)
		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate=datetime.datetime(2015,5,1,12,0,0),dateposted='2015-02-03')
		trip.save()
		self.assertEqual((trip.cost >= 0), True)

	"""
	   Check if model Trip accepts tripdate < current date
	"""

	def test_ensure_tripdate_is_not_pas(self):

		user2 = User(id = 1)
		



		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate =datetime.datetime(2013,5,1,12,0,0),dateposted='2015-02-03')
		trip.save()
		today = datetime.datetime.today()
		
		self.assertEqual((trip.tripdate >= today), True)

	"""
	   Checks if model Rating accepts rating < 0
	"""

	def test_ensure_rating_is_not_negative(self):
		user = User(id = 1)

		rating_test = Rating(user,user,-1)
		rating_test.save()
		self.assertEqual((rating_test.rating >= 0), True)

	"""
	    If no trips exist, an appropriate message sould be displayed
	"""

	def test_index_view_with_no_trips(self):
        	
        	response = self.client.get(reverse('index'))
        	self.assertEqual(response.status_code, 200)
	
	def test_index_view_with_trips(self):
    		"""
   		 If no trips exist, an appropriate message should be displayed.
   		 """
		user2 = User(id = 1)

		t = Trip.objects.get_or_create(desc='test')[0]
		t.creator = user2
		t.destination = 'testd'
		t.source = 'tests'
		t.pass_num = 1
		t.cost = 1
		t.tripdate = datetime.datetime(2015,5,1,12,0,0)
		t.dateposted = datetime.datetime(2015,5,1,11,0,0)
		t.save()




    		response = self.client.get(reverse('index'))
    		self.assertEqual(response.status_code, 200)
    		self.assertContains(response, 'test')

    		#num_cats =len(response.context['categories'])
    		#self.assertEqual(num_cats , 4)

	def test_index_view_with_registers(self):
    		"""
   		 If no trips exist, an appropriate message should be displayed.
   		 """
		user2 = User(id = 1)
		profile = UserProfile(user = user2,isDriver = True,dob="1990-2-3")



    		response = self.client.get(reverse('register'))
    		self.assertEqual(response.status_code, 200)
    		self.assertContains(response, "1990-2-3")

    		#num_cats =len(response.context['categories'])
    		#self.assertEqual(num_cats , 4)
