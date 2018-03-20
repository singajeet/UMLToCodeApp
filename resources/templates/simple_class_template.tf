{#
    Name: simple_class_template
    Description: Template for generating an simple class
    Author: Ajeet Singh
#}
#-- start class --
class {{ class_name }} ({{ inherits|default('object') }}):
    """{{ Description|default('No Description') }}

    {%- if example %}}
    Example:
        {{ example }}
    {% endif %}

    """

    #-- default constructor --
{% if constructors -%}
    {% if '0' is in constructors %}
        def __init__(self):
            """{{ constructors['0']['description'] }}

            """
        {#{% if fields %}
            {% for field, fd in fields.items() %}
                {% if fd.type == 'string' %}
            self.{{ field }} = '{{ fd.default|default('') }}'
                {% else %}
            self.{{ field }} = None
                {% endif %}
            {% endfor %}
        {% endif %}#}
    {%- endif %}
{%- endif %}
#-- end class --
{#
{% if args is not None %}
    Args:
    {% for arg, arg_details in args.items() %}
        {{ arg }} ({{ arg_details.type }}): {{ arg_details.description }} ({{ arg_details.optional }})
    {% endfor %}
{% endif %}

    Returns:
        {{ return_details }}
#}
