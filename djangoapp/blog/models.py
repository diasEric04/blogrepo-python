from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User
from utils.images import resize_image
from django_summernote.models import AbstractAttachment
from django.urls import reverse


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name

        current_file = str(self.file.name)
        super().save(*args, **kwargs)
        changed = False

        if self.file:
            changed = current_file != self.file

        if changed:
            resize_image(self.file, 900, True, 70)


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True,
        blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True,
        blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PageManager(models.Manager):
    def get_published(self):
        return self\
            .filter(is_published=True) \
            .order_by('-pk')


class Page(models.Model):
    objects = PageManager()
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default='',
        null=False, max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text='indica se o site vai poder ser acessado'
    )
    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:page', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 5)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostManager(models.Manager):
    def get_published(self):
        return self\
            .filter(is_published=True) \
            .order_by('-pk')


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    # objects = models.Manager()  # padrao
    objects = PostManager()

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default='',
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text='indica se o post vai poder ser acessado'
    )
    content = models.TextField()
    cover = models.ImageField(
        upload_to='post/%Y/%m/',
        blank=True, default=''
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text="exibe a imagem de capa tambem dentro do post"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )

    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 5)

        current_cover = str(self.cover.name)

        super().save(*args, **kwargs)

        changed = False

        if self.cover:
            changed = current_cover != self.cover

        if changed:
            resize_image(self.cover, 900, True, 70)
