import React, { useState, useContext } from 'react';
import { View, Text, Image } from 'react-native';
import { Formik } from 'formik';
import { loginInitialValue, loginValidationSchema } from './utils';
import InputBox from '../../components/inputBox';
import CustomButton from '../../components/customButton';
import { useNavigation } from '@react-navigation/native';
import Spinner from 'react-native-loading-spinner-overlay';
import { AuthContext } from '../../context/AuthContext';


const Login = () => {
    const navigation = useNavigation();
    const [username, setUsername] = useState(null);
    const [password, setPassword] = useState(null);
    const { isLoading, login } = useContext(AuthContext);


    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-between' }}>
            <Spinner visible={isLoading} />
            <View style={{ flex: 0.8, justifyContent: 'center' }}>
                <Image style={{ alignSelf: 'center', width: 200, height: 160, marginBottom: 20 }} source={require('../../assets/images/buzx.png')} />

                
                            <View>
                                <InputBox placeholder={'Username,email address or mobile number'}
                                    value={username}
                                    OnChangedText={text => setUsername(text)}
                                />

                                <InputBox placeholder={'password'}
                                    value={password}
                                    securetextEntry={true}
                                    OnChangedText={text => setPassword(text)} />
                                <CustomButton ButtonTitle={'Login'} onPress={() => {
                                    login(username, password);
                                }} />
                                <View style={{ marginTop: 20 }}><Text style={{ textAlign: "center" }}>Forgotten Password?</Text></View>
                            </View>
                       
            </View>
            <View style={{ flex: 0.2, marginBottom: 20, justifyContent: "flex-end" }} ><Text onPress={() => navigation.navigate('openCamera')}>Create new account</Text></View>
        </View>
    )
}

export default Login;