# Generated by Django 2.0 on 2018-06-03 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='default-college-code', max_length=50)),
                ('name', models.CharField(default='default-college-name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='default-course-code', max_length=50)),
                ('name', models.CharField(default='default-course-name', max_length=50)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='forum.College')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default-section', max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('type', models.CharField(choices=[('CL', 'college'), ('CE', 'course'), ('TR', 'teacher')], default='TR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='forum.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default-course-name', max_length=50)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='forum.College')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='forum.Course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='forum.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CL', 'closed'), ('OP', 'open')], default='OP', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('signature', models.TextField()),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='thread',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User'),
        ),
        migrations.AddField(
            model_name='thread',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Section'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='forum.User'),
        ),
        migrations.AddField(
            model_name='section',
            name='admin',
            field=models.ManyToManyField(related_name='admin', to='forum.User'),
        ),
        migrations.AddField(
            model_name='reply_reply',
            name='from_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyreply_from', to='forum.User'),
        ),
        migrations.AddField(
            model_name='reply_reply',
            name='reply_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyreply', to='forum.Reply'),
        ),
        migrations.AddField(
            model_name='reply_reply',
            name='to_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyreply_to', to='forum.User'),
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='forum.Thread'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='forum.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='forum.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='forum.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='forum.Section'),
        ),
        migrations.AddField(
            model_name='college',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='college', to='forum.Section'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice', to='forum.Section'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='forum.User'),
        ),
    ]
