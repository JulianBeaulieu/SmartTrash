import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_redux/flutter_redux.dart';
import 'package:hello_world/store/AppState.dart';
import 'package:hello_world/store/store.dart';
import 'package:hello_world/utils/notificationHelper.dart';
import 'package:intl/intl.dart';
import 'package:redux/redux.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'builder/NotificationSwitchBuilder.dart';
import 'builder/ReminderAlertBuilder.dart';
import 'builder/RemindersListViewBuilder.dart';
import 'models/index.dart';
import 'package:pubnub/pubnub.dart';

final pubnub = PubNub(//PubNub Connect
    defaultKeyset: Keyset(
        subscribeKey: 'sub-c-c13906c4-c6cd-11ea-a827-3a9bd744da8f',
        publishKey: 'pub-c-73bf7982-70fc-451d-9b62-b2f34032716e',
        uuid: UUID('Smart-Trash')
    )
);

final df = new DateFormat('dd-MM-yyyy hh:mm a');

final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
    FlutterLocalNotificationsPlugin();
NotificationAppLaunchDetails notificationAppLaunchDetails;
Store<AppState> store;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initStore();
  store = getStore();
  notificationAppLaunchDetails =
      await flutterLocalNotificationsPlugin.getNotificationAppLaunchDetails();
  await initNotifications(flutterLocalNotificationsPlugin);
  requestIOSPermissions(flutterLocalNotificationsPlugin);

  runApp(LaunchingApp(store));
}

class LaunchingApp extends StatelessWidget {
  final Store<AppState> store;
  LaunchingApp(this.store);

  @override
  Widget build(BuildContext context) {
    return StoreProvider<AppState>(
      child: MaterialApp(
          title: 'Smart Trash',
          theme: ThemeData(
            primaryColor: Color.fromARGB(255,35,35,35),
            canvasColor: Color.fromARGB(255,85,85,85),
          ),//Theme
          home: Scaffold(
            appBar: AppBar(
              title: Text('SmartTrash App'),
            ),
            body: Center(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.start,
                children: <Widget>[
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: <Widget>[
                      Padding(
                          padding: EdgeInsets.all(10),
                          child: ReminderAlertBuilder()),
                      Padding(
                          padding: EdgeInsets.all(10),
                          child: NotificationSwitchBuilder()),
                    ],
                  ),
                  Padding(
                      padding: EdgeInsets.all(10),
                      child: Text(
                        "Reminders",
                        style: TextStyle(
                            fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
                      )),
                  Padding(
                      padding: EdgeInsets.all(20),
                      child: Container(
                          decoration: BoxDecoration(
                            border: Border.all(
                              color: Colors.grey,
                              width: 2,
                            ),
                            borderRadius:
                                BorderRadius.all(Radius.circular(15.0)),
                          ),
                          child: SizedBox(
                            child: StoreConnector<AppState, List<Reminder>>(
                                converter: (store) =>
                                    store.state.remindersState.reminders,
                                builder: (context, reminders) {
                                  return RemindersList(reminders: reminders);
                                }),
                            height: Platform.isAndroid ? 420 : 550,
                          ))),
                ],
              ),
            ),
            bottomNavigationBar: BottomNavigationBar(
              items: const <BottomNavigationBarItem>[
                BottomNavigationBarItem(
                  icon: Icon(Icons.lock_open, color: Colors.black45,),
                  title: Text('Open', style: TextStyle(fontSize: 20, color: Colors.black),),
                ),
                BottomNavigationBarItem(
                  icon: Icon(Icons.lock, color: Colors.black45,),
                  title: Text('Close', style: TextStyle(fontSize: 20,color: Colors.black),),
                ),
              ],
              backgroundColor: Colors.grey,
              iconSize: 50,
            ),
          )),
      store: store,
    );
  }
}
