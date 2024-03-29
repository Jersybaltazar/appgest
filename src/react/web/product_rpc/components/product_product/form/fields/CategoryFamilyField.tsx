import React from 'react';
import { useAppDispatch, useAppSelector } from "../../../../app/hooks";
import { selectCatalogs } from "../../../../app/slice/product/catalogSlice";
import {
  selectProductFamilyId,
  selectProductLineId,
  updateFamily,
  selectProductWeight,
} from "../../../../app/slice/product/productSlice";
import { Select } from "../../../shared/Select";

export const CategoryFamilyField = () => {
  const catalogs = useAppSelector(selectCatalogs);
  const lineId = useAppSelector(selectProductLineId);
  const familyId = useAppSelector(selectProductFamilyId);
  const dispatch = useAppDispatch();
  const weight = useAppSelector(selectProductWeight);

  const handleCategoryFamily = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newId = Number(e.target.value);
    dispatch(
      updateFamily({
        categoryFamilyId: newId,
        categoryFamilies: catalogs.product_category_family,
      })
    );
    const selectedFamily = catalogs.product_category_family.find(
      (catFamily) => catFamily.id === newId
    );
    if (selectedFamily) {
      const familyWeight = selectedFamily.weight;
      dispatch(updateFamily(familyWeight));
    }
  };

  return (
    <div className="inline-flex flex-col w-40 mr-1">
      <label htmlFor="cat_family" className="text-xs">
        Familia 
      </label>
      <Select
        id={familyId}
        handler={handleCategoryFamily}
        catalog={catalogs.product_category_family.filter(
          (catFamily) => catFamily.parent_id === lineId
        )}
        name={"cat_family"}
        autoFocus={false}
      />
    </div>
  );
};
