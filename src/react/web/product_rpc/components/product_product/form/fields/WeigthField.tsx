import React from "react";
import {useAppDispatch, useAppSelector} from "../../../../app/hooks";
import { updateWeight
} from "../../../../app/slice/product/productSlice";


interface WeightFieldProps{
    weight:number;
    onWeightChange:(value:number)=>void;
}

    export const WeightField:React.FC<WeightFieldProps> = ({
        weight,
        onWeightChange,
    })=>{
   
    const dispatch = useAppDispatch();

    const handleWeigthChange =(e: React.ChangeEvent<HTMLInputElement>)=>{
        const newValue =e.target.valueAsNumber; 
        dispatch(updateWeight({weight:newValue}))
    };
    return(
        <div className="inline-flex flex-col w-40 mr-1">
            <label htmlFor="weight" className="text-xs">
                Peso
            </label>
            <input
                className="border border-gray-300 rounded text-sm px-1"
                type="number"
                autoComplete="on"
                id="weight"
                name="weight"
                value={weight}
                onChange={handleWeigthChange}
                onFocus={(e)=>e.target.select()}
            
            
            ></input>


        </div>



    ); 
};
