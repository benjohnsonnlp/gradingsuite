import os


class Submission:
    def __init__(self, filename):
        self.filename = filename


def get_submissions(filename):
    submissions = []
    for subdir, dirs, files in os.walk(filename):
        for file in files:
            submissions.append(Submission(os.path.join(subdir, file)))

    return submissions
