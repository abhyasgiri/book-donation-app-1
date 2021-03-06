from application import app, db
from application.models import Books, Shops
from application.forms import BookForm, ShopForm, LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, flash

@app.route("/")
@app.route("/home")
def home():
    all_shops = Shops.query.all()
    all_books = Books.query.all() 
    return render_template("index.html", title="Home", all_books=all_books, all_shops=all_shops)

@app.route("/createshop", methods = ["GET", "POST"])
def createshop():
    form = ShopForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_shop = Shops(shop_name=form.shop_name.data, location=form.location.data)
            db.session.add(new_shop)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create a shop", form=form)

@app.route("/create_book/<int:shop_id>/<int:user_id>", methods = ["GET", "POST"])
def create_book(shop_id, user_id):
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_book = Books(book_title=form.book_title.data, shop_id=shop_id, user_id=user_id)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add_book.html", title="Create a book", shop_id=shop_id, user_id=user_id, form=form)

@app.route("/update-shop/<int:id>", methods = ["GET", "POST"])            
def update_shop(id):
    form = ShopForm()
    shop = Shops.query.filter_by(id=id).first()
    if request.method == "POST":
        shop.shop_name = form.shop_name.data
        shop.location = form.location.data
        db.session.commit()
        flash("Shop updated")
        return redirect(url_for("home"))

    return render_template("update_shop.html", form=form, title="Update Shop", shop=shop)

#@app.route("/register", methods=['GET', 'POST'])
#def register():
#    form = RegistrationForm()
#   if form.validate_on_submit():
#        flash(f'Profile created for {form.username.data}!', 'Successful')
#        return redirect(url_for('home'))
#    return render_template('register.html', title='Register', form=form)

#@app.route("/login", methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        if form.email.data == 'admin@donationapp.com' and form.password.data == 'password':
#            flash('You have been logged in!', 'success')
#            return redirect(url_for('home'))
#        else:
#            flash('Login Unsuccessful. Please check username and password', 'danger')
#    return render_template('login.html', title='Login', form=form)


@app.route("/delete-shop/<int:id>", methods = ["GET"])
def delete_shop(id):
    shop = Shops.query.filter_by(id=id).first()
    db.session.delete(shop)
    db.session.commit()
    flash("Deleted shop")
    return redirect(url_for("home")) 

