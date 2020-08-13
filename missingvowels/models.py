from django.db import models

class Category(models.Model):
    """
    A category of related answers (e.g. Web Browsers).
    """
    title = models.CharField(blank=False, max_length=64, unique=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    A item within a Category (e.g. Edge, Firefox, Chrome, etc...)
    """
    class Meta:
        unique_together = (('category', 'answer'))

    answer = models.CharField(blank=False, max_length=128)
    category = models.ForeignKey(
        "Category", blank=False, on_delete=models.CASCADE)
    render_format = models.CharField(blank=True, max_length=128)

    def __str__(self):
        return (
            f"{self.category}: "
            f"{self.render_format if self.render_format else ''.join([c.lower() for c in self.answer if c.lower() not in 'aeiou'])}"
        )
