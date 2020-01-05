from django.test import TestCase, Client #same base module, so you can separate by commas
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    #setup function is function that is run before every test that is run
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        #uses the client helper function that allows you to log a user in with the django authentication (don't have to manually log user in)
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        #type the app that you are going for : then the url that you are going for and these urls are defined in django admin documentation
        #generates the url for the list user page and the reason we use the reverse function is that if we ever want to change
        #the url in the future it means we don't have to go through and change it everywhere in our test because it should update automatically based
        #on reverse
        url = reverse('admin:core_user_changelist')
        #res is response
        res = self.client.get(url) #this will use test client to perform an http get on the url that we found above
        #assertContains function is a django custom assertion that will check that the response will contain certain items ie 200 and content has user name
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id]) #anything we pass in here will get assigned to the arguments below
        #/admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)  #test that the status code is 200


    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

        
