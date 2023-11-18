import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  Dimensions,
  Image,
  TouchableOpacity
} from 'react-native';
import { AppColor } from "../utils/appColors";
import SearchBox from '../components/SearchBox';
import Icon from 'react-native-vector-icons/FontAwesome';
import Tags from '../components/Tags';
import { useNavigation } from '@react-navigation/native';


const width = Dimensions.get('window').width;

const tags = [
  { icon: 'shopping-basket', tagName: 'Shop' },
  { icon: 'heart', tagName: 'Well-beight' },
  { icon: '', tagName: 'Travel' },
];

const SearchHomeScreen = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.container}>
      <View style={styles.headerWrapper}>
        <View style={styles.header}>
          <SearchBox />
          <Icon style={styles.qrCode} size={30} name="qrcode" />
        </View>
        <ScrollView horizontal={true} style={styles.tagWrapper}>
          <Tags tags={tags} />
        </ScrollView>
      </View>
      <ScrollView>
        <View style={styles.videoContainer} />
        <View>
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
        </View>
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
        <Image
          style={styles.footerIcon}
          source={require('../assets/images/profilePage/heart.png')}
        />
        <TouchableOpacity onPress={() => navigation.navigate('Profile')}>
          <Image
            style={styles.footerIcon}
            source={require('../assets/images/profilePage/profile.png')}
          />
        </TouchableOpacity>

      </View>
    </View>
  );
}

export default SearchHomeScreen;

export const styles = StyleSheet.create({
  container: {
    display: 'flex',
    flex: 1,
  },
  headerWrapper: {
    backgroundColor: AppColor.gray1,
  },
  header: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  qrCode: {
    padding: 10,
  },
  tagWrapper: {
    padding: 10,
  },
  videoContainer: {
    backgroundColor: AppColor.black,
    height: width,
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
  imagesWrapper: {
    flexDirection: 'row',
  },
  galleryIMage: {
    display: 'flex',
    flex: 1,
    height: 150,
    margin: 1,
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

  },
  footerIcon: {
    width: 35,
    height: 35,
    margin: 8
  },
  btnCam: {
    alignSelf: 'center',
    justifyContent: 'center',

  }
});
