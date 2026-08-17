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