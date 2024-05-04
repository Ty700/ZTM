# If we have a package inside another package

# Like more_shopping/ inside shopping
# We can do:
import shopping.more_shopping.example

# Then we can call it as:

shopping.more_shopping.example()

# However, this is long, so we can do:

from shopping.more_shopping import example

# then we can call it as just:

example()

# Sometimes we have functions with the same name, so we couldn't do this

# If we had more functions in more_shopping, we can do:

# from shopping.more_shopping import example, another_function

# or, we can just import that package within shopping and call it by:

# from shopping import more_shopping
# more_shopping.example() 
# This way avoid name collisions

# or from utility import * <= This imports everything in utility
# I don't really like this way since it's not explict





