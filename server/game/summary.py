import re


class GameSummary(object):
    def __init__(self):
        self.winner = None

    def set_winner(self, winner):
        assert(self.winner is None)
        self.winner = winner

    def __repr__(self):
        return 'Winner: {}\n'.format(self.winner)

    @classmethod
    def from_repr(cls, str_repr):
        repr_re = re.compile(r'''
            ^
            Winner:\ (?P<winner>.+)\n
            $
        ''', re.VERBOSE)

        m = repr_re.match(str_repr)
        winner = m.group('winner')

        summary = cls()
        summary.set_winner(winner)
        return summary
