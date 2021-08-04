# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template= 'Hello,'):
    return f"{greeting_template} {name}!" 

print(greet('Paul', "What's up"))


planets = {
'Sun': 274,
'Jupiter': 24.9,
'Neptune': 11.2,
'Saturn': 10.4,
'Earth': 9.8,
'Uranus': 8.9,
'Venus': 8.9,
'Mars':	3.7,
'Mercury': 3.7,
'Moon':	1.6,
'Pluto': 0.6
}

#maakt de keys van functie 'planets' in lowercase
planets_lower = dict((k.lower(), v) for k, v in planets.items()) 

def force(mass=float(), body= 'earth'):
    if body in planets_lower:
        return mass * planets_lower.get(body) 

print(force(14.23,'pluto'))



def pull(m1=float(), m2=float(), d=float()):
    G = (6.674*(10**-11))
    gravity = G * m1*m2/d**2
    return gravity

print(pull(0.1,5.972*10**24,6.371*10**6))
