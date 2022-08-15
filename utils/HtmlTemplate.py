import time

from bean.CheckResponseResult import CheckResponseResult
from config.JarProjectUtil import JarProjectUtil


class HtmlTemplate:

    def generateHtmlReport(self,checkResponseResult: CheckResponseResult = None) -> str:
        # 文件名
        fileName = 'index_'+str(checkResponseResult.get_millis())+".html"
        # 项目根目录
        path = JarProjectUtil.project_root_path()
        # 获取Html和结果的组装数据
        modulInfo = HtmlTemplate().initHtmlModul(checkResponseResult)
        # 组装地址
        address = path+fileName
        f = open(address,"a")
        f.write(modulInfo)
        f.close()
        return address

    def initHtmlModul(self,checkResponseResult: CheckResponseResult = None) -> str:
        sb = ""
        sb += ("<!doctype html>\n" +
               "<html lang=\"zh-CN\">\n" +
               "  <head>\n" +
               "    <meta charset=\"utf-8\">\n" +
               "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n" +
               "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" +
               "    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->\n" +
               "    <title>自动化接口测试报告</title>\n" +
               "\n" +
               "    <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\" integrity=\"sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu\" crossorigin=\"anonymous\">\n" +
               "      <script src=\"https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js\"></script>\n" +
               "      <script src=\"https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js\"></script>\n" +
               "\n" +
               "\n" +
               "  </head>\n");

        sb += ("  <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->\n" +
               "    <script src=\"https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js\" integrity=\"sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ\" crossorigin=\"anonymous\"></script>\n" +
               "    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->\n" +
               "    <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js\" integrity=\"sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd\" crossorigin=\"anonymous\"></script>\n");

        sb += ("<script>\n" +
               "\n" +
               "// 执行加载方法之后,设置.样式.\n" +
               "var up = function updates(){\n" +
               "  //使用id选择器;例如:tab对象->tr->td对象.\n" +
               "  $(\".centerContentTd\").each(function(i){\n" +
               "  //获取td当前对象的文本,如果长度大于25;\n" +
               "  if($(this).text().length>100){\n" +
               "  //给td设置title属性,并且设置td的完整值.给title属性.\n" +
               "  $(this).attr(\"title\",$(this).text());\n" +
               "  //获取td的值,进行截取。赋值给text变量保存.\n" +
               "  var text=$(this).text().substring(0,60)+\"...\";\n" +
               "  //重新为td赋值;\n" +
               "  $(this).text(text);\n" +
               "\n" +
               "      }\n" +
               "    });\n" +
               "}\n" +
               "\n" +
               "var dataHandel = function getDataResult(millers){\n" +
               "  $.getJSON(\"http:121.199.33.137:8089/searchReport?millis=\"+millers,function(data){\n" +
               "    var result = '';\n" +
               "    result+= '<table  class=\"table table-striped table-bordered table-hover table-condensed\">'\n" +
               "    result+= '<thead>'\n" +
               "    result+= '<tr>'\n" +
               "    result+= '<th width=5px>#</th>'\n" +
               "    result+= '<th width=80px>名称</th>'\n" +
               "    result+= '<th width=80px>执行结果</th>'\n" +
               # // "    // result+= '<th>请求头</th>'\n" +
               # // "    result+= '<th width=100px>请求链接及其请求参数</th>'\n" +
               # // "    result+= '<th>返回信息</th>'\n" +
               "    result+= '<th width=80px>错误信息</th>'\n" +
               "    result+= '</tr>'\n" +
               "    result+= '</thead>'\n");
        # // 这里需要替换
        sb += ("$.each(data.resultInfList,function(idx,item){\n" +
               # // "        if(idx==0){\n" +
               # // "          return true;\n" +
               # // "        }\n" +
               "        result+= '<tbody>'\n" +
               "        result+= '<tr>'\n" +
               "        result+= '<td>'+(idx+1)+'</td>'\n" +
               # // "        result+= '<td>'+item.interfaceName+'</td>'\n" +
               "        result+= '<td>'+item.test_case_name+'</td>'\n" +
               "        if(item.inf_end==true){\n" +
               "          result+= '<td>Pass</td>'\n" +
               "        }else if(item.inf_end==false){\n" +
               "          result+= '<td>Fail</td>'\n" +
               "        }\n" +
               # // "        // result+= '<td>'+item.infRequestHeader+'</td>'\n" +
               # // "        result+= '<td class=\"centerContentTd\">'+item.infRequestParam+'</td>'\n" +
               # // "        result+= '<td class=\"centerContentTd\">'+item.infReturnMsg+'</td>'\n" +
               "        if(item.errorMsg !== undefined){\n" +
               "          result+= '<td class=\"centerContentTd\">'+item.error_msg+'</td>'\n" +
               "        }\n" +
               "        result+= '</tr>'\n" +
               "        result+= '</tbody>'\n" +
               "    });");
        # // 改变id
        sb += ("result+= '</table>'\n" +
               "\n" +
               "  $(\"#tt\").after(result);" +
               "\n" +
               "\n" +
               "    setTimeout(function()\n" +
               "      {\n" +
               "          if($('.centerContentTd').is(':visible'))\n" +
               "            up();\n" +
               # // "          else\n" +
               "      }, 3);\n" +
               "  });\n" +
               "}");

        sb += ("</script>\n");

        sb += ("  <body>\n" +
               "\t\t<div id='contents' class=\"container\">\n" +
               "\t<h2>表格</h2>\n" +
               "\t<p>总执行结果:</p>\n" +
               "\t<table id='moban' class=\"table table-striped table-bordered table-hover table-condensed\">\n" +
               "\t\t<thead>\n" +
               "\t\t\t<tr>\n" +
               "\t\t\t\t<th>#</th>\n" +
               "\t\t\t\t<th>模块名称</th>\n" +
               "\t\t\t\t<th>结果</th>\n" +
               "\t\t\t</tr>\n" +
               "\t\t</thead>\n" +
               "\t\t<tbody>");

        if checkResponseResult is not None:
            sb += "<tr>"

            sb += "<td>"
            sb += str(1)
            sb += "</td>";

            sb += "<td>";
            sb += (checkResponseResult.get_msg())
            sb += "</td>"

            sb += "<td>"
            sb += (str(checkResponseResult.get_result()))
            sb += "</td>";

            sb += "<td width='100px'>"
            # 这里是发送请求获取总报告下的所有接口信息
            sb += (
                        "<button id=\"" + str(checkResponseResult.get_millis()) + "\" type=\"button\" onclick=\"dataHandel('" + str(checkResponseResult.get_millis()) + "')\" class=\"btn btn-success dropdown-toggle \" ><span  aria-hidden=\"true\"  ></span> 查看</button>\n");
            sb += "</td>"

            sb += "<tr/>"

        sb += ("\t\t</tbody>\n" +
               "\t</table>\n" +
               "</div>\n")

        sb += "<div id=\"tt\" class=\"container\"></div>\n";
        sb += ("\t</body>\n" +
               "</html>")
        return sb


if __name__ == '__main__':
    result = CheckResponseResult()
    result.set_result(False)
    result.set_msg("hhhh")
    result.set_millis(int(round(time.time()*1000)))
    var = HtmlTemplate.generateHtmlReport(result)
    print(var)
