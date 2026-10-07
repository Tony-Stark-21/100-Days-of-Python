class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date



def find_cheapest_flight(data, return_date):
    if data is None or "best_flights" not in data:
        print("No flight data found.")
        return None

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    if not all_flights:
        return None
    lowest_price = 99999999
    cheapest_flight = None

    for flight in all_flights:
        current_price = flight["price"]
        if current_price < lowest_price:
            lowest_price = current_price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    return cheapest_flight
