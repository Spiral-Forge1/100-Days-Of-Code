#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
print(capitals)
#Nesting a List in a Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log)

#Nesting a Dictionary in a Dictionary
travel_log2 = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_vists" :
                12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits":
                 9}
}
print(travel_log2)

#Nesting a dictionary inside a list
travel_log3 = [
    {
    "country": "France",
     "cities_visited" : ["Paris", "Lille", "Dijon"],
     "total_vists" :12},
    {
     "country":"Germany",
     "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits":9
    }
]
print(travel_log3)