def KelvinToFahrenheit(temperatura):
   assert (temperatura >= 0),"Mais frio do que o zero absoluto!"
   return ((temperatura-273)*1.8)+32

print(int(KelvinToFahrenheit(0))) # passa
print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))

print(KelvinToFahrenheit(-5))
