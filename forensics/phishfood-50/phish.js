var firstLoad = true;
$('#frame').on('load', function() {
    if (!firstLoad) {
        location.href = 'done.html';
    } else {
        // $('#frame').contents().find('div').click(function() {
        //     location.href = 'done.html';
        // });
    }
    firstLoad = false;
});

