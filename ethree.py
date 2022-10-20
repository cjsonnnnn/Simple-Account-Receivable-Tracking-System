from flask import Flask, redirect, request, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta
from uuid import uuid4

from traitlets import default

# init
app = Flask(__name__)
app.config['SECRET_KEY'] = "eThree"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/ethree'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create database models
class Customer(db.Model):
    __tablename__ = "customer"
    customer_id = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    tel_num = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    status = db.Column(db.String(200), nullable=False)

    sInvoice_re = db.relationship("SaleInvoice", backref="sale_invoice")
    mActivity_re = db.relationship("ManagerActivity", backref="manager_activity")

    def __init__(self, name, address, tel_num, password):
        self.customer_id = "c-" + datetime.now().strftime('%Y%m%d%H%M%S')
        self.name = name
        self.address = address
        self.tel_num = tel_num
        self.password = password
        self.status = "ACTIVE"


class ActivityType(db.Model):
    __tablename__ = "activitytype"
    activity_id = db.Column(db.String(200), primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    mActivity_re = db.relationship("ManagerActivity")

    def __init__(self, activity_id, description):
        self.activity_id = activity_id
        self.description = description


class Employee(db.Model):
    __tablename__ = "employee"
    employee_id = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    role = db.Column(db.String(200), nullable=False)
    

    mActivity_re = db.relationship("ManagerActivity")
    pInvoice_re = db.relationship("PaymentInvoice", backref="payment_invoice")
    sInvoice_re = db.relationship("SaleInvoice")

    def __init__(self, name, password, role):
        if role == "admin_sale":
            self.employee_id = "s-" + datetime.now().strftime('%Y%m%d%H%M%S')
        elif role == "admin_finance":
            self.employee_id = "f-" + datetime.now().strftime('%Y%m%d%H%M%S')
        elif role == "manager":
            self.employee_id = "m-" + datetime.now().strftime('%Y%m%d%H%M%S')
        self.name = name
        self.password = password
        self.role = role
        

class ManagerActivity(db.Model):
    __tablename__ = "manager_activity"
    manager_activity_id = db.Column(db.String(200), nullable=False, primary_key=True)
    employee_id = db.Column(db.String(200), db.ForeignKey('employee.employee_id'), nullable=False)
    customer_id = db.Column(db.String(200), db.ForeignKey('customer.customer_id'), nullable=False)
    activity_id = db.Column(db.String(200), db.ForeignKey('activitytype.activity_id'), nullable=False)

    def __init__(self, employee_id, customer_id, activity_id):
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.activity_id = activity_id


class SaleInvoice(db.Model):
    __tablename__ = "sale_invoice"
    invoice_id = db.Column(db.String(200), primary_key=True)
    sale_date = db.Column(db.String(200), nullable=False)
    payment_date = db.Column(db.String(200), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.String(200), db.ForeignKey('employee.employee_id'))
    customer_id = db.Column(db.String(200), db.ForeignKey('customer.customer_id'), nullable=False)
    remark_id = db.Column(db.String(200), nullable=False)

    pInvoice_re = db.relationship("PaymentInvoice")

    def __init__(self, total, customer_id, duration, remark_id, employee_id="NULL"):
        self.invoice_id = "inv-" + datetime.now().strftime('%Y%m%d%H%M%S')
        self.sale_date = datetime.now().strftime('%Y-%m-%d')
        self.payment_date = (datetime.now() + timedelta(days=duration*30)).strftime('%Y-%m-%d')   # will be revised
        self.total = total
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.remark_id = remark_id


class PaymentInvoice(db.Model):
    __tablename__ = "payment_invoice"
    payment_invoice_id = db.Column(db.String(200), nullable=False, primary_key=True)
    invoice_id = db.Column(db.String(200), db.ForeignKey('sale_invoice.invoice_id'), nullable=False)
    employee_id = db.Column(db.String(200), db.ForeignKey('employee.employee_id'), nullable=False)

    def __init__(self, invoice_id, employee_id):
        self.invoice_id = invoice_id
        self.employee_id = employee_id









# functions
# customer page stuffs
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/cust")
def custPage():
    curCust = session["customer_id"]
    return render_template("custPage.html", custTransactions=SaleInvoice.query.filter_by(customer_id=curCust).order_by(SaleInvoice.sale_date.asc()).all())

@app.route("/addtransaction")
def newTransaction():
    return render_template("addtransaction.html")

@app.route("/addtransactionprocess", methods=["POST"])
def newtransactionProcess():
    total = int(request.form.get("nominal"))
    curCust = session["customer_id"]
    duration = int(request.form.get("durR"))
    remark_id = "WAITING"

    # process the interest
    if duration == 1:
        total += (total*0.1)
    elif duration == 3:
        total += (total*0.18)
    elif duration == 6:
        total += (total*0.23)
    else:
        total += (total*0.27)

    # add new transaction
    newTran = SaleInvoice(total, curCust, duration, remark_id)
    db.session.add(newTran)
    db.session.commit()

    # go back to cust page
    return redirect(url_for('custPage'))



# login and signup stuffs
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        cust = request.form['name']

        found_cust = Customer.query.filter_by(name=cust).first()
        if found_cust:
            if request.form['password'] == found_cust.password:
                session["customer_id"] = found_cust.customer_id
                return redirect(url_for("custPage"))
        
        return redirect(url_for("signup"))
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # found_cust = Customer.query.filter_by(name=request.form['name']).first() 
    if request.method == 'POST':
        cust = request.form['name']
        found_cust = Customer.query.filter_by(name=cust).first() 
        if found_cust:
            return render_template('signup.html')
        else:
            cust_name = request.form['name']
            address = request.form['address']
            tel_num = request.form['tel_num']
            password = request.form['password']
            new_cust = Customer(cust_name,  address, tel_num, password)
            db.session.add(new_cust)
            db.session.commit()
            return redirect(url_for("login"))
    else:
        return render_template('signup.html')

@app.route('/loginadmin', methods=['GET', 'POST'])
def loginadmin(): 
    if request.method == 'POST':
        adminName = request.form['name']

        found_admin = Employee.query.filter_by(name=adminName).first()
        if found_admin:
            if request.form["password"] == found_admin.password:
                if found_admin.role == 'admin_sale':
                    session["admin_sale_id"] = found_admin.employee_id
                    return redirect(url_for("get_invoice_admin")) #admin sale page
                elif found_admin.role == 'admin_finance':
                    session["admin_finance_id"] = found_admin.employee_id
                    return redirect(url_for("get_invoice_sale")) #admin finance page
                else:
                    session["manager_id"] = found_admin.employee_id
                    return redirect(url_for("signup")) #admin manager page

        return redirect(url_for("loginadmin"))
    else:
        return render_template('loginadmin.html')

@app.route('/logout')
def logout(): 
    session.pop("customer_id", None)
    session.pop("admin_sale_id", None)
    session.pop("admin_finance_id", None)
    session.pop("manager_id", None)
    return redirect(url_for("login"))



# admin sale and admin finance stuffs
@app.route("/sales", methods=["GET", "POST"])
def get_invoice_admin():
    a = SaleInvoice.query.all()
    invoice_id = []
    sale_date = []
    payment_date = []
    total = []
    employee_id = []
    customer_id = []
    remark = []

    if request.form != None:
        for i in request.form.keys():
            b = SaleInvoice.query.filter_by(invoice_id=i).first()
            b.remark_id = request.form[i]
            db.session.commit()

    for i in a:
        invoice_id.append(i.invoice_id)
        sale_date.append(i.sale_date)
        payment_date.append(i.payment_date)
        total.append(i.total)
        employee_id.append(i.employee_id)
        customer_id.append(i.customer_id)
        remark.append(i.remark_id)

    for i in range(len(remark)):

        # replace hardik with shardul
        if remark[i] == "0":
            remark[i] = "Not Registered"

        # replace pant with ishan
        elif remark[i] == "1":
            remark[i] = "Have Not Paid"

        elif remark[i] == "2":
            remark[i] = "Paid"

    table = []
    for i in range(len(invoice_id)):
        table.append(
            [
                invoice_id[i],
                sale_date[i],
                payment_date[i],
                total[i],
                employee_id[i],
                customer_id[i],
                remark[i],
                invoice_id[i],
            ]
        )

    return render_template("admin_sale.html", data=table)

@app.route("/finance", methods=["GET", "POST"])
def get_invoice_sale():
    a = SaleInvoice.query.all()
    invoice_id = []
    sale_date = []
    payment_date = []
    total = []
    employee_id = []
    customer_id = []
    remark = []

    param = dict()
    for i in request.form.keys():
        param[i] = request.form.getlist(i)

    for i in param.keys():
        if param[i][0] != "":
            b = SaleInvoice.query.filter_by(invoice_id=i).first()
            b.remark_id = param[i][1]
            b.payment_date = param[i][0]
            db.session.commit()
        else:
            b = SaleInvoice.query.filter_by(invoice_id=i).first()
            b.remark_id = param[i]
            db.session.commit()

    for i in a:
        invoice_id.append(i.invoice_id)
        sale_date.append(i.sale_date)
        payment_date.append(i.payment_date)
        total.append(i.total)
        employee_id.append(i.employee_id)
        customer_id.append(i.customer_id)
        remark.append(i.remark_id)

    notdone = []

    for i in range(len(remark)):

        # replace hardik with shardul
        if remark[i] == "0":
            notdone.append(i)

        # replace pant with ishan
        elif remark[i] == "1":
            remark[i] = "Have Not Paid"

        elif remark[i] == "2":
            remark[i] = "Paid"

    table = []
    for i in range(len(invoice_id)):
        table.append(
            [
                invoice_id[i],
                sale_date[i],
                payment_date[i],
                total[i],
                employee_id[i],
                customer_id[i],
                remark[i],
                invoice_id[i],
            ]
        )

    table = [j for i, j in enumerate(table) if i not in notdone]

    return render_template("admin_finance.html", data=table)

@app.route("/blacklist", methods=["GET", "POST"])
def blacklist():
    a = Customer.query.filter_by(status="Blacklisted").all()

    cust_id = []
    name = []
    address = []
    tel_num = []
    status = []

    if request.form != None:
        for i in request.form.keys():
            b = Customer.query.filter_by(customer_id=i).first()
            b.status = request.form[i]
            db.session.commit()

    for i in a:
        cust_id.append(i.customer_id)
        name.append(i.name)
        address.append(i.address)
        tel_num.append(i.tel_num)
        status.append(i.status)

    table = []
    for i in range(len(cust_id)):
        table.append(
            [cust_id[i], name[i], address[i], tel_num[i], status[i], cust_id[i]]
        )

    return render_template("blacklist.html", data=table)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # dummy data
        # newAdmin = Employee("caleb", "cal009", "admin_sale")
        # db.session.add(newAdmin)
        # db.session.commit()

        # total, customer_id, duration, remark_id, employee_id="NDAK ADA"
        # newTran = SaleInvoice(2100000, "c-20221018180102", 3, "ACCEPTED")
        # db.session.add(newTran)
        # db.session.commit()


    app.run(debug=True)