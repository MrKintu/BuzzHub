import React, { useState } from 'react'
import { Button, Text, View, TouchableOpacity } from 'react-native'
import DatePicker from 'react-native-date-picker'
import { AppColor } from "../utils/appColors";
import CustomButton from './customButton';
import { StyleSheet, Pressable } from 'react-native';



const DatePick = ({ title }) => {
    const [date, setDate] = useState(new Date())
    const [open, setOpen] = useState(false)

    return (
        <>
            {/* <View>
            <TouchableOpacity onPress={setOpen(true)} >
                <View style={{width: 350, backgroundColor : "white", borderRadius: 5}}>
                <Text style={{color: AppColor.BUTTON , paddingVertical: 12 , font: 18, textAlign: "center"}}>{title}</Text>
                </View>
            </TouchableOpacity>
        </View> */}
            <View style={{height:70, display:'flex', alignItems:'center'}}>

                <Pressable style={styles.button} onPress={() => setOpen(true)}>
                    <Text style={styles.text}>{title}</Text>
                </Pressable>
                {/* <Button backgroundColor="white" title="Open" onPress={() => setOpen(true)} /> */}
                {/* <CustomButton title={"Date of birth"} onPress={() => setOpen(true)} /> */}
                <DatePicker
                    modal
                    open={open}
                    date={date}
                    onConfirm={(date) => {
                        setOpen(false)
                        setDate(date)
                    }}
                    onCancel={() => {
                        setOpen(false)
                    }}
                />
            </View>

        </>
    )
}

export default DatePick;

const styles = StyleSheet.create({
    button: {
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 12,
        paddingHorizontal: 32,
        borderRadius: 4,
        elevation: 3,
        width: '50%',
        borderRadius:5
    },
    text: {
        fontSize: 16,
        lineHeight: 21,
        fontWeight: 'bold',
        letterSpacing: 0.25,
        color: 'grey',
    },
});