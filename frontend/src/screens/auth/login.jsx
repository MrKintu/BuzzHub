import { View, Text, Image } from 'react-native';
import React from 'react';
import { Formik } from 'formik';
import { loginInitialValue, loginValidationSchema } from './utils';
import InputBox from '../../components/inputBox';
import CustomButton from '../../components/customButton';
import{useNavigation} from'@react-navigation/native';

const Login = () => {
    const navigation = useNavigation();
    

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-between' }}>
            <View style={{ flex: 0.8, justifyContent: 'center' }}>
                <Image style={{alignSelf: 'center', width: 200, height: 60, marginBottom : 20 }} source={require('../../assets/images/instagramLogo.png')} />

                <Formik
                    initialValues={loginInitialValue}
                    validationSchema={loginValidationSchema}
                    onSubmit={() => navigation.navigate('FeedScreen')}>
                    {({
                        handleChange,
                        handleBlur,
                        handleSubmit,
                        values,
                        touched,
                        errors,
                        isValid
                    }) => {
                        return (
                            <View>
                                <InputBox placeholder={'Username,email address or mobile number'}
                                    OnChangedText={handleChange('username')}
                                    onBlur={handleBlur('username')}
                                    value={values.username}
                                    touched={touched.username}
                                    errors={errors.username} />

                                <InputBox placeholder={'password'}
                                    OnChangedText={handleChange('password')}
                                    onBlur={handleBlur('password')}
                                    value={values.password}
                                    touched={touched.password}
                                    errors={errors.password} />
                                <CustomButton ButtonTitle={'Login'} onPress={() => navigation.navigate('FeedScreen')} />
                                <View style={{marginTop: 20}}><Text style={{textAlign:"center"}}>Forgotten Password?</Text></View>
                            </View>
                        )
                    }}
                </Formik>
            </View>
            <View style={{flex: 0.2, marginBottom: 20, justifyContent: "flex-end"}} ><Text onPress={() => navigation.navigate('signup')}>Create new account</Text></View>
        </View>
    )
}

export default Login;