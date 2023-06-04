from django.shortcuts import render
import datetime
from .models import Age_Table

# Create your views here.


def home(request):
    message = ""
    years = ""
    months = ""
    days = ""
    age = ""
    name = None
    gender = None

    # fetch data from front ends
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')

        Birth_Year = int(year)
        Birth_Month = int(month)
        Birth_Day = int(day)

        # logics of calculating the age
        current_date = datetime.date.today()
        if (Birth_Year > 0) & (Birth_Month > 0 & Birth_Month <= 12) & (Birth_Day > 0 & Birth_Day <= 31):
            birth_date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
            age = current_date - birth_date 
            years = age.days // 365
            months = (age.days % 365) // 30
            days = (age.days % 365) % 30

        else:
            message = "Year , month and days is not invalid! (year, month and day must be greater than zero!)"

        ##inserting the data into db
        if name and gender and years and months and days is not None:
            save_age_data=Age_Table(full_name=name,gender=gender,birth_year=years,birth_month=months,birth_day=days)
            save_age_data.save()
            print("data has inserted!")

    context = {
        # 'age': age,
        'years': years,
        'month': months,
        'days': days,
        'message': message,
    }

    return render(request, "index.html", context)
