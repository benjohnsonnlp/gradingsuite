import os


def file_endings(language):
    endings = {
        "python": [
            ".py",
        ],
    }
    return endings[language]


class Submission:
    def __init__(self, filename, assignment):
        self.filename = filename
        self.assignment = assignment
        self.files = []

    def project_files(self):
        if self.files:
            return self.files  # cache so we don't hit the HD more than necessary
        full_path = os.path.join(self.assignment.home_dir, self.filename)
        for subdir in os.listdir(full_path):
            full_subdir = os.path.join(full_path, subdir)

            # if it's a file with one of the endings for the language of the assignment
            if not os.path.isdir(full_subdir):
                for ending in file_endings(self.assignment.language):
                    if full_subdir.endswith(ending):
                        self.files.append(subdir)

        return self.files

    def __str__(self):
        return self.filename


def get_submissions(filename, assignment):
    submissions = []
    for subdir in os.listdir(filename):
        full_subdir = os.path.join(filename, subdir)
        if os.path.isdir(full_subdir):
            submissions.append(Submission(subdir, assignment))

    return submissions
