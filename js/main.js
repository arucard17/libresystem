
// Pluging para pasar el form a un objeto JSON
  (function(a){a.fn.serializeFormJSON=function(){var c={},b=this.serializeArray();a.each(b,function(){if(c[this.name]){if(!c[this.name].push){c[this.name]=[c[this.name]]}c[this.name].push(this.value||"")}else{c[this.name]=this.value||""}});return c}})(jQuery);
 
// INicia cuando el documento este listo
$(document).on('ready',init);

function init(){
  $('#btn-enviar').on('click',sendData);
}

function sendData(){

  var data = {}
      ,form = $('#form-contacto').serializeFormJSON();

  for(var item in form){
    if(form[item] === ''){
      alert('Los campos no pueden estar vacios.')
      return false;
    }
  }

  data.url = '/sendmail';
  console.log(form);
  data.sendData = form;
  data.fun = function (data){
    data = jQuery.parseJSON(data);
    if(data.success){
      alert(data.msg);
      window.location.href = 'http://www.libressystem.appspot.com/'
    }else
      alert(data.error);
  } 

  send(data);

}

function send(data){
  $.ajax({
      type: 'POST',
      url: data.url,
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data.sendData),
      success: data.fun,
      processData: false
  });
}
