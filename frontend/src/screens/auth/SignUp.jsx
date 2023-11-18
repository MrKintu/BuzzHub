import { View, Text} from 'react-native';
import React from 'react';
import { Formik } from 'formik';
import { SignupInitialValue, SignupValidationSchema } from './utils';
import InputBox from '../../components/inputBox';
import CustomButton from '../../components/customButton';
import DatePick from '../../components/datePick';
import{useNavigation} from'@react-navigation/native';


const Signup = () => {
    const navigation = useNavigation();
    const handleSignup = () => {
        console.log("Signed in");
    }

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-between' }}>
            <View style={{ flex: 1, justifyContent: 'center' }}>
                <Text style={{fontSize:20, fontWeight: 700, marginBottom:20, textAlign:"center"}}>Enter details</Text>
                <Formik
                    initialValues={SignupInitialValue}
                    validationSchema={SignupValidationSchema}
                    onSubmit={handleSignup}>
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
                                <InputBox placeholder={'First Name'}
                                    OnChangedText={handleChange('First Name')}
                                    onBlur={handleBlur('First Name')}
                                    value={values.firstName}
                                    touched={touched.firstName}
                                    errors={errors.firstName} 
                                    />
                                    <InputBox placeholder={'Last Name'}
                                    OnChangedText={handleChange('Last Name')}
                                    onBlur={handleBlur('Last Name')}
                                    value={values.lastName}
                                    touched={touched.lastName}
                                    errors={errors.lastName} 
                                    />
                                    <InputBox placeholder={'Date of Birth'}
                                    OnChangedText={handleChange('Date of Birth')}
                                    onBlur={handleBlur('Date of Birth')}
                                    value={values.DOB}
                                    touched={touched.DOB}
                                    errors={errors.DOB} 
                                    />
                                    <DatePick title={"Date of Birth"} />
                                    <InputBox placeholder={'Gender'}
                                    OnChangedText={handleChange('Gender')}
                                    onBlur={handleBlur('Gender')}
                                    value={values.Gender}
                                    touched={touched.Gender}
                                    errors={errors.Gender} 
                                    />
                                    <InputBox placeholder={'Country'}
                                    OnChangedText={handleChange('Country')}
                                    onBlur={handleBlur('Country')}
                                    value={values.country}
                                    touched={touched.country}
                                    errors={errors.country} 
                                    />  
                                <CustomButton ButtonTitle={'Sign Up'} onPress={handleSubmit} disabled={!isValid} />
                            </View>
                        )
                    }}
                </Formik>
            </View>
            <View style={{flex: 0.2, marginBottom: 20, justifyContent: "flex-end"}}><Text onPress={() => navigation.goBack()}>Login</Text></View>
        </View>
    )
}

export default Signup;