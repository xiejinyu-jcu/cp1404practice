"""
CP1404 Practical 07 - Project
Estimate: 30 minutes
Actual: 20 minutes
"""
from datetime import datetime

class Project:
    """create the project to manage and store the details"""
    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project instance."""
        self.name=name
        self.start_date=start_date if start_date else datetime.now().date()
        self.priority=priority
        self.cost_estimate=cost_estimate
        self.completion_percentage=completion_percentage


    def __str__(self):
        """make the object convert to string """
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
