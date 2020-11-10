import json
import pprint

payload = '{"kvs":[{"at":"2020-10-21T19:56:47.000+0000","k":"audio-manager/default/LUM_LastHearedSourceMediaSinkFront","v":"Q"},{"at":"2020-10-21T19:56:47.000+0000","k":"hmi/icwidgets/WidgetConfiguration","v":[{"ENABLED_ROAD":true,"ENABLED_SPORT":true,"ENABLED_TRACK":true,"UUID":"87269ed8-0a73-47a4-a3d0-1762f94c1185","id":0},{"ENABLED_ROAD":true,"ENABLED_SPORT":true,"ENABLED_TRACK":true,"UUID":"c898bd91-f993-4a56-be16-37813d755f89","id":1}]},{"at":"2020-10-21T19:56:47.000+0000","k":"hmi/mainmenu/MainMenuCells","v":{"cells":[{"ID":0,"appletID":26,"keyLayoutType":1,"uuID":"d72513ef-2b7c-4c97-a772-e8a61b484c8e"},{"ID":1,"appletID":23,"keyLayoutType":1,"uuID":"7f9978d5-f082-4d09-9f65-5904dbeb9f8b"},{"ID":2,"appletID":33,"keyLayoutType":1,"uuID":"a475d54b-5480-4e32-ab6e-af885285168e"},{"ID":3,"appletID":54,"keyLayoutType":1,"uuID":"47bc63f7-6011-4aee-98ea-4a223eaf79b9"},{"ID":4,"appletID":0,"keyLayoutType":1,"uuID":"8375cecb-6764-4469-a252-e67dd532f973"},{"ID":5,"appletID":52,"keyLayoutType":1,"uuID":"22fb2a5e-7b93-41ee-b39b-8e6d20ba9798"},{"ID":6,"appletID":26,"keyLayoutType":1,"uuID":"a82f7967-e9fa-46df-a1d6-f233cb063a80"}]}},{"at":"2020-10-21T19:56:47.000+0000","k":"hmi/menudrawer/MenuDrawerSorting","v":[{"UUID":"b99d7aa3-b44e-4f33-b1f4-d5741eca50f5","id":0},{"UUID":"d209b5cb-7e43-45aa-b4e1-e5002c1343ec","id":1},{"UUID":"8889c516-915b-4983-8898-b851addc862b","id":2},{"UUID":"c202fcaa-e5a3-4d77-a8c9-b0f521e1bcff","id":3},{"UUID":"b0a0c4b8-bfe5-45ce-8ea6-ef8ab15f2df7","id":4},{"UUID":"0dc54a8f-dc76-4805-a228-c25165dbc75f","id":5},{"UUID":"1cb5922a-2cc7-4074-90b9-b92c55cc43ca","id":6},{"UUID":"d7f2b7e7-d0a8-44d8-a05b-6bb7d09a55c4","id":7},{"UUID":"47bc63f7-6011-4aee-98ea-4a223eaf79b9","id":8},{"UUID":"9eebd13c-44c3-43bf-babd-3b7cc31d050e","id":9},{"UUID":"31699827-f608-4fa9-87cb-ef48ee11a5e1","id":10},{"UUID":"33fb005b-2100-41d1-85df-24b614a37768","id":11},{"UUID":"54cfc5d4-145f-4f9c-ad8e-f89c79596f81","id":12},{"UUID":"f96279f0-1bb6-4df0-983a-7dc09e352057","id":13},{"UUID":"db77f849-88af-4f5b-862b-da5470b2da55","id":14},{"UUID":"456befcf-e149-4b94-ae83-fc6ca5454b9e","id":15},{"UUID":"31aaf7a8-8c47-4b13-a7d1-1dbc2d67e55d","id":16},{"UUID":"5eb40fea-6911-41e3-9c8a-f822d1e1f80e","id":17},{"UUID":"9c56e110-85af-4a4f-8312-5a4c438b3544","id":18},{"UUID":"607a29b6-afe9-49a4-9c67-765abab3e713","id":19},{"UUID":"b9a00dc6-546e-4644-af3e-d0c4ac4ca20a","id":20},{"UUID":"363f7d05-8433-43e0-b7c2-5af6d6c38874","id":21},{"UUID":"884aeb65-1d88-4106-9102-3801406f6641","id":22},{"UUID":"0c63a79d-a506-4c97-9388-70343e171d4d","id":23},{"UUID":"267da880-39a1-45f0-a8d7-81740c9300e8","id":24},{"UUID":"738f68b0-c1a7-40eb-b663-5b5b88687c54","id":25},{"UUID":"6c40d3cb-2d4b-4fac-934a-5e98da95152a","id":26},{"UUID":"6d8b1096-f5e5-4c76-86cb-5de58b07abcc","id":27},{"UUID":"83a3e44a-f8b2-4d10-a7b6-9e74533bfbd2","id":28}]},{"at":"2020-10-21T19:56:47.000+0000","k":"hmi/notificationcenter/GoodbyeScreenChannels","v":[{"UUID":"0012c2d3-fbe9-427f-b54f-d16c2e3f1926","enabled":true,"id":9},{"UUID":"20548618-6c0e-4ee2-9eca-6a2863ebc96b","enabled":true,"id":10},{"UUID":"24383299-5b71-4086-b2c0-92a64c5ee4ad","enabled":true,"id":11},{"UUID":"34580194-1573-499e-9926-563968e1044b","enabled":true,"id":12},{"UUID":"6062f088-e6c4-4858-8247-adce7168d879","enabled":true,"id":13},{"UUID":"7d9769ec-94b9-4413-9155-cd8af789abf0","enabled":true,"id":14},{"UUID":"9a10c423-5f7e-4ea8-bf88-727e6c282e3a","enabled":false,"id":15},{"UUID":"b3bab52b-3f4f-4834-9860-3aa52eb4c8d4","enabled":true,"id":16},{"UUID":"c334a132-2e37-4193-9d8c-10c669dcf6b5","enabled":true,"id":17}]},{"at":"2020-10-21T19:56:47.000+0000","k":"hmi/notificationcenter/NotificationCenterChannels","v":[{"UUID":"0012c2d3-fbe9-427f-b54f-d16c2e3f1926","enabled":true,"id":0},{"UUID":"20548618-6c0e-4ee2-9eca-6a2863ebc96b","enabled":true,"id":1},{"UUID":"24383299-5b71-4086-b2c0-92a64c5ee4ad","enabled":true,"id":2},{"UUID":"34580194-1573-499e-9926-563968e1044b","enabled":true,"id":3},{"UUID":"6062f088-e6c4-4858-8247-adce7168d879","enabled":true,"id":4},{"UUID":"7d9769ec-94b9-4413-9155-cd8af789abf0","enabled":true,"id":5},{"UUID":"9a10c423-5f7e-4ea8-bf88-727e6c282e3a","enabled":true,"id":6},{"UUID":"b3bab52b-3f4f-4834-9860-3aa52eb4c8d4","enabled":true,"id":7},{"UUID":"c334a132-2e37-4193-9d8c-10c669dcf6b5","enabled":true,"id":8}]},{"at":"2020-10-21T19:56:47.000+0000","k":"nav-controller/system/parkingConfiguration","v":{"parkingFinderAutomaticEnabled":true,"parkingThemeMapAutomaticEnabled":true}},{"at":"2020-10-21T19:56:47.000+0000","k":"nav-controller/system/enabledFeatures","v":[{"feature":"BanDay","id":1603310106139,"idAsString":"1603310106139"}]},{"at":"2020-10-21T19:56:47.000+0000","k":"perso/user/givenName","v":"Test"},{"at":"2020-10-21T19:56:47.000+0000","k":"perso/user/surname","v":"User"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x222_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x443_1","v":"0x55555550"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x444_1","v":"0x55555551"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x447_1","v":"0x55555552"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x448_1","v":"0x01000814"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x451_1","v":"0x01000814"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x881_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x887_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0x88a_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0xa21_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0xa22_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0xa25_1","v":"0x01000c14"},{"at":"2020-10-21T19:56:47.000+0000","k":"pia/default/0xa27_1","v":"0x01000c14"}]}'

