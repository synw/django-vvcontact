{% load i18n %}
loadContactForm: function() {
	action = function(data) {
		app.flush();
		app.contactForm = data;
		app.activate("contact");
		document.title = "{% trans 'Contact' %}";
	}
	this.loadRawData("{% url 'contact-rest' %}", action);
},