import { StyleSheet, Image, Text, View, Touchable, TouchableOpacity, Pressable } from "react-native";
import React, { useState, useContext } from 'react';
import { launchCamera, launchImageLibrary } from "react-native-image-picker";
import { AuthContext } from "../../context/AuthContext";
import { useNavigation } from '@react-navigation/native';


const OpenCamera = () => {
    const navigation = useNavigation();

    const [imgUrl, setImgUrl] = useState('https://imgv3.fotor.com/images/slider-image/a-man-holding-a-camera-with-image-filter.jpg')
    const [image, setImage] = useState('')
    const {  uploadDoc } = useContext(AuthContext);


    const open = async () => {
        console.log('Cam')
        const result = await launchCamera();
        setImgUrl(result?.assets[0]?.uri);
        setImage(result?.assets[0])
        console.log('result===>', result);
    }

    const openLib = async () => {
        console.log('Lib')
        const result = await launchImageLibrary();
        setImgUrl(result?.assets[0]?.uri);
        uploadDoc(result?.assets[0])
        console.log('result===>', result);
    }

  

    return (
        <View>
            <Image resizeMode="contain" style={styles.img} source={{ uri: imgUrl }} />
            <TouchableOpacity style={styles.btnCam} onPress={open} >
                <Text style={styles.txtBtn}>Open camera</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.btnCam} onPress={openLib} >
                <Text style={styles.txtBtn}>Open Library</Text>
            </TouchableOpacity>
            <Pressable
                style={[styles.button, styles.buttonClose]}
                onPress={() => navigation.navigate('signup')}>
                <Text style={{ textAlign:'center', margin:20, fontWeight:600 }} >Upload</Text>
            </Pressable>

        </View>
    )
}

export default OpenCamera;


const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    img: {
        width: '90%',
        height: 300,
        alignSelf: 'center'
    },
    btnCam: {
        alignSelf: 'center',
        justifyContent: 'center',

    },
    txtBtn: {
        margin: 10
    }
})
