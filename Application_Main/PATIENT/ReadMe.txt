Project Structure
	
	Application Main 
			- Application Main
					- url.py
						- All urls of the website
					- settings.py
						- Necessary Configuration
			- COMMON_APP
					- models.py
						- Receptionist
						- Appointment
						- HR
					- views.py
						- All Views Functions
			- DOCTER
					- models.py
						- Docter
						- Prescription2
			- media
					- All Patient Reports Stored Here
			- PATIENT
					- models.py
						- Patient
						- Invoice
			- static
					- Project Images
			- templates
					- All Templates
			- db.sqlite3
					- Stored Data
			- manage.py



How To Start Project ?
Download the zip file , unzip it and go to Application_Main Folder , open cmd at that location and run command "manage.py runserver" , Server will started , copy the location and open in browser.



Patient Login - Username=>Password
				Patient1=>1
				Patient2=>1
Docter Login -  Username=>Password
				Docter1=>1
				Docter2=>1
Receptionist Login -  Username=>Password
						r1=>ankit@98
HR Login -  Username=>Password
			hr1=>ankit@98



Functionalities

1. Patient can register himself , login , can see his/her appointment , invoice and payments he/she have done with dynamic generated invoice pdf , date and more info. He/She can see medical history (Prescrition given by the docter) as well.He/she can also manage his/her Profile or edit/update it.

2. Docter can regsiter himself , login , can able to see his/her own appoinments with patients , can able to create prescription , can see his/her last given prescription and Patient name dynamically removed after Prescription Given. He/she can also manage his/her Profile or edit/update it.

3. Receptionist can not register , can only login as per requirement. A Receptionist can see total appointments , appointments done , upcoming appointments . He/she can create appoitnment b/w docter and patient with time and date , after appointment he/she can also update paid and outstanding amount and can also update status pf appointment ,i.e,Pending or completed .He/she can create patient with complete details , outstanding and Paid amount.

4. HR can not register , can only login as per requirement. HR can see Total docters , Total Patients and On Duty Docters . He can config Docter Profile along with department , attendance , salary , status (active/inactive) and also remove docter.In accounting part he/she can send emails by clicking a button and mail will be sended with amount information on Patient email. He can see Consulation's information and dynamic generated invoice.