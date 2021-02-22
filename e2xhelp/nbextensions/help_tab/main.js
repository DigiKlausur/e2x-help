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
        $('#tabs').append(
            $('<li/>').append(
                $('<a/>')
                .attr('href', Jupyter.notebook_list.base_url + 'e2xhelp/shared/cheatsheet/python_basics_cheatsheet_and_plot.pdf')
                .attr('target', '_blank')
                .text('Shared test')
            )
        );
    };

    return {
        load_ipython_extension: load
    }

});