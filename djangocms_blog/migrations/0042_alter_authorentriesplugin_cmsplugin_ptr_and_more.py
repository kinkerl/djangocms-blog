# Generated by Django 4.2.3 on 2023-08-04 09:10

import aldryn_apphooks_config.fields
import django.db.models.deletion
import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("djangocms_blog", "0041_auto_20230720_1508"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authorentriesplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="genericblogplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="latestpostsplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.CreateModel(
            name="FeaturedPostsPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "current_site",
                    models.BooleanField(
                        default=True, help_text="Select items from the current site only", verbose_name="current site"
                    ),
                ),
                (
                    "template_folder",
                    models.CharField(
                        choices=[("plugins", "Default template")],
                        default="plugins",
                        help_text="Select plugin template to load for this instance",
                        max_length=200,
                        verbose_name="Plugin template",
                    ),
                ),
                (
                    "app_config",
                    aldryn_apphooks_config.fields.AppHookConfigField(
                        blank=True,
                        help_text="When selecting a value, the form is reloaded to get the updated default",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djangocms_blog.blogconfig",
                        verbose_name="app. config",
                    ),
                ),
                (
                    "posts",
                    sortedm2m.fields.SortedManyToManyField(
                        help_text=None, to="djangocms_blog.post", verbose_name="Featured posts"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]