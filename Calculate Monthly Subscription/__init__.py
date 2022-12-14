import datetime
import calendar


def monthly_charge(month, subscription, users) -> int:
    """
    Computes the monthly charge for a given subscription.

    @rtype: int
    @returns: the total monthly bill for the customer in cents, rounded
      to the nearest cent. For example, a bill of $20.00 should return 2000.
      If there are no active users or the subscription is None, returns 0.

    @type month: str
    @param month - Always present
      Has the following structure:
      "2022-04"  # April 2022 in YYYY-MM format

    @type subscription: dict
    @param subscription - May be None
      If present, has the following structure:
      {
        'id': 763,
        'customer_id': 328,
        'monthly_price_in_cents': 359  # price per active user per month
      }

    @type users: list
    @param users - May be empty, but not None
      Has the following structure:
      [
        {
          'id': 1,
          'name': "Employee #1",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 11, 4),

          # last day to bill for user
          # should bill up to and including this date
          # since user had some access on this date
          'deactivated_on': datetime.date(2022, 4, 10)
        },
        {
          'id': 2,
          'name': "Employee #2",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 12, 4),

          # hasn't been deactivated yet
          'deactivated_on': None
        },
      ]
    """
    # Your code goes here
    year, month_str, *extra = month.split('-')
    return_amount: int = 0
    temp_date: datetime.date = datetime.date(int(year), int(month_str), 1)
    day_one: datetime.date = first_day_of_month(temp_date)
    day_n: datetime.date = last_day_of_month(temp_date)

    for user in users:
        start_date = day_one if (user['activated_on'] <= day_one) else user['activated_on']
        limit_date = user.get('deactivated_on') if (user.get('deactivated_on') is not None) else day_n

        time_active = limit_date - start_date
        if time_active.days > 0:
            # If there was a daily rate you would do the following:
            # return_amount += (time_active.days * int(subscription['monthly_price_in_cents']))
            return_amount += (1 * int(subscription['monthly_price_in_cents']))

    return return_amount  # Removes the decimal if present


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 1)                           # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 31)                         # Mar 31

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2022, 3, 17))   # Mar 17
    datetime.date(2022, 3, 18)                 # Mar 18

    >>> next_day(datetime.date(2022, 3, 31))  # Mar 31
    datetime.date(2022, 4, 1)                 # Apr  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)
