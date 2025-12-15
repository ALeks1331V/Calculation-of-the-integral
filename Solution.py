class integral_calculation:
    def __init__(self, start_point, end_point, n):
        self.start_point = start_point
        self.end_point = end_point
        self.n = n
    def fx(self, x):
        return -pow(x, 2) + 2*x + 8

    def rectangle_method(self):
        sum = 0
        step = (abs(self.start_point) + abs(self.end_point))/self.n
        i = self.start_point
        while i < self.end_point:
            current_x = i+step/2
            sum += self.fx(current_x)*step
            i+=step
        return sum

    def trapezoidal_integration(self):  
        step = (abs(self.start_point) + abs(self.end_point))/self.n
        result = 0 
        for i in range(1, self.n):  
            x_current = self.start_point + i * step  
            result += (self.fx(x_current)+self.fx(x_current+step))*step/2
        return result

    def simpson_method(self):
        result = (self.end_point - self.start_point)/6 * (self.fx(self.start_point) + 4*self.fx((self.start_point+self.end_point)/2) + self.fx(self.end_point))
        return result

    def Monte_Carlo_method(self):
        sum = 0
        i = 0
        step = (abs(self.start_point) + abs(self.end_point))/self.n
        for i in range (1, self.n):
            x_current = self.start_point + i * step 
            sum += self.fx(x_current)
        return (self.end_point-self.start_point)/self.n * sum


integral = integral_calculation(-2, 4, 100)

print("Ответ методом прямоугольников = ", integral.rectangle_method())
print("Ответ методом трапеций: ", integral.trapezoidal_integration())
print("Ответ методом Симпсона: ", integral.simpson_method())
print("Ответ методом Монте-Карло: ", integral.Monte_Carlo_method())