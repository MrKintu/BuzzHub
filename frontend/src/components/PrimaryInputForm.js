import React, {Component} from 'react';
import {Text, View, TextInput, StyleSheet} from 'react-native';
import { AppColor } from "../utils/appColors";

export class PrimaryInputForm extends Component {
  render() {
    const {placeHolderText} = this.props;
    return (
      <View style={styles.container}>
        <View style={styles.inputContainer}>
          <TextInput placeholder={placeHolderText} />
        </View>
      </View>
    );
  }
}

export default PrimaryInputForm;

const styles = StyleSheet.create({
  container: {
    display: 'flex',
  },
  inputContainer: {
    backgroundColor: AppColor.gray1,
    borderWidth: 0.5,
    borderColor: AppColor.gray,
    borderRadius: 5,
  },
});
