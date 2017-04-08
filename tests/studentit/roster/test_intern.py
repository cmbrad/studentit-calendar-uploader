from studentit.roster.intern import Intern

def test_intern_should_have_name_and_email_address():
    for key in ['name', 'email_address']:
        assert Intern.__dict__

