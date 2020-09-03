define([
    'jquery',
    'base/js/namespace'
], function ($, Jupyter) {

    'use strict';

    function load() {
        if (!Jupyter.notebook_list) {
            return;
        }
        $('#tabs').append(
            $('<li/>').append(
                $('<a/>')
                .attr('href', Jupyter.notebook_list.base_url + 'e2xhelp/base/html/en')
                .attr('target', '_blank')
                .text('Help')
            )
        );
    };

    return {
        load_ipython_extension: load
    }

});