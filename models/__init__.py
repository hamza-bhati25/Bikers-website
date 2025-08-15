class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
