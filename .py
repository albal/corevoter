from fuzzywuzzy import process
def suggest_courses(title):
    all_titles = [course.title for course in Course.query.all()]
    suggestions = process.extract(title, all_titles, limit=10)
    # return courses with suggested titles...