var ProcessSum=0;	//������
var Timeslice=0;//ʱ��Ƭ��С
var SumTime=0;//��ʱ��
var NowTime=0;//��ǰʱ��
var ReadyList=new Array() //��ǰ���̱�
//ProcessList=new Array(); �����ȫ������

//���ݽ���1������ֵ��������2���ɽ���1��ȷ��������
function CreateTable(){
	var input1=document.getElementById("input1");
	ProcessSum=parseInt(document.getElementById("processsum").value);
	Timeslice=parseInt(document.getElementById("timeslice").value);
	if ((ProcessSum != "1" && ProcessSum != "2" && ProcessSum != "3" && ProcessSum != "4" && ProcessSum != "5" && ProcessSum != "6" && ProcessSum != "7" && ProcessSum != "8" && ProcessSum != "9" && ProcessSum != "10")||(Timeslice != "1" && Timeslice != "2" && Timeslice != "3" && Timeslice != "4" && Timeslice != "5" && Timeslice != "6" && Timeslice != "7" && Timeslice != "8" && Timeslice != "9" && Timeslice != "10")) {
		alert("��ʾ��\n��������1~10\nʱ��Ƭ��1~10");
	}//�ж������Ƿ�Ϸ�
	else {
		input1.style.display = "none";//���ص�һ�������
		//���Ʊ��
		var data="";
		data+="<table id=\"table\">";
		//��һ��
		data+="<tr>"+"<th>���̺�</th>";
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
		//�ڶ���
		data+="<tr>"+"<th>����ʱ��</th>";
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
		//������
		data+="<tr>"+"<th>����ʱ��</th>";
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
		data+="<input id=\"return\" type=\"button\" value=\"����\" onClick=\"ReturnInput1()\"/ >"
		data+="</div><div>"
		data+="<input id=\"define\" type=\"button\" value=\"ȷ��\" onClick=\"Initialization()\"/ >"
		data+="</div></div>";
		document.getElementById("input2").innerHTML = data;
	}
}
//���ؽ�������ʱ��Ƭ��Сѡ����棨����1�����ɷ��ذ�ť����
function ReturnInput1() {
	location.reload();//ˢ�½���
	//ɾ�����
	//var parent=document.getElementById("input2");
	//var child=document.getElementById("table");
	//parent.removeChild(child);
	//child=document.getElementById("define");
	//parent.removeChild(child);
	//child=document.getElementById("return");
	//parent.removeChild(child);
	//input1.style.display = "inline";//��ʾ��һ�������
}
//������̵���������process
function process(processname,processnum,cometime,staytime) {
	this.processname=processname;				//����name
	this.processnum=processnum;					//���̱�Ŵ�1��ʼ
	this.cometime=cometime;							//����ʱ��
	this.staytime=staytime;								//����ʱ��
	this.laststaytime=staytime;							//ʣ�����ʱ��
	this.finishtime=0;										//���ʱ��
	this.usetime=0;											//��תʱ��
	this.weightedusetime=0;							//��Ȩ��תʱ��
}
//��ȡ����ĸ������̣�����ProcessList
function Initialization() {
	document.getElementById("define").style.display = "none";//���ص�һ�������
	//��ȡ�������ݲ��ж��Ƿ�Ϸ�
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
		alert("��������Чʱ�䣨����ʱ�䲻��Ϊ0��");
	}
	else {
		//������̱�
		ProcessList=new Array(); //ȫ�ֱ���
		for (var i=0;i<ProcessSum ;i++ ) {
			//Processprocessname=String.fromCharCode(65+i);
			//ProcessList[i].processnum=1+i;
			//ProcessList[i].cometime=parseInt(tempcome[i]);
			//ProcessList[i].staytime=parseInt(tempstay[i]);
			ProcessList[i]=new process(String.fromCharCode(65+i),1+i,parseInt(tempcome[i]),parseInt(tempstay[i]));
			SumTime+=parseInt(tempstay[i]);
		}
		//������ת����
		lunzhuan();
	}
}
//��ת����������������Initiailization()����
function lunzhuan() {
	updatelist();
	while (!checklistfinished())
	{
		if (ReadyList.length==0)
		{
			for (var i=0; i<Timeslice; i++)
			{
				showprocess(0);
				NowTime+=1; //ִ����һ����λʱ��
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
	//��ת������������
	showresultchart();
}
//���¾������У���ΪReadyList����lunzhuan()����
function updatelist() {
	for (var i=0; i<ProcessSum; i++)
	{
		if (ProcessList[i].cometime==NowTime)
		{
			ReadyList.push(ProcessList[i].processnum); //����������� .shift()������
		}
	}
}
//��鵥�������Ƿ���ɣ�������ִ������򷵻�true����֮false��ʱ��Ƭ�ڼ���ǵ���
function checkprocessfinished(processnum) {
	if (ProcessList[processnum-1].laststaytime==0)
	{
		return true;
	}
	else {
		return false;
	}
}
//����Ƿ����н���ȫ��ִ����ɣ�������ȫ��ִ������򷵻�true����֮false����lunzhuan()����
function checklistfinished() {
	var tag=true;
	for (var i=1; i<=ProcessSum; i++)
	{
		if (checkprocessfinished(i)==false)
		{
			tag=false;
		}
	}
	return tag; //������ȫ��ִ������򷵻�true����֮false
}
//���Ƶ�λʱ���
function showprocess(processnum) {
	document.getElementById("input3title").innerHTML = "ִ�й�����ʾ";
	var elem=document.createElement("div");
	var data="draw"+NowTime;
	var title;
	switch (processnum)
	{
		case 0:
			title="״̬������\n��ǰʱ�䣺"+NowTime;
			elem.setAttribute("class","drawws");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "-";
			break;
		case 1:
			title="״̬��A����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[0].staytime-ProcessList[0].laststaytime)+"\nʣ�����ʱ��"+ProcessList[0].laststaytime;
			elem.setAttribute("class","drawas");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "A";
			break;
		case 2:
			title="״̬��B����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[1].staytime-ProcessList[1].laststaytime)+"\nʣ�����ʱ��"+ProcessList[1].laststaytime;
			elem.setAttribute("class","drawbs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "B";
			break;
		case 3:
			title="״̬��C����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[2].staytime-ProcessList[2].laststaytime)+"\nʣ�����ʱ��"+ProcessList[2].laststaytime;
			elem.setAttribute("class","drawcs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "C";
			break;
		case 4:
			title="״̬��D����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[3].staytime-ProcessList[3].laststaytime)+"\nʣ�����ʱ��"+ProcessList[3].laststaytime;
			elem.setAttribute("class","drawds");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "D";
			break;
		case 5:
			title="״̬��E����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[4].staytime-ProcessList[4].laststaytime)+"\nʣ�����ʱ��"+ProcessList[4].laststaytime;
			elem.setAttribute("class","drawes");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "E";
			break;
		case 6:
			title="״̬��F����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[5].staytime-ProcessList[5].laststaytime)+"\nʣ�����ʱ��"+ProcessList[5].laststaytime;
			elem.setAttribute("class","drawfs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "F";
			break;
		case 7:
			title="״̬��G����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[6].staytime-ProcessList[6].laststaytime)+"\nʣ�����ʱ��"+ProcessList[6].laststaytime;
			elem.setAttribute("class","drawgs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "G";
			break;
		case 8:
			title="״̬��H����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[7].staytime-ProcessList[7].laststaytime)+"\nʣ�����ʱ��"+ProcessList[7].laststaytime;
			elem.setAttribute("class","drawhs");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "H";
			break;
		case 9:
			title="״̬��I����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[8].staytime-ProcessList[8].laststaytime)+"\nʣ�����ʱ��"+ProcessList[8].laststaytime;
			elem.setAttribute("class","drawis");
			elem.setAttribute("id",data);
			elem.setAttribute("title",title);
			document.getElementById("input3").appendChild(elem);
			document.getElementById(data).innerHTML = "I";
			break;
		case 10:
			title="״̬��J����\n��ǰʱ�䣺"+NowTime+"\n�ѷ���ʱ�䣺"+(ProcessList[9].staytime-ProcessList[9].laststaytime)+"\nʣ�����ʱ��"+ProcessList[9].laststaytime;
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
//ģ�����н��̣��ı�process��������ֵ
function doprocess(processnum) {
	ProcessList[processnum-1].finishtime=NowTime;
	ProcessList[processnum-1].usetime=(ProcessList[processnum-1].finishtime) - (ProcessList[processnum-1].cometime);
	ProcessList[processnum-1].laststaytime-=1;
}
//��������ֵ������ִ�����ʱ����
function countwut(processnum) {
	ProcessList[processnum-1].weightedusetime=(ProcessList[processnum-1].usetime)/(ProcessList[processnum-1].staytime);
}
//��ת���������ƽ��ͼ��
function showresultchart() {
	var data="";
	data+="<table id=\"table2\">";
	//��һ��
	data+="<tr>"+"<th>���̺�</th>";
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
	data+="<th>ƽ��</th>";
	data+="</tr>";
	//�ڶ���
	data+="<tr>"+"<th>����ʱ��</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].cometime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//������
	data+="<tr>"+"<th>����ʱ��</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].staytime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//������
	data+="<tr>"+"<th>���ʱ��</th>";
	for (var i=0; i<ProcessSum; i++)
	{
		data+="<td>";
		data+=ProcessList[i].finishtime;
		data+="</td>";
	}
	data+="<td>-</td>";
	data+="</tr>";
	//������
	data+="<tr>"+"<th>��תʱ��</th>";
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
	//������
	data+="<tr>"+"<th>��Ȩ��תʱ��</th>";
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