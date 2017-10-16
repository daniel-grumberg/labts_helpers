#!/usr/local/bin/python3

from html.parser import HTMLParser

class LabTSMainPageParser(HTMLParser):
    def __init__(self):
        self.table_nest = 0
        self.links = {}
        self.curr_td = False
        self.curr_link = ''
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.table_nest += 1

        if tag == 'td':
            self.curr_td = True

        if tag == 'a' and self.table_nest == 2:
            attrs_dict = dict(attrs)
            self.curr_link = attrs_dict['href']

    def handle_data(self, data):
        if self.curr_link != "":
            self.links[data] = self.curr_link
        self.curr_link = ""


    def handle_endtag(self, tag):
        if tag == 'table':
            self.table_nest -= 1
        elif tag == 'td':
            self.curr_td = False

################################################################################

class ExercisePageParser(HTMLParser):
    def __init__(self, students):
        self.students = students
        self.submissions = {}
        self.tds = 0
        self.curr_student = ''
        self.curr_tag = ''
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.curr_tag = tag
        if tag == 'td':
            self.tds += 1
        if tag == 'a' and self.tds == 5:
            attrs_dict = dict(attrs)
            if 'final' in attrs_dict['href']:
                self.submissions[self.curr_student] = attrs_dict['href']

    def handle_data(self, data):
        if self.tds == 1 and self.curr_tag == 'a':
            for s in self.students:
                if s in data.strip() and data.strip():
                    self.curr_student = s
                    break

    def handle_endtag(self, tag):
        if tag == 'td' and self.tds == 6:
            self.tds = 0
            self.curr_student = ''
