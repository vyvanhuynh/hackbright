'use strict';

/** ***** Functions & event handlers ****** */

function changeColor() {
  const colorChangeEls = $('.color-change');

  for (const el of colorChangeEls) {
    $(el).toggleClass('red');
  }
}

function validateNumber(evt) {
  evt.preventDefault();

  const numberInput = $('input[name="number"]');
  const userNum = Number(numberInput.val()); // typecast to num

  const formFeedback = $('#formFeedback');
  if (!userNum || userNum >= 10) {
    formFeedback.text('Please enter a smaller number');
  } else {
    formFeedback.text('You are good to go!');
  }
}

/** ***** Attach event handlers ****** */

$('.color-changer').on('click', changeColor);
$('.number-form').on('submit', validateNumber);
