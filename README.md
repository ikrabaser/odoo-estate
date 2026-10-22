# Odoo Real Estate (`estate`)

A small real estate management module for **Odoo 19**, built while following the Odoo server framework tutorial. It lets you manage properties, property types, tags and buyer offers, and walks each property through a simple sales workflow.

> Note: some field labels and messages in the UI are in Turkish.

## Features

- **Properties**: name, description, availability date, expected and selling price, bedrooms, living area, garden and garden area. The total area and the best offer are computed automatically.
- **Property types** and **tags**: group and label properties. Tag names are unique and tags can have a color. The property type form lists all properties of that type.
- **Offers**: each offer has a price, a partner and a status (accepted or refused). Offers can be accepted or refused directly from the list.
- **Sales workflow** with a status bar: `New` → `Offer Received` → `Offer Accepted` → `Sold`, plus `Cancelled`.

## Business rules

- The first offer on a new property moves it to **Offer Received**.
- Accepting an offer sets the property's buyer and selling price and moves it to **Offer Accepted**.
- A property can only have one accepted offer.
- An accepted offer cannot be refused.
- A cancelled property cannot be sold, and a sold property cannot be cancelled.
- An offer price must be greater than 0 (SQL constraint).
- Offers are read-only once a property is accepted, sold or cancelled.
- Tag names must be unique (SQL constraint).

## Installation

1. Put the module in a folder named `estate` inside one of your Odoo `addons_path` directories:

   ```bash
   git clone https://github.com/ikrabaser/odoo-estate.git estate
   ```

2. Restart Odoo, enable developer mode and click **Apps → Update Apps List**.
3. Search for **Real Estate** and click **Install**.

Or install it from the command line:

```bash
python odoo-bin -c odoo.conf -d <your_database> -i estate
```

After changing the code or views, upgrade the module:

```bash
python odoo-bin -c odoo.conf -d <your_database> -u estate
```

## Module structure

```
estate/
├── __manifest__.py
├── models/
│   ├── estate_property.py          # properties, computed fields, sell/cancel actions
│   ├── estate_property_offer.py    # offers, accept/refuse actions, price constraint
│   ├── estate_property_tag.py      # tags with a unique name
│   └── estate_property_type.py     # property types
├── security/
│   └── ir.model.access.csv         # access rights for internal users
└── views/
    ├── estate_property_views.xml
    ├── estate_property_offer_views.xml
    ├── estate_property_type_views.xml
    ├── estate_property_tag_views.xml
    └── estate_menus.xml
```

## Access rights

All internal users (`base.group_user`) can read, create, edit and delete properties, property types, tags and offers.

## Requirements

- Odoo 19.0
- Depends only on the `base` module

## License

LGPL-3, as declared in `__manifest__.py`.

## Author

Leyla İkra Başer
