import logging
import os
import csv

logger = logging.getLogger(__name__)


class JdClassification:

    def __init__(self):
        self.male = []
        self.female = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, '../../media/keywords.csv'), 'r') as f:
            cr = csv.DictReader(f)
            for row in cr:
                self.male_keywords.add_keyword(row['male'])
                self.female_keywords.add_keyword(row['female'])

    def find_male_female_words_match(self, paragraph):
        """

        :return:
        """
        males = self.male_keywords(paragraph)
        females = self.female_keywords(paragraph)
