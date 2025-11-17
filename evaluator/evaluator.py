def score_clarity(text):
    return min(len(text) / 50, 10)

def score_accuracy(text):
    return 8.5  # mocked

def score_completeness(text):
    return 9.0  # mocked

class Evaluator:
    def evaluate(self, output):
        return {
            "clarity": score_clarity(output),
            "accuracy": score_accuracy(output),
            "completeness": score_completeness(output)
        }
