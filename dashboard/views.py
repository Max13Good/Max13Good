from django.shortcuts import render


def student_dashboard(request):
    """Render demo student dashboard with static data."""
    context = {
        "student_name": "Иван Иванов",

        "lesson": {
            "subject": "Английский язык",
            "teacher": "Елена Смирнова",
            "datetime": "26 июня, 10:00",
        },
        "homework": [
            "Выучить слова из Unit 5",
            "Сделать упражнения на времена",
        ],
        "payment": {
            "last_payment": "20 июня",
            "paid_until": "30 июня",
            "status": "Оплачено",
        },
    }
    return render(request, "dashboard/student.html", context)

