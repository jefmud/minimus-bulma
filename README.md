Examples of Minimus and Bulma macros.

Bulma - an excellent lightweight framework

https://bulma.io/

https://github.com/jgthms/bulma

Jinja2 - the best templating system for Minimus (and Flask, Django, etc.)

https://jinja.palletsprojects.com/en/3.0.x/

Minimus - my easy framework, similar to Flask and Bottle

https://github.com/jefmud/minimus

These are files I use to test Minimus and make developmnet super easy with Bulma.

Here's an example of its usage.  If anyone finds it useful, great!  Or if you have some improvements please, please let me know.

```html
{% extends 'utility/base.html' %}
{% from 'utility/macros.html' import button, field, ckeditor, checkbox %}

{% block content %}
<form>
  {{ field("mytitle", "Title", fields.mytitle, pre) }}
  {{ field("mysubtitle", "Subtitle", fields.mysubtitle) }}
  {{ field("author", "Author", fields.author) }}
  {{ checkbox("is_published", "Published", fields.is_published) }}
  {{ ckeditor("content", "Content", fields.content) }}
  {{ button("save", "Save", category="is-info") }}
</form>
{% endblock %}
```

