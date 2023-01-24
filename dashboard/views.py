from django.views.generic import TemplateView
from django.contrib import messages
from pyairtable import Table
from purrfectCreations.settings import AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_ORDERS_TABLE_ID
from datetime import datetime
import logging


# Create your views here.
def get_dashboard_data():
    """
    :return: (total_orders, total_orders_this_month, number_of_orders_in_progress, revenue, recent_orders)
        total_orders int:
        total_orders_this_month int:
        number_of_orders_in_progress: int
        revenue int:
        recent_orders List<dict>: List of most recent 50 orders. See orders on airtable for object details
    :raises: KeyError, Exception
    """
    orders_table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_ORDERS_TABLE_ID)
    all_orders = orders_table.all(sort=["-order_placed"])
    total_orders = len(all_orders)
    logging.debug(f"retrieved orders {total_orders} from airtable")
    total_orders_this_month = 0
    number_of_orders_in_progress = 0
    recent_orders = []  # most recent 50
    revenue = 0
    today = datetime.today()
    for i in range(total_orders):
        order_dict = all_orders[i]["fields"]
        if i < 50:
            recent_orders.append(order_dict)
        order_placed = order_dict["order_placed"]
        order_status = order_dict["order_status"]
        order_placed = datetime.fromisoformat(order_placed).date()
        if order_placed.year == today.year and order_placed.month == today.month:
            total_orders_this_month += 1
        if order_status != "cancelled":
            revenue += order_dict["price"]
        if order_status == "in_progress":
            number_of_orders_in_progress += 1
    return total_orders, total_orders_this_month, number_of_orders_in_progress, revenue, recent_orders


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        try:

            context["total_orders"], context["total_orders_this_month"], context["number_of_orders_in_progress"], \
            context[
                "revenue"], context[
                "recent_orders"] = get_dashboard_data()
        except Exception as exc:
            """
            Ideally should be more specific but the airtable package does not document any specific exceptions
            """
            logging.error(exc)
            messages.add_message(message=f"An error was encountered while retrieving data from airtable: {exc}",
                                 level=messages.ERROR, request=self.request)

        return context
