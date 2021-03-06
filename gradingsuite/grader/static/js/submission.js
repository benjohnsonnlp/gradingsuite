// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function () {
    $('.filelink').click(function () {
        assignment_id = $(this).attr("assignment");
        file = $(this).attr("file");
        submission = $(this).attr("submission");
        $.post("file_contents", {
            csrfmiddlewaretoken: csrftoken,
            csrf_token: csrftoken,
            filename: file,
            submission: submission,
        }, function (result) {
            //$('#editor').text(result);
            var editor = ace.edit("editor");
            editor.setTheme("ace/theme/monokai");
            editor.session.setMode("ace/mode/python");
            editor.setValue(result);
        });
    });

    $('#additive').click(function () {
        if (confirm("Changing grading mode will modify all current grades.  Continue?")) {
            $('.grade-input').each(function () {
                $(this).attr("value", 0);
            });
        }
    });

    $('#subtractive').click(function () {
        if (confirm("Changing grading mode will modify all current grades.  Continue?")) {
            $('.grade-input').each(function () {
                $(this).attr("value", $(this).attr('max-value'));
            });
        }
    });
});