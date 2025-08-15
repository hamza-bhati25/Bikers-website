@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
