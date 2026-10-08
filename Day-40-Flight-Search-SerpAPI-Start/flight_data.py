class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops, via_city):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops
        self.via_city = via_city


def find_cheapest_flight(data, return_date):
    best_list = data.get("best_flights", [])
    other_list = data.get("other_flights", [])

    all_flights = best_list + other_list
    if not all_flights:
        print("Both flight pools came back empty.")
        return None
    if not all_flights:
        return None
    lowest_price = 99999999
    cheapest_flight = None

    for flight in all_flights:
        current_price  = flight.get("price", 99999999)
        if current_price < lowest_price:
            lowest_price = current_price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            nr_of_stops = len(flight["flights"]) - 1

            if nr_of_stops > 0:
                via_city = flight["flights"][0]["arrival_airport"]["name"]
            else:
                via_city = ""
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date,nr_of_stops, via_city)

    return cheapest_flight
