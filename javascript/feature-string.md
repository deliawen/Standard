
### 字符串

##### [强制] 字符串开头和结束使用单引号 `'`。

解释：

1. 输入单引号不需要按住 `shift`，方便输入。
2. 实际使用中，字符串经常用来拼接 HTML。为方便 HTML 中包含双引号而不需要转义写法。

示例：

```javascript
var str = '我是一个字符串';
var html = '<div class="cls">拼接HTML可以省去双引号转义</div>';
```

##### [建议] 使用 `数组` 或 `+` 拼接字符串。

解释：

1. 使用 `+` 拼接字符串，如果拼接的全部是 StringLiteral，压缩工具可以对其进行自动合并的优化。所以，静态字符串建议使用 `+` 拼接。
2. 在现代浏览器下，使用 `+` 拼接字符串，性能较数组的方式要高。
3. 如需要兼顾老旧浏览器，应尽量使用数组拼接字符串。

示例：

```javascript
// 使用数组拼接字符串
var str = [
    // 推荐换行开始并缩进开始第一个字符串, 对齐代码, 方便阅读.
    '<ul>',
        '<li>第一项</li>',
        '<li>第二项</li>',
    '</ul>'
].join('');

// 使用 `+` 拼接字符串
var str2 = '' // 建议第一个为空字符串, 第二个换行开始并缩进开始, 对齐代码, 方便阅读
    + '<ul>',
    +    '<li>第一项</li>',
    +    '<li>第二项</li>',
    + '</ul>';
```

##### [建议] 使用字符串拼接的方式生成HTML，需要根据语境进行合理的转义。

解释：

在 `JavaScript` 中拼接，并且最终将输出到页面中的字符串，需要进行合理转义，以防止安全漏洞。下面的示例代码为场景说明，不能直接运行。


示例：

```javascript
// HTML 转义
var str = '<p>' + htmlEncode(content) + '</p>';

// HTML 转义
var str = '<input type="text" value="' + htmlEncode(value) + '">';

// URL 转义
var str = '<a href="/?key=' + htmlEncode(urlEncode(value)) + '">link</a>';

// JavaScript字符串 转义 + HTML 转义
var str = '<button onclick="check(\'' + htmlEncode(strLiteral(name)) + '\')">提交</button>';
```


##### [建议] 复杂的数据到视图字符串的转换过程，选用一种模板引擎。

解释：

使用模板引擎有如下好处：

1. 在开发过程中专注于数据，将视图生成的过程由另外一个层级维护，使程序逻辑结构更清晰。
2. 优秀的模板引擎，通过模板编译技术和高质量的编译产物，能获得比手工拼接字符串更高的性能。
3. 模板引擎能方便的对动态数据进行相应的转义，部分模板引擎默认进行HTML转义，安全性更好。

- artTemplate: 体积较小，在所有环境下性能高，语法灵活。
- dot.js: 体积小，在现代浏览器下性能高，语法灵活。
- etpl: 体积较小，在所有环境下性能高，模板复用性高，语法灵活。
- handlebars: 体积大，在所有环境下性能高，扩展性高。
- hogon: 体积小，在现代浏览器下性能高。
- nunjucks: 体积较大，性能一般，模板复用性高。