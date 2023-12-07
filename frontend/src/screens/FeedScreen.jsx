import React, { useState, useContext, useEffect } from 'react';
import { View, StyleSheet, ScrollView, Image, TouchableOpacity } from 'react-native';
import { AppColor } from "../utils/appColors";
import Feed from '../components/Feed';
import Stories from '../components/Stories';
import { AuthContext } from '../context/AuthContext';


import { useNavigation } from '@react-navigation/native';


const FeedScreen = () => {

    const navigation = useNavigation();

    const { profile } = useContext(AuthContext);

    useEffect( () => {
        profile();
          }, []);

    return (

        <View style={styles.container}>
            <View style={styles.header}>
                <Image
                    style={styles.icon}
                    source={require('../assets/images/camera.jpg')}
                />
                <Image
                    style={styles.logo}
                    source={require('../assets/images/instagramLogo.png')}
                />
                <View style={styles.headerRightWrapper}>
                    <Image
                        style={styles.icon}
                        source={require('../assets/images/igtv.png')}
                    />
                    <Image
                        style={styles.icon}
                        source={require('../assets/images/message.jpg')}
                    />
                </View>
            </View>
            <View style={styles.storiesWrapper}>
                <Stories />
            </View>

            <ScrollView style={styles.feedContainer}>
                <Feed />
            </ScrollView>
            <View style={styles.footer}>
                <TouchableOpacity onPress={() => navigation.navigate('FeedScreen')}>
                    <Image
                        style={styles.footerIcon}
                        source={require('../assets/images/profilePage/home.png')}
                    />
              
                </TouchableOpacity>

                <TouchableOpacity onPress={() => navigation.navigate('Search')}>
                    <Image
                        style={styles.footerIcon}
                        source={require('../assets/images/profilePage/search.png')}
                    />
                </TouchableOpacity>
                {/* <Image
                    style={styles.footerIcon}
                    source={require('../assets/images/profilePage/heart.png')}
                /> */}
                <TouchableOpacity onPress={() => navigation.navigate('Profile')}>
                    <Image
                        style={styles.footerIcon}
                        source={require('../assets/images/profilePage/profile.png')}
                    />
                </TouchableOpacity>

            </View>
        </View>
    )
}


export default FeedScreen;

export const styles = StyleSheet.create({
    container: {
        display: 'flex',
        flex: 1,
    },
    header: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        padding: 10,
        borderBottomColor: AppColor.gray1,
        borderBottomWidth: 1,
    },
    footer: {
        display: 'flex',
        flexDirection: 'row',
        bottom: 0,
        justifyContent: 'space-between',
        padding: 10,
        borderTopColor: AppColor.gray1,
        borderTopWidth: 1,
    },
    feedContainer: {
        display: 'flex',
    },
    icon: {
        width: 40,
        height: 40,
    },
    logo: {
        width: 150,
        height: '100%',
    },
    headerRightWrapper: {
        display: 'flex',
        flexDirection: 'row',
    },
    storiesWrapper: {
        backgroundColor: AppColor.gray1,
        borderBottomColor: AppColor.gray1,
        borderBottomWidth: 1,
    },
    footerIcon: {
        width: 35,
        height: 35,
        margin: 8
    },
    footer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    btnCam: {
        alignSelf: 'center',
        justifyContent: 'center',

    }
});