payload_dict = json.loads(payload)

# pprint.pprint(payload_dict)

# print(type(payload))
# print(type(payload_dict))
# print(type(payload_dict["kvs"]))
# print(type(payload_dict["kvs"][-1]))
# print(type(payload_dict["kvs"][-1]["k"]))

# print(payload_dict["kvs"][-1]["k"])

# for i in range(len(payload_dict["kvs"])):
#     print(i)
#     print(payload_dict["kvs"][i])
#     print(payload_dict["kvs"][i].keys())
#     print(payload_dict["kvs"][i].get("k"))
#     print(payload_dict["kvs"][i]["k"])

PROVISIONING_DEFAULT_DATA = """
{
    "pers": {
        "-enabled": "true",
        "min_transfer_upload_timer_debounce": "10",
        "vehicle_trigger_partitions": "personalization/update",
        "vehicle_trigger_url": "com.bmw.perseus.int",
        "perseus_url": "https://perseus.e2e.cd-emea.bmw:6600/service/api/vehicle/v1/",
        "credentialinfo_url": "https://cac.e2e.cd-emea.bmw:6500/cac/credentialinfo/v1",
        "dpm_url": "https://dpm.e2e.cd-emea.bmw:6340/dpm/vehicle/v1",
        "create_account_url": "https://www.bmw-connecteddrive.de/app/de/index.htm/portal/register",
        "pw_reset_url": "https://reset_url.bmw.de"
    }
}
"""

provisioning_dict = json.loads(PROVISIONING_DEFAULT_DATA)

print(type(provisioning_dict))
provisioning_dict["pers"]["vehicle_trigger_url"] = "test"
print(provisioning_dict["pers"]["vehicle_trigger_url"])

provisioning_dict["pers"].update({"supported_profiles": "3"})

provisioning_str = json.dumps(provisioning_dict)
print(provisioning_str)
