yam.ns('onboardie');

onboardie.App = yam.ctor('yam.onboardie.App', {

  init: function(){
    this.observeDOMEvents();
    this.bootNav();
    $('#firstName').focus();
  },

  bootNav: function(){
    var path = window.location.pathname;
    if(path === '/'){
      path = 'add';
    }
    else {
      path = path.substr(1);
    }
    var navItems = $('ul.nav li');
    var context = navItems.filter('.' + path);
    navItems.removeClass('active');
    context.addClass('active');

    if(onboardie[path]){
      var controller = new onboardie[path]();
    }

  },

  observeDOMEvents: function(){

    window.form = $('#addUser').submit(function(){ 
      if($(this).valid()){
        $('#myModal').modal(); 
        var vals = $(this).serialize();
        var deferred = $.post('/', vals);
        var alerts = $('.alert');
        deferred.success(function(){
          alerts.hide().filter('.alert-success').show(); 
        });
        deferred.error(function(e){
          alerts.hide().filter('.alert-error').show(); 
          //TODO move to success handler
        });
        $('#myModal').modal('hide');
      }
      return false;
    })

    window.form.validate();

    var ndaRow = $('#ndaRow');

    $('input[type=reset]').click(function(){
      $('label.error').hide();
      ndaRow.fadeOut();
    });

    $('#earlyAccess').click(function(){
      !!$(this).attr('checked') ?  ndaRow.fadeIn() : ndaRow.fadeOut();
      ndaRow.find(':checkbox').prop('checked', false);
    });

  }

});

onboardie.api_process = yam.ctor('yam.onboardie.process', {

  init: function(){
    this.timer = setInterval(yam.bind(this, this.poll), 1000);
  },

  poll: function(){

    var services = {
      "Google Apps": "google", 
      "One Login": "onelogin", 
      "yammer": "yammer"
    }

    $.get('/api_process_update', yam.bind(this, function(data){

      $.each(data, function(index, user){
        var userTable = $('#user-status-' + user.id);
        var service = services[user.account_name];
        var statusCell = userTable.find('tr.' + service + ' div.status');
        var newStatus = user.status.toLowerCase();
        statusCell.removeClass().addClass('status ' + newStatus);
      });

      if($('div.status').filter('.pending').length === 0){
        clearInterval(this.timer);
      }

    }));
  }
 
});

$(document).ready(function(){
  var app = new onboardie.App;
});

