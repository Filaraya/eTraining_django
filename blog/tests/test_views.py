from django.test import TestCase
from django.urls import reverse

from blog.models import Instructor

class InstructorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 instructors for pagination tests
        number_of_instructors = 13

        for instructor_id in range(number_of_instructors):
            Instructor.objects.create(
                first_name=f'James {instructor_id}',
                last_name=f'Jackson {instructor_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/instructors/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('instructors'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('instructors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/instructor_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('instructors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['instructor_list']) == 10)

    def test_lists_all_instructors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('instructors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['instructor_list']) == 3)