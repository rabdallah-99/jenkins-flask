{% extends 'main.html' %}
{% block todo %}
    <h3>All Tasks:</h3>
    <p>
    {% for task in tasks %}
        Name: {{ task.name }} <br>
        Description: {{ task.description }} <br>
        <!--The following line checks if the task is completed or not-->
        {% if task.completed == True %}
        <!--The following line provides a text color based on if the task is complete or not-->
        Status: <span style="color: green">Completed</span>
        {% else %}
        Status: <span style="color: red">Incompleted</span>
        {% endif %}
        <br>
        <!--The following line provides a link to the url for the complete/incomplete function and also passes in the required argument 'name'-->
        <!--Any of these links could be made in to buttons by using the <button> tag-->
        <button><a href="{{ url_for('complete', name=task.name) }}">Complete</a></button>
        <button><a href="{{ url_for('incomplete', name=task.name) }}">Incomplete</a></button> 
        <br>
        <span><a href="{{ url_for('update', name=task.name) }}">Update</a></span>
        <span><a href="{{ url_for('delete', name=task.name) }}">Delete</a></span> 
        <br>
        <br>
    {% endfor %}
    </p>
{% endblock todo %}
