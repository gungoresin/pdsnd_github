import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to see data for Chicago, New York City or Washington?\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("You type the city wrong. Please enter a valid input!")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to filter the data by?\
        january, february, march, april, may, june or all\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("You type the month wrong. Please enter a valid input!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week do you want to filter? Type day name else type 'all'\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("You type the day wrong. Please enter a valid input!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #creating new columns for month, day_of_week and start hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filtering by month
        df = df[df['month'] == month]

    if day != 'all':
        # filtering by day of the week
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    try:
        print("The most common month is ", df['month'].mode()[0], "\n")
    except Exception as e:
        print( "The program cannot calculate the most common month. An error occurred: {}".format(e))
        # display the most common day of week
    try:
        print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")
    except Exception as e:
        print( "The program cannot calculate the most common day of week. An error occurred: {}".format(e))

    # display the most common start hour
    try:
        print("The most common start hour is ", df['hour'].mode()[0])
    except Exception as e:
        print( "The program cannot calculate the most common start hour. An error occurred: {}".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")
    except Exception as e:
        print("The program cannot show the most commonly used start station. An error occurred: {}".format(e))
    # display most commonly used end station
    try:
        print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")
    except Exceotion as e:
        print("The program cannot show the mmost commonly used end station. An error occurred: {}".format(e))

    # display most frequent combination of start station and end station trip
    try:
        df['combination'] = df['Start Station'] + " " + df['End Station']
        print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])
    except Exception as e:
        print("The program cannot show the most frequent combination of start and end station trip. An error occurred: {}".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        total_travel_time=np.round(df['Trip Duration'].sum()/86400, decimals=2)
        print("The total travel time is", total_travel_time, "days.", "\n")
    except Exception as e:
        print("The program cannot calculate the total travel time. An error occurred: {}".format(e))
    # display mean travel time
    try:
        mean_travel_time=df['Trip Duration'].mean()
        mean_travel_time_minute=int(mean_travel_time//60)
        mean_travel_time_seconds=int(mean_travel_time%60)
        print("The total mean time is ", mean_travel_time_minute, " minute ",mean_travel_time_seconds, "seconds.","\n")
    except Exception as e:
        print("The program cannot calculate the mean travel time. An error occurred: {}".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:\n\n", user_types)

    # Display counts of gender
    if city != 'washington':
        gender_types = df.groupby(['Gender'])['Gender'].count()
        print("Counts of Gender Types:\n\n", gender_types)

    # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print('\nThe Earliest Year of birth:', earliest_year)

        most_recent_year = int(df['Birth Year'].max())
        print('\nMost Recent Year of birth:', most_recent_year)

        most_common_year = int(df['Birth Year'].value_counts().idxmax())
        print('\nMost Common Year of birth:', most_common_year)

    else:
            print("\n\nEarliest, most recent, most common year of birth are only available for NYC and Chicago.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
