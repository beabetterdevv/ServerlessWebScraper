from product_resolvers.cc_resolver import CanadaComputersResolver
import os
from aws_accesors import ssm_accessor, dynamodb_accessor
from discord import discord_publisher
from models.store import Store
from models.product import Product

PRODUCT_ID = "9800x3d"
PRODUCT_TITLE = "AMD Radeon 9800x3d"
# PRODUCT_URL = "https://www.canadacomputers.com/en/desktop-memory/99478/g-skill-ripjaws-v-32gb-2x16gb-ddr4-3200mhz-cl16-udimm-f4-3200c16d-32gvk.html"
PRODUCT_URL = "https://www.canadacomputers.com/en/amd-desktop-processors/264908/amd-ryzen-7-9800x3d-8-core-4nm-am5-104mb-cache-120w-zen-5-cpu-100-100001084wof.html"

def find_product_availability() -> Product:
    resolver = CanadaComputersResolver(PRODUCT_ID, PRODUCT_URL, PRODUCT_TITLE)
    return resolver.resolve()

def publish_to_discord(product: Product) -> None:
    discord_webhook_url_arn = os.environ['DISCORD_WEBHOOK_URL_ARN']
    discord_webhook_url = ssm_accessor.retrieve_parameter(discord_webhook_url_arn)
    discord_publisher.publish(discord_webhook_url, product)



def handle(event, context):

    product = find_product_availability()
    previous = dynamodb_accessor.query_item(PRODUCT_ID, Store.CANADA_COMPUTERS.name)

    # Case 1 - First time we've run - save state, publish if IS
    # Case 2 - Previous=OOS, Current=IS - publish & Save
    # Case 3 - Previous=IS, Current=OOS - save
    # Case 4 - Previous=OOS, Current=OOS - do nothing
    # Case 5 - Previous=IS, Current=IS - do nothing

    if previous is None:
        # Case 1
        print("First run - adding the item to dynamodb")
        dynamodb_accessor.put_item(product)
        if product.in_stock:
            print("Item is in stock - publish to discord")
            publish_to_discord(product)
    else:
        if previous.in_stock is False and product.in_stock is True:
            #Case 2    
            print("Product was previously out of stock, but is now in stock - publish and save!")
            publish_to_discord(product)
            dynamodb_accessor.put_item(product)
        elif previous.in_stock is True and product.in_stock is False:
            # Case 3
            print("Product was previously in stock but is now out of stock, just save state")
            dynamodb_accessor.put_item(product)
        else:
            #Case 4 & 5
            print("No change in stock status - noop")
