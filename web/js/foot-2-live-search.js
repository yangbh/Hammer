/**
 * LiveSearch 1.0
 *
 * TODO
 */
var LiveSearch = {
	init: function (input, conf) {
		var config = {
			url: conf.url || false, 
			appendTo: conf.appendTo || 'after', 
			data: conf.data || {}
		};

		var appendTo = appendTo || 'after';

		input.setAttribute('autocomplete', 'off');

		// Create search container
		var container = document.createElement('div');

		container.id = 'live-search-' + input.name;

		container.classList.add('live-search');

		// Append search container
		if (appendTo == 'after') {
			input.parentNode.classList.add('live-search-wrap');
			input.parentNode.insertBefore(container, input.nextSibling);
		}
		else {
			appendTo.appendChild(container);
		}

		// Hook up keyup on input
		input.addEventListener('keyup', function (e) {
			if (this.value != this.liveSearchLastValue) {
				this.classList.add('loading');

				var q = this.value;

				// Clear previous ajax request
				if (this.liveSearchTimer) {
					clearTimeout(this.liveSearchTimer);
				}

				// Build the URL
				var url = config.url + q;

				if (config.data) {
					if (url.indexOf('&') != -1 || url.indexOf('?') != -1) {
						url += '&' + LiveSearch.serialize(config.data);
					}
					else {
						url += '?' + LiveSearch.serialize(config.data);
					}
				}

				// Wait a little then send the request
				var self = this;

				this.liveSearchTimer = setTimeout(function () {
					if (q) {
						$.ajax({
							method: 'get', 
							url: url, 
							success: function (data) {
								self.classList.remove('loading');
								container.innerHTML = data;
							}
						});
					}
					else {
						container.innerHTML = '';
					}
				}, 300);

				this.liveSearchLastValue = this.value;
			}
		});
	}, 

	// http://stackoverflow.com/questions/1714786/querystring-encoding-of-a-javascript-object
	serialize: function (obj) {
		var str = [];

		for(var p in obj) {
			if (obj.hasOwnProperty(p)) {
				str.push(encodeURIComponent(p) + '=' + encodeURIComponent(obj[p]));
			}
		}

		return str.join('&');
	}
};

if (typeof(jQuery) != 'undefined') {
	jQuery.fn.liveSearch = function (conf) {
		return this.each(function () {
			LiveSearch.init(this, conf);
		});
	};
}
