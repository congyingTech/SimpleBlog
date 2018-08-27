clean: 
	find . -name *.pyc |xargs rm  
	find . -name *.log |xargs rm
	find . -name test.log* |xargs rm
	find . -name crawler.log* |xargs rm
	find . -name *.csv |xargs rm 
	find . -name *.tar.gz |xargs rm 
	find . -name *.idea |xargs rm -rf
