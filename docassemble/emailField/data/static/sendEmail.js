// Uses custom button to send email. Hope this is only instantiated once
$('.send-email-button').click(function(){

  let message = 'We are trying to send the email to ' + val('email_address') + '.';
  flash(message, 'secondary');

  url_action_call( 'send_email_event',
    { address: val( 'email_address' ) },
    function email_attempted ( obj_or_html, result_as_text, response ) {
      console.log(response)
      if (response.status === 200) {
        flash( 'The email got sent to ' + obj_or_html.email_address + '!', 'success', true );
      } else {
        let message = 'Sorry about this, but the email didn\'t get sent. Try giving it some time and then try again.';
        flash( message, 'danger', true );
        console.log( 'response:', response );
        url_action_call('log_action_to_docassemble', {
          message: response.body  // log this object to see its props
        });
      }
  });  // ends url_action_call and callback
});
