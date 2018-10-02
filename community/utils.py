from django.core.mail import send_mail

class Sendmail():
    def send(email,name,postcode,mylng,homeland,overseas,noneng,first_name,second_name,third_name,forth_name,
                 first_per,second_per,third_per,forth_per,kindergarten,primary,secondary,p12,mental,
                 dental,gp,pharmacy,allied,complementary,disability,residential):
        message = """<html>
                             <head>
                             <style>
                                table {
                                    border-collapse: collapse;
                                }
                                
                                table, td, th {
                                    border: 1px solid black;
                                    text-align: center;
                                }
                            </style>
                             </head>
                             <body>
                             <p>Hello,</p>
                             
                             <p>Thank you for using our service. For information of other suburbs please click <a href="vic-migrant-health.com">here</a>.
                             <br>
                             <div>
                             <table>
                                <thead>
                                    <tr>
                                        <th></th>
                                        """
        for suburb_name in name:
            message = message + "<th>" + suburb_name + "</th>"
        message = message + """
                                    </tr>
                                </thead>
                                <tbody>
                                """
        message = message + """
                                    <tr>
                                        <td>Postcode</td>
                                    """
        for suburb_postcode in postcode:
            message = message + """<td>""" + str(suburb_postcode) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>People Speaking """ + mylng + """</td>
                                    """
        for suburb_homeland in homeland:
            message = message + """<td>""" + str(suburb_homeland) + """%</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Born overseas</td>
                                    """
        for suburb_overseas in overseas:
            message = message + """<td>""" + str(suburb_overseas) + """%</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Non-English speakers</td>
                                    """
        for suburb_noneng in noneng:
            message = message + """<td>""" + str(suburb_noneng) + """%</td>"""
        message = message + """
                                    </tr>
                                    <tr><td colspan="100%"><strong>Top 4 Cultural Groups</strong></td></tr>
                                    <tr>
                                        <td>1st cultural group</td>
                                    """
        for i in range(len(first_name)):
            message = message + """<td>""" + first_name[i] + '(' + str(first_per[i]) + """%)</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>2nd cultural group</td>
                                    """
        for i in range(len(second_name)):
            message = message + """<td>""" + second_name[i] + '(' + str(second_per[i]) + """%)</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>3rd cultural group</td>
                                    """
        for i in range(len(third_name)):
            message = message + """<td>""" + third_name[i] + '(' + str(third_per[i]) + """%)</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>4th cultural group</td>
                                    """
        for i in range(len(forth_name)):
            message = message + """<td>""" + forth_name[i] + '(' + str(forth_per[i]) + """%)</td>"""
        message = message + """
                                    </tr>
                                    <tr><td colspan="100%"><strong>Education Services (counts)</strong></td></tr>
                                    <tr>
                                        <td>Kindergarten</td>
                                    """
        for suburb_kindergarten in kindergarten:
            message = message + """<td>""" + str(suburb_kindergarten) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Primary school</td>
                                    """
        for suburb_primary in primary:
            message = message + """<td>""" + str(suburb_primary) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Secondary school</td>
                                    """
        for suburb_secondary in secondary:
            message = message + """<td>""" + str(suburb_secondary) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>P-12 school</td>
                                    """
        for suburb_p12 in p12:
            message = message + """<td>""" + str(suburb_p12) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr><td colspan="100%"><strong>Health Services (counts)</strong></td></tr>
                                    <tr>
                                        <td>Mental health service</td>
                                    """
        for suburb_mental in mental:
            message = message + """<td>""" + str(suburb_mental) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Dental site</td>
                                    """
        for suburb_dental in dental:
            message = message + """<td>""" + str(suburb_dental) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>General practice site</td>
                                    """
        for suburb_gp in gp:
            message = message + """<td>""" + str(suburb_gp) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Pharmacy site</td>
                                    """
        for suburb_pharmacy in pharmacy:
            message = message + """<td>""" + str(suburb_pharmacy) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Allied health site</td>
                                    """
        for suburb_allied in allied:
            message = message + """<td>""" + str(suburb_allied) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Complementary health site</td>
                                    """
        for suburb_complementary in complementary:
            message = message + """<td>""" + str(suburb_complementary) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Disability health service</td>
                                    """
        for suburb_disability in disability:
            message = message + """<td>""" + str(suburb_disability) + """</td>"""
        message = message + """
                                    </tr>
                                    <tr>
                                        <td>Residential aged care facility</td>
                                    """
        for suburb_residential in residential:
            message = message + """<td>""" + str(suburb_residential) + """</td>"""
        message = message + """</tr></table>"""
        message = message + """
                          <p>Regards,
                          <p><strong><i>Team RAWS</i></strong></p>
                          </body>
                          </html>"""
        send_mail('Suburbs details', 'Here is the message.', 'do-not-reply@vic-migrant-health.com',
                  [email], html_message=message, fail_silently=False)