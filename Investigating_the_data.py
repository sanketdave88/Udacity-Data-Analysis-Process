import unicodecsv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments_data = read_csv('/datasets/ud170/udacity-students/enrollments.csv')
daily_engagement_data = read_csv('/datasets/ud170/udacity-students/daily_engagement.csv')
project_submissions_data = read_csv('/datasets/ud170/udacity-students/project_submissions.csv')

# For each of these three tables, find the number of rows in the table and
# the number of unique students in the table. To find the number of unique
# students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments_data)
enrollment_num_unique_students = len(set([enrollment['account_key'] for enrollment in enrollments_data]))

engagement_num_rows = len(daily_engagement_data)
engagement_num_unique_students = len(set([engagement['acct'] for engagement in daily_engagement_data]))

submission_num_rows = len(project_submissions_data)
submission_num_unique_students = len(set([submission['account_key'] for submission in project_submissions_data]))

print(enrollment_num_rows)
print(enrollment_num_unique_students)
print(engagement_num_rows)
print(engagement_num_unique_students)
print(submission_num_rows)
print(submission_num_unique_students)
