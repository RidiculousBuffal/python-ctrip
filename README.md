# Python-Ctrip sdk

- 携程商旅python sdk (非官方)
- 参考 https://openapi.ctripbiz.com/#/serviceApi

## 支持功能
- SSO PC 跳转
- 人事信息批量开卡
- 获取对账单
- 城市信息查询 （这里在携程的上层做了一些模糊匹配的工作，已经不同国家地级市下方县级市的缓存，包括国家列表的缓存，不然真实用的时候会有麻烦，同时会缓存到本地的json中避免多次请求api开销，支持导出到json,从json导入缓存）
- 提前审批接口

## build
```bash
uv build
```

## 使用
假设下载whl后，把他放到如下的位置 
```txt
backend 
| 
|-- lib 
|---- python_ctrip-0.1.16-py3-none-any.whl 
```
### uv

```toml
[tool.uv.source]
python_ctrip = {path='backend/lib/python_ctrip-0.1.16-py3-none-any.whl'}
```
`uv sync`
### pip
```bash
pip install ./backend/lib/python_ctrip-0.1.16-py3-none-any.whl 
```


## 环境变量
应该是 xiecheng的，但是开发的时候打成了xiechen 就不改了~
```dotenv
XIECHEN_CORPORATE_ID=
XIECHEN_APP_KEY=
XIECHEN_APP_SECURITY=
XIECHEN_SUB_ACCOUNT_NAME=
```
默认读取环境变量，如果涉及到多个租户也可以自己传

### 查询城市信息示例

`BaseDataQueryClient` 内置了国家列表。调用方可以先通过国家名称取得 `countryId`，再按城市名称查询 POI 和城市信息：

```python

base_client = BaseDataClient(
    corporate_id="<CORPORATE_ID>",
    app_key="<APP_KEY>",
    app_security="<APP_SECURITY>",
    sub_account_name="<SUB_ACCOUNT>",
)
city_client = BaseDataQueryClient(base_client)

country = city_client.country_map.get("<COUNTRY_NAME>")
if country is None or country.countryId is None:
    raise ValueError("country is not available in the SDK country map")

try:
    response = await city_client.query(
        country_id=country.countryId,
        name="<CITY_NAME>",
    )
except NoDataException:
    # 没有匹配结果时由 SDK 抛出 NoDataException
    raise

city_items = [
    city
    for poi_data in (response.dataList or [])
    for city in (poi_data.prefectureLevelCityInfoList or [])
]

for city in city_items:
    print(city.cityId, city.cityName, city.cityCode)
```

返回值是 `QueryAllPOIInfoResponseType`。城市对象位于 `response.dataList[*].prefectureLevelCityInfoList[*]`，常用字段包括 `cityId`、`cityName`、`cityCode` 和 `cityEnName`。同一个 `BaseDataQueryClient` 实例会按 `(country_id, normalized_name)` 缓存查询结果；项目启动时会尝试导入对应模式的本地城市缓存。

### 上游审批到 SDK 模型的转换

1. 读取提交人和同行人，转换为差旅平台所需的员工 ID。
2. 根据审批表单中的行程模板构造 SDK 明细模型：
   - `FlightEndorsementDetail`
   - `HotelEndorsementDetail`
   - `TrainEndorsementDetail`
   - `CarQuickEndorsementDetail`
3. 查询国家、城市和城市 ID，填入对应的国家 ID、城市 ID/Code、日期和乘客列表。
4. 将项目、基金和消费事由转换为 `ExtendField`，字段名为 `CostCenter1`、`CostCenter2`、`CostCenter3`。（这个是下面例子的示例，并非强制要求，但是消费是由建议写到成本中心而非remark,不然对账单拉不出来） 
5. 组合成 `SaveApprovalRequest`，最后调用 `ApprovalClient.save_approval()`。
6. **建议让携程对接人员为企业打开城市向下兼容** 

简化后的 SDK 调用形态如下，示例字段均为占位值：

```python


client = ApprovalClient(
    corporate_id="<CORPORATE_ID>",
    app_key="<APP_KEY>",
    app_security="<APP_SECURITY>",
    sub_account_name="<SUB_ACCOUNT>",
)

request = SaveApprovalRequest(
    ApprovalNumber="<APPROVAL_NUMBER>",
    Status=1,
    EmployeeID="<EMPLOYEE_ID>",
    FlightEndorsementDetails=[
        FlightEndorsementDetail(
            ProductType="<DOMESTIC_OR_INTERNATIONAL_PRODUCT>",
            DepartCountryIds=["<DEPART_COUNTRY_ID>"],
            ArrivalCountryIds=["<ARRIVAL_COUNTRY_ID>"],
            DepartCityIds=["<DEPART_CITY_ID>"],
            ArrivalCityIds=["<ARRIVAL_CITY_ID>"],
            DepartDateBegin="<YYYY-MM-DD>",
            DepartDateEnd="<YYYY-MM-DD>",
            PassengerList=[PassengerDetail(EID="<TRAVELER_EID>")],
        )
    ],
    ExtendFieldList=[
        ExtendField(FieldName="CostCenter1", FieldValue="<PROJECT>"),
        ExtendField(FieldName="CostCenter2", FieldValue="<FUND>"),
        ExtendField(FieldName="CostCenter3", FieldValue="<REASON>"),
    ],
    Remark="<REMARK>",
)

result = await client.save_approval(request)
```
### 人员同步
```python

client = PeopleClient(
    corporate_id="<CORPORATE_ID>",
    app_key="<APP_KEY>",
    app_security="<APP_SECURITY>",
    sub_account_name="<SUB_ACCOUNT>",
)

items = [
    AuthenticationInfo(
        Sequence="<SEQUENCE>",
        Authentication=AuthenticationEntity(
            EmployeeID="<EMPLOYEE_ID>",
            Name="<NAME>",
            Nationality="CN",
            MobilePhone="<MOBILE>",
            Email="<EMAIL>",
            Valid="A",
            RankName="<RANK>",
            Dept1="<DEPARTMENT>",
        ),
    )
]
result = await client.save_corp_cust_info_list(items)

```

- 注意: 如果携程管理后台勾选了 自动绑定登录账号（勾选即表示贵司已获得员工授权并同意自动绑定添加员工时所填写的手机号或邮箱地址，绑定后用于员工登录），勾选了自动绑定手机号， **则业务系统应该即使关卡离职员工，避免员工入职新公司后又被绑定回了原公司导致需要找客服处理**

- 注意: 职级信息应先告诉携程的对接人员，让其先加入到职级列表后才能同步，否则会出现未配置职级的错误

- 注意: EID一旦确定不能更改（修改需要联系携程侧对接人员）

### SSO

```python

client = SSOClient(
    app_key="<APP_KEY>",
    app_security="<APP_SECURITY>",
)
ticket = await client.get_ticket()
fields = client.build_login_form_fields(
    ticket=ticket or "",
    employee_id="<EMPLOYEE_ID>",
    email="<EMAIL>",
    ta="<TRAVEL_ASSISTANT>",
    for_corp=0,
    cost1="<COST_CENTER_1>",
    cost2="<COST_CENTER_2>",
    cost3="<COST_CENTER_3>",
    init_page="<INITIAL_PAGE>",
    current_lang="zh-CN",
)
login_url = SSOClient.login_url()
```

注意： `UID`、`EmployeeID`、`Email` 至少需要提供一个。
