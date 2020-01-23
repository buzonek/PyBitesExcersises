scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        if new_score < scores[0]:
            return None
        if new_score >= scores[-1]:
            return BELTS[scores[-1]]

        for score, next_score in zip(scores, scores[1:]):
            if score <= new_score < next_score:
                return BELTS[score]

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError
        if self._score > new_score:
            return
        self._score = new_score
        belt = self._get_belt(self._score)

        if belt == self._last_earned_belt:
            print(NEW_SCORE_MSG.format(score=self._score))
        else:
            self._last_earned_belt = belt
            print(CONGRATS_MSG.format(score=self._score,
                                      rank=self._last_earned_belt.capitalize()))

    score = property(_get_score, _set_score)
