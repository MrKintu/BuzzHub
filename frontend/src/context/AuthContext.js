import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import React, { createContext, useEffect, useState } from 'react';
import { BASE_URL } from '../config';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [userInfo, setUserInfo] = useState({});
    const [isLoading, setIsLoading] = useState(false);
    const [splashLoading, setSplashLoading] = useState(false);
    const [log, setLogin] = useState(false);
    const [data, setData] = useState([]);
    const [info, setInfo] = useState('')

    const register = (file_name, firstname, lastname, username, Dob, gender,bio, country, password) => {
        let formData = new FormData();
        formData.append('file_name',file_name);
        formData.append('username', username);
        formData.append('password', password);
        formData.append('email', 'tabhinav300@gmail.com');
        formData.append('first_name', firstname);
        formData.append('last_name', lastname);
        formData.append('doc_id', '12345');
        formData.append('dob', Dob);
        formData.append('doe', '2025-12-31');
        formData.append('bio', bio);
        formData.append('location', "oshawa");
        formData.append('country', country);

        console.log(formData);

        setIsLoading(true);
        axios({
            url: `${BASE_URL}users/sign-up/`,
            method: 'POST',
            data: formData,
            headers: {
                'content-type': 'multipart/form-data',
            }
        })
            .then(function (response) {
                console.log("response :", response.data);
                if(response.data){
                    login(username,password);
                }
                setIsLoading(false);

            })
            .catch(function (error) {
                console.log(error);
                setIsLoading(false);

            })

        // fetch(`${BASE_URL}users/sign-up/`, {
        //     method: 'post',
        //     body: formData,
        //     headers: {
        //         'Content-Type': 'multipart/form-data;',
        //     }
        // })
        //     .then((res => {
        //         console.log(res);
        //         // setUserInfo(userInfo);
        //         setIsLoading(false);
        //     }));
    };

    const login = async (username, password) => {
        console.log(username,password);
        let formdata = new FormData();
        formdata.append('username', username);
        formdata.append('password', password);
        console.log(formdata);

        axios({
            url: `${BASE_URL}users/sign-in/`,
            method: 'POST',
            data: formdata,
            headers: {
                'content-type': 'multipart/form-data',
            }
        })
            .then((response) => {
                console.log("response :", response.data);
                setLogin(response.data);
                setUserInfo(username);
                console.log(log);

            })
            .catch(function (error) {
                console.log(error);

            })
    }

    const launch = async () => {
        let formdata = new FormData();
        formdata.append('name', "Abhinav");
        console.log(formdata);

        axios({
            url: `${BASE_URL}/users/train-face/`,
            method: 'POST',
            data: formdata,
            headers: {
                'content-type': 'multipart/form-data',
            }
        })
            .then((response) => {
                console.log("response :", response.data);
                setLogin(response.data);
                console.log(log);

            })
            .catch(function (error) {
                console.log(error);

            })
    }

    const profile = async () => {


        axios({
            url: `${BASE_URL}/abhi001/`,
            method: 'GET',
           
        })
            .then((response) => {
                console.log(response.data);
                setInfo(response.data)

            })
            .catch(function (error) {
                console.log(error);

            })
    }

        


    // const login = async (username, password) => {
    //     let formData = new FormData();
    //     formData.append('username', username);
    //     formData.append('password', password);
    //     setIsLoading(true);

    //     let res = await fetch(`${BASE_URL}users/sign-in/`, {
    //         method: 'post',
    //         body: JSON.stringify(formData),
    //         headers: {
    //             'Content-Type': "application/json",
    //         }
    //     })
    //     res = await res.json();
    //     if (res) {
    //         console.warn(res);
    //     }
        // .then((res => {
        //     console.log(res);
        //     // setUserInfo(userInfo);
        //     setLogin(res);
        //     AsyncStorage.setItem('login', JSON.stringify(res));
        //     setIsLoading(false);
        // }));

        // axios
        //     .post(`${BASE_URL}/users/sign-in/`, 
        //         formData)
        //     .then(res => {
        //         console.log(res);
        //         // setUserInfo(userInfo);
        //         setLogin(res);
        //         AsyncStorage.setItem('login', JSON.stringify(res));
        //         setIsLoading(false);
        //     })
        //     .catch(e => {
        //         console.log(`login error ${e}`);
        //         setIsLoading(false);
        //     });
    // };

    const logout = () => {
        setIsLoading(true);
        fetch(`${BASE_URL}users/sign-out/`, {
            method: 'get'
        })
            .then((res => {
                console.log(res);
                setLogin(false);
                AsyncStorage.removeItem('login');
                setIsLoading(false);
            }));

        // axios
        //     .post(
        //         `${BASE_URL}/logout`,
        //         {},
        //         {
        //             headers: { Authorization: `Bearer ${userInfo.access_token}` },
        //         },
        //     )
        //     .then(res => {
        //         console.log(res.data);
        //         AsyncStorage.removeItem('userInfo');
        //         setUserInfo({});
        //         setIsLoading(false);
        //     })
        //     .catch(e => {
        //         console.log(`logout error ${e}`);
        //         setIsLoading(false);
        //     });
    };

    const uploadDoc = (dat) => {

        const formData = new FormData();
        formData.append('NewFile', {
            uri: dat.uri,
            name: dat.fileName,
            type: dat.type

        });
        setIsLoading(true);

        axios({
            url: `${BASE_URL}users/upload-ID/`,
            method: 'POST',
            data: formData,
            headers: {
                'content-type': 'multipart/form-data',
            }
        })
            .then(function (response) {
                console.log("response :", response.data);
                setData(response.data);
                setIsLoading(false);

            })
            .catch(function (error) {
                console.log(error);
            })

      
    }


    const isLoggedIn = async () => {
        try {
            setSplashLoading(true);

            let userInfo = await AsyncStorage.getItem('userInfo');
            userInfo = JSON.parse(userInfo);

            if (userInfo) {
                setUserInfo(userInfo);
            }

            setSplashLoading(false);
        } catch (e) {
            setSplashLoading(false);
            console.log(`is logged in error ${e}`);
        }
    };

    useEffect(() => {
        isLoggedIn();
    }, []);

    return (
        <AuthContext.Provider
            value={{
                isLoading,
                userInfo,
                splashLoading,
                register,
                login,
                logout,
                profile,
                log,
                data,
                launch,
                uploadDoc,
                info
            }}>
            {children}
        </AuthContext.Provider>
    );
};