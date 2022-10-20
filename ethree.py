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
        self.status = "not defined"


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
    role_id = db.Column(db.String(200), db.ForeignKey('roletype.role_id'), nullable=False)
    

    mActivity_re = db.relationship("ManagerActivity")
    pInvoice_re = db.relationship("PaymentInvoice", backref="payment_invoice")
    sInvoice_re = db.relationship("SaleInvoice")

    def __init__(self, employee_id, name, password,role_id):
        self.employee_id = employee_id
        self.name = name
        self.password = password
        self.role_id = role_id
        


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

    def __init__(self, total, customer_id, duration, remark_id, employee_id="NDAK ADA"):
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


# class RemarkType(db.Model):
#     __tablename__ = "remarktype"
#     remark_id = db.Column(db.String(200), primary_key=True)
#     description = db.Column(db.String(200), nullable=False)

#     sInvoice_re = db.relationship("SaleInvoice")

#     def __init__(self, remark_id, description):
#         self.remark_id = remark_id
#         self.description = description


class RoleType(db.Model):
    __tablename__ = "roletype"
    role_id = db.Column(db.String(200), primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    employee_re = db.relationship("Employee", backref="employee")

    def __init__(self, role_id, description):
        self.role_id = role_id
        self.description = description









# functions
# customer page stuffs
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


# @app.route('/')
# def dummy() :
#     return render_template("dummy.html")
    
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
    # cust = 
    # # session["cust_name"] = cust
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
        session["adminName"] = adminName
        # return redirect(url_for('cust'))

        found_admin = Employee.query.filter_by(name=adminName).first()
        if found_admin:
            session['password'] = found_admin.password
            if found_admin.role_id == 'a1':
                return redirect(url_for("dummy")) #admin sale page
            elif found_admin.role_id == 'a2':
                return redirect(url_for("dummy")) #admin finance page
            else:
                return redirect(url_for("dummy")) #admin manager page
        else:
           return redirect(url_for("loginadmin"))
    else:
        return render_template('loginadmin.html')


@app.route('/logout')
def logout(): 
    session.pop("customer_id", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # dummy data
        # newCust = Customer("Jason", "sersan an", "239123", "sdkaks")
        # db.session.add(newCust)
        # db.session.commit()

        # total, customer_id, duration, remark_id, employee_id="NDAK ADA"
        # newTran = SaleInvoice(2100000, "c-20221018180102", 3, "ACCEPTED")
        # db.session.add(newTran)
        # db.session.commit()


    app.run(debug=True)