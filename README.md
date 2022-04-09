# Human Design Repo
This repo will be to assist people in learning more about their Human Design chart. Get your free chart here:  https://mybodygraph.com

# Must Haves

1. Ability for user to provide the following:<br><br>
    - type (strategies are based on type)
    - signature
    - definition (optional)
    - authority
    - profile
    - incarnation cross
    - red/black planetary activations + hex lines
      - do each side separately - but leverage the same class
      - only distinction is if red or black
    - channels (potentially could make this automatic based on what gates they have defined)
    - which centers are defined, undefined, and completely open
    - for each center, what gate numbers are activated


2. For each piece provided, be able to return important information about the different parts


3. Ability to save data to local machine or Google

# Structure

Classes will be created per energy center & major section (_e.g.:  type, signature, authority, etc_). Each one has its own unique needs, and each person's "chart" should be able to pull them together.

As a user provides data about their chart, instances of the respective classes will be created. When the data is read in from a local file or a Google sheet, they will be re-created for easy access.

# Resources

Most of the material provided will be included in the code itself.

If you would like to purchase the "definitive" book that will be referenced in this code, you can purchase through Amazon via [my affiliate link here](https://amzn.to/3rdomd4).