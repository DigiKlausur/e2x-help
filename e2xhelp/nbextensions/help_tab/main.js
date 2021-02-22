define([
    'jquery',
    'base/js/utils',
    'base/js/namespace'
], function ($, utils, Jupyter) {

    'use strict';

    function get_tab() {
        let body = $('<div/>').attr('id', 'e2xhelp').addClass('tab-pane');
        let help = $('<div/>').attr('id', 'help');
        help.append($('<h4/>').append('General Help:'));
        let help_list = $('<ul/>');


        help_list.append($('<li/>').append($('<a/>')
            .attr('href', Jupyter.notebook_list.base_url + 'e2xhelp/base/html/en')
            .attr('target', '_blank')
            .append('E2X Help (English)')));
        help_list.append($('<li/>').append($('<a/>')
            .attr('href', Jupyter.notebook_list.base_url + 'e2xhelp/base/html/de')
            .attr('target', '_blank')
            .append('E2X Hilfe (Deutsch)')));
        body.append(help.append(help_list));

        let resources = $('<div/>').attr('id', 'resources');
        resources.append($('<h4/>').append('Additional Resources:'));
        body.append(resources);
        return body;
    }

    function load() {
        if (!Jupyter.notebook_list) {
            return;
        }
        $('.tab-content').append(get_tab());
        $('#tabs').append(
            $('<li/>').append(
                $('<a/>')
                .attr('href', '#e2xhelp')
                .attr('data-toggle', 'tab')
                .text('Help')
                .click(function (e) {
                    window.history.pushState(null, null, '#e2xhelp');
                    let url = utils.url_path_join(Jupyter.notebook_list.base_url, 'e2xhelp/api/files');
                    utils.ajax(url, {
                        type: 'GET',
                        dataType: 'json',
                        processData: false,
                        cache: false,
                        success: function(data, status, xhr) {
                            let links = $('<ul/>');
                            data.forEach(function(entry) {
                                links.append($('<li/>').append(
                                    $('<a/>')
                                    .attr('href', utils.url_path_join('e2xhelp/shared/', entry[1]))
                                    .append(entry[0])));
                            });
                            if (data.length > 0) {
                                $('#resources').append(links);
                            } else {
                                $('#resources').append('There are no additional resources!');
                            }

                        },
                        error: utils.log_ajax_error,
                    })

                })
            )
        );
    };

    return {
        load_ipython_extension: load
    }

});