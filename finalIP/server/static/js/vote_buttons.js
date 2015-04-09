/**
 * Created by Dylan on 30/03/2015.
 */
$(document).ready(function() {
    // Vote button event handler
    $("button.vote-button").click(function () {
        var voteWrapper = $(this).closest(".vote-button-wrapper");
        var itemId = voteWrapper.data('item-id');
        var votes = voteWrapper.find('.votes');
        var dislikes = voteWrapper.data('idea-dislikes');
        var isLike = $(this).hasClass('vote-button-like');
        var rating = isLike ? 1 : -1;
        if (!$(this).hasClass('active')) {
            // User added their rating
            $(this).addClass('active');
            var otherButton = $(this).siblings('button.vote-button');
            // Remove previous rating
            if (otherButton.hasClass('active')) {
                otherButton.removeClass('active');
                if (isLike) {
                    dislikes -= 1;
                } else {
                    likes -= 1;
                }
            }
            if (isLike) {
                likes += 1;
            } else {
                dislikes += 1;
            }
        } else {
            // User removed their rating
            $(this).removeClass('active')
            rating = 0;
            if (isLike) {
                likes -= 1;
            } else {
                dislikes -= 1;
            }
        }
        voteWrapper.find('.vote-likes').text(likes);
        voteWrapper.find('.idea-dislikes').text(dislikes);
        // Perform ajax call to rate the idea
        $.post('/idea/' + itemId + '/rate', {
            rating: rating
        }).done(function() {
            console.log("Successfully rated idea " + itemId);
        }).fail(function() {
            console.log("Failed to rate idea " + itemId);
        });
    });
});