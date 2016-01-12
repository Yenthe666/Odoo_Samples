(function() {
    function demo_alert(view) {
        window.setTimeout(function() {

            var active_view = view.action_manager.inner_widget.active_view;
            if (typeof(active_view) != 'undefined'){
                var controller = view.action_manager.inner_widget.views[active_view].controller;
                var action = view.action_manager.inner_widget.action;
                if (active_view == "form" && controller.model == "static.resource.demo"){
                    alert('hi there!')
                }
            }
	demo_alert(view);
        }, 5000);
    }

    openerp.web.WebClient.include({
        start: function() {
            this._super();
            demo_alert(this);
        },
    });
})();

