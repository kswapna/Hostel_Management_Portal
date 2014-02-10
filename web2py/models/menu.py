response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [(T('HOME'),URL('default','index')==URL(),URL('default','index'),[]),
]
response.complaint=[(T('COMPLAINT'),URL('default,complaint')==URL(),URL('default','complaint'),[]),]
response.search=[(T('SEARCH'),URL('default,search')==URL(),URL('default','search'),[]),]
response.enter_laptop_details=[(T('Laptop Records'),URL('default,enter_laptop_details')==URL(),URL('default','enter_laptop_details'),[]),]
response.laptop_out_details=[(T('Laptop Movement'),URL('default,laptop_out_details')==URL(),URL('default','laptop_out_details'),[]),]
response.student_out_details=[(T('Outing Details'),URL('default,student_out_details')==URL(),URL('default','student_out_details'),[]),]
response.vcomplaint=[(T('View Complaints'),URL('default,vcomplaint')==URL(),URL('default','vcomplaint'),[]),]
response.staff_vcomplaint=[(T('View Complaints'),URL('default,staff_vcomplaint')==URL(),URL('default','staff_vcomplaint'),[]),]
response.view_rooms=[(T('Room Vacancy'),URL('default,view_vacant_rooms')==URL(),URL('default','view_vacant_rooms'),[]),]
response.change_rooms=[(T('Room Vacancy'),URL('default,vacant_rooms')==URL(),URL('default','vacant_rooms'),[]),]
response.vmedical=[(T('Medical Requests'),URL('default,vmedical')==URL(),URL('default','vmedical'),[]),]
response.medical=[(T('Medical Requests'),URL('default,byroll')==URL(),URL('default','byroll'),[]),]
response.studentrules=[(T('Rules'),URL('default,studentrules')==URL(),URL('default','studentrules'),[]),]
response.rules=[(T('Edit Rules'),URL('default,rules')==URL(),URL('default','rules'),[]),]
response.editmedical=[(T('Edit Doctor Details '),URL('default,amedreq')==URL(),URL('default','amedreq'),[]),]


response.student=response.menu+response.complaint+response.view_rooms+response.medical+response.studentrules
response.staff=response.menu+response.staff_vcomplaint+response.vmedical+response.change_rooms+response.enter_laptop_details+response.student_out_details
response.admin=response.menu+response.vcomplaint+response.change_rooms+response.rules+response.editmedical
