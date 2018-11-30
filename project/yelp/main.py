import json
import datetime


def load_feedback(filename):
    with open(filename) as file:
        return json.load(file)


def save_feedback(feedback_list, filename):
    with open(filename, 'w') as file:
        json.dump(feedback_list, file, indent=2)


def add_comment(feedback_list, author, comment):
    now = datetime.datetime.now().isoformat()
    new_comment = {
        "author": author,
        "comment": comment,
        "added_at": now,
    }
    feedback_list.append(new_comment)


def search_for_date(feedback_list, date):
    result = []
    iso_date = date.isoformat()

    for feedback_item_dict in feedback_list:
        added_at = feedback_item_dict["added_at"]
        if added_at.startswith(iso_date):
            result.append(feedback_item_dict)
    return result


def migration_forward(feedback_list):
    """Convert existing list of lists into a list of dictionaries"""
    result = []
    for author, comment in feedback_list:
        # default date is "one week ago" ;)
        date = datetime.datetime.now() - datetime.timedelta(days=7)
        result.append(dict(
            author=author,
            comment=comment,
            added_at=date.isoformat()
        ))
    return result


def print_today(feedback):
    today = datetime.date.today()
    print 'Feedbacks for', today
    for item in search_for_date(feedback_list, today):
        print item['author'], '-', item['comment']


def main(filename):
    feedback_list = load_feedback(filename)

    # add_comment(feedback_list, 'alisa', 'Hate! Olivye salad was terrible :X')
    print_today(feedback)

    save_feedback(feedback_list, filename)


if __name__ == '__main__':
    main('feedback.json')
