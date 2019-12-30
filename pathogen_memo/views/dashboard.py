"""Routes for logged-in application."""
from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
#from .assets import compile_auth_assets
from flask_login import login_required

from pathogen_memo.views.barplota import barplota
from pathogen_memo.views.barplotb import barplotb
from pathogen_memo.views.barplotc import barplotc
from pathogen_memo.views.barplotd import barplotd

from pathogen_memo.controllers import countqueries


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
#compile_auth_assets(app)


def createpngs():
    #Serve first plot
    barplota()
    #Serve first plot
    barplotb()
    #Serve first plot
    barplotc()
    #Serve first plot
    barplotd()


@main_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""

    createpngs()
    pathogenscount = countqueries.get_queries_count()
    print("Total pathognes: ", pathogenscount)
    return render_template('dashboard.html',
                           title='PathogenMemo-Dash.',
                           template='dashboard-template',
                           current_user=current_user,
                           data= pathogenscount)
