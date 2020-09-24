create or replace function totalEmployee(n in Works.did %type)
  return Works.did %type
  is

A Works.did %type;
n_count Works.did %type;

begin
n_count :=0;	
FOR R IN (SELECT did FROM Works) LOOP
	A := R.did;
	IF A=n THEN 
	n_count:=n_count+1;
	END  IF;
END LOOP;
return n_count;	

END totalEmployee;
/