# Day 40: Flight Club (final version)

## What it does
Reads destination cities and price limits from a Google Sheet through
Sheety, fills in missing IATA codes automatically and writes them back,
searches live Google Flights data through SerpApi starting from LOS,
finds the cheapest flight including indirect ones with layover details,
and emails every subscriber from a Google Form when a flight is under
budget.

## Files
- .env: API keys, Sheety login, email and app password (never committed)
- main.py: runs everything, caches requests, loops over destinations and subscribers
- data_manager.py: Sheety GET and PUT for destinations, customer emails and IATA codes
- flight_search.py: SerpApi calls for IATA lookup and flight prices
- flight_data.py: FlightData class and find_cheapest_flight function
- notification_manager.py: SMTP email sender using TLS on port 587

## Bugs that cost me hours, and what each one taught me
1. 401 Unauthorized from Sheety. load_dotenv must run at the very top of
   main.py, before the modules that read environment variables are imported.
2. Variables holding None. I was printing the JSON instead of returning it.
   Print only shows data, return passes it on.
3. Blank results with no errors. I compared a budget in naira against
   prices in dollars. Always check units and currency.
4. Indirect flights broke my indexes. Hardcoded positions failed when the
   number of legs changed. Fixed with index -1 for the final leg and
   len of legs minus 1 for the number of stops.
5. Google Form data through Sheety. Column names became the literal
   question text, plus blank rows. Fixed with a guard condition that
   checks the key exists before reading it.

## The honest part
Built late at night with power outages, a draining laptop battery and
phonk music to stay focused. This was the hardest stretch of the course
so far, worked through step by step with Gemini. A quiz on the five bugs
above scored 5 out of 5 afterwards. It is the third time (Days 34, 35 and
39-40) that the hardest feeling day turned out to be one I understood
well. If a future day feels impossible, reread this.

Written: October 2026