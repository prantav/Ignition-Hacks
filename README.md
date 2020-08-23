# Ignition-Hacks Hackathon
# MFunctions

Hi my name is Pranav and I'm 12 years old. This program is for Division Delta.

One thing I've noticed about High school students is that they struggle to grasp the concept of a mathamtical function. Side-note here: Please do not confuse my mathematical function  with a python function. Functions are powerful. I have written this program to show the world how powerful they are. It is not a long program or a particularly good program but this program shows the true power of functions.

## Using it

This program creates a class called MFunction. "M" standing for maths by the way.

To instantiate a MFunctions simply type:
`f1 =  MFunction({equation})`
Replace {equation} with your equation as a string so for example:
`f1 =  MFunction("x**2")`

Now you have instantiated an object of the class MFunction we can now work with it.
To see whether our object works type  `f1.plot_graph(-10,10)`.
If you have used the equation I have used above the output should look like this.
![alt text](https://github.com/prantav/Ignition-Hacks/blob/master/Figure_1.png)

Moving on you can also add, subtract, multiply and divide functions with one another like this:
`f1 =  MFunction("x**2")
h1 =  MFunction("x+2")
g1 = f1+h1`
So here g1 would equal `(x+2)+(x**2)`.

If you want to see the original equation you can type `str(f1)`.
Next there is a function called deriv wich can be called by `f1.deriv({x})`.
This function requires a value or a numpy array of x values. This function return the derivative.
You can also plot the derivative function with `f1.plot_deriv({x_min},{x_max})`.
The x_min and x_max specifyies what area of the graph is wanted.

Thanks for reading this!

