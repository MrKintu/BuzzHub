import React, { useState, useContext, useEffect } from 'react';
import {
    Text,
    View,
    StyleSheet,
    Image,
    TouchableOpacity,
    ScrollView
} from 'react-native';
import { AppColor } from "../utils/appColors";
import { useNavigation } from '@react-navigation/native';
import { Alert, Modal, Pressable } from 'react-native';
import { AuthContext } from '../context/AuthContext';




const ProfileScreen = () => {

    const navigation = useNavigation();

    const [modalVisible, setModalVisible] = useState(false);
    const { logout,profile,info } = useContext(AuthContext);
    

    useEffect( () => {
    profile();
      }, []);


    return (
        <View style={styles.container}>
            <View style={styles.header}>
                <View style={styles.leftHeaderWrapper}>
                    <TouchableOpacity onPress={() => navigation.goBack()}>
                        <Image
                            style={{ height: 30, width: 35 }}
                            source={require('../assets/images/profilePage/leftArrow.png')}
                        />
                    </TouchableOpacity>
                    <Text style={styles.headerText}>{info?.profile?.user}</Text>
                </View>
                <TouchableOpacity style={styles.ButtonItemWrapper} onPress={() => setModalVisible(true)}>
                    <Image
                        style={styles.buttonIcon}
                        source={require('../assets/images/profilePage/dropdown.png')}
                    />
                </TouchableOpacity>
                {/* <Pressable
                    onPress={() => setModalVisible(true)}>
                    <Image
                        style={{ height: 50 }}
                        source={require('../assets/images/profilePage/threedots.png')}
                    />
                </Pressable> */}
                {/* <View onPress={() => setModalVisible(true)}>
                    <Image
                        style={{ height: 50 }}
                        source={require('../assets/images/profilePage/threedots.png')}
                    />
                </View> */}
            </View>
            <ScrollView>
                <View style={styles.ProfileSectionWrapper}>
                    <View style={styles.ImageSection}>
                        <Image
                            style={styles.instaImageBorder}
                            source={require('../assets/images/profilePage/storiescircle.png')}
                        />
                        <Image
                            style={styles.userImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.userName}>{info?.profile?.user}</Text>
                    </View>
                    <View style={styles.followersCountSection}>
                        <View style={styles.followingCount}>
                            <View>
                                <Text style={styles.countTitle}>334</Text>
                                <Text style={styles.countSubTitle}>Posts</Text>
                            </View>
                            <View>
                                <Text style={styles.countTitle}>211K</Text>
                                <Text style={styles.countSubTitle}>Followers</Text>
                            </View>
                            <View>
                                <Text style={styles.countTitle}>134</Text>
                                <Text style={styles.countSubTitle}>Following</Text>
                            </View>
                        </View>
                        {/* <View style={styles.buttonWrapper}>
                            <TouchableOpacity style={styles.messagesButtonWrapper}>
                                <Text style={styles.mesagesTitle}>Messages</Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={styles.ButtonItemWrapper}>
                                <Image
                                    style={styles.buttonIcon}
                                    source={require('../assets/images/profilePage/profielbuttonplus.png')}
                                />
                            </TouchableOpacity>
                           
                        </View> */}
                    </View>
                </View>
                <View style={styles.moreInfoWrapper}>
                    <Text style={styles.introText}>
                    {info?.profile?.bio}
                    </Text>
                    <Text style={styles.urlText}>{info?.profile?.country}</Text>
                </View>
                {/* <ScrollView style={styles.storiesWrapper} horizontal={true}>
                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 1</Text>
                    </View>
                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 2</Text>
                    </View>

                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 3</Text>
                    </View>

                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 4</Text>
                    </View>

                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 5</Text>
                    </View>

                    <View>
                        <Image
                            style={styles.storiesImage}
                            source={require('../assets/images/profilePage/face.jpeg')}
                        />
                        <Text style={styles.storyProfName}>Catherin 6</Text>
                    </View>
                </ScrollView> */}

                <View style={styles.viewIconsWrapper}>
                    <Image
                        source={require('../assets/images/profilePage/gridview.png')}
                    />
                    <Image
                        source={require('../assets/images/profilePage/listView.png')}
                    />
                    <Image
                        source={require('../assets/images/profilePage/profielplus.png')}
                    />
                </View>

                <ScrollView>
                    <View style={styles.imagesWrapper}>
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/1.jpg')}
                        />
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/2.jpg')}
                        />
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/4.jpg')}
                        />
                    </View>
                    <View style={styles.imagesWrapper}>
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/5.jpg')}
                        />
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/6.jpg')}
                        />
                        <Image
                            style={styles.galleryIMage}
                            source={require('../assets/images/profilePage/7.jpg')}
                        />
                    </View>
                </ScrollView>
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
            <Modal
                animationType="silde"
                transparent={true}
                visible={modalVisible}
                onRequestClose={() => {
                    Alert.alert('Modal has been closed.');
                    setModalVisible(!modalVisible);
                }}>
                <TouchableOpacity
                    style={styles.container}
                    activeOpacity={1}
                    onPressOut={() => { setModalVisible(!modalVisible); }}
                >
                    <View style={styles.centeredView}>
                        <View style={styles.modalView}>
                            {/* <Text style={styles.modalText}>Hello World!</Text> */}
                            <Pressable
                                style={[styles.button, styles.buttonClose]}
                                onPress={logout}>
                                <Text style={styles.textStyle}>Logout</Text>
                            </Pressable>
                        </View>
                    </View>
                </TouchableOpacity>
            </Modal>
        </View >
    )
}


export default ProfileScreen;

export const styles = StyleSheet.create({
    container: {
        display: 'flex',
        flex: 1,
    },
    header: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        height: 50
    },
    leftHeaderWrapper: {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
    },
    headerText: {
        fontSize: 20,
        fontWeight: '700',
    },
    ProfileSectionWrapper: {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
    },
    ImageSection: {
        display: 'flex',
        flex: 1,
        padding: 5,
    },
    followersCountSection: {
        display: 'flex',
        flex: 2,
    },
    instaImageBorder: {
        width: 130,
        height: 130,
    },
    userImage: {
        position: 'absolute',
        width: 115,
        height: 115,
        borderRadius: 70,
        margin: 13,
    },
    followingCount: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-evenly',
    },
    buttonWrapper: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        margin: 10,
    },
    messagesButtonWrapper: {
        borderRadius: 5,
        borderWidth: 2,
        borderColor: AppColor.gray1,
        width: '60%',
        padding: 4,
    },
    ButtonItemWrapper: {
        borderRadius: 5,
        borderWidth: 2,
        borderColor: AppColor.gray1,
        width: 50,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        margin: 3
    },
    buttonIcon: {
        width: 25,
        height: 25,
    },
    mesagesTitle: {
        fontWeight: '700',
        textAlign: 'center',
    },
    countTitle: {
        fontSize: 20,
        fontWeight: '700',
        textAlign: 'center',
    },
    countSubTitle: {
        color: AppColor.gray,
        textAlign: 'center',
    },
    userName: {
        fontSize: 19,
        fontWeight: '600',
        textAlign: 'center',
    },
    moreInfoWrapper: {
        marginLeft: 15,
    },
    introText: {
        fontSize: 16,
    },
    urlText: {
        color: AppColor.blue,
    },
    storiesImage: {
        borderRadius: 70,
        width: 70,
        height: 70,
        borderColor: AppColor.gray1,
        borderWidth: 3,
        marginRight: 10,
    },
    storiesWrapper: {
        padding: 15,
        borderBottomWidth: 2,
        borderBottomColor: AppColor.gray1,
    },
    storyProfName: {
        textAlign: 'center',
    },
    viewIconsWrapper: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    imagesWrapper: {
        flexDirection: 'row',
    },
    galleryIMage: {
        display: 'flex',
        flex: 1,
        height: 200,
        margin: 1,
    },
    footer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    footerIcon: {
        width: 35,
        height: 35,
        margin: 8
    },
    btnCam: {
        alignSelf: 'center',
        justifyContent: 'center',

    },
    centeredView: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 22,
    },
    modalView: {
        margin: 20,
        backgroundColor: 'white',
        borderRadius: 20,
        padding: 35,
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 4,
        elevation: 5,
    },
    button: {
        borderRadius: 20,
        padding: 10,
        elevation: 2,
    },
    buttonOpen: {
        backgroundColor: '#F194FF',
    },
    buttonClose: {
        backgroundColor: '#2196F3',
    },
    textStyle: {
        color: 'white',
        fontWeight: 'bold',
        textAlign: 'center',
    },
    modalText: {
        marginBottom: 15,
        textAlign: 'center',
    }
});
