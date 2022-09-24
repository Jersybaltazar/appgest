import datetime as dt
from enum import Enum

from .parser import product_client_result, transform_product_json
from .models import ProductStats
from .utils import rpc
from django.conf import settings


class ProductResult(Enum):
    ALL = 1
    INCOMPLETE = 2
    NONE = 3

class Product():

    def __init__(self):
        # DEFAULTS
        self.active = True
        self.sale_ok = True
        self.purchase_ok = True
        self.type = "product"
        self.property_cost_method = False
        self.company_id = 1
        self.uom_id = 1
        self.uom_po_id = 1
        self.available_in_pos = True
        self.sale_delay = 0
        self.tracking = "none"
        self.property_stock_production = 7
        self.property_stock_inventory = 5
        self.property_account_income_id = False
        self.property_account_expense_id = False
        self.property_account_creditor_price_difference = False
        self.property_valuation = False
        self.property_stock_account_input = False
        self.property_stock_account_output = False
        self.purchase_method = "receive"
        self.invoice_policy = "order"
        self.service_type = "manual"
        self.sale_line_warn = "no-message"
        self.purchase_line_warn = "no-message"
        self.website_published = False
        self.image_medium = False
        self.__last_update = False
        self.barcode = False
        self.cod_sunat = False
        self.cod_detraction_sunat = False
        self.standard_price = 0
        self.to_weight = False
        self.weight = 0
        self.volume = 0
        self.description = False
        self.description_sale = False
        self.description_purchase = False
        self.description_pickingout = False
        self.description_pickingin = False
        self.description_picking = False

        # UNIQUE PROPERTIES
        self.responsible_id = None

        self.name = None
        self.default_code = None
        self.list_price = None
        self.categ_id = None
        self.pos_categ_id = None
        self.attribute_line_ids = []

    def __set_attrs(self, attr_lines):
        virtual_count = 1110 ## just because

        for attr in attr_lines:
            virtual = 'virtual_{}'.format(virtual_count)
            self.attribute_line_ids.append(
                [
                    0,
                    virtual,
                    {
                        "attribute_id": attr['attribute_id'],
                        "value_ids": [[6, False, attr['value_ids']]]
                    }
                ]
            )
            virtual_count += 10

    def set_responsible_id(self, id):
        self.responsible_id = id

    def set_product_dict(self, dict):
        self.name = dict['name']
        self.default_code = dict['default_code']
        self.list_price = dict['list_price']
        self.categ_id = dict['categ_id']
        self.pos_categ_id = dict['pos_categ_id']
        self.attribute_line_ids = []
        self.__set_attrs(dict['attribute_line_ids'])

    def clear_prod_vals(self):
        self.name = None
        self.default_code = None
        self.list_price = None
        self.categ_id = None
        self.pos_categ_id = None
        self.attribute_line_ids = []

def edit_product_default_code(df_map, product_product_list, product_template, uid, proxy):
    # SINGLE DEFAULT CODE FOR ALL
    if len(df_map) == 0 and product_template['default_code'] != '':
        rpc.update_model('product.product', [product_product['id'] for product_product in product_product_list],
        {'default_code': product_template['default_code']}, uid, proxy=proxy)

    # MULTIPLE DEFAULT CODES
    if len(df_map) > 0:
        default_code_by_prod_ids = {}
        for product_product in product_product_list:
            for df_map_item in df_map:
                if(set(df_map_item['ids']).issubset(set(product_product['attribute_value_ids']))):
                    # default_code_by_prod_ids
                    if df_map_item['default_code'] in default_code_by_prod_ids:
                        default_code_by_prod_ids[df_map_item['default_code']].append(product_product['id'])
                    else:
                        default_code_by_prod_ids[df_map_item['default_code']] = [product_product['id']]
                    break
        for default_code, ids in default_code_by_prod_ids.items():
            rpc.update_model('product.product', ids, {'default_code':  default_code}, uid, proxy=proxy)

def edit_product_list_price(lp_map, tmpl_id, uid, proxy):
    if len(lp_map) > 0:
        rpc.update_model('product.template', [tmpl_id], {'list_price': 0}, uid, proxy=proxy)

        context = {
            'active_model': 'product.template',
            'default_product_tmpl_id': tmpl_id,
            'active_id': tmpl_id,
            'uid': uid,
            'search_disable_custom_filters': True,
        }

        # MULTIPLE LIST PRICES
        list_price_by_prod_ids = {}
        for lp_map_item in lp_map:
            if lp_map_item['list_price'] in list_price_by_prod_ids:
                list_price_by_prod_ids[lp_map_item['list_price']].append(lp_map_item['ids'][0])
            else:
                list_price_by_prod_ids[lp_map_item['list_price']] = [lp_map_item['ids'][0]]
        for list_price, ids in list_price_by_prod_ids.items():
            rpc.update_model('product.attribute.value', ids,
            {'price_extra': list_price}, uid, context=context, proxy=proxy)

def create_product_new(product_template, default_code_map, list_price_map, client_id, uid, proxy):
    # CREATE PRODUCT
    tmpl_id = rpc.create_model('product.template', product_template, uid, proxy=proxy)
    # GET PRODUCT.PRODUCT IDS
    product_product_list = rpc.get_model('product.product', [[['product_tmpl_id', '=', tmpl_id]]],
                            ['attribute_value_ids'], proxy=proxy)

    edit_product_default_code(default_code_map, product_product_list, product_template, uid, proxy)
    edit_product_list_price(list_price_map, tmpl_id, uid, proxy)

    # SAVE PRODUCT ODOO ID AND REACT ID INTO DB
    ProductStats.objects.create(odoo_id=tmpl_id, client_id=client_id, user_id=uid, created=dt.datetime.now())

    return tmpl_id

def product_new(transf_list, uid, pid):
    product_template = None
    product_tmpl_ids = []
    for transf in transf_list:
        if product_template is None:
            product_template = Product()
            product_template.set_responsible_id(uid)

        proxy = rpc.get_proxy()
        product_template.set_product_dict(transf['product'])
        tmpl_id = create_product_new(
                  product_template.__dict__,
                  transf['default_code_map'],
                  transf['list_price_map'],
                  transf['client_id'],
                  uid,
                  proxy)
        product_template.clear_prod_vals()
        product_tmpl_ids.append(tmpl_id)

    return product_tmpl_ids


def create_products_v2(raw_data):
    transf_list = transform_product_json(raw_data)
    product_tmpl_ids = product_new(transf_list, int(settings.ODOO_UID), 0)
    product_results = product_client_result(product_tmpl_ids)
    return product_results
