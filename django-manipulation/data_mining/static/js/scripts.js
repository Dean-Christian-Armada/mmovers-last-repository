<<<<<<< HEAD
$(document).ready(function() {;
	$(".add-btn").click(function(){
		$('#dialog').dialog('open');
	});
	$(".update-form").click(function(){
		id = $(this).attr('data-catid');	
		$.get(update_form, { update_id: id }, function(data){
			$('#update-dialog').html(data);
		});
		setTimeout(function(){ $('#update-dialog').dialog('open'); }, 300);
	});
	$(".view-cert").click(function(){
		width = 900; height = 600;
		id = $(this).attr('data-catid');
		$.get(cert_url, { id: id }, function(data){
			$('#view-cert').html(data);
		});
		setTimeout(function(){ $('#view-cert').dialog('open'); }, 300);

		$( "#view-cert" ).dialog({
			autoOpen: false,
			modal: true,
			width: width,
			height: height,
			closeOnEscape: true,
			draggable: false,
		});
	});
	$(".view-cert-info").click(function(){
		width = 'auto'; height = 'auto';
		id = $(this).attr('data-catid');
		info = "info";
		$.get(cert_url, { id: id, info: info }, function(data){
			$('#view-cert').html(data);
		});
		setTimeout(function(){ $('#view-cert').dialog('open'); }, 300);
		$( "#view-cert" ).dialog({
			autoOpen: false,
			modal: true,
			width: width,
			height: height,
			closeOnEscape: true,
			draggable: false,
		});
	});
	$(".delete-btn").click(function(){
		id = $(this).attr('data-catid');
		$.get(delete_url, { id: id }, function(data){
			$('.members').html(data);
		});
	});
	$(".restore-btn").click(function(){
		id = $(this).attr('data-catid');
		$.get(restore_url, { id: id }, function(data){
			$('.members').html(data);
		});
	});
	$(".recycle-btn").click(function(){
		id = $(this).attr('data-catid');
		$.get(trash_url, { id: id }, function(data){
			$('.members').html(data);
		});
	});
	$( "#dialog" ).dialog({
		autoOpen: bool,
		modal: true,
		width: 'auto',
		closeOnEscape: true,
		draggable: false,
	});	
	$( "#update-dialog" ).dialog({
		autoOpen: false,
		modal: true,
		width: 'auto',
		closeOnEscape: true,
		draggable: false,
	});
	$( "#view-cert" ).dialog({
		autoOpen: false,
		modal: true,
		closeOnEscape: true,
		draggable: false,
	});
	$('#search').keyup(function(){
		name = $(this).val();
		$.get(search_url, { name: name }, function(data){
			$('.members').html(data)
		});
	});
	$('table.table td').click(function(){
		value = $(this).text();
		selector = $(this).index();
		name = $(this).siblings('td:nth-child(3)').text();
		var update = $( "#update-dialog" ).dialog({
			title: "Updating "+name,
		});
		var cert = $( "#view-cert" ).dialog({
			title: name,
		});
	});

});
=======
$(document).ready(function() {;$(".add-btn").click(function(){$('#dialog').dialog('open');});$(".update-form").click(function(){id = $(this).attr('data-catid');	$.get(update_form, { update_id: id }, function(data){$('#update-dialog').html(data);});setTimeout(function(){ $('#update-dialog').dialog('open'); }, 300);});$(".view-cert").click(function(){width = 900; height = 600;id = $(this).attr('data-catid');$.get(cert_url, { id: id }, function(data){$('#view-cert').html(data);});setTimeout(function(){ $('#view-cert').dialog('open'); }, 300);$( "#view-cert" ).dialog({autoOpen: false,modal: true,width: width,height: height,closeOnEscape: true,draggable: false,});});$(".view-cert-info").click(function(){width = 'auto'; height = 'auto';id = $(this).attr('data-catid');info = "info";$.get(cert_url, { id: id, info: info }, function(data){$('#view-cert').html(data);});setTimeout(function(){ $('#view-cert').dialog('open'); }, 300);$( "#view-cert" ).dialog({autoOpen: false,modal: true,width: width,height: height,closeOnEscape: true,draggable: false,});});$(".delete-btn").click(function(){id = $(this).attr('data-catid');$.get(delete_url, { id: id }, function(data){$('.members').html(data);});});$(".restore-btn").click(function(){id = $(this).attr('data-catid');$.get(restore_url, { id: id }, function(data){$('.members').html(data);});});$(".recycle-btn").click(function(){id = $(this).attr('data-catid');$.get(trash_url, { id: id }, function(data){$('.members').html(data);});});$( "#dialog" ).dialog({autoOpen: bool,modal: true,width: 'auto',closeOnEscape: true,draggable: false,});	$( "#update-dialog" ).dialog({autoOpen: false,modal: true,width: 'auto',closeOnEscape: true,draggable: false,});$( "#view-cert" ).dialog({autoOpen: false,modal: true,closeOnEscape: true,draggable: false,});$('#search').keyup(function(){name = $(this).val();$.get(search_url, { name: name }, function(data){$('.members').html(data)});});$('table.table td').click(function(){value = $(this).text();selector = $(this).index();name = $(this).siblings('td:nth-child(3)').text();var update = $( "#update-dialog" ).dialog({title: "Updating "+name,});var cert = $( "#view-cert" ).dialog({title: name,});});});
>>>>>>> deec45f1880fd8315cb85e307555269f5022d885
