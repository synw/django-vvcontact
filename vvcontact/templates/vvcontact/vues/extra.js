function postContactForm() {
	var url = "{% url 'contact-rest' %}";
	var arr = $("#contact_form").serializeArray();
	var frm = {};
	for (i=0;i<arr.length;i++) {
		var el = arr[i];
		frm[el.name] = el.value;
	}
	$.ajax({
	      type: 'POST',
	      contentType: "application/json; charset=utf-8",
	      url: url,
	      data: JSON.stringify(frm),
	      success: function (response) {
	    	  if (response.ok == 1) {
	    		  app.contactForm = "";
	    		  app.contactResp = true;
	    	  } else {
	    		  app.contactForm = "";
	    		  app.contactErr = true;
	    		  console.log("err");
	    	  }
	    	  
	      },
	      error: function(xhr, textStatus, error) {
	      	console.log("Error:");
	          console.log(xhr.statusText);
			    console.log(textStatus);
			    console.log(error);
			    app.contactErr = true;
			    app.activate(["contactErr"]);
	      }
	  })
}
$( document ).ready(function() {
	var frm = $('#contact_form');
	frm.submit(function (ev) {
		ev.preventDefault();
		ev.stopImmediatePropagation();
		postContactForm();
	  return false;
	});
});
