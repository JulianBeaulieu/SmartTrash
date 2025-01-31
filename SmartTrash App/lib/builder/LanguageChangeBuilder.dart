import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:hello_world/main.dart';

class LanguageChangeBuilder extends StatefulWidget {
  LanguageChangeBuilder({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _LanguageChangeBuilderState createState() => _LanguageChangeBuilderState();
}

class _LanguageChangeBuilderState extends State<LanguageChangeBuilder> {
  String dropValue = 'English';
  double margin = Platform.isIOS ? 10 : 5;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          RaisedButton(
            child: Text('Change Language'),
            color: Colors.black45,
            onPressed: _showMaterialDialog,
            textColor: Colors.white,
          ),
        ],
      ),
    );
  }

  _showMaterialDialog() {
    showDialog(
        context: context,
        barrierDismissible: true,
        builder: (BuildContext context) {
          return AlertDialog(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(Radius.circular(10.0))),
              contentPadding: EdgeInsets.all(0.0),
              backgroundColor: Colors.grey,
              content: StatefulBuilder(
                  builder: (BuildContext context, StateSetter setState) {
                    return Center(
                      child: Container(
                        width: MediaQuery.of(context).size.width - 10,
                        height: MediaQuery.of(context).size.height - 80,
                        padding: EdgeInsets.all(20),
                        color: Colors.grey,
                        child: Column(
                          children: [
                            Padding(
                                padding: new EdgeInsets.only(
                                    bottom: margin, top: margin),
                                  child: DropdownButton<String>(
                                    value: dropValue,
                                    icon: Icon(Icons.arrow_drop_down),
                                    iconSize: 40,
                                    itemHeight: 100,
                                    elevation: 05,
                                    dropdownColor: Color.fromARGB(255, 130, 130, 130),
                                    focusColor: Color.fromARGB(255, 80, 80, 80),
                                    style: TextStyle( fontSize: 48, color: Color.fromARGB(255, 255, 255, 255)),
                                    onChanged: (String newValue){
                                      setState((){
                                        dropValue = newValue;
                                      });
                                    },
                                    items: <String>['English','German','Arabic','Spanish','Chinese'].map<DropdownMenuItem<String>>((String value){
                                      return DropdownMenuItem<String>(
                                        value: value,
                                        child:Text(value),
                                        onTap: (){
                                          if(value == 'English')
                                            pubnub.publish('Trash-Client', {"requester":"App","trigger":"languageChange","status":0});
                                          else if(value == 'German')
                                            pubnub.publish('Trash-Client', {"requester":"App","trigger":"languageChange","status":1});
                                          else if(value == 'Arabic')
                                            pubnub.publish('Trash-Client', {"requester":"App","trigger":"languageChange","status":2});
                                          else if(value == 'Spanish')
                                            pubnub.publish('Trash-Client', {"requester":"App","trigger":"languageChange","status":3});
                                          else if(value == 'Chinese')
                                            pubnub.publish('Trash-Client', {"requester":"App","trigger":"languageChange","status":4});
                                        },
                                      );
                                    }).toList(),
                                  ),
                            ),
                            Padding(
                                padding: new EdgeInsets.only(
                                      top: margin * 2, bottom: margin),
                                child: RaisedButton(
                                    color: Colors.black45,
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                    child: Text(
                                      "Close",
                                      style: TextStyle(color: Colors.white),
                                    )),
                            ),
                            Padding(
                                padding: new EdgeInsets.only(
                                    bottom: margin, top: margin),
                                child: Text(
                                  'Language of the app itself will not change, this '
                                      'is used to change the language that the trashcan'
                                      ' speaker will use',
                                  style: TextStyle(
                                      fontSize: 16,
                                      color: Colors.black,
                                      decoration: TextDecoration.none,
                                      fontWeight: FontWeight.w500),
                                )
                            ),
                          ],
                        ),
                      ),
                    );
                  }));
        });
  }

}
