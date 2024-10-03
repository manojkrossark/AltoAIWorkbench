from flask import Blueprint, request, jsonify
from models.demand_forecast import DemandForecast
from models.store_locator import StoreLocator
from models.inventory_management import InventoryManagement
from models.delivery_scheduler import DeliveryScheduler

api_bp = Blueprint('api', __name__)

@api_bp.route('/forecast', methods=['POST'])
def forecast():
    data = request.json
    forecast_model = DemandForecast()
    predictions = forecast_model.predict(data)
    return jsonify(predictions)

@api_bp.route('/store-locations', methods=['POST'])
def store_locations():
    data = request.json
    locator = StoreLocator()
    recommended_stores = locator.get_optimal_locations(data)
    return jsonify(recommended_stores)

@api_bp.route('/inventory-adjustment', methods=['POST'])
def inventory_adjustment():
    data = request.json
    inventory_manager = InventoryManagement()
    adjustments = inventory_manager.adjust_inventory(data)
    return jsonify(adjustments)

@api_bp.route('/schedule-delivery', methods=['POST'])
def schedule_delivery():
    data = request.json
    scheduler = DeliveryScheduler()
    optimal_times = scheduler.get_optimal_schedule(data)
    return jsonify(optimal_times)