$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const langCode = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
