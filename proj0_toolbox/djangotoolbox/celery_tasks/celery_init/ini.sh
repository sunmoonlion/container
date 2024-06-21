sudo bash -c 'cat <<EOF > /etc/systemd/system/celery.service
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=forking
User=zym
Group=zym
WorkingDirectory=/home/zym/container/proj0_toolbox/djangotoolbox
ExecStart=/home/zym/anaconda3/envs/django/bin/celery multi start worker1 -A celery_tasks.main -l info
ExecStop=/home/zym/anaconda3/envs/django/bin/celery multi stopwait worker1
ExecReload=/home/zym/anaconda3/envs/django/bin/celery multi restart worker1 -A celery_tasks.main -l info
Environment=PYTHONPATH=/home/zym/container/proj0_toolbox/djangotoolbox
Environment=DJANGO_SETTINGS_MODULE=djangotoolbox.settings.dev

[Install]
WantedBy=multi-user.target
EOF'
