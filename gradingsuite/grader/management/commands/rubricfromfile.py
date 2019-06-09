import json

from django.core.management import BaseCommand

from grader.models import Rubric, Assignment, RubricSection, RubricItem


class Command(BaseCommand):
    help = 'Creates a rubric in the db from a json file.  See sample_rubric for format'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)
        parser.add_argument('assignment_id', nargs=1, type=int)

    def handle(self, *args, **options):
        filename = options['filename'][0]
        with open("sample_rubric.json", 'r') as f:
            rubric_from_file = json.load(f)
        rubric = Rubric()
        rubric.assignment = Assignment.objects.get(pk=options['assignment_id'][0])
        rubric.is_blank = True
        rubric.save()
        for section in rubric_from_file:
            rubric_section = RubricSection()
            rubric_section.name = section['name']
            rubric_section.rubric = rubric
            rubric_section.save()
            for item in section['items']:
                rubric_item = RubricItem()
                rubric_item.text = item['text']
                rubric_item.possible_points = item['value']
                rubric_item.earned_points = item['value']
                rubric_item.optional = (item['optional'] == 'true')
                rubric_item.section = rubric_section
                rubric_item.save()
