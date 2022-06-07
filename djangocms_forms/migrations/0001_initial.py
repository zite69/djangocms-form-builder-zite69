# Generated by Django 3.2.13 on 2022-06-01 10:21

from django.conf import settings
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djangocms_forms.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0035_auto_20220601_1021'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_forms_form', serialize=False, to='cms.cmsplugin')),
                ('form_selection', models.CharField(blank=True, choices=[('No forms registered', ())], default='', max_length=256, verbose_name='Form')),
                ('form_name', models.CharField(blank=True, default='', max_length=256, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Form name')),
                ('form_login_required', models.BooleanField(blank=True, default=False, help_text='To avoid issues with user experience use this type of form only on pages, which require login.', verbose_name='Login required to submit form')),
                ('form_unique', models.BooleanField(default=False, help_text='Requires "Login required" to be checked to work.', verbose_name='User can reopen form')),
                ('form_floating_labels', models.BooleanField(default=False, verbose_name='Floating labels')),
                ('form_spacing', models.CharField(choices=[('mb-3', 'Default')], default='mb-3', max_length=16, verbose_name='Margin between fields')),
                ('form_actions', models.CharField(choices=[('643864cc8a67dc30f06bf597aaae64f39fb76224', 'Save form submission'), ('7b33f4e069df1285257d246e4e2d54b48ec7b483', 'Send email to administrators')], default='643864cc8a67dc30f06bf597aaae64f39fb76224', max_length=1024, verbose_name='Actions to be taken after form submission')),
                ('attributes', djangocms_forms.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('captcha_widget', models.CharField(blank=True, choices=[('', '-----'), ('v2-checkbox', 'v2 checkbox'), ('v2-invisible', 'v2 invisible')], default='v2-invisible', help_text='Read more in the <a href="https://developers.google.com/recaptcha" target="_blank">documentation</a>.', max_length=16, verbose_name='reCaptcha widget')),
                ('captcha_requirement', models.DecimalField(decimal_places=2, default=0.5, help_text='Only for reCaptcha v3: Minimum score required to accept challenge.', max_digits=3, verbose_name='Minimum score requirement')),
                ('captcha_config', djangocms_forms.fields.AttributesField(blank=True, default=dict, help_text='The reCAPTCHA widget supports several <a href="https://developers.google.com/recaptcha/docs/display#render_param" target="_blank">data attributes</a> that customize the behaviour of the widget, such as <code>data-theme</code>, <code>data-size</code>. The reCAPTCHA api supports several <a href="https://developers.google.com/recaptcha/docs/display#javascript_resource_apijs_parameters" target="_blank">parameters</a>. Add these api parameters as attributes, e.g. <code>hl</code> to set the language.', verbose_name='Recaptcha configuration parameters')),
                ('tag_type', djangocms_forms.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
            ],
            options={
                'verbose_name': 'Form',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_forms_formfield', serialize=False, to='cms.cmsplugin')),
                ('ui_item', models.CharField(max_length=30)),
                ('tag_type', djangocms_forms.fields.TagTypeField(blank=True, choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('config', models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            options={
                'verbose_name': 'Form UI item',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.SlugField(verbose_name='Form')),
                ('entry_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('html_headers', models.JSONField(blank=True, default=dict)),
                ('entry_created_at', models.DateTimeField(auto_now_add=True)),
                ('entry_updated_at', models.DateTimeField(auto_now=True)),
                ('form_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Form entry',
                'verbose_name_plural': 'Form entries',
            },
        ),
        migrations.CreateModel(
            name='BooleanField',
            fields=[
            ],
            options={
                'verbose_name': 'Boolean field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='CharField',
            fields=[
            ],
            options={
                'verbose_name': 'Character field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
            ],
            options={
                'verbose_name': 'Choice',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='DateField',
            fields=[
            ],
            options={
                'verbose_name': 'Date field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='DateTimeField',
            fields=[
            ],
            options={
                'verbose_name': 'Date field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='DecimalField',
            fields=[
            ],
            options={
                'verbose_name': 'Decimal field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='EmailField',
            fields=[
            ],
            options={
                'verbose_name': 'Email field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='IntegerField',
            fields=[
            ],
            options={
                'verbose_name': 'Integer field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
            ],
            options={
                'verbose_name': 'Select',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='SubmitButton',
            fields=[
            ],
            options={
                'verbose_name': 'Submit button',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='TextareaField',
            fields=[
            ],
            options={
                'verbose_name': 'Text field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='TimeField',
            fields=[
            ],
            options={
                'verbose_name': 'Date field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
        migrations.CreateModel(
            name='UrlField',
            fields=[
            ],
            options={
                'verbose_name': 'URL field',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djangocms_forms.formfield',),
        ),
    ]
