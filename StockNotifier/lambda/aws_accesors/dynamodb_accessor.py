import boto3
from botocore.exceptions import ClientError
from models.product import Product
from typing import Optional
from boto3.dynamodb.conditions import Key

DYNAMODB_STOCK_TABLE_NAME = "StockTable"
table = boto3.resource('dynamodb').Table(DYNAMODB_STOCK_TABLE_NAME)

def from_product(product: Product) -> dict:
    return {
        "PartId": product.id,
        "StoreId": product.store.name,
        "Name": product.name,
        "Price": product.price,
        "Url": product.url,
        "InStock": product.in_stock
    }

def to_product(structured_item: dict) -> Product:
    return Product(id=structured_item["PartId"],
                   store=structured_item["StoreId"],
                   name=structured_item["Name"],
                   price=structured_item["Price"],
                   url=structured_item["Url"],
                   in_stock=structured_item["InStock"])


def put_item(product: Product) -> None:

    print(f"Putting item into DynamoDB: {product}")
    try:
        table.put_item(Item=from_product(product))
        print("Successfully put_item to DynamoDB")
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise e

def query_item(part_id: str, store_id: str) -> Optional[Product]:
    print(f"Querying DynamoDB for part_id: {part_id} and store_id: {store_id}")
    try:
        response = table.query(
            KeyConditionExpression=Key('PartId').eq(part_id) & Key('StoreId').eq(store_id)
        )
        if "Items" in response and response["Items"]:
            print(f"Query successful")
            print(f"Found Object: {response['Items'][0]}")
            return to_product(response["Items"][0])
        else:
            print("No items found for the given part_id and store_id")
            return None
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise e