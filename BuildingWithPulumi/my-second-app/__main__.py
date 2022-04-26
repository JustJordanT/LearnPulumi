import pulumi

config = pulumi.Config()
stack = pulumi.get_stack()
org = config.require("org")

stack_ref = pulumi.StackReference(f"{org}/pulumifundamentals/{stack}")

pulumi.export("shopUrl", stack_ref.get_output("url"))