[1mdiff --git a/e_commerce/db.sqlite3 b/e_commerce/db.sqlite3[m
[1mindex 1425634..cfe0c1c 100644[m
Binary files a/e_commerce/db.sqlite3 and b/e_commerce/db.sqlite3 differ
[1mdiff --git a/e_commerce/e_commerce_app/__pycache__/models.cpython-311.pyc b/e_commerce/e_commerce_app/__pycache__/models.cpython-311.pyc[m
[1mindex 44f7522..03c68ae 100644[m
Binary files a/e_commerce/e_commerce_app/__pycache__/models.cpython-311.pyc and b/e_commerce/e_commerce_app/__pycache__/models.cpython-311.pyc differ
[1mdiff --git a/e_commerce/e_commerce_app/models.py b/e_commerce/e_commerce_app/models.py[m
[1mindex e7d1e7a..91c4524 100644[m
[1m--- a/e_commerce/e_commerce_app/models.py[m
[1m+++ b/e_commerce/e_commerce_app/models.py[m
[36m@@ -16,6 +16,7 @@[m [mclass Product(models.Model):[m
     """The different products being sold on the store"""[m
     category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)[m
     heading = models.CharField(max_length=255)[m
[32m+[m[32m    cost = models.DecimalField(max_digits=6, decimal_places=2)[m
     text = models.TextField()[m
     date_added = models.DateTimeField(auto_now_add=True)[m
     image = models.ImageField(upload_to='images/', blank=True, null=True)[m
