from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from .table_managers.images_manager import ImagesManager
from .constants import STATIC_PATH
from .table_managers.images_manager import ImagesManager
from .table_managers.locations_manager import LocationsManager

main = Blueprint("main", __name__)
images_manager = ImagesManager()
locations_manager = LocationsManager()

start_date_filter = None
end_date_filter = None
location_filter = None
sort = "Rank"

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/bio")
def bio():
    return render_template("bio.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/portfolio", methods=["GET"])
def portfolio():
    date_filtered_images = images_manager.filter_by_date(start_date_filter, end_date_filter)
    location_filtered_images = images_manager.filter_by_location(location_filter)
    filtered_images = set(date_filtered_images) & set(location_filtered_images)
    filtered_images = sorted(list(filtered_images), key=lambda image: image.date)
    filtered_images = sort_images(filtered_images)
    all_locations = locations_manager.select_all_locations()
    return render_template("portfolio.html", images=filtered_images, locations=all_locations, filters=return_filters_display(), sort=sort, no_images=len(filtered_images)==0)

@main.route("/portfolio/set-filters", methods=["POST"])
def set_filters():
    global start_date_filter
    global end_date_filter
    global location_filter
    start_date_form = request.form.get("start_date")
    end_date_form = request.form.get("end_date")
    location_form = request.form.get("location")
    start_date_filter = start_date_form if not start_date_form == "" else None
    end_date_filter = end_date_form if not end_date_form == "" else None
    location_filter = location_form if not location_form == "" else None
    return redirect(url_for("main.portfolio"))

@main.route("/portfolio/set-sort", methods=["POST"])
def set_sort():
    global sort
    sort = request.form.get("sort")
    if sort is None:
        sort = "Rank"
    return redirect(url_for("main.portfolio"))

@main.route("/portfolio/clear-fields", methods=["POST"])
def clear_fields():
    global start_date_filter
    global end_date_filter
    global location_filter
    global sort
    start_date_filter = None
    end_date_filter = None
    location_filter = None
    sort = "Rank"
    return redirect(url_for("main.portfolio"))

def sort_images(images):
    if sort is None:
        return images
    elif sort == "Rank":
        return sorted(images, key=lambda image: image.rank)
    elif sort == "Newest":
        sorted_list = sorted(images, key=lambda image: image.date)
        sorted_list.reverse()
        return sorted_list
    else:
        return sorted(images, key=lambda image: image.date)

# Return the display that will be showm above the filter button that will show which filters are active
def return_filters_display():
    if start_date_filter is None and end_date_filter is None and location_filter is None:
        return "None"
    else:
        filter_display = ""
        if start_date_filter is not None:
            filter_display += "Start Date, "
        if end_date_filter is not None:
            filter_display += "End Date, "
        if location_filter is not None:
            filter_display += "Location, "
        # Return the whole filter display except for the trailing comma and space
        return filter_display[:-2]