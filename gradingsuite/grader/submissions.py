import os


class Submission:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return self.filename


def get_submissions(filename):
    submissions = []
    for subdir in os.listdir(filename):
        full_subdir = os.path.join(filename, subdir)
        if os.path.isdir(full_subdir):
            submissions.append(Submission(full_subdir))

    return submissions
