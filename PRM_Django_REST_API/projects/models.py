from django.db import models
from django.utils.datetime_safe import datetime
from simple_history.models import HistoricalRecords


class Project(models.Model):
    """
    Used to house information pertaining to a particular project. The below fields are the bare minimum - additional
    relevant fields can be added.
    """
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=300, blank=False)
    users_assigned = models.ManyToManyField(
        "users.Profile", related_name="projects", blank=True
    )

    def __str__(self):
        return self.name


class Risk(models.Model):
    """
    Used to create records describing particular Project Risks.
    """
    class Background(models.TextChoices):
        FINANCE = "1", "Finance"
        OPERATIONS = "2", "Operations"
        STAFFING = "3", "Staffing"

    class Priority(models.TextChoices):
        LOW = "1", "Low"
        MEDIUM = "2", "Medium"
        HIGH = "3", "High"

    class Probability(models.TextChoices):
        ZERO_PERCENT = "0", "0%"
        TEN_PERCENT = "1", "10%"
        TWENTY_PERCENT = "2", "20%"
        THIRTY_PERCENT = "3", "30%"
        FORTY_PERCENT = "4", "40%"
        FIFTY_PERCENT = "5", "50%"
        SIXTY_PERCENT = "6", "60%"
        SEVENTY_PERCENT = "7", "70%"
        EIGHTY_PERCENT = "8", "80%"
        NINETY_PERCENT = "9", "90%"
        HUNDRED_PERCENT = "10", "100%"

    name = models.CharField(max_length=100, blank=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="risks", blank=False
    )
    background = models.CharField(
        max_length=50, choices=Background.choices, blank=False
    )
    priority = models.CharField(max_length=2, choices=Priority.choices, blank=False)
    probability_percentage = models.CharField(
        max_length=2, choices=Probability.choices, blank=False
    )
    resolvers_assigned = models.ManyToManyField(
        "users.Profile", related_name="resolvers_assigned", blank=True
    )
    change_history = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def get_change_history(self) -> list:
        """
        Retrieves information from the historical records of a Model and presents them in the form of
        :return: a list of changes applied to a Risk object
        """
        history = self.change_history.all().values()
        changes_list = list(history)
        irrelevant_changes = ["history_id", "history_date", "history_type"]
        changes_descriptions = list()
        for index, change in enumerate(changes_list):
            if index != 0:
                for key, value in change.items():
                    if changes_list[index - 1][key] != changes_list[index][key]:
                        if key not in irrelevant_changes:
                            new_value = changes_list[index - 1][key]
                            old_value = changes_list[index][key]
                            timestamp = datetime.strftime(
                                changes_list[index]["history_date"],
                                "%d-%m-%Y, %H:%M:%S",
                            )
                            changes_descriptions.append({
                                "change": {
                                    "field_changed": key,
                                    "old_value": old_value,
                                    "new_value": new_value,
                                    "changed_on": timestamp}
                                }
                            )
        return changes_descriptions
