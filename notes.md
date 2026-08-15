# Aggregations
Loose "has-a" relationship.  
In aggregation, the parent object uses the child object, but the child is completely independent. If the parent object is destroyed, the child object continues to live on.  
> Represents a relationship where on object (the whole) contains references to one or more INDEPENDANT objects (the parts)

## The problem it solves
Aggregation solves the need for objects to collaborate without being permanently coupled. *It allows you to share a single resource (like a database connection or a client) across many different objects*, promoting modularity. This is often implemented via **Dependency Injection**.

# Composition
Strict "part-of" relationship.  
In composition, the parent object owns the child object.  
They share a strict lifecycle dependency: **if the parent is destroyed (garbage collected), the child is destroyed with it.**  
> The child cannot logically exist on its own outside the context of the parent.

## The problem it solves
Composition solves the need to encapsulate complex, multi-part data structures where the internal pieces have no business being accessed or existing independently.

# Why Favor Composition/Aggregation over Inheritance?
In modern software engineering, there is a core principle: "Favor object composition over class inheritance" (popularized by the Gang of Four design patterns).  

If you try to use inheritance to solve everything, you end up with deeply nested, fragile class hierarchies.

- **The Fragile Base Class Problem:** If you change a method in a parent class, it can unexpectedly break all the child classes that inherit from it.
- **Inflexibility:** Inheritance locks you in at compile time. A FirewallLog is always a Log. But what if you want to dynamically change how it behaves at runtime?
- **Testing:** Aggregation makes unit testing drastically easier. Because the MalwareDataPipeline takes the S3Client as a parameter, you can easily pass in a "FakeS3Client" when writing your pytest suite, rather than accidentally uploading test data to an actual AWS bucket.