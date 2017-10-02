`steering = desired - velocity`

![desired.png](Image)

How to calculate desired velocity?
We need to get vector pointing from location do target

```python
PVector desired = PVector.sub(target, location)
desired.setMag(maxSpeed)

PVector steering = PVector.sub(desired, velocity)
applyForce(steering)
steering.limit(maxForce)
```

