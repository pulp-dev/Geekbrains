def salary_counter(hours, payment_per_hour, reward):
    return (hours * payment_per_hour) + reward


print(salary_counter(int(input('количество рабочих часов - ')), int(input('плата в час - ')), int(input('премия - '))))