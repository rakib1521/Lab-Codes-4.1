SET SERVEROUTPUT ON;

DECLARE
	A works.did%TYPE := &did;
	B works.did%TYPE := 0;

BEGIN
	B := totalEmployee(A);
	--procEven(A);
	DBMS_OUTPUT.PUT_LINE('Total Employee '||B);
END;
/