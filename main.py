from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route('/post/category')
def post_category():
    return render_template("post_category.html",
                           categories_list=db.getCategories(),
                           post_numbers = db.GetCategoriesByQuantity()[0])


@app.route('/post/category/<id>', methods =["GET", "POST"])
def all_posts_in_category(id):

    if request.method == "POST":
        post_text = request.form.get("text")
    
        if len(post_text) > 0:
            db.addPost(id, post_text)
            return redirect(f'/post/category/{id}')

    return render_template("post_in_category.html",
                           posts_list=db.GetPostsInCategory(id),
                           category_name = db.GetCategoriesById(id)[0]
                           )

@app.route("/post/view")
def post_view():
    return render_template('post_view.html',posts_list=db.getPosts())

@app.route("/about")
def about():
    return render_template('base.html')

@app.route("/post/delete/<id>")
def delete_post(id):
    db.deletePost(id)
    return redirect("/post/view")


app.run(debug = True, host = '0.0.0.0')