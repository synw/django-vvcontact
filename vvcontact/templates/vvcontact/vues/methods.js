{% load i18n %}
loadContactForm: function() {
	action = function(data) {
		app.flush();
		app.contactForm = data;
		app.activate("contact");
		document.title = "{% trans 'Contact' %}";
	}
	this.loadData("{% url 'contact-rest' %}", action);
},
postContactForm: function() {
	var url = "{% url 'contact-rest' %}";
	var form = document.getElementById("contact_form");
	var frm = this.serializeForm(form);
	function error(err) {
		console.log(err)
	}
	function action(response) {
		if (response.data.error != 0) {
			app.pageContent = "<h1>Error sending email</h1>";
			return
		}
		app.pageContent = response.data.content;
		app.flush();
		app.activate("pageContent");
		document.title = "{% trans 'Contact' %}";
	}
	this.postForm(url, frm, action, error, frm.csrfmiddlewaretoken)
},