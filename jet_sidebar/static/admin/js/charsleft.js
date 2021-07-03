$.fn.charsLeft = function (options) {
    console.log($);

    var defaults = {
        'source': 'input',
        'dest': '.count'
    }
    var options = $.extend(defaults, options);

    var calculate = function (source, dest, maxlength) {
        var remaining = source.val().length;
        dest.html(remaining);

        p = (remaining / maxlength) * 100;

        if (p > 80) {
            dest.addClass('red');
        }
    };

    this.each(function (i, el) {
        var maxlength = $(this).find('.maxlength').html();
        var dest = $(this).find(options.dest);
        var source = $(this).find(options.source);
        source.keyup(function () {
            calculate(source, dest, maxlength)
        });
        source.change(function () {
            calculate(source, dest, maxlength)
        });
    });
};
$(function () {
    $(".charsleft-input").charsLeft({
        'source': 'input',
        'dest': ".count"
    });
});
