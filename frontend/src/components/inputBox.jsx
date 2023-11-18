import { StyleSheet, Text, TextInput, View } from "react-native";
import React from 'react';

const InputBox = ({placeholder,onBlur,OnChangedText,value,touched,securetextEntry,keyboardtype,maxLength,errors}) => {
    return (
        <View style={styles.mainContainer}>
            <TextInput style={styles.TextInput} placeholder={placeholder} 
            onChangeText={OnChangedText} onBlur={onBlur} value={value} touched={touched}
            secureTextEntry={securetextEntry} keyboardType={keyboardtype} maxLength={maxLength}
            />
            {errors && touched && <Text style={{color:"red", paddingLeft: 5}} >{errors}</Text> }
        </View>
    )
}

export default InputBox;

const styles = StyleSheet.create({
    mainContainer: {
        height: 78
    },
    TextInput: {
        borderWidth: 1,
        width: 350,
        borderColor: 'grey',
        borderRadius:5,
        paddingHorizontal: 10
    }
})