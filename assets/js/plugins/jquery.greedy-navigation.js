/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');

var breaks = [];

function updateNav() {

  var availableSpace = $btn.hasClass('hidden') ? $nav.width() : $nav.width() - $btn.width() - 30;

  // The visible list is overflowing the nav
  if($vlinks.width() > availableSpace) {

    // Check if the last item is a language selector, if so, try the previous item
    var $lastItem = $vlinks.children().last();
    var $itemToMove = $lastItem;
    
    // If the last item contains a language selector, don't move it
    if($lastItem.find('.language-selector').length > 0) {
      // Try the previous item instead
      $itemToMove = $lastItem.prev();
      
      // If there's no previous item or it also contains a language selector, don't move anything
      if($itemToMove.length === 0 || $itemToMove.find('.language-selector').length > 0) {
        return; // Don't hide the language selector
      }
    }

    // Record the width of the list
    breaks.push($vlinks.width());

    // Move item to the hidden list
    $itemToMove.prependTo($hlinks);

    // Show the dropdown btn
    if($btn.hasClass('hidden')) {
      $btn.removeClass('hidden');
    }

  // The visible list is not overflowing
  } else {

    // There is space for another item in the nav
    if(availableSpace > breaks[breaks.length-1]) {

      // Move the item to the visible list
      $hlinks.children().first().appendTo($vlinks);
      breaks.pop();
    }

    // Hide the dropdown btn if hidden list is empty
    if(breaks.length < 1) {
      $btn.addClass('hidden');
      $hlinks.addClass('hidden');
    }
  }

  // Keep counter updated
  $btn.attr("count", breaks.length);

  // Recur if the visible list is still overflowing the nav
  if($vlinks.width() > availableSpace) {
    updateNav();
  }

}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();