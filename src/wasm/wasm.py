from wasmer import Store, Module, Instance

# Create a store, which holds the engine, the compiler etc.
store = Store()

# Let's assume we don't have WebAssembly bytes at hand. We will
# write WebAssembly manually.
module = Module(
    store,
    """
    (module
      (type (func (param i32 i32) (result i32)))
      (func (type 0)
        local.get 0
        local.get 1
        i32.add)
      (export "sum" (func 0)))
    """
)

# Instantiates the module.
instance = Instance(module)

# Now, let's execute the `sum` function.
assert instance.exports.sum(1, 2) == 3
