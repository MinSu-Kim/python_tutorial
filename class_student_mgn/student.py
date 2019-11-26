import json


class Student(object):
    def __init__(self, no=1, name="학생", kor=0, eng=0, math=0):
        self.no = int(no)
        self.name = name
        self.score = {'국어': kor, '영어': eng, '수학': math}

    def __init__(self, userdict=None):
        self.no = userdict['no']
        self.name = userdict['name']
        self.score = {'국어': userdict['score']['국어'], '영어': userdict['score']['영어'], '수학': userdict['score']['수학']}

    def get_total(self):
        return sum([s for s in self.score.values()])

    def get_average(self):
        return self.get_total() / float(3)

    def __json__(self):
        return {'no': self.no, 'name': self.name,
                'score': {'국어': self.score['국어'], '영어': self.score['영어'], '수학': self.score['수학']}}

    def __str__(self) -> str:
        return "{} {} {} {} {} {} {:.2f}".format(self.no, self.name, self.score['국어'], self.score['영어'],
                                                 self.score['수학'], self.get_total(), self.get_average())

    def to_json(self):
        dict_std = {'no': self.no, 'name': self.name,
                    'score': {'국어': self.score['국어'], '영어': self.score['영어'], '수학': self.score['수학']}}
        return json.dumps(dict_std, ensure_ascii=False)

    def __eq__(self, other) -> bool:
        if isinstance(other, dict):
            return self.no == other['no']
        return self.no == other.no
