An example of how file authentication can be implemented. To log in, the __user can__ either __enter username/password or drag and drop__ an authentication __file__.

![Figure](../master/fileauth.png?raw=true)

You can generate a new authentication file with the “makeauthfile” management command:

    python manage.py makeauthfile [user_id] [filename]

For example:

    python manage.py makeauthfile 1 key.txt
