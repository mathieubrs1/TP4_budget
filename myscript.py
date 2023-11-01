import os

bad_revision = "c1a4be04b972b6c17db242fc37752ad517c29402"
good_revision = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

start_command = f'git bisect start {bad_revision} {good_revision}'

run_command = 'git bisect run python manage.py test'

reset_command = 'git bisect reset'

os.system(start_command)
os.system(run_command)
os.system(reset_command)