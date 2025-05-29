from django.db import models

class AbcModel(models.Model):
    full_name = models.CharField(
        verbose_name="ФИО",
        max_length=255,
        default=""
    )
    x = models.FloatField(
        verbose_name="Значение X",
        default=0.0
    )
    y = models.FloatField(
        verbose_name="Значение Y",
        default=0.0
    )
    final_score = models.FloatField(
        verbose_name="Итоговая оценка (0.5 * X + 0.5 * Y)",
        default=0.0,
        help_text="Результат вычислений"
    )
    result = models.CharField(
        verbose_name="Описание результата",
        max_length=255,
        default="Результат не определён",
        help_text="Например: ошибка или пояснение"
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now=True
    )

    def save(self, *args, **kwargs):
        try:
            self.final_score = 0.5 * self.x + 0.5 * self.y
            self.result = f"Итоговая оценка: {self.final_score}"
        except Exception as e:
            self.result = f"Ошибка при расчёте: {e}"
            self.final_score = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} — {self.final_score:.2f} (X={self.x}, Y={self.y})"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        ordering = ("-pk",)
