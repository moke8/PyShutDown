# PyShutDown
<p>一开始只是单纯的想自动关机 </p>
<p>然后想方便点   点一下就自动关机。。。 那就bat批处理吧</p>
<p>呃。。。固定时间怎么行    必须有用户输入    哇输入的万一不是数字？？？</p>
<p>呃，，，字符串转数字   判断是不是数字？    bat好麻烦    那就用python吧   python简单点</p>
<p>呃，有设置定时关机就要有取消吧？</p>
<p>哇，都写好了   干脆做一个UI 编译成exe好了   还能给朋友用。</p>
<hr>
<p>以上大概就是项目背景。</p>
<p>一个学校晚上的无聊之作</p>
<hr>
<p><b>主要功能：</b></p>
<ul>
  <li>将毫秒转化为大家都经常使用的单位"小时"</li>
  <li>将得到的时间组合为批处理语句</li>
  <li>检测之前有没有关机任务，有则取消后执行批处理语句，没有则直接执行</li>
  <li>设置取消关机任务功能</li>
</ul>
 <p><b>使用方式：</b></p>
 <ol type="I">
 <li>直接在python环境下运行</li>
 <li>使用pyinstaller编译为exe文件运行
  <ol type="i">
   <li>安装pyinstaller（需要python环境）:<br>在命令行中执行<code>pip install pyinstaller</code></li>
   <li>用命令行打开文件所在目录<br>执行<code>pyinstaller -w -F py文件地址</code><br>其中 -F指打包成独立exe文件，-w指屏蔽命令行界面</li>
  </ol>
 </li>
</ol>
<p><b>图片：</b></p>

<img src="https://s2.ax1x.com/2019/03/01/kbGPcd.png" alt="kbGPcd.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kbG99e.png" alt="kbG99e.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kbGShD.png" alt="kbGShD.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kbGijA.png" alt="kbGijA.png" border="0">
