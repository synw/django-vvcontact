{% load i18n %}
page('/contact/', function(ctx, next) { app.loadChunk('{% url "contact-rest" %}', "{% trans 'Contact' %}") } );
page('/contact/ok/', function(ctx, next) { app.loadChunk('{% url "contact-ok" %}', "{% trans 'Mail sent' %}") } );