import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:hello_world/actions/actions.dart';
import 'package:hello_world/main.dart';
import 'package:hello_world/models/index.dart';
import 'package:hello_world/store/store.dart';
import 'package:hello_world/utils/notificationHelper.dart';

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
                                    items: <String>['English','Spanish','German','French'].map<DropdownMenuItem<String>>((String value){
                                      return DropdownMenuItem<String>(
                                        value: value,
                                        child:Text(value),
                                        onTap: (){
                                          pubnub.publish('Trash-Client', {'text': 'Language: ' + value});
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
                          ],
                        ),
                      ),
                    );
                  }));
        });
  }

}
