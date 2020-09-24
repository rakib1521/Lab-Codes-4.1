SET SERVEROUTPUT ON;

DECLARE
v_ename Emp.ename%type;
n_salary Emp.salary%type;

BEGIN
DBMS_OUTPUT.PUT_LINE('ename'||'      '||'salary');
FOR R IN (select managerid from dept where budget=(select max(budget) from dept)) LOOP

FOR J IN (select ename, salary from Emp where eid =R.managerid) LOOP
	v_ename := J.ename;
	n_salary := J.salary;
	DBMS_OUTPUT.PUT_LINE(v_ename||' '||n_salary);
END LOOP;

END LOOP;
END;
/