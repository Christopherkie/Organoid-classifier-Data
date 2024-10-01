

imagepath="C:/img/";
subtype="16992"
totimgname=imagepath+getInfo("image.title");
//saveAs("tiff", totimgname);
min=0
max=nSlices
//min = getNumber("min:", min);
max = getNumber("max:", min);
for (i = 1; i <= nSlices; i++) {
    setSlice(i);
    if(i<	min) {
    	continue
    }
    else{if(i>max){
    	continue
    	}
    	else{
		    resetMinAndMax();
		    run("Enhance Contrast", "saturated=0.35");
		    wait(150);
		    
		    imgph=getInfo("image.title");
		    img=substring(imgph,0,lengthOf(imgph)-4);
		    //print(img);
		   if(i<10){
		    	imagename=imagepath+subtype+"_"+img+"_00"+i+".jpg";}
		    	else{
		    		imagename=imagepath+subtype+"_"+img+"_0"+i+".jpg";}
		    	
		    //print(imagename);
		    saveAs("Jpeg", imagename);}}
	   }
close();
    
   


    
