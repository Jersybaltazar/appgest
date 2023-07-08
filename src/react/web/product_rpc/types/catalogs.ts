import { CatalogGeneric } from "./shared";

export interface ProductCategoryLine extends CatalogGeneric {
  parent_id: number;
}

export interface ProductCategoryFamily extends CatalogGeneric {
  parent_id: number;
}

export interface ProductCategoryBrand extends CatalogGeneric {
  parent_id: number;
}

export interface PosCategory extends CatalogGeneric {
  parent_id: number;
}

export interface ProductAttribute extends CatalogGeneric {}

export interface ProductAttributeValue extends CatalogGeneric {
  attribute_id: number;
}

export interface Partner extends CatalogGeneric {
  vat: string;
}
export interface ProductWeight extends CatalogGeneric{
  parent_id:number; //cambios
}

export interface Catalogs {
  product_category_line: ProductCategoryLine[];
  product_category_family: ProductCategoryFamily[];
  product_category_brand: ProductCategoryBrand[];
  pos_category: PosCategory[];
  product_attribute: ProductAttribute[];
  product_attribute_value: ProductAttributeValue[];
  product_weight: ProductWeight[];//cambios
}

export interface OrderCatalogs {
  res_partner: Partner[];
}

export enum CatalogType {
  product = 1,
  order = 2,
}
