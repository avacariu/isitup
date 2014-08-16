import datetime
import uuid

from flask import request, url_for, render_template, g, session, redirect, flash

from flask.ext.login import login_required, logout_user, current_user
from social.apps.flask_app import routes

from . import app, db, lm
from .models import User, Thing
from .forms import NewThingForm, EditThingForm

@lm.user_loader
def load_user(userid):
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():
    if g.user.is_authenticated():
        return redirect(url_for('things'))

    return render_template('index.html',
            title='Isitup?')

@app.route('/logout')
def logout():
    logout_user()
    flash("Bye!")
    return redirect(url_for('index'))

@app.route('/thing')
@login_required
def things():
    """Show a list of all things registered for this account."""
    def isitdown(timestamp, delta):
        dt_delta = datetime.timedelta(0, delta * 60)
        now = datetime.datetime.utcnow()

        if timestamp is None:
            return None
        elif now - timestamp < dt_delta:
            return False
        else:
            return True

    return render_template('things.html',
            title = 'your things',
            things = g.user.things,
            isitdown = isitdown)

@app.route('/thing/<uuid>', methods=['GET', 'POST'])
@login_required
def thing(uuid):
    """Show details for one thing.

    These will be stuff like last_request.
    """
    thing = Thing.query.filter_by(uuid=uuid).first()

    if not thing or thing.owner_id != g.user.id:
        return redirect(url_for('things'))

    form = EditThingForm(obj=thing)

    if form.validate_on_submit():
        form.populate_obj(thing)

        if form.delete.data:
            db.session.delete(thing)
        else:
            db.session.add(thing)

        db.session.commit()

        return redirect(url_for('things'))

    return render_template('thing.html',
            thing=thing,
            form=form)

@app.route('/new-thing', methods=['GET', 'POST'])
@login_required
def new_thing():
    """Register a new thing."""

    form = NewThingForm()

    if form.validate_on_submit():
        thing = Thing(form.name.data, form.delta.data, str(uuid.uuid4()))

        g.user.things.append(thing)

        db.session.add(thing)
        db.session.add(g.user)

        db.session.commit()

        return redirect(url_for('things'))

    return render_template('new-thing.html',
            title = 'Register a new thing',
            form = form)

@app.route('/help')
@login_required
def help_page():
    return render_template('help.html',
            title = 'Help')


@app.route('/api/callhome/<uuid>')
def api_callhome(uuid):
    """A thing is calling home."""
    thing = Thing.query.filter_by(uuid=uuid).first()
    if thing:
        thing.timestamp = datetime.datetime.utcnow()

        db.session.add(thing)
        db.session.commit()

    return "OK"
