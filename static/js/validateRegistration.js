// alert($('button[type="submit"]').text());
(function(){
    var app = {
        initialize:function(){
            this.modules();
            this.setUpListeners();
        },
        modules: function(){},
        setUpListeners: function(){
            $('form').on('submit', app.submitForm);
        },
        submitForm: function(e){
            // e.preventDefault();
            if (app.validate($(this))){
                // alert('а вот на этом моменте форма должна отправляться через $.ajax, но я пока хз, куда ее отправлять')
                var a = 1
                return true;
            }
            return false;            
        },
        validate: function(form){
            // alert('validation started');
            var inputs = form.find("input"), 
                isValid = true,
                pass = form.find('[name="password"]'),
                passAgain = form.find('[name="passwordAgain"]');
            inputs.tooltip('hide');

            $.each(inputs, function(index, el){
                var input = $(el),
                    val = input.val();
                if (val.length==0) {
                    input.removeClass('border-success').addClass('border-danger');

                    input.tooltip({
                        trigger: 'manual',
                        placement: 'right',
                        title: 'Aizpidliet'
                    }).tooltip('show');

                    isValid = false;
                }
                else {
                    input.removeClass('border-danger').addClass('border-success');
                }
            });
            if (pass.val() != passAgain.val()){
                passAgain.removeClass('border-success').addClass('border-danger');
                alert("Paroles nesakrīt!");
                return false;
            }
            alert("На этом моменте валидация окончена, и он должен добавить tooltip'ы к input'ам, которые не прошли проверку (пустые или не совпадает пароль)");
            return isValid;
        }
    }
    app.initialize();
}());