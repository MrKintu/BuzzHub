import { View,Text, TouchableOpacity } from "react-native";
import React from 'react';
import { AppColor } from "../utils/appColors";

const CustomButton = ({ButtonTitle, onPress,disabled}) => {
    return (
        <View>
            <TouchableOpacity onPress={onPress} disabled={disabled}>
                <View style={{width: 350, backgroundColor : disabled? AppColor.DISABLE_BUTTON : AppColor.BUTTON, borderRadius: 5}}>
                <Text style={{color:"white" , paddingVertical: 12 , fontSize: 18, textAlign: "center"}}>{ButtonTitle}</Text>
                </View>
            </TouchableOpacity>
        </View>
    )
}

export default CustomButton;