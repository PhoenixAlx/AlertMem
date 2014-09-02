#!/usr/bin/env python
# #  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# Autor Alex Bueno ( @Phoenix_Alx)

#This script tell you if te RAM consume of one app is gretter than one limit 

import subprocess
import time
import sched

def getMem(n=1):
	#get the app with consume most high
	orden="ps aux | awk '{print $2, $4, $11}' | sort -k2r | head -n "+ str(n);
	salida=subprocess.check_output(orden,shell=True);
	info=salida.split(b' ');
	consume = float(info[1].decode('utf8'));
	nameApp=info[2].decode('utf8');
	valor=[consume,nameApp];
	return valor;
def umbral(datos,m=40):
	#check umbral
	d1=datos[0];
	d2=datos[1];
	if (d1>m):
		alerta(d2);
	return 0;
def alerta(app):
	#notify alert
	mensaje=app+u'alerta mem mire el top';
	subprocess.call(["notify-send", mensaje])
	subprocess.call(["echo", u' \x07 '])
	return 0;
def main():
	umbral(getMem(1),40);
	return 0;
def scheduler_mem():
	#control of time execution
	scheduler.enter(0, 1, main, ())
	scheduler.run()
	time.sleep(10)

scheduler = sched.scheduler(time.time, time.sleep);
while 1:
	scheduler_mem()
  

