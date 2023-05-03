$(document).ready(()=>{
	$('INPUT#btn_translate').click(()=>{
		const lang_code = $('INPUT#language_code').val();
		$.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang_code}`, (data)=>{
			$('DIV#hello').text(data.hello);
		});

	})
});

