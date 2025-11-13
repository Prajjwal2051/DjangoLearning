from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from .models import Trainer

# Create your tests here.

class TrainerModelTest(TestCase):
    """Test cases for the Trainer model"""
    
    def setUp(self):
        """Set up test data"""
        self.trainer = Trainer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@nie.ac.in',
            phone='1234567890',
            department='CS',
            specialization='AI',
            years_of_experience=5,
            bio='Experienced AI trainer with 5 years of teaching experience.',
            joined_date=date(2020, 1, 15)
        )
    
    def test_trainer_creation(self):
        """Test that a trainer is created successfully"""
        self.assertEqual(self.trainer.first_name, 'John')
        self.assertEqual(self.trainer.last_name, 'Doe')
        self.assertEqual(self.trainer.email, 'john.doe@nie.ac.in')
        self.assertTrue(self.trainer.is_active)
    
    def test_trainer_str(self):
        """Test the string representation of trainer"""
        expected = 'John Doe - Computer Science'
        self.assertEqual(str(self.trainer), expected)
    
    def test_get_full_name(self):
        """Test the get_full_name method"""
        self.assertEqual(self.trainer.get_full_name(), 'John Doe')
    
    def test_trainer_ordering(self):
        """Test that trainers are ordered by last name"""
        trainer2 = Trainer.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice.smith@nie.ac.in',
            department='ME',
            specialization='ML',
            years_of_experience=3,
            joined_date=date(2021, 3, 10)
        )
        
        trainers = Trainer.objects.all()
        self.assertEqual(trainers[0], self.trainer)  # Doe comes before Smith
        self.assertEqual(trainers[1], trainer2)


class TrainerViewTest(TestCase):
    """Test cases for trainer views"""
    
    def setUp(self):
        """Set up test data and client"""
        self.client = Client()
        
        # Create multiple trainers for testing
        self.trainer1 = Trainer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@nie.ac.in',
            department='CS',
            specialization='AI',
            years_of_experience=5,
            joined_date=date(2020, 1, 15)
        )
        
        self.trainer2 = Trainer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@nie.ac.in',
            department='EC',
            specialization='ML',
            years_of_experience=3,
            joined_date=date(2021, 6, 20)
        )
        
        self.trainer3 = Trainer.objects.create(
            first_name='Bob',
            last_name='Johnson',
            email='bob.johnson@nie.ac.in',
            department='CS',
            specialization='WEB',
            years_of_experience=7,
            is_active=False,  # Inactive trainer
            joined_date=date(2019, 9, 5)
        )
    
    def test_trainer_list_view(self):
        """Test the trainer list view loads successfully"""
        response = self.client.get(reverse('trainers:trainer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trainers/trainer_list.html')
        # Should only show active trainers
        self.assertEqual(len(response.context['trainers']), 2)
    
    def test_trainer_list_search_by_name(self):
        """Test searching trainers by name"""
        response = self.client.get(reverse('trainers:trainer_list'), {'q': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trainers']), 1)
        self.assertEqual(response.context['trainers'][0], self.trainer1)
    
    def test_trainer_list_search_by_email(self):
        """Test searching trainers by email"""
        response = self.client.get(reverse('trainers:trainer_list'), {'q': 'jane.smith'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trainers']), 1)
        self.assertEqual(response.context['trainers'][0], self.trainer2)
    
    def test_trainer_list_filter_by_department(self):
        """Test filtering trainers by department"""
        response = self.client.get(reverse('trainers:trainer_list'), {'department': 'CS'})
        self.assertEqual(response.status_code, 200)
        # Only trainer1 should appear (trainer3 is inactive)
        self.assertEqual(len(response.context['trainers']), 1)
        self.assertEqual(response.context['trainers'][0], self.trainer1)
    
    def test_trainer_list_filter_by_specialization(self):
        """Test filtering trainers by specialization"""
        response = self.client.get(reverse('trainers:trainer_list'), {'specialization': 'ML'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trainers']), 1)
        self.assertEqual(response.context['trainers'][0], self.trainer2)
    
    def test_trainer_list_combined_filters(self):
        """Test using multiple filters together"""
        response = self.client.get(reverse('trainers:trainer_list'), {
            'q': 'Doe',
            'department': 'CS'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trainers']), 1)
        self.assertEqual(response.context['trainers'][0], self.trainer1)
    
    def test_trainer_detail_view(self):
        """Test the trainer detail view"""
        response = self.client.get(reverse('trainers:trainer_detail', args=[self.trainer1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trainers/trainer_detail.html')
        self.assertEqual(response.context['trainer'], self.trainer1)
    
    def test_trainer_detail_view_inactive(self):
        """Test that inactive trainers return 404"""
        response = self.client.get(reverse('trainers:trainer_detail', args=[self.trainer3.pk]))
        self.assertEqual(response.status_code, 404)
    
    def test_trainer_detail_view_nonexistent(self):
        """Test that nonexistent trainers return 404"""
        response = self.client.get(reverse('trainers:trainer_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)


class TrainerAdminTest(TestCase):
    """Test cases for trainer admin"""
    
    def setUp(self):
        """Set up test data"""
        self.trainer = Trainer.objects.create(
            first_name='Test',
            last_name='Trainer',
            email='test@nie.ac.in',
            department='IS',
            specialization='DB',
            years_of_experience=2,
            joined_date=date(2023, 1, 1)
        )
    
    def test_trainer_admin_registered(self):
        """Test that Trainer model is registered in admin"""
        from django.contrib import admin
        from .models import Trainer
        
        self.assertTrue(admin.site.is_registered(Trainer))
