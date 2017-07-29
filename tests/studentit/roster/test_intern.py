from studentit.roster.employee import Employee


def test_intern_should_have_name_and_email_address():
    for key in ['name', 'email_address']:
        assert Employee.__dict__
