var ProcessSum=0;	//进程数
var Timeslice=0;//时间片大小
var SumTime=0;//总时间
var NowTime=0;//当前时间
var ReadyList=new Array() //当前进程表
//ProcessList=new Array(); 输入的全部进程

//根据界面1的输入值创建界面2，由界面1的确定键调用
function CreateTable(){
	var input1=document.getElementById("input1");
	ProcessSum=parseInt(document.getElementById("processsum").value);
	Timeslice=parseInt(document.getElementById("timeslice").value);
	if ((ProcessSum != "1" && ProcessSum != "2" && ProcessSum != "3" && ProcessSum != "4" && ProcessSum != "5" && ProcessSum != "6" && ProcessSum != "7" && ProcessSum != "8" && ProcessSum != "9" && ProcessSum != "10")||(Timeslice != "1" && Timeslice != "2" && Timeslice != "3" && Timeslice != "4" && Timeslice != "5" && Timeslice != "6" && Timeslice != "7" && Timeslice != "8" && Timeslice != "9" && Timeslice != "10")) {
		alert("提示！\n进程数：1~10\n时间片：1~10");
	}//判断输入是否合法
	else {
		input1.style.display = "none";//隐藏第一个输入框
		//绘制表格
		var data="";
		data+="<table id=\"table\">";
		//第一行
		data+="<tr>"+"<th>进程号</th>";
		for (var i=0; i<ProcessSum; i++)
		{
			switch(i) {
				case 0 :
					data+="<th>A</th>";
					break;
				case 1 :
					data+="<th>B</th>";
					break;
				case 2 :
					data+="<th>C</th>";
					break;
				case 3 :
					data+="<th>D</th>";
					break;
				case 4 :
					data+="<th>E</th>";
					break;
				case 5 :
					data+="<th>F</th>";
					break;
				case 6 :
					data+="<th>G</th>";
					break;
				case 7 :
					data+="<th>H</th>";
					break;
				case 8 :
					data+="<th>I</th>";
					break;
				case 9 :
					data+="<th>J</th>";
					break;
				default:
					break;
			}
		}
		data+="</tr>";
		//第二行
		data+="<tr>"+"<th>到达时间</th>";
		for (var i=0; i<ProcessSum; i++)
		{
			switch(i) {
				case 0 :
					data+="<td><input type=\"text\" id=\"comeA\"/></td>";
					break;
				case 1 :
					data+="<td><input type=\"text\" id=\"comeB\"/></td>";
					break;
				case 2 :
					data+="<td><input type=\"text\" id=\"comeC\"/></td>";
					break;
				case 3 :
					data+="<td><input type=\"text\" id=\"comeD\"/></td>";
					break;
				case 4 :
					data+="<td><input type=\"text\" id=\"comeE\"/></td>";
					break;
				case 5 :
					data+="<td><input type=\"text\" id=\"comeF\"/></td>";
					break;
				case 6 :
					data+="<td><input type=\"text\" id=\"comeG\"/></td>";
					break;
				case 7 :
					data+="<td><input type=\"text\" id=\"comeH\"/></td>";
					break;
				case 8 :
					data+="<td><input type=\"text\" id=\"comeI\"/></td>";
					break;
				case 9 :
					data+="<td><input type=\"text\" id=\"comeJ\"/></td>";
					break;
				default:
					break;
			}
		}
		data+="</tr>";
		//第三行
		data+="<tr>"+"<th>服务时间</th>";
		for (var i=0; i<ProcessSum; i++)
		{
			switch(i) {
				case 0 :
					data+="<td><input type=\"text\" id=\"stayA\"/></td>";
					break;
				case 1 :
					data+="<td><input type=\"text\" id=\"stayB\"/></td>";
					break;
				case 2 :
					data+="<td><input type=\"text\" id=\"stayC\"/></td>";
					break;
				case 3 :
					data+="<td><input type=\"text\" id=\"stayD\"/></td>";
					break;
				case 4 :
					data+="<td><input type=\"text\" id=\"stayE\"/></td>";
					break;
				case 5 :
					data+="<td><input type=\"text\" id=\"stayF\"/></td>";
					break;
				case 6 :
					data+="<td><input type=\"text\" id=\"stayG\"/></td>";
					break;
				case 7 :
					data+="<td><input type=\"text\" id=\"stayH\"/></td>";
					break;
				case 8 :
					data+="<td><input type=\"text\" id=\"stayI\"/></td>";
					break;
				case 9 :
					data+="<td><input type=\"text\" id=\"stayJ\"/></td>";
					break;
				default:
					break;
			}
		}
		data+="</tr>";
		data+="</table>";
		data+="<div><div>";
		data+="<input id=\"return\" type=\"button\" value=\"返回\" onClick=\"ReturnInput1()\"/ >"
		data+="</div><div>"
		data+="<input id=\"define\" type=\"button\" value=\"确定\" onClick=\"Initialization()\"/ >"
		data+="</div></div>";
		document.getElementById("input2").innerHTML = data;
	}
}
//返回进程数，时间片大小选择界面（界面1），由返回按钮调用
function ReturnInput1() {
	location.reload();//刷新界面
	//删除表格
	//var parent=document.getElementById("input2");
	//var child=document.getElementById("table");
	//parent.removeChild(child);
	//child=document.getElementById("define");
	//parent.removeChild(child);
	//child=document.getElementById("return");
	//parent.removeChild(child);
	//input1.style.display = "inline";//显示第一个输入框
}
//定义进程的数据类型process
function process(processname,processnum,cometime,staytime) {
	this.processname=processname;				//进程name
	this.processnum=processnum;					//进程编号从1开始
	this.cometime=cometime;							//到达时间
	this.staytime=staytime;								//服务时间
	this.laststaytime=staytime;							//剩余服务时间
	this.finishtime=0;										//完成时间
	this.usetime=0;											//周转时间
	this.weightedusetime=0;							//带权周转时间
}
//获取输入的各个进程，存入ProcessList
function Initialization() {
	document.getElementById("define").style.display = "none";//隐藏第一个输入框
	//获取进程数据并判断是否合法
	var tempcome=new Array();
	var tempstay=new Array();
	var tag=ProcessSum;
	switch(tag) {
		case 1:
			tempcome[0]=document.getElementById("comeA").value;
			tempstay[0]=document.getElementById("stayA").value;
			break;
		case 2:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			break;
		case 3:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			break;
		case 4:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			break;
		case 5:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			break;
		case 6:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempcome[5]=document.getElementById("comeF").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			tempstay[5]=document.getElementById("stayF").value;
			break;
		case 7:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempcome[5]=document.getElementById("comeF").value;
			tempcome[6]=document.getElementById("comeG").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			tempstay[5]=document.getElementById("stayF").value;
			tempstay[6]=document.getElementById("stayG").value;
			break;
		case 8:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempcome[5]=document.getElementById("comeF").value;
			tempcome[6]=document.getElementById("comeG").value;
			tempcome[7]=document.getElementById("comeH").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			tempstay[5]=document.getElementById("stayF").value;
			tempstay[6]=document.getElementById("stayG").value;
			tempstay[7]=document.getElementById("stayH").value;
			break;
		case 9:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempcome[5]=document.getElementById("comeF").value;
			tempcome[6]=document.getElementById("comeG").value;
			tempcome[7]=document.getElementById("comeH").value;
			tempcome[8]=document.getElementById("comeI").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			tempstay[5]=document.getElementById("stayF").value;
			tempstay[6]=document.getElementById("stayG").value;
			tempstay[7]=document.getElementById("stayH").value;
			tempstay[8]=document.getElementById("stayI").value;
			break;
		case 10:
			tempcome[0]=document.getElementById("comeA").value;
			tempcome[1]=document.getElementById("comeB").value;
			tempcome[2]=document.getElementById("comeC").value;
			tempcome[3]=document.getElementById("comeD").value;
			tempcome[4]=document.getElementById("comeE").value;
			tempcome[5]=document.getElementById("comeF").value;
			tempcome[6]=document.getElementById("comeG").value;
			tempcome[7]=document.getElementById("comeH").value;
			tempcome[8]=document.getElementById("comeI").value;
			tempcome[9]=document.getElementById("comeJ").value;
			tempstay[0]=document.getElementById("stayA").value;
			tempstay[1]=document.getElementById("stayB").value;
			tempstay[2]=document.getElementById("stayC").value;
			tempstay[3]=document.getElementById("stayD").value;
			tempstay[4]=document.getElementById("stayE").value;
			tempstay[5]=document.getElementById("stayF").value;
			tempstay[6]=document.getElementById("stayG").value;
			tempstay[7]=document.getElementById("stayH").value;
			tempstay[8]=document.getElementById("stayI").value;
			tempstay[9]=document.getElementById("stayJ").value;
			break;
		default:
			break;
	}
	var no=0;
	for (var i=0; i<ProcessSum; i++)
	{
		if ((/^\d+$/.test(tempcome[i]))&&((/^\d+$/.test(tempstay[i]))&&(tempstay[i]!=0)))
		{
		}
		else {
			no=1;
		}
	}
	if (no==1)
	{
		alert("请输入有效时间（服务时间不可为0）");
	}
	else {
		//存入进程表
		ProcessList=new Array(); //全局变量
		for (var i=0;i<ProcessSum ;i++ ) {
			//Processprocessname=String.fromCharCode(65+i);
			//ProcessList[i].processnum=1+i;
			//ProcessList[i].cometime=parseInt(tempcome[i]);
			//ProcessList[i].staytime=parseInt(tempstay[i]);
			ProcessList[i]=new process(String.fromCharCode(65+i),1+i,parseInt(tempcome[i]),parseInt(tempstay[i]));
			SumTime+=parseInt(tempstay[i]);
		}
		//调用轮转函数
		lunzhuan();
	}
}
//轮转函数（主函数）由Initiailization()调用
function lunzhuan() {
	updatelist();
	while (!checklistfinished())
	{
		if (ReadyList.length==0)
		{
			for (var i=0; i<Timeslice; i++)
			{
				showprocess(0);
				NowTime+=1; //执行完一个单位时间
				updatelist();
			}
		}
		else {
			var temp=ReadyList.shift();
			var finishedtag=false;
			for (var i=0; i<Timeslice; i++)
			{
				showprocess(temp);
				NowTime+=1;
				doprocess(temp);
				updatelist();
				if (checkprocessfinished(temp))
				{
					countwut(temp);
					finishedtag=true;
					break;
				}
			}
			if (finishedtag==false)
			{
				ReadyList.push(temp);
			}
		}
	}
	//轮转结束，输出结果
	showresultchart();
}
//更新就绪队列，存为ReadyList，由lunzhuan()调用
function updatelist() {
	for (var i=0; i<ProcessSum; i++)
	{
		if (ProcessList[i].cometime==NowTime)
		{
			ReadyList.push(ProcessList[i].processnum); //加入就绪队列 .shift()出队列
		}
	}
}
//检查单个进程是否完成，若进程执行完成则返回true，反之false，时间片内检测是调用
function checkprocessfinished(processnum) {
	if (ProcessList[processnum-1].laststaytime==0)
	{
		return true;
	}
	else {
		return false;
	}
}
//检查是否所有进程全部执行完成，若进程全部执行完成则返回true，反之false，由lunzhuan()调用
function checklistfinished() {
	var tag=true;
	for (var i=1; i<=ProcessSum; i++)
	{
		if (checkprocessfinished(i)==false)
		{
			tag=false;
		}
	}
	return tag; //若进程全部执行完成则返回true，反之false
}
//绘制单位时间块
function showprocess(processnum) {
	document.getElementById("input3title").innerHTML = "执行过程演示";
	var elem=document.createElement("div");
	var data="draw"+NowTime;
	var title;
	switch (processnum)
	{
		case 0:
			title="状态：空闲\n当前时间："+NowTime;
			elem.setAttribute("class","drawws");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "-";
			break;
		case 1:
			title="状态：A进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[0].staytime-ProcessList[0].laststaytime)+"\n剩余服务时间"+ProcessList[0].laststaytime;
			elem.setAttribute("class","drawas");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "A";
			break;
		case 2:
			title="状态：B进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[1].staytime-ProcessList[1].laststaytime)+"\n剩余服务时间"+ProcessList[1].laststaytime;
			elem.setAttribute("class","drawbs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "B";
			break;
		case 3:
			title="状态：C进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[2].staytime-ProcessList[2].laststaytime)+"\n剩余服务时间"+ProcessList[2].laststaytime;
			elem.setAttribute("class","drawcs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "C";
			break;
		case 4:
			title="状态：D进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[3].staytime-ProcessList[3].laststaytime)+"\n剩余服务时间"+ProcessList[3].laststaytime;
			elem.setAttribute("class","drawds");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "D";
			break;
		case 5:
			title="状态：E进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[4].staytime-ProcessList[4].laststaytime)+"\n剩余服务时间"+ProcessList[4].laststaytime;
			elem.setAttribute("class","drawes");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "E";
			break;
		case 6:
			title="状态：F进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[5].staytime-ProcessList[5].laststaytime)+"\n剩余服务时间"+ProcessList[5].laststaytime;
			elem.setAttribute("class","drawfs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "F";
			break;
		case 7:
			title="状态：G进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[6].staytime-ProcessList[6].laststaytime)+"\n剩余服务时间"+ProcessList[6].laststaytime;
			elem.setAttribute("class","drawgs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "G";
			break;
		case 8:
			title="状态：H进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[7].staytime-ProcessList[7].laststaytime)+"\n剩余服务时间"+ProcessList[7].laststaytime;
			elem.setAttribute("class","drawhs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "H";
			break;
		case 9:
			title="状态：I进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[8].staytime-ProcessList[8].laststaytime)+"\n剩余服务时间"+ProcessList[8].laststaytime;
			elem.setAttribute("class","drawis");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "I";
			break;
		case 10:
			title="状态：J进程\n当前时间："+NowTime+"\n已服务时间："+(ProcessList[9].staytime-ProcessList[9].laststaytime)+"\n剩余服务时间"+ProcessList[9].laststaytime;
			elem.setAttribute("class","drawjs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "J";
			break;
		default:
			break;
	}
	if (document.getElementsByName("W")!=undefined) {
		document.getElementsByName("W").innerHTML = "-";
	}
	if (document.getElementsByName("A")!=undefined) {
		document.getElementsByName("A").innerHTML = "A";
	}
	if (document.getElementsByName("B")!=undefined) {
		document.getElementsByName("B").innerHTML = "B"
	}
	if (document.getElementsByName("C")!=undefined) {
		document.getElementsByName("C").innerHTML = "C";
	}
	if (document.getElementsByName("D")!=undefined) {
		document.getElementsByName("D").innerHTML = "D";
	}
	if (document.getElementsByName("E")!=undefined) {
		document.getElementsByName("E").innerHTML = "E";
	}
	if (document.getElementsByName("F")!=undefined) {
		document.getElementsByName("F").innerHTML = "F";
	}
	if (document.getElementsByName("G")!=undefined) {
		document.getElementsByName("G").innerHTML = "G";
	}
	if (document.getElementsByName("H")!=undefined) {
		document.getElementsByName("H").innerHTML = "H";
	}
	if (document.getElementsByName("I")!=undefined) {
		document.getElementsByName("I").innerHTML = "I";
	}
	if (document.getElementsByName("J")!=undefined) {
		document.getElementsByName("J").innerHTML = "J";
	}
}
//模拟运行进程，改变process对象属性值
function doprocess(processnum) {
	ProcessList[processnum-1].finishtime=NowTime;
	ProcessList[processnum-1].usetime=(ProcessList[processnum-1].finishtime) - (ProcessList[processnum-1].cometime);
	ProcessList[processnum-1].laststaytime-=1;
}
//计算属性值，进程执行完成时调用
function countwut(processnum) {
	ProcessList[processnum-1].weightedusetime=(ProcessList[processnum-1].usetime)/(ProcessList[processnum-1].staytime);
}
//轮转结束，绘制结果图表
function showresultchart() {
	var data="";
	data+="<table id=\"table2\">";
	//第一行
	data+="<tr>"+"<th>进程号</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		switch(i) {
			case 0 :
				data+="<th>A</th>";
				break;
			case 1 :
				data+="<th>B</th>";
				break;
			case 2 :
				data+="<th>C</th>";
				break;
			case 3 :
				data+="<th>D</th>";
				break;
			case 4 :
				data+="<th>E</th>";
				break;
			case 5 :
				data+="<th>F</th>";
				break;
			case 6 :
				data+="<th>G</th>";
				break;
			case 7 :
				data+="<th>H</th>";
				break;
			case 8 :
				data+="<th>I</th>";
				break;
			case 9 :
				data+="<th>J</th>";
				break;
			default:
				break;
		}
	}
	data+="<th>平均</th>";
	data+="</tr>";
	//第二行
	data+="<tr>"+"<th>到达时间</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].cometime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//第三行
	data+="<tr>"+"<th>服务时间</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].staytime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//第四行
	data+="<tr>"+"<th>完成时间</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].finishtime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//第五行
	data+="<tr>"+"<th>周转时间</th>";
	var tempnum=0;
	for (var i=0; i<ProcessSum; i++)
	{
		tempnum+=ProcessList[i].usetime;
		data+="<td>";
		data+=ProcessList[i].usetime;
		data+="</td>";
	}
	tempnum=tempnum/ProcessSum;
	data+="<td>";
	data+=tempnum.toFixed(2);
	data+="</td>";
	data+="</tr>";
	//第六行
	data+="<tr>"+"<th>带权周转时间</th>";
	tempnum=0;
	for (var i=0; i<ProcessSum; i++)
	{
		tempnum+=ProcessList[i].weightedusetime;
		data+="<td>";
		data+=ProcessList[i].weightedusetime.toFixed(2);
		data+="</td>";
	}
	tempnum=tempnum/ProcessSum;
	data+="<td>";
	data+=tempnum.toFixed(2);
	data+="</td>";
	data+="</tr>";
	data+="</table>";
	document.getElementById("input4").innerHTML = data;
}