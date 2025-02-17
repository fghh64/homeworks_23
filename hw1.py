"""Calculate the top 3 salaries and their ratio to the total salary."""


def get_salary_stats(limit: tuple = None, **departments: dict[str, dict[str, float]]) -> tuple:
    """
    Calculate the 3 smallest salaries and their ratio to the total salary.

    Args:
        limit: The departments to consider.
        departments: The department and employee salary information.

    Returns:
        The top 3 salaries and their ratio to the total salary.
    """
    salaries = []
    if limit is not None:
        limit = set(limit)
    for department, employees in departments.items():
        if limit is None or department in limit:
            salaries.extend(employees.values())

    salaries.sort()
    top_salaries = salaries[:3]
    total_salary = sum(salaries)
    try:
        top_ratio = sum(top_salaries) / total_salary * 100
    except ZeroDivisionError:
        top_ratio = 0

    return [round(salary, 2) for salary in top_salaries], round(top_ratio, 2)
