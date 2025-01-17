# Generated by Django 3.1.4 on 2021-01-01 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1011_auto_20210101_2340"),
        ("paperless_mail", "0005_help_texts"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailaccount",
            options={
                "verbose_name": "mail account",
                "verbose_name_plural": "mail accounts",
            },
        ),
        migrations.AlterModelOptions(
            name="mailrule",
            options={"verbose_name": "mail rule", "verbose_name_plural": "mail rules"},
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="imap_port",
            field=models.IntegerField(
                blank=True,
                help_text="This is usually 143 for unencrypted and STARTTLS connections, and 993 for SSL connections.",
                null=True,
                verbose_name="IMAP port",
            ),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="imap_security",
            field=models.PositiveIntegerField(
                choices=[(1, "No encryption"), (2, "Use SSL"), (3, "Use STARTTLS")],
                default=2,
                verbose_name="IMAP security",
            ),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="imap_server",
            field=models.CharField(max_length=256, verbose_name="IMAP server"),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="name",
            field=models.CharField(max_length=256, unique=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="password",
            field=models.CharField(max_length=256, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="mailaccount",
            name="username",
            field=models.CharField(max_length=256, verbose_name="username"),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rules",
                to="paperless_mail.mailaccount",
                verbose_name="account",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="action",
            field=models.PositiveIntegerField(
                choices=[
                    (3, "Mark as read, don't process read mails"),
                    (4, "Flag the mail, don't process flagged mails"),
                    (2, "Move to specified folder"),
                    (1, "Delete"),
                ],
                default=3,
                verbose_name="action",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="action_parameter",
            field=models.CharField(
                blank=True,
                help_text="Additional parameter for the action selected above, i.e., the target folder of the move to folder action.",
                max_length=256,
                null=True,
                verbose_name="action parameter",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="assign_correspondent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.correspondent",
                verbose_name="assign this correspondent",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="assign_correspondent_from",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Do not assign a correspondent"),
                    (2, "Use mail address"),
                    (3, "Use name (or mail address if not available)"),
                    (4, "Use correspondent selected below"),
                ],
                default=1,
                verbose_name="assign correspondent from",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="assign_document_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.documenttype",
                verbose_name="assign this document type",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="assign_tag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.tag",
                verbose_name="assign this tag",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="assign_title_from",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Use subject as title"),
                    (2, "Use attachment filename as title"),
                ],
                default=1,
                verbose_name="assign title from",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="filter_body",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="filter body",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="filter_from",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="filter from",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="filter_subject",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="filter subject",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="folder",
            field=models.CharField(
                default="INBOX",
                max_length=256,
                verbose_name="folder",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="maximum_age",
            field=models.PositiveIntegerField(
                default=30,
                help_text="Specified in days.",
                verbose_name="maximum age",
            ),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="name",
            field=models.CharField(max_length=256, unique=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="mailrule",
            name="order",
            field=models.IntegerField(default=0, verbose_name="order"),
        ),
    ]
