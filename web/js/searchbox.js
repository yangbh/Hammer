// Author: Ryan Heath
// http://rpheath.com

(function($) {
  $.searchbox = {}
  
  $.extend(true, $.searchbox, {
    settings: {
      url: '/search',
      param: 'query',
      dom_id: '#results',
      delay: 100,
      loading_css: '#loading'
    },
    
    loading: function() {
      $($.searchbox.settings.loading_css).show()
    },
    
    resetTimer: function(timer) {
      if (timer) clearTimeout(timer)
    },
    
    idle: function() {
      $($.searchbox.settings.loading_css).hide()
    },
    
    process: function(terms) {
      var path = $.searchbox.settings.url.split('?'),
        query = [$.searchbox.settings.param, '=', terms].join(''),
        base = path[0], params = path[1], query_string = query
      
      if (params) query_string = [params.replace('&amp;', '&'), query].join('&')
      
      $.get([base, '?', query_string].join(''), function(data) {
        $($.searchbox.settings.dom_id).html(data)
      })
    },
    
    start: function() {
      $(document).trigger('before.searchbox')
      $.searchbox.loading()
    },
    
    stop: function() {
      $.searchbox.idle()
      $(document).trigger('after.searchbox')
    }
  })
  
  $.fn.searchbox = function(config) {
    var settings = $.extend(true, $.searchbox.settings, config || {})
    
    $(document).trigger('init.searchbox')
    $.searchbox.idle()
    
    return this.each(function() {
      var $input = $(this)
      
      $input
      .focus()
      .ajaxStart(function() { $.searchbox.start() })
      .ajaxStop(function() { $.searchbox.stop() })
      .keyup(function() {
        if ($input.val() != this.previousValue) {
          $.searchbox.resetTimer(this.timer)

          this.timer = setTimeout(function() {  
            $.searchbox.process($input.val())
          }, $.searchbox.settings.delay)
        
          this.previousValue = $input.val()
        }
      })
    })
  }
})(jQuery);