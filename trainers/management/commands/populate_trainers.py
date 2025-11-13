from django.core.management.base import BaseCommand
from trainers.models import Trainer
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with sample trainer data'

    def handle(self, *args, **kwargs):
        # Clear existing trainers
        Trainer.objects.all().delete()
        
        trainers_data = [
            {
                'first_name': 'Rajesh',
                'last_name': 'Kumar',
                'email': 'rajesh.kumar@nie.ac.in',
                'phone': '9876543210',
                'department': 'CS',
                'specialization': 'AI',
                'years_of_experience': 8,
                'bio': 'Expert in Artificial Intelligence and Machine Learning with a focus on deep learning and neural networks.',
                'joined_date': date(2018, 6, 15)
            },
            {
                'first_name': 'Priya',
                'last_name': 'Sharma',
                'email': 'priya.sharma@nie.ac.in',
                'phone': '9876543211',
                'department': 'CS',
                'specialization': 'ML',
                'years_of_experience': 6,
                'bio': 'Specialized in Machine Learning algorithms, statistical analysis, and data science.',
                'joined_date': date(2019, 8, 20)
            },
            {
                'first_name': 'Amit',
                'last_name': 'Patel',
                'email': 'amit.patel@nie.ac.in',
                'phone': '9876543212',
                'department': 'CS',
                'specialization': 'WEB',
                'years_of_experience': 5,
                'bio': 'Full-stack web developer with expertise in modern JavaScript frameworks and backend technologies.',
                'joined_date': date(2020, 1, 10)
            },
            {
                'first_name': 'Sneha',
                'last_name': 'Reddy',
                'email': 'sneha.reddy@nie.ac.in',
                'phone': '9876543213',
                'department': 'EC',
                'specialization': 'NW',
                'years_of_experience': 7,
                'bio': 'Network security specialist with extensive experience in cloud computing and network architecture.',
                'joined_date': date(2018, 9, 5)
            },
            {
                'first_name': 'Vikram',
                'last_name': 'Singh',
                'email': 'vikram.singh@nie.ac.in',
                'phone': '9876543214',
                'department': 'ME',
                'specialization': 'OTHER',
                'years_of_experience': 10,
                'bio': 'Mechanical engineering expert with focus on robotics and automation.',
                'joined_date': date(2016, 3, 12)
            },
            {
                'first_name': 'Anita',
                'last_name': 'Desai',
                'email': 'anita.desai@nie.ac.in',
                'phone': '9876543215',
                'department': 'IS',
                'specialization': 'DB',
                'years_of_experience': 9,
                'bio': 'Database administrator and architect specializing in SQL and NoSQL databases.',
                'joined_date': date(2017, 7, 18)
            },
            {
                'first_name': 'Karthik',
                'last_name': 'Iyer',
                'email': 'karthik.iyer@nie.ac.in',
                'phone': '9876543216',
                'department': 'EE',
                'specialization': 'OTHER',
                'years_of_experience': 4,
                'bio': 'Electrical engineering trainer with expertise in power systems and renewable energy.',
                'joined_date': date(2021, 2, 25)
            },
            {
                'first_name': 'Meera',
                'last_name': 'Nair',
                'email': 'meera.nair@nie.ac.in',
                'phone': '9876543217',
                'department': 'CS',
                'specialization': 'AI',
                'years_of_experience': 3,
                'bio': 'AI researcher focusing on natural language processing and computer vision.',
                'joined_date': date(2022, 5, 8)
            },
            {
                'first_name': 'Suresh',
                'last_name': 'Babu',
                'email': 'suresh.babu@nie.ac.in',
                'phone': '9876543218',
                'department': 'CV',
                'specialization': 'OTHER',
                'years_of_experience': 12,
                'bio': 'Civil engineering veteran with specialization in structural design and construction management.',
                'joined_date': date(2014, 11, 30)
            },
            {
                'first_name': 'Divya',
                'last_name': 'Krishnan',
                'email': 'divya.krishnan@nie.ac.in',
                'phone': '9876543219',
                'department': 'EC',
                'specialization': 'ML',
                'years_of_experience': 5,
                'bio': 'Electronics engineer with focus on embedded systems and machine learning applications.',
                'joined_date': date(2020, 4, 15)
            },
        ]
        
        created_count = 0
        for data in trainers_data:
            trainer = Trainer.objects.create(**data)
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created trainer: {trainer.get_full_name()}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} trainers!'))
