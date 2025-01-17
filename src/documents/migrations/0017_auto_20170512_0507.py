# Generated by Django 1.10.5 on 2017-05-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0016_auto_20170325_1558"),
    ]

    operations = [
        migrations.AlterField(
            model_name="correspondent",
            name="matching_algorithm",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Any"),
                    (2, "All"),
                    (3, "Literal"),
                    (4, "Regular Expression"),
                    (5, "Fuzzy Match"),
                ],
                default=1,
                help_text='Which algorithm you want to use when matching text to the OCR\'d PDF.  Here, "any" looks for any occurrence of any word provided in the PDF, while "all" requires that every word provided appear in the PDF, albeit not in the order provided.  A "literal" match means that the text you enter must appear in the PDF exactly as you\'ve entered it, and "regular expression" uses a regex to match the PDF.  (If you don\'t know what a regex is, you probably don\'t want this option.)  Finally, a "fuzzy match" looks for words or phrases that are mostly—but not exactly—the same, which can be useful for matching against documents containg imperfections that foil accurate OCR.',
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="matching_algorithm",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Any"),
                    (2, "All"),
                    (3, "Literal"),
                    (4, "Regular Expression"),
                    (5, "Fuzzy Match"),
                ],
                default=1,
                help_text='Which algorithm you want to use when matching text to the OCR\'d PDF.  Here, "any" looks for any occurrence of any word provided in the PDF, while "all" requires that every word provided appear in the PDF, albeit not in the order provided.  A "literal" match means that the text you enter must appear in the PDF exactly as you\'ve entered it, and "regular expression" uses a regex to match the PDF.  (If you don\'t know what a regex is, you probably don\'t want this option.)  Finally, a "fuzzy match" looks for words or phrases that are mostly—but not exactly—the same, which can be useful for matching against documents containg imperfections that foil accurate OCR.',
            ),
        ),
    ]
