import { View, Text, Pressable } from 'react-native';
import React, { useState, useContext , useEffect} from 'react';
import InputBox from '../../components/inputBox';
import CustomButton from '../../components/customButton';
import DatePick from '../../components/datePick';
import { useNavigation } from '@react-navigation/native';
import { AuthContext } from '../../context/AuthContext';



const Signup = () => {
    const navigation = useNavigation();
    const { register,data } = useContext(AuthContext);

    const [username, setUsername] = useState(null);
    const [firstname, setFirstname] = useState(null);
    const [password, setPassword] = useState(null);
    const [lastname, setLastname] = useState(null);
    const [Dob, setDob] = useState(null);
    const [bio, setBio] = useState(null);
    const [gender, setGender] = useState(null);
    const [country, setCountry] = useState(null);

    useEffect( () => {
        setFirstname(data.details?.first_name);
        setLastname(data.details?.last_name);
        setDob(data.details?.DOB);
        setCountry(data.details?.country);
        console.log("ooo",data);

      }, []);


    

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-between' }}>
            <View style={{ flex: 1, justifyContent: 'center' }}>
                <Text style={{ fontSize: 20, fontWeight: 700, marginBottom: 20, textAlign: "center" }}>Enter details</Text>
                
                            <View>
                                <InputBox placeholder={'First Name'}
                                    OnChangedText={text => setFirstname(text)}
                                    value={firstname}
                                />
                                <InputBox placeholder={'Last Name'}
                                    OnChangedText={text => setLastname(text)}
                                    value={lastname}
                                />
                                <InputBox placeholder={'Username'}
                                    OnChangedText={text => setUsername(text)}
                                    value={username}
                                />

                                <InputBox placeholder={'Password'}
                                    OnChangedText={text => setPassword(text)}
                                    value={password}
                                    // touched={touched.password}
                                    // errors={errors.password}
                                    securetextEntry={true}

                                />
                                <InputBox placeholder={'Bio'}
                                    OnChangedText={text => setBio(text)}
                                    value={bio}
                                    // touched={touched.password}
                                    // errors={errors.password}
                                />

                                <InputBox placeholder={'Date of Birth'}
                                    OnChangedText={text => setDob(text)}
                                    value={Dob}
                                    // touched={touched.password}
                                    // errors={errors.password}

                                />

                                {/* <DatePick value={Dob} title={"Date of Birth"} /> */}
                                {/* <InputBox placeholder={'Gender'}
                                    OnChangedText={text => setGender(text)}
                                    onBlur={handleBlur('Gender')}
                                    value={gender}
                                    touched={touched.Gender}
                                    errors={errors.Gender}
                                /> */}
                                <InputBox placeholder={'Country'}
                                    OnChangedText={text => setCountry(text)}
                                    value={country}
                                />
                                <CustomButton ButtonTitle={'Sign Up'} onPress={() => register(data.file_name, firstname, lastname, username, Dob, gender,bio, country,password)}  />
                            </View>
                       
            </View>
            <Pressable style={{ marginBottom: 10, justifyContent: "flex-end" }}><Text onPress={() => navigation.navigate('Login')}>Login</Text></Pressable>
        </View>
    )
}

export default Signup;