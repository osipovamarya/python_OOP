class EmailVerificationPage:

    attributetest = 'attributetest'

    def set_value(koshka, value):
        koshka.attributetest = value


def test_1(page):
    # print(EmailVerificationPage.__dict__)
    # print(EmailVerificationPage.attributetest)
    # print(getattr(EmailVerificationPage, 'attributetest'))
    # EmailVerificationPage.attributetest = {1}
    # print(EmailVerificationPage.attributetest)
    # setattr(EmailVerificationPage, 'attributetest', '1')
    # print(EmailVerificationPage.__dict__)
    # del EmailVerificationPage.attributetest
    # print(EmailVerificationPage.__dict__)
    # delattr(EmailVerificationPage, 'attributetest')
    example = EmailVerificationPage(page)
    example.set_value('1111')
    print(example.__dict__)
