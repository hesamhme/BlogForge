{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activativation 
{% endblock %}

{% block html %}
    {{token}}
{% endblock %}