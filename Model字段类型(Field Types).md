Models常用字段类型

======

# 常用字段参数：
- null， 是否可以为空；
- default， 默认值；
- primary_key， 主键；
- db_column， 列名；
- db_index， 索引；
- unique， 唯一索引；
- unique_for_date， unique_for_mouth， unique_for_year，
- auto_now， 创建时，自动生成时间
- auto_now_add， 更新时，自动更新时间
- choices， django admin 中显示下拉框，避免连表查询
- blank， django admin 是否可以为空
- verbose_name， django admin 显示字段中文
- editable， django admin 是否可以被编辑
- error_messages， 错误信息
- help_text， django admin 提示
- validators， django form ，自定义错误信息

# 常用字段：
**AutoField**
它是一个根据 ID 自增长的 IntegerField 字段。通常，你不必直接使用该字段。如果你没在别的字段上指定主 键，Django 就会自动添加主键字段。

**BigIntegerField**
64位整数，类似于IntegerField，范围从-9223372036854775808 到9223372036854775807。默认的form widget 是TextInput。

**BinaryField**
二进制

**BooleanField**
一个布尔值(true/false)字段。
默认的form widget是CheckboxInput。
如果要使用null作为空值，可使用NullBooleanField。

**CharField**
它是一个字符串字段，对小字符串和大字符串都适用。
对于更大的文本，应该使用TextField 。
默认的form widget是TextInput。
CharField 有一个必须传入的参数：max_length,字段的最大字符数。它作用于数据库层级和 Django 的数据验证层级。

**CommaSeparatedInterField**
它用来存放以逗号间隔的整数序列。和 CharField 一样，必须为它提供 max_length 参数。而且要注意不同数据库对 max_length 的限制。

**DateField**
该字段利用 Python 的 datetime.date 实例来表示日期。下面是它额外的可选参数：
DateField.auto_now：每一次保存对象时，Django 都会自动将该字段的值设置为当前时间。一般用来表示 "最后修改" 时间。要注意使用的是当前日期，而并非默认值，所以不能通过重写默认值的办法来改变保存时间。
DateField.auto_now_add：在第一次创建对象时，Django 自动将该字段的值设置为当前时间，一般用来表示对象创建时间。它使用的同样是当前日期，而非默认值。
默认的form widget是TextInput。
Note:当auto_now或者auto_now_add设置为True时，字段会有editable=True和blank=True的设定。

**DateTimeField**
该字段利用 datetime.datetime 实例表示日期和时间。该字段所按受的参数和 DateField 一样。
默认的form widget是TextInput。

**EmailField**
它是带有 email 合法性检测的A CharField 。
Note：最大长度默认为75，并不能存储所有与RFC3696/5321兼容的email地址。如果要存储所有，请设置 
max_length=254。设置为75是历史遗留问题。

**FileField**
文件上传字段
- 它有一个必须的参数：FileField.upload_to
用于保存文件的本地文件系统。它根据 MEDIA_ROOT 设置确定该文件的 url 属性。
该路径可以包含 时间格式串strftime()，可以在上传文件的时候替换成当时日期／时间
- instance ：定义了当前 FileField 的 model 实例。更准确地说，就是以该文件为附件的 model 实例。
- filename ：上传文件的原始名称。在生成最终路径的时候，有可能会用到它。
- 还有一个可选的参数：FileField.storage，负责保存和获取文件的对象。
默认的form widget是FileInput。

**FloatField**
该字段在 Python 中使用float 实例来表示一个浮点数。
- max_digits：总位数(不包括小数点和符号）
默认的form widget是TextInput。
请注意FloatField与DecimalField的区别。

**ForeignKey**
```例：
# Tag以Contect为外键，一个Contect可以对应多个Tag
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
```

**ImageField**
和 FileField 一样，只是会验证上传对象是不是一个合法的图象文件
除了那些在 FileField 中有效的参数之外， ImageField 还可以使用 File.height and File.width 两个属性 。
它有两个可选参数：
- ImageField.height_field，保存图片高度的字段名称。在保存对象时，会根据该字段设定的高度，对图片文件进行缩放转换。
- ImageField.width_field，保存图片宽度的字段名称。在保存对象时，会根据该字段设定的宽度，对图片文件进行缩放转换。
默认情况下， ImageField 实例对应着数据库中的varchar(100) 列。和其他字段一样，你可以使 用 max_length 参数来改变字段的最大长度。

**IntegerField**
整数字段。默认的form widget是TextInput。

**IPAddressField**
以字符串形式(比如 "192.0.2.30")表示 IP 地址字段。默认的form widget是TextInput。

**GenericIPAddressField**
以字符串形式(比如 "192.0.2.30"或者"2a02:42fe::4")表示 IP4或者IP6 地址字段。默认的form widget是TextInput。
- GenericIPAddressField.protocol，验证输入协议的有效性。默认值是 ‘both’ 也就是IPv4或者IPv6。该项不区分大小写。
- GenericIPAddressField.unpack_ipv4，解释IPv4映射的地址，像   ::ffff:192.0.2.1  。如果启用该选项，该地址将必解释为 192.0.2.1 。默认是禁止的。只有当 protocol 被设置为 ‘both’ 时才可以启用。

**NullBooleanField**
与 BooleanField 相似，但多了一个 NULL 选项。建议用该字段代替使用 null=True 选项的 BooleanField 。 
默认的form widget是NullBooleanSelect。

**PositiveIntegerField**
和 IntegerField 相似，但字段值必须是非负数。

**TextField**
大文本字段。默认的form widget是Textarea。

**TimeField**
该字段使用 Python 的 datetime.time 实例来表示时间。它和 DateField 接受同样的自动填充的参数。
默认的form widget是TextInput。

**URLField**
保存 URL 的 CharField 。
和所有 CharField 子类一样，URLField 接受可选的 max_length 参数，该参数默认值是200。