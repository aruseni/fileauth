# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from fileauth.utils import generate_random_string, salted_hash

from django.contrib.auth.models import User

from fileauth.models import AuthenticationKey

class Command(BaseCommand):
    args = '<user_id> <filename>'
    help = 'Make a new authentication key for the specified user'

    def handle(self, *args, **options):
        if len(args) != 2 or not args[0].isdigit():
            raise CommandError('Invalid parameters')

        try:
            user = User.objects.get(id=args[0])
        except User.DoesNotExist:
            raise CommandError('User "%s" does not exist' % args[0])

        random_string = generate_random_string(128)

        AuthenticationKey.objects.create(
            key=salted_hash(random_string),
            user=user
        )

        f = open(args[1], "w")
        f.write(random_string)

        self.stdout.write("Created auth file %s" % args[1])
